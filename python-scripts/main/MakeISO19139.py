# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# ISO19139.py
# Created on: 31 January 2022 by benoit fricheteau
# edited on: 
#
# Parameter: none
# 
# ---------------------------------------------------------------------------

from lxml import etree
import os
import inspect
import time
import copy
import uuid
import getpass
import gemet
import pandas
import readISO19139
import inspect
import numpy
import rdfParsing
from geonetwork.geonetwork import GeoNetwork
import requests

gn_username = raw_input("GeoNetwork UserName")
gn_password=getpass.getpass("GeoNetwork Password")


UploadSession=GeoNetwork("https://geobru-geonetwork.irisnet.be", gn_username, gn_password)


localisation_script=localisation_script = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
templates=localisation_script+"\\"+"templates"


MD_MetadataXML=templates+"\\"+"MD_Metadata.xml"



inspirethemes=localisation_script+"\\"+"Metadata"+"\\"+"thesauri"+"\\"+"inspiretheme.rdf"
inspireconcept=localisation_script+"\\"+"Metadata"+"\\"+"thesauri"+"\\"+"inspireconcept.rdf"
federalthesaurus=localisation_script+"\\"+"Metadata"+"\\"+"thesauri"+"\\"+"federalthesaurus.rdf"
datagov=localisation_script+"\\"+"Metadata"+"\\"+"thesauri"+"\\"+"datagovthesaurus.rdf"
limitations=localisation_script+"\\"+"Metadata"+"\\"+"thesauri"+"\\"+"restrictionPublicAccess.rdf"
licenses=localisation_script+"\\"+"Metadata"+"\\"+"thesauri"+"\\"+"licenses.rdf"



limitations=rdfParsing.thesaurusRdf(limitations, "xml")
licenses=rdfParsing.thesaurusRdf(licenses, "xml")
inspirethemes=rdfParsing.thesaurusRdf(inspirethemes, "xml")
federalthesaurus=rdfParsing.thesaurusRdf(federalthesaurus, "xml")
datagov=rdfParsing.thesaurusRdf(datagov, "xml")
inspireconcept=rdfParsing.thesaurusRdf(inspireconcept, "xml")



mediaTypes={
    "CSV":"https://www.iana.org/assignments/media-types/text/csv",
    "TIFF":"https://www.iana.org/assignments/media-types/image/tiff",
    "ASCII":"http://inspire.ec.europa.eu/media-types/application/x-ascii-grid",
    "XML":"https://www.iana.org/assignments/media-types/text/xml",
    "Esri Shapefile":"https://www.iana.org/assignments/media-types/application/vnd.shp",
    "GML":"https://www.iana.org/assignments/media-types/application/gml+xml",
    "Esri Geodatabase":"http://inspire.ec.europa.eu/media-types/application/x-filegdb",
    "Excel":"https://www.iana.org/assignments/media-types/application/vnd.ms-excel",
    "GeoPackage":"https://www.iana.org/assignments/media-types/application/geopackage+sqlite3",
    "GeoJSON":"https://www.iana.org/assignments/media-types/application/geo+json",
    "PDF": "https://www.iana.org/assignments/media-types/application/pdf",
    "Word": "https://www.iana.org/assignments/media-types/application/msword",
    "HTML": "https://www.iana.org/assignments/media-types/text/html",
    "MicroStation DGN": "https://docs.fileformat.com/cad/dgn/",
    "Autocad DWG": "https://www.iana.org/assignments/media-types/image/vnd.dwg",
    "MapInfo TAB": "https://web.archive.org/web/20060909054240/http://resource.mapinfo.com/static/files/document/1074660800077/interchange_file.pdf",
    "SketchUp":None,
    "MrSID": None,
    "ECW": None,
    "JPEG": "https://www.iana.org/assignments/media-types/image/jpeg",
    "Las": "https://www.iana.org/assignments/media-types/application/vnd.las",
    "KML": "https://www.iana.org/assignments/media-types/application/vnd.google-earth.kml+xml",
    "ODF": "https://www.iana.org/assignments/media-types/application/vnd.oasis.opendocument.presentation"
}
extensionFormat={
    "csv":"https://www.iana.org/assignments/media-types/text/csv",
    "tiff":"https://www.iana.org/assignments/media-types/image/tiff",
    "ascii":"http://inspire.ec.europa.eu/media-types/application/x-ascii-grid",
    "xml":"https://www.iana.org/assignments/media-types/text/xml",
    "shp":"https://www.iana.org/assignments/media-types/application/vnd.shp",
    "gml":"https://www.iana.org/assignments/media-types/application/gml+xml",
    "gdb":"http://inspire.ec.europa.eu/media-types/application/x-filegdb",
    "gpkg":"https://www.iana.org/assignments/media-types/application/geopackage+sqlite3",
    "geojson":"https://www.iana.org/assignments/media-types/application/geo+json",
    'pdf': "https://www.iana.org/assignments/media-types/application/pdf",
    "docx": "https://www.iana.org/assignments/media-types/application/msword",
    "html": "https://www.iana.org/assignments/media-types/text/html",
    "jpeg": "https://www.iana.org/assignments/media-types/image/jpeg",
    "las":"https://www.iana.org/assignments/media-types/application/vnd.las",
    "xlsx": "https://www.iana.org/assignments/media-types/application/vnd.ms-excel",
    "odt": "https://www.iana.org/assignments/media-types/application/vnd.oasis.opendocument.presentation"
}


versionformat={"Esri Shapefile":"10.2","GML":"3.2.1"}


