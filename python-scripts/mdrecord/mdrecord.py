# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# verhuis.py
# Created in: November 2019 by benoit fricheteau
# edited on: 
#
# Parameter: none
# 
# ---------------------------------------------------------------------------

import copy
# import urlparse
# import urllib2
import urllib
import pandas
from owslib.wms import WebMapService

from lxml import etree
from datetime import datetime

from params.params import get_param

schemas = {
    "gmd": "http://"+"www.isotc211.org/2005/gmd",
    "gco": "http://"+"www.isotc211.org/2005/gco",
    "gmx": "http://"+"www.isotc211.org/2005/gmx",
    "xmlns": "http://www.opengis.net/wms",
    "xlink": "http://www.w3.org/1999/xlink",
    'atom': "http://www.w3.org/2005/Atom",
    'wfs': "http://www.opengis.net/wfs/2.0",
    'srv': 'http://www.isotc211.org/2005/srv',
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "skos": "http://www.w3.org/2004/02/skos/core#"
}


class MDRecord(object):

    citation_xp = "//*/gmd:identificationInfo/*/gmd:citation/gmd:CI_Citation"

    date_datetype_rxp = "gmd:CI_Date/gmd:dateType/gmd:CI_DateTypeCode"

    date_by_type_rxp = "gmd:date[" + date_datetype_rxp + "[{date_type}]]"

    date_date_rxp = "gmd:CI_Date/gmd:date/gco:Date"

    identifier_xp = "//*/gmd:fileIdentifier/gco:CharacterString"

    operates_on_xp = "//*/gmd:identificationInfo/*/srv:operatesOn"

    service_url_xp = "//*/gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions" \
                     "/gmd:onLine/gmd:CI_OnlineResource/gmd:linkage/gmd:URL"

    def __init__(self, xml, xpath_definition_file='metadata_elmt.xlsx'):
        self.xml = xml
        self.xpath_definition_file = xpath_definition_file

    def _get_xpath(self, xpath_key):
        return get_param(xpath_key, path=self.xpath_definition_file)

    def select_tag(self, xpath):
        node = self.xml.xpath(xpath, namespaces=schemas)
        return node

    def select_tag_by_key(self, xpath_key, predicates=None, path_suffix_key=None):
        """
        This function returns an xml tag matching the provided xpath parameter. The xpath parameter
        is a self defined key for a certain xpath. The mapping is defined in an excel file.

        Some predicates must be defined if the matched xpath contains templates. An extrapath can be added
        to the first xpath.

        predicates = string du predicat, a encoder sous forme de liste ;
        path_suffix_key = maintag pour la balise principale, PT_FreeText pour une balise d'une langue locale
                    et demeure vide pour les balises sans texte (code liste, date, ...)
        """
        path = self._get_xpath(xpath_key)
        if path_suffix_key is not None:
            path = path + self._get_xpath(path_suffix_key)
        if predicates is not None:
            path = path.format(*predicates)
        node = self.xml.xpath(path, namespaces=schemas)
        return node

    def get_identifier(self):
        tag = self.select_tag(MDRecord.identifier_xp)
        if tag:
            return tag[0].text
        return None

    def update_date(self, d=datetime.now()):
        string_now = d.strftime("%Y-%m-%dT%H:%M:%S")
        metadata_date = self.xml.xpath("//*/gmd:dateStamp/*", namespaces=schemas)[0]
        metadata_date.text = string_now

    def modify_tag(self, old_tag, new_tag, modif_date=True):
        # 1 balise peut repondre au XPATH
        old_tag.tag = new_tag
        if modif_date:
            self.update_date()

    def modify_attribute(self, old_tag, attribute, value, modif_date=True):
        old_tag.set(attribute, value)
        if modif_date:
            self.update_date()

    def modifycontent(self, oldtag, value, modif_date=True):
        oldtag.text = value
        if modif_date:
            self.update_date()

    def add_tag(self, mother_tag, input_xml, position=0, modif_date=True):
        mother_tag = self.xml.xpath(self._get_xpath(mother_tag), namespaces=schemas)[0]
        mother_tag.insert(position, input_xml)
        if modif_date:
            self.update_date()

    def empty_tag(self, tag, reason):
        self.modify_attribute(tag, "{" + schemas["gco"] + '}nilReason', reason)
        if len(tag) > 0:
            for i in tag:
                tag.remove(i)

    def get_revision_date(self):
        cls = type(self)
        xp = cls.citation_xp + "/" + cls.date_by_type_rxp.format(date_type="@codeListValue='revision'")
        revision_tag = self.select_tag(xp)
        if revision_tag:
            date_date_tag = revision_tag[0].xpath("./" + cls.date_date_rxp, namespaces=schemas)
            try:
                return datetime.strptime(date_date_tag[0].text, "%Y-%m-%d")
            except ValueError:
                return datetime.strptime(date_date_tag[0].text, "%Y-%m-%dT%H:%M:%S")
        return None

    def update_revision_date(self, d=datetime.now(), modif_date=True):
        cls = type(self)
        string_date = d.strftime("%Y-%m-%d")
        metadata_date = self.xml.xpath("//*/gmd:dateStamp/*", namespaces=schemas)[0]
        metadata_date.text = string_date

        xp = cls.citation_xp + "/" + cls.date_by_type_rxp.format(date_type="@codeListValue='revision'")
        revision_tag = self.select_tag(xp)

        # if the revision date cannot be found, create a copy of an existing 'date' tag tree
        if not revision_tag:
            xp = cls.citation_xp + "/" + cls.date_by_type_rxp.format(
                date_type="@codeListValue='creation' or 'publication'")
            existing_date_tag = self.select_tag(xp)[0]
            revision_tag = copy.deepcopy(existing_date_tag)
            revision_tag.xpath("./" + cls.date_datetype_rxp, namespaces=schemas)[0].set('codeListValue', 'revision')

            citation = self.select_tag(cls.citation_xp)[0]
            # we insert the new date tag at the old position of the previous one (first selected date)
            idx = citation.index(existing_date_tag)
            citation.insert(idx, revision_tag)
        else:
            revision_tag = revision_tag[0]

        date_date_tag = revision_tag.xpath("./" + cls.date_date_rxp, namespaces=schemas)

        date_date_tag[0].text = string_date

        if modif_date:
            self.update_date()

    def _update_operates_on(self, get_md_urls):
        cls = type(self)
        operates_on = self.select_tag(cls.operates_on_xp)
        # il y a toujours au moins une balise (dans le cas d'un nouveau service, il s'agit de la balise vers la fiche
        # jeu de données template
        service_identification = operates_on[0].getparent()
        index = service_identification.index(operates_on[0])
        service_url = self.select_tag(cls.service_url_xp)

        data_metadata_urls = set()
        for url in service_url:
            data_metadata_urls.update(get_md_urls(url.text))

        for data_metadata_url in data_metadata_urls:
            # parsed = urlparse.urlparse(data_metadata_url)
            parsed = urllib.parse.urlparse(data_metadata_url)
            md_id = urlparse.parse_qs(parsed.query)['id'][0]
            new_operates = copy.deepcopy(operates_on[0])

            new_operates.set('uuidref', md_id)
            new_operates.set("{" + schemas["xlink"] + '}href', data_metadata_url)
            service_identification.insert(index, new_operates)

        for tag in operates_on:
            service_identification.remove(tag)
        self.update_date()

    def update_operates_on_atom(self):
        def get_md_urls(url):
            data_metadata_urls = set()
            atom = urllib2.urlopen(url).read()
            try:
                atom = etree.fromstring(atom)
                datasets = atom.xpath("//atom:feed/atom:entry/atom:link[@rel='describedby']", namespaces=schemas)
            except:
                # it was not an inspire atom feed
                return data_metadata_urls
            print ("verif len datasets", len(datasets))
            for dataset in datasets:
                print ("DATASET VERIF", dataset)
                data_metadata_urls.add(dataset.get('href'))
            return data_metadata_urls
        self._update_operates_on(get_md_urls)

    def update_operates_on_wfs(self):
        raise Exception("Not implemented.")

    def update_operates_on_wms(self):
        def get_md_urls(url):
            data_metadata_urls = set()
            try:
                wms = WebMapService(url, "1.3.0")
            except:
                print ("failed")
                # it was not a wms
                return data_metadata_urls
            # filter duplicates
            for layer in list(wms.contents):
                for data_metadata_url in wms[layer].metadataUrls:
                    print (data_metadata_url)
                    data_metadata_urls.add(data_metadata_url["url"])
            return data_metadata_urls
        self._update_operates_on(get_md_urls)

    def __repr__(self):
        return etree.tostring(self.xml)
 