localeDico={"monoLingual":"#EN",
            "french":"#FR",
            "dutch":"NL"
}
Licenses={"CC-0":"https://creativecommons.org/publicdomain/zero/1.0/deed.en",
            "CC-BY":"https://creativecommons.org/licenses/by/4.0/",
            "Fee required":"https://www.ejustice.just.fgov.be/eli/arrete/2018/02/01/2018010589/justel"
}

PublicRestrictions={"No limitations":"http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess/noLimitations",
                    "Privacy":"http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess/INSPIRE_Directive_Article13_1f",
                    "Copyright":"http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess/INSPIRE_Directive_Article13_1e"
}

DicoProj={"EPSG:3812": "http://www.opengis.net/def/crs/EPSG/0/3812",
           "EPSG:31370":"http://www.opengis.net/def/crs/EPSG/0/31370"
}
class FromExcel(object):
    def __init__(self,inputPandas):
        self.EN=None
        self.FR=None
        self.NL=None
        
        if pandas.isnull(inputPandas.iloc[0])==False:
            self.EN=inputPandas.iloc[0]  
        if pandas.isnull(inputPandas.iloc[1])==False:
            self.FR=inputPandas.iloc[1]   
        if pandas.isnull(inputPandas.iloc[2])==False:   
            self.NL=inputPandas.iloc[2]
        
        if len(inputPandas)<4 or pandas.isnull(inputPandas.iloc[3])==True:
                
            self.URI=None 
        else:
            self.URI=inputPandas.iloc[3]    
            


class Content(object):
    def __init__(self,monoLingual, french=None, dutch=None,  URI=None, type=None):
        self.EN=monoLingual
        self.FR=french
        self.NL=dutch
        self.URI=URI
        self.type=type

class MD_Metadata(object):
    def __init__(self,excel):
        self.excel=excel
        self.uuid=str(uuid.uuid1())
        self.fileIdentifier=Content(self.uuid)
        self.language="eng"
        self.characterSet="utf8"
        if typerecord=='dataset':
            self.hierarchyLevel=self.excel.loc['hierarchyLevel','URI']
        else:
            self.hierarchyLevel='service'
        self.hierarchyLevelName=None
        self.contact=None
        self.dateStamp=dateStamp
        self.metadataStandardName=metadataStandardName
        self.metadataStandardVersion=None
        self.locale=locales
        self.identificationInfo=None
        self.distributionInfo=None
        self.dataQualityInfo=None
        self.referenceSystemInfo=None
        
    def readExcel(self):
        """
        METADATA ABOUT METADATA
        """

        MD_deliveryPoint=FromExcel(self.excel.loc['MD_deliveryPoint',['content_eng','content_fre','content_dut','URI']])
        MD_city=FromExcel(self.excel.loc['MD_city',['content_eng','content_fre','content_dut']])
        MD_country=FromExcel(self.excel.loc['MD_country',['content_eng','content_fre','content_dut']])
        MD_Site=FromExcel(self.excel.loc['MD_onlineResource',['content_eng','content_fre','content_dut']])
        MD_Name=FromExcel(self.excel.loc['MD_organisationName',['content_eng','content_fre','content_dut', 'URI']])        
        if pandas.isnull(self.excel.loc['MD_postalCode','URI']) == False:
            MD_postalCode=Content(self.excel.loc['MD_postalCode','URI'])
        else :
            MD_postalCode=None  
        if pandas.isnull(self.excel.loc['MD_electronicMailAddress','URI']) == False:
            MD_electronicMailAddress=Content(self.excel.loc['MD_electronicMailAddress','URI'])
        else :
            MD_electronicMailAddress=None       
        MetadataAddress=CI_Address(Content(MD_deliveryPoint.EN, MD_deliveryPoint.FR, MD_deliveryPoint.NL, MD_deliveryPoint.URI), Content(MD_city.EN, MD_city.FR, MD_city.NL), MD_postalCode, Content(MD_country.EN, MD_country.FR, MD_country.NL),MD_electronicMailAddress)
        MetadataWebsite=CI_OnlineResource(MD_Site.EN,name=Content(MD_Site.EN, MD_Site.FR, MD_Site.NL))
        MetadataContactInfo=CI_Contact(MetadataAddress, MetadataWebsite)
        MetadataPoc=Content(MD_Name.EN, MD_Name.FR, MD_Name.NL, MD_Name.URI)
        if pandas.isnull(self.excel.loc['MD_individualName','URI']) == False:
            MD_individualName=Content(self.excel.loc['MD_individualName','URI'])
        else :
            MD_individualName=None
        self.contact=CI_ResponsibleParty(MetadataPoc, "pointOfContact" , MetadataContactInfo, MD_individualName)
        
        if self.hierarchyLevel !='study': #études n'ont aucune composante spatiale --> pas de système de proj direct ou indirect
            self.referenceSystemInfo=[]
            if pandas.isnull(excel.loc['referenceSystemInfo','URI'])==False:                                        

                for proj in self.excel.loc['referenceSystemInfo','URI'].split('#'):
                    if proj in DicoProj:
                        URI=DicoProj[proj]
                    else:
                        URI = None
                    projection=RS_Identifier(Content(proj, proj, proj, URI), Content("EPSG"))
                    self.referenceSystemInfo.append(projection)
        
        self.distributionInfo=MD_Distribution(self.excel)
        self.distributionInfo.readExcel()      
        
        self.dataQualityInfo=DQ_DataQuality(self.excel)
        self.dataQualityInfo.readExcel()
        
        
        if typerecord=='dataset':
            self.identificationInfo=MD_DataIdentification(self.excel)
            self.identificationInfo.readExcel() 
        
        if typerecord=='service':
            self.identificationInfo=SV_ServiceIdentification(self.excel)
            self.identificationInfo.readExcel()   
            if self.excel.loc['serviceType','URI'] == 'download':
               self.hierarchyLevelName=Content(u'Download service', u'Service de téléchargement', u'Downloaddienst')            
            if self.excel.loc['serviceType','URI'] == 'view':
                self.hierarchyLevelName=Content(u'View service', u'Service de consultation', u'Raadpleegdienst')            
            if self.excel.loc['serviceType','URI'] == 'search':
                self.hierarchyLevelName=Content(u'Search service', u'Service de découverte', u'Zoekdienst')            
            if self.excel.loc['serviceType','URI'] == 'application':
                self.hierarchyLevelName=Content(u'Application', u'Application', u'Applicatie')

           
        
        
        
class PT_Locale(object):
    def __init__(self, internalID, languageCode, characterEncoding=None):
        self.internalID=internalID
        self.languageCode=languageCode
        self.characterEncoding=characterEncoding
        
        
class CI_ResponsibleParty(object):
    def __init__(self,organisationName, role,contactInfo=None, individualName=None):
        self.individualName=individualName
        self.organisationName=organisationName
        self.contactInfo=contactInfo
        self.role=role
        
class CI_Contact(object):
    def __init__(self,address,onlineResource):
        self.address=address
        self.onlineResource=onlineResource

class CI_Citation(object):
    def __init__(self,title, date=None, identifier=None):
        self.title=title
        self.date=date
        self.identifier=identifier
        
        

class CI_Date(object):
    def __init__(self,date, dateType=None):
        self.date=date
        self.dateType=dateType
        
        
class RS_Identifier(object):
    def __init__(self,code,codeSpace):
        self.code=code
        self.codeSpace=codeSpace
        
        
class CI_Address(object):
    def __init__(self,deliveryPoint,city, postalCode,country, electronicMailAddress):
        self.deliveryPoint=deliveryPoint
        self.city=city
        self.postalCode=postalCode
        self.country=country
        self.electronicMailAddress=electronicMailAddress

class CI_OnlineResource(object):
    def __init__(self,linkage, protocol=None,function=None, name=None, description=None):
        self.linkage=linkage
        self.name=name
        self.protocol=protocol
        self.description=description
        self.function=function

class MD_Resolution(object):
    def __init__(self,equivalentScale=None,distance=None):
        self.equivalentScale=equivalentScale
        self.distance=distance
        
class MD_RepresentativeFraction(object):
    def __init__(self,denominator=None,distance=None):
        self.denominator=denominator


class MD_Keywords(object):
    def __init__(self,keyword,thesaurusName=None, type=None):
        self.keyword=keyword
        self.thesaurusName=thesaurusName
        self.type=type



class MD_LegalConstraints(object):
    def __init__(self,otherConstraints,accessConstraints=None, useConstraints=None):
        self.useConstraints=useConstraints
        self.accessConstraints=accessConstraints
        self.otherConstraints=otherConstraints



class MD_BrowseGraphic(object):
    def __init__(self,fileName):
        self.fileName=fileName



class EX_GeographicBoundingBox(object):
    def __init__(self,westBoundLongitude,eastBoundLongitude, southBoundLongitude,northBoundLongitude ):
        self.westBoundLongitude=westBoundLongitude
        self.eastBoundLongitude=eastBoundLongitude
        self.southBoundLongitude=southBoundLongitude
        self.northBoundLongitude=northBoundLongitude
        
        
class EX_Extent(object):
    def __init__(self,description,geographicElement):
        self.description=description
        self.geographicElement=geographicElement