class Exportrecords (object): 

    def __init__(self,IDs,cswconnexion, xpath_definition_file='metadata_elmt.xlsx'):
        self.CSW = cswconnexion
        self.xpath_definition_file = xpath_definition_file
        self.IDs=IDs
        
    def loop(self, tags, directory, namefile):        #tags sous forme de dico {'tag1':['langue1', 'langue2'], 'tag2':['langue1']}
        self.rows=[]
        for ID in self.IDs:
            self.row=[]     #lignes de données
            self.row.append(ID)
            columns=["UUID"]        #nom des colonnes
            for tag in tags:
                self.tag=tag            #transformer les tag en tuple (xpaht, [predicats]) à la place de str(xpath)
                self.predicates=tags[tag].get("predicates")
                self.langues=tags[tag]["langues"]
                self.list=self._exportcontent(ID, tag=self.tag, langues=self.langues,predicates=self.predicates)
                self.row.extend(self.list)
                columns.extend(self.columns)#nom des colonnes
            self.rows.append(self.row)#ajout d'un nouvelle ligne de données de données
        
        df=pandas.DataFrame(self.rows,columns = columns)
        df.to_excel(directory+"//"+namefile+".xlsx",index=False)
   
    def _readcontent(self,mdrecord, tag, predicates=None, langue=None):
        self.predicates=[]
        self.xpath=mdrecord._get_xpath(tag)
        if predicates is not None:
            self.xpath = self.xpath.format(*predicates)
        if langue is not None:
            self.suffixe=mdrecord._get_xpath('PT_FreeText')
            self.xpath=self.xpath+self.suffixe
            self.xpath=self.xpath.format(langue)
        else:
            self.suffixe=mdrecord._get_xpath('maintag')
            self.xpath=self.xpath+self.suffixe
            
        self.xpath=mdrecord.select_tag(self.xpath)        
        self.content=""
        if len(self.xpath)>0:
            for cont in self.xpath:
                if self.content=="":
                    self.content=cont.text         #supporter la cardinalité>1 ({})
                else:
                    self.content=self.content+"{}"+cont.text
        return self.content
        
    def _exportcontent (self,ID, tag, langues, predicates=None ):        
        self.xml=self.CSW.get_record(ID)
        self.record=MDRecord(self.xml,self.xpath_definition_file)
        self.tag=tag
        self.predicates=predicates
        self.list=[]
        self.columns=[]
        if len(langues) >0:
            for self.langue in langues:
                self.columns.append(self.tag+"_"+self.langue)
                self.content=self._readcontent(self.record, self.tag,self.predicates, self.langue)
                self.list.append(self.content)
        else:
            self.columns.append(self.tag)
            self.list.append(self._readcontent(self.record, self.tag,self.predicates))
        return self.list    


    
    
    
    
# if __name__ == "__main__": 
    # idfiche='a2366b58-aff1-493b-a359-4a891a570484'
    # import os
    # import inspect
    # import getpass
    # from lxml import etree
    # from mdrecord import MDRecord
    # from params.params import get_param
    # from geonetwork.geonetwork import GeoNetwork, CSW
    # localisation_script=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


    # gn_username = raw_input("GeoNetwork UserName")
    # gn_password=getpass.getpass("GeoNetwork Password")     
    # cswconnexion = CSW("http://publish.geo.be/geonetwork/srv/eng/csw-NGIhosted", gn_username,gn_password) 
    # md = MDRecord(cswconnexion.get_record(idfiche))

    # md.update_operates_on_atom()
    
    # newxml = etree.ElementTree(md.xml)
    # path = localisation_script + "\\"+"verif.xml"
    # newxml.write(path, xml_declaration=True, encoding='UTF-8')
    # with open(localisation_script+"\\"+"verif.xml", 'r') as f:
        # test_xml = f.read()
    # print "written",       
    
    
    # cswconnexion.update_record(idfiche, etree.tostring(md.xml))

    
     
    
    