class MD_AbstractIdentification(object):
    def __init__(self,excel):
        self.excel=excel
        self.citation=None
        self.abstract=None
        self.pointOfContact=None
        self.resourceMaintenance=self.excel.loc['resourceMaintenance','URI']
        self.descriptiveKeywords=[]        
        self.resourceConstraints=[]
        self.extent=extent 
        self.graphicOverview=None         
        if pandas.isnull(excel.loc['graphicOverview','URI'])==False:                               
            self.graphicOverview=MD_BrowseGraphic(Content(excel.loc['graphicOverview','URI']))
        
        
    def readExcel(self):
        abstract=FromExcel(excel.loc['abstract',['content_eng','content_fre','content_dut','URI']])
        title=FromExcel(excel.loc['title',['content_eng','content_fre','content_dut','URI']])

        RS_uuid=str(uuid.uuid1())
        self.abstract=Content(abstract.EN, abstract.FR, abstract.NL)
        self.citation=CI_Citation(Content(title.EN, title.FR, title.NL), 
        [CI_Date(str(excel.loc['creationdate','URI']),'creation' ), CI_Date(str(excel.loc['creationdate','URI']),'revision')], 
        RS_Identifier(Content(RS_uuid), Content(excel.loc['codeSpace','URI'])))
        
        #Licenses/Constrains
        
        limitations.findPrefLabel(PublicRestrictions[excel.loc['Limitations','URI']], 'fr')
        fre=limitations.prefLabel
        limitations.findPrefLabel(PublicRestrictions[excel.loc['Limitations','URI']], 'nl')
        dut=limitations.prefLabel
        limitations.findPrefLabel(PublicRestrictions[excel.loc['Limitations','URI']], 'en')
        eng=limitations.prefLabel                                    
        legalConstraints=MD_LegalConstraints( Content(eng,fre, dut, PublicRestrictions[excel.loc['Limitations','URI']]), accessConstraints='otherRestrictions')        
        
        
        
        licenses.findPrefLabel(Licenses[excel.loc['License','URI']], 'fr')
        fre=licenses.prefLabel
        licenses.findPrefLabel(Licenses[excel.loc['License','URI']], 'nl')
        dut=licenses.prefLabel
        licenses.findPrefLabel(Licenses[excel.loc['License','URI']], 'en')
        eng=licenses.prefLabel                        
        useConstraints=MD_LegalConstraints(Content(eng,fre, dut, Licenses[excel.loc['License','URI']]), useConstraints='otherRestrictions',)
        

        self.resourceConstraints=[legalConstraints, useConstraints]
        RS_deliveryPoint=FromExcel(excel.loc['RS_deliveryPoint',['content_eng','content_fre','content_dut','URI']])
        RS_city=FromExcel(excel.loc['RS_city',['content_eng','content_fre','content_dut','URI']])
        RS_country=FromExcel(excel.loc['RS_country',['content_eng','content_fre','content_dut','URI']])
        RS_Site=FromExcel(excel.loc['RS_onlineResource',['content_eng','content_fre','content_dut']])
        RS_Name=FromExcel(excel.loc['RS_organisationName',['content_eng', 'content_fre','content_dut','URI']])
        
        
        if pandas.isnull(self.excel.loc['RS_postalCode','URI']) == False:
            RS_postalCode=Content(self.excel.loc['RS_postalCode','URI'])
        else :
            RS_postalCode=None               
        if pandas.isnull(self.excel.loc['RS_electronicMailAddress','URI']) == False:
            RS_electronicMailAddress=Content(self.excel.loc['RS_electronicMailAddress','URI'])
        else :
            RS_electronicMailAddress=None      
            
        DataAddress=CI_Address(Content(RS_deliveryPoint.EN, RS_deliveryPoint.FR, RS_deliveryPoint.NL, RS_deliveryPoint.URI), Content(RS_city.EN, RS_city.FR, RS_city.NL), RS_postalCode, Content(RS_country.EN, RS_country.FR, RS_country.NL),RS_electronicMailAddress)
        DataWebsite=CI_OnlineResource(RS_Site.EN,name=Content(RS_Site.EN, RS_Site.FR, RS_Site.NL))

        DataContactInfo=CI_Contact(DataAddress, DataWebsite)
        DataPoc=Content(RS_Name.EN, RS_Name.FR, RS_Name.NL, RS_Name.URI)
        if pandas.isnull(self.excel.loc['RS_individualName','URI']) == False:
            RS_individualName=Content(self.excel.loc['RS_individualName','URI'])
        else :
            RS_individualName=None
        self.pointOfContact=CI_ResponsibleParty(DataPoc, "custodian" , DataContactInfo, RS_individualName)
                
        self.descriptiveKeywords=[]


        if pandas.isnull(excel.loc['EUROVOC_descriptiveKeywords','URI'])==False:                                        
            keywords=[]
            excel.loc['EUROVOC_descriptiveKeywords','URI']
            
            for uri in excel.loc['EUROVOC_descriptiveKeywords','URI'].split("#"):
                
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

               
                r=session.get(uri,headers=headers )
                r = etree.fromstring(r.content)
                newxml = etree.ElementTree(r)
                path = localisation_script + "\\"+"verif.xml"
                newxml.write(path, xml_declaration=True, encoding='UTF-8')
                eurovoc=rdfParsing.thesaurusRdf(path, "xml")
                eurovoc.findPrefLabel(uri, 'fr')
                fre=eurovoc.prefLabel
                eurovoc.findPrefLabel(uri, 'nl')
                dut=eurovoc.prefLabel
                eurovoc.findPrefLabel(uri, 'en')
                eng=eurovoc.prefLabel
                keyword=Content(eng,fre, dut, uri)
                keywords.append(keyword)
            
            os.remove(path)                         
            thesaurus = CI_Citation (Content(u"EUROVOC - Concept themes", u"EUROVOC - Concept themes", u"EUROVOC - Concept themes", "http://publications.europa.eu/resource/dataset/eurovoc") , [CI_Date('2021-12-17', 'publication')])
            dico=MD_Keywords(keywords, thesaurus)      
            self.descriptiveKeywords.append(dico)
            
            
        if pandas.isnull(excel.loc['GEMET_descriptiveKeywords','URI'])==False:                                        
            keywords=[]
            excel.loc['GEMET_descriptiveKeywords','URI']
            concept=gemet.conceptrdf(session)

            for uri in excel.loc['GEMET_descriptiveKeywords','URI'].split("#"):
                              
                concept.findpreflabel(uri,"fr")
                fre=concept.preflabel
                dut=concept.findpreflabel(uri,"nl")
                dut=concept.preflabel
                eng=concept.findpreflabel(uri,"en") 
                eng=concept.preflabel
                keyword=Content(eng, fre, dut, uri)
                keywords.append(keyword)                     
                
            thesaurus = CI_Citation (Content(u"Thèmes GEMET", u"GEMET Thema's", u"GEMET Themes", "https://www.eionet.europa.eu/gemet/en/themes/") , [CI_Date('2020-04-23', 'publication')])
            dico=MD_Keywords(keywords, thesaurus)      
            self.descriptiveKeywords.append(dico)

        if pandas.isnull(excel.loc['BOSA_descriptiveKeywords','URI'])==False:                            
            keywords=[]
            for uri in excel.loc['BOSA_descriptiveKeywords','URI'].split("#"):
            
                           
                datagov.findPrefLabel(uri, 'fr')
                fre=datagov.prefLabel
                datagov.findPrefLabel(uri, 'nl')
                dut=datagov.prefLabel
                datagov.findPrefLabel(uri, 'en')
                eng=datagov.prefLabel 
                
                keyword=Content(eng,fre, dut, uri)
                keywords.append(keyword)
            
            
            thesaurus = CI_Citation (Content(u"Data.gov.be themes", u"Thèmes Data.gov.be", u"Data.gov.be thema's", "http://vocab.belgif.be/auth/datatheme") , [CI_Date('2019-01-31', 'publication')])
            dico=MD_Keywords(keywords, thesaurus)           
            self.descriptiveKeywords.append(dico)
     
        if pandas.isnull(excel.loc['INSPIRE_descriptiveKeywords','URI'])==False:
            keywords=[]
            for uri in excel.loc['INSPIRE_descriptiveKeywords','URI'].split("#"):

                inspirethemes.findPrefLabel(uri, 'fr')
                fre=inspirethemes.prefLabel
                inspirethemes.findPrefLabel(uri, 'nl')
                dut=inspirethemes.prefLabel
                inspirethemes.findPrefLabel(uri, 'en')
                eng=inspirethemes.prefLabel 
                
                keyword=Content(eng,fre, dut, uri)
                keywords.append(keyword)
                
            thesaurus = CI_Citation (Content("GEMET - INSPIRE themes, version 1.0", "GEMET - INSPIRE themes, version 1.0", "GEMET - INSPIRE themes, version 1.0", "http://inspire.ec.europa.eu/theme") , [CI_Date('2008-06-01', 'publication')])
            dico=MD_Keywords(keywords, thesaurus)     
            self.descriptiveKeywords.append(dico)

        # if numpy.isnan(excel.loc['Regional_descriptiveKeywords','URI'])==False:
            # keywords=[]
            # for uri in excel.loc['Regional_descriptiveKeywords','URI'].split("#"):
            
            
                # inspirethemes.findconcept(uri)
                # inspirethemes.findPrefLabel(uri, 'fr')
                # fre=inspirethemes.prefLabel
                # inspirethemes.findPrefLabel(uri, 'nl')
                # dut=inspirethemes.prefLabel
                # inspirethemes.findPrefLabel(uri, 'en')
                # eng=inspirethemes.prefLabel 
                
                # keyword=Content(eng, fre, dut, uri)
                # keywords.append(keyword)
            
            # thesaurus = CI_Citation (Content("GEMET - INSPIRE themes, version 1.0", "GEMET - INSPIRE themes, version 1.0", "GEMET - INSPIRE themes, version 1.0", "http://inspire.ec.europa.eu/theme") , [CI_Date('2008-06-01', 'publication')])
            # dico=MD_Keywords(keywords, thesaurus)   
            # self.descriptiveKeywords.append(dico)
            
        if pandas.isnull(excel.loc['FREE_descriptiveKeywords','content_eng'])==False: #content_eng parce que pas d'URI
            keywords=[]
            for eng, fre, dut in zip(excel.loc['FREE_descriptiveKeywords','content_eng'].split("#"), excel.loc['FREE_descriptiveKeywords','content_fre'].split("#"), excel.loc['FREE_descriptiveKeywords','content_dut'].split("#")):
         
                keyword=Content(fre, dut, eng, uri)
                keywords.append(keyword)
            
            dico=MD_Keywords(keywords)   

            self.descriptiveKeywords.append(dico)
            
        
        thesaurus = CI_Citation (Content(u"Spatial scope", u"Champ géographique", u"Ruimtelijke dekking", "http://inspire.ec.europa.eu/metadata-codelist/SpatialScope") , [CI_Date('2019-05-22', 'publication')])
        dico=MD_Keywords([Content(u'Régional',u'Regional', u'Regionaal', 'http://inspire.ec.europa.eu/metadata-codelist/SpatialScope/regional')], thesaurus)     
        self.descriptiveKeywords.append(dico)
        
class MD_DataIdentification(MD_AbstractIdentification):
    def __init__(self, excel):     
        self.excel=excel
        super(MD_DataIdentification, self).__init__(self.excel)
        self.status='completed'      
        self.spatialRepresentationType=None
        self.spatialResolution=None
        self.language=None
        self.topicCategory=None        
        self.characterSet=['utf8']
       
        
    def readExcel(self):
        super(MD_DataIdentification, self).readExcel()  
        if pandas.isnull(excel.loc['INSPIREConcept_descriptiveKeywords','URI'])==False:
       
            keywords=[]
            for uri in self.excel.loc['INSPIREConcept_descriptiveKeywords','URI'].split("#"):           
                inspireconcept.findPrefLabel(uri, 'fr')
                fre=inspireconcept.prefLabel
                inspireconcept.findPrefLabel(uri, 'nl')
                dut=inspireconcept.prefLabel
                inspireconcept.findPrefLabel(uri, 'en')
                eng=inspireconcept.prefLabel 
                
                keyword=Content(eng,fre, dut, uri)
                keywords.append(keyword)
            
            
            thesaurus = CI_Citation (Content("INSPIRE feature concept dictionary", "Dictionnaire des types d'objets INSPIRE", "INSPIRE objecttyppen woordenboek", "http://inspire.ec.europa.eu/featureconcept") , [CI_Date('2012-07-20', 'publication')])
            dico=MD_Keywords(keywords, thesaurus)           
            self.descriptiveKeywords.append(dico)
            
        if self.excel.loc['spatialRepresentationType','URI']=='vector':
            self.spatialResolution=MD_Resolution(equivalentScale=MD_RepresentativeFraction(self.excel.loc['spatialResolution','URI']))
        elif self.excel.loc['spatialRepresentationType','URI']=='grid':
            self.spatialResolution=MD_Resolution(distance=self.excel.loc['spatialResolution','URI'])
            
        self.spatialRepresentationType=self.excel.loc['spatialRepresentationType','URI']
        self.language=self.excel.loc['RS_language','URI'].split('#')
        self.topicCategory=self.excel.loc['topicCategory','URI']

class SV_ServiceIdentification(MD_AbstractIdentification):
    def __init__(self, excel):     
        self.excel=excel
        super(SV_ServiceIdentification, self).__init__(self.excel)
        self.serviceType=self.excel.loc['serviceType','URI']
        self.coupledResource=[]  
        self.couplingType="tight"
        self.containsOperations=None
        self.csw=csw   
        self.operatesOn=self.excel.loc['operatesOn','URI'].split('#')

        
    def readExcel(self):
        super(SV_ServiceIdentification, self).readExcel()

        if typerecord=="service" and self.excel.loc['serviceType','URI']=="download":
            keyword=[Content(u"Feature access service",u"Service d’accès aux éléments", u"Dienst objecttoegang", "http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceCategory/infoFeatureAccessService")]
            
        if typerecord=="service" and self.excel.loc['serviceType','URI']=="view":
            keyword=[Content(u"Map access service",u"Service d’accès aux cartes", u"Dienst kaarttoegang", "http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceCategory/infoMapAccessService")]


        if typerecord=="service" and self.excel.loc['serviceType','URI']=="search":
            keyword=[Content(u"Catalogue service",u"Service de catalogue", u"Catalogusdienst", "http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceCategory/infoCatalogueService")]

            MD_Keywords(["infoCatalogueService"], thesaurus) 
            
        if typerecord=="service" and self.excel.loc['serviceType','URI']=="application":
            keyword=[Content(u"Geographic human interaction services",u"Services géographiques avec interaction humaine", u"Geografische menselijke-interactiediensten", "http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceCategory/humanInteractionService")]

        if typerecord == "service" and self.excel.loc['serviceType', 'URI'] == "geolocation":
            keyword = [Content(u"Positioning service", u"Service de positionnement", u"Positioneringsdienst","http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceCategory/spatialPositioningService")]

        thesaurus = CI_Citation (Content(u"Classification of spatial data services", u"Classification des services de données géographiques", u"Classificatie van diensten met betrekking tot ruimtelijke gegevens", "http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceCategory") , [CI_Date('2008-12-08', 'publication')])
        dico=MD_Keywords(keyword, thesaurus)   
        self.descriptiveKeywords.append(dico)
        
        self.containsOperations=SV_OperationMetadata(Content('GetCapabilities'),"WebServices", CI_OnlineResource(excel.loc['containsOperations_linkage','URI']))

        for operatesOn in self.operatesOn:
            coupledResource=SV_CoupledResource(Content("GetCapabilities"), Content(operatesOn))
            self.coupledResource.append(coupledResource)
        
        
        
class SV_CoupledResource (object):
     
    def __init__(self, operationName,identifier):
    
        self.operationName=operationName
        self.identifier=identifier


class SV_OperationMetadata (object):

    def __init__(self, operationName,DCP,connectPoint):
    
        self.operationName=operationName
        self.DCP=DCP
        self.connectPoint=connectPoint

        
class MD_Distribution(object):
    def __init__(self,excel):
        self.excel=excel
        self.distributionFormat=None
        self.transferOptions=[]
        
        
    def readExcel(self):
        if typerecord=="dataset":
            self.distributionFormat=[]
            for distributionFormat in excel.loc['distributionFormat','URI'].split("#"):
                uri=mediaTypes[distributionFormat]
                version=None
                if distributionFormat in versionformat:
                    version=Content(versionformat[distributionFormat])
                format=MD_Format(Content(distributionFormat, distributionFormat, distributionFormat, uri), version)
                
                self.distributionFormat.append(format)
            
        
        if typerecord=="dataset":
                   
            if pandas.isnull(excel.loc['WMS_transferOptions','URI'])==False:       
                link=MD_DigitalTransferOptions(CI_OnlineResource(excel.loc['WMS_transferOptions','URI'], Content("OGC:WMS"), "view"))
                self.transferOptions.append(link)        

            if pandas.isnull(excel.loc['WFS_transferOptions','URI'])==False:       
                link=MD_DigitalTransferOptions(CI_OnlineResource(excel.loc['WFS_transferOptions','URI'], Content("OGC:WFS"), "download"))
                self.transferOptions.append(link)        
            
            if pandas.isnull(excel.loc['Download_transferOptions','URI'])==False:                   
                for downloadLink in excel.loc['Download_transferOptions','URI'].split("#") :
                    if len(downloadLink.split('/')[-1].split('.'))==2:
                        name=downloadLink.split('/')[-1].split('.')[0]
                        extension=downloadLink.split('/')[-1].split('.')[1]
                        extension=extensionFormat[extension].split('media-types/')[1]
                        name=Content(name, type=extension)
                    else:
                        name=None
                    link=MD_DigitalTransferOptions(CI_OnlineResource(downloadLink, Content("WWW:DOWNLOAD-1.0-http--download"), "download", name=name))
                    self.transferOptions.append(link)
                       
            if pandas.isnull(excel.loc['Info_transferOptions','content_fre'])==False:       #liens linguistiquement spécifiques
                Link=FromExcel(excel.loc['Info_transferOptions',['content_eng', 'content_fre', 'content_dut']] )
                link=MD_DigitalTransferOptions(CI_OnlineResource(excel.loc['Info_transferOptions','content_eng'], Content("WWW:LINK-1.0-http--link"), "information",Content(Link.EN, Link.FR, Link.NL)))
                self.transferOptions.append(link)
        else:
            description=Content('accessPoint',URI='http://inspire.ec.europa.eu/metadata-codelist/OnLineDescriptionCode/accessPoint', )
            if excel.loc['serviceType','URI']=='download':
                link=MD_DigitalTransferOptions(CI_OnlineResource(excel.loc['containsOperations_linkage','URI'], Content(excel.loc['containsOperations_protocol','URI']),"download", description=description))
            if excel.loc['serviceType','URI']=='view':
                link=MD_DigitalTransferOptions(CI_OnlineResource(excel.loc['containsOperations_linkage','URI'], Content(excel.loc['containsOperations_protocol','URI']), "view", description=description))
            if excel.loc['serviceType','URI']=='search':
                link=MD_DigitalTransferOptions(CI_OnlineResource(excel.loc['containsOperations_linkage','URI'], Content(excel.loc['containsOperations_protocol','URI']), "search", description=description))            
            if excel.loc['serviceType','URI']=='application':
                link=MD_DigitalTransferOptions(CI_OnlineResource(excel.loc['containsOperations_linkage','URI'], Content(excel.loc['containsOperations_protocol','URI']), "application", description=description))
            if excel.loc['serviceType', 'URI'] == 'geolocation':
                link=MD_DigitalTransferOptions(CI_OnlineResource(excel.loc['containsOperations_linkage', 'URI'],Content(excel.loc['containsOperations_protocol', 'URI']),"geolocation", description=description))
            self.transferOptions.append(link)

        

class MD_MaintenanceInformation(object):
    def __init__(self,maintenanceAndUpdateFrequency):
        self.maintenanceAndUpdateFrequency=maintenanceAndUpdateFrequency


        
class MD_Format(object):
    def __init__(self,name,version):
        self.name=name
        self.version=version


        
class MD_DigitalTransferOptions(object):
    def __init__(self,onLine):
        self.onLine=onLine


class DQ_DataQuality(object):
    def __init__(self,excel):
        self.excel=excel
        self.scope=None
        self.report=[]
        self.lineage=None
        
    def readExcel(self):
        if MD.hierarchyLevel=="dataset":
            lineage=FromExcel(excel.loc['lineage',['content_eng','content_fre','content_dut']])
            self.lineage=LI_Lineage(Content(lineage.EN, lineage.FR, lineage.NL))                        
            # self.scope=DQ_Scope(excel.loc['hierarchyLevel','URI'])
           
            if pandas.isnull(excel.loc['FREE_descriptiveKeywords','content_eng'])==False and "Reporting INSPIRE" in excel.loc['FREE_descriptiveKeywords','content_eng'].split("#") : #préciser URI exacte du reporting INSPIRE dans les keywords du thésaurus régional
                testResult="false"
                explanation=Content(u"The dataset does not fullfill the minimal requirements",u"Le jeu de données ne répond pas aux exigences minimales prédécrites", u"De dataset volgt niet de minimale vereissen")
                if excel.loc['passINSPIRE','URI']==1 :
                    explanation=Content(u"The dataset does fullfill the minimal requirements",u"Le jeu de données répond aux exigences minimales prédécrites", u"De dataset volgt de minimale vereissen")
                    testResult="true"
                testINSPIRE = CI_Citation(Content(u"Commission regulation (EU) No 1089/2010 of 23 November 2010 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards interoperability of spatial data sets and services", 
                u"Règlement (UE) No 1089/2010 de la Commission du 23 novembre 2010 portant modalités d'application de la directive 2007/2/CE du Parlement européen et du Conseil en ce qui concerne l'interopérabilité des séries et des services de données géographiques",
                u"Verordening (UE) Nr.1089/2010 van de Commissie van 23 november 2010 ter uitvoering van Richtlijn 2007/2/EG van het Europees Parlement en de Raad betreffende de interoperabiliteit van verzamelingen ruimtelijke gegevens en van diensten met betrekking tot ruimtelijke gegevens", 
                "http://data.europa.eu/eli/reg/2010/1089") , [CI_Date('2008-12-08', 'publication')])

                report=DomainConsistency(DQ_ConformanceResult(testINSPIRE, testResult, explanation))
                self.report.append(report) 
                self.scope=DQ_Scope(excel.loc['hierarchyLevel','URI']) #à implémenter
                
                
            else:
                if pandas.isnull(excel.loc['Specifications','content_eng'])==False and pandas.isnull(excel.loc['Specifications','content_fre'])==False and pandas.isnull(excel.loc['Specifications','content_dut'])==False :       
                    specInterne = CI_Citation(Content(u"Technical specifications of the product", u"Spécifications techniques du produit", u"Technische specificaties van het product"), [CI_Date(str(excel.loc['creationdate','URI']),'publication' )])
                    explanation=FromExcel(excel.loc['Specifications',['content_eng','content_fre','content_dut']])
                    explanation=Content(explanation.EN, explanation.FR, explanation.NL)
                    report=DomainConsistency(DQ_ConformanceResult(specInterne, "true", explanation))
                    self.report.append(report)
                    self.scope=DQ_Scope(excel.loc['hierarchyLevel','URI']) #à implémenter

        elif  MD.hierarchyLevel=="service" : #politique CIRB = webservices uniquement INSPIRE compliant (à part les applications pour lesquelles c'est sans objet)
            testINSPIRE = CI_Citation (Content(u"COMMISSION REGULATION (EU) No 976/2009 of 19 October 2009 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards the Network Services", 
            u"Règlement (UE) N° 976/2009 de la Commission du 19 octobre 2009 portant modalités d'application de la directive 2007/2/CE du Parlement européen et du Conseil en ce qui concerne les services en réseau",
            u"Verordening (EU) n r. 976/2009 van de Commissie van 19 oktober 2009 tot uitvoering van Richtlijn 2007/2/EG van het Europees Parlement en de Raad wat betreft de netwerkdiensten",
            "http://data.europa.eu/eli/reg/2009/976") , [CI_Date('2009-08-19', 'publication')])
            explanation=Content(u"The service does fullfill the minimal requirements",u"Le service répond aux exigences minimales prédécrites", u"De dataset service de minimale vereissen")
            report=DomainConsistency(DQ_ConformanceResult(testINSPIRE, "true", explanation))
            self.report.append(report)
            if self.excel.loc['serviceType','URI'] == 'download':
               serviceDescription=Content(u'Download service', u'Service de téléchargement', u'Downloaddienst')            
            if self.excel.loc['serviceType','URI'] == 'view':
                serviceDescription=Content(u'View service', u'Service de consultation', u'Raadpleegdienst')            
            if self.excel.loc['serviceType','URI'] == 'search':
                serviceDescription=Content(u'Search service', u'Service de découverte', u'Zoekdienst')
            if self.excel.loc['serviceType', 'URI'] == 'geolocation':
                serviceDescription = Content(u'Geolocation service', u'Service de géolocalisation', u'Geolocatiedienst')
            self.scope=DQ_Scope('service', serviceDescription) #à implémenter
        else:
            MD.dataQualityInfo=None

class DQ_Scope(object):
    def __init__(self,level,levelDescription=None):
        self.level=level
        self.levelDescription=levelDescription


class DomainConsistency(object):
    def __init__(self,result,nameOfMeasure=None):
        self.nameOfMeasure=nameOfMeasure
        self.result=result


class DQ_ConformanceResult(object):
    def __init__(self,specification,passtest, explanation=None):
        self.specification=specification
        self.passtest=passtest
        self.explanation=explanation
        
        
class MD_ScopeDescription(object):
    def __init__(self,other):
        self.other=other

class LI_Lineage(object):
    def __init__(self,statement):
        self.statement=statement

LI_Lineage ("test")
    
######### Elements de métadonnées propre au profil régional bruxellois --> instances hardcodées ici #############"



locales=[PT_Locale("FR", "fre", "utf8"), PT_Locale("NL", "dut", "utf8"), PT_Locale("EN", "eng", "utf8")]

metadataStandardName=Content(u"Brussels INSPIRE metadata profil", u"Profil bruxellois de métadonnées", u"Brusselse INSPIRE metadata profiel")
extent=EX_Extent(Content(u'Brussels-Capital Region',u'Région de Bruxelles-Capitale', u'Brussel Hoofstedelijk Gewest'), EX_GeographicBoundingBox('4.24', '4.55', '50.70', '50.95'))
csw="https://geobru-geonetwork.irisnet.be/geonetwork/srv/fre/csw?Request=GetRecordById&Service=CSW&Version=2.0.2&elementSetName=full&outputSchema=http://www.isotc211.org/2005/gmd&id="

typerecord=input("which type of record do you want to create : dataset or service?")


yy = str(time.strftime("%Y"))
mm = str(time.strftime("%m"))
dd=str(time.strftime("%d"))
hour=str(time.strftime("%H"))
min=str(time.strftime("%M"))
sec=str(time.strftime("%S"))
dateStamp=yy+"-"+mm+"-"+dd+"T"+hour+":"+min+":"+sec
folder=typerecord+"_OK"
files = os.listdir(localisation_script+"\\"+"Metadata"+"\\"+folder)


for file in files:
    print (file)
    excel=pandas.ExcelFile(localisation_script+"\\"+"Metadata"+"\\"+folder+"\\"+str(file)).parse(sheet_name='Sheet1', index_col ='Mnemotique', na_values='',  encoding='utf-8', decimal=".", dtype=str)
    excel.fillna(0)
    MD=MD_Metadata(excel)
    session=requests.Session()
    MD.readExcel()
    MyMetadata=readISO19139.MD_Metadata(MD_MetadataXML, "MD_Metadata")    
    MyMetadata.create(MD)
    newxml = etree.ElementTree(MyMetadata.xml.getroot())
    createdFile = localisation_script + "\\"+MD.uuid+".xml"
    newxml.write(createdFile, xml_declaration=True, encoding='UTF-8')
    with open(createdFile, 'r', encoding="utf-8") as f:
        newxml = f.read()
    UploadSession.upload_record(newxml)
    os.remove(createdFile)
    
    
yy = str(time.strftime("%Y"))
mm = str(time.strftime("%m"))
dd=str(time.strftime("%d"))
hour=str(time.strftime("%H"))
min=str(time.strftime("%M"))
sec=str(time.strftime("%S"))
dateStamp2=yy+"-"+mm+"-"+dd+"T"+hour+":"+min+":"+sec

print ("CONSUMED TIME", dateStamp2, dateStamp)
