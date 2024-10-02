# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# readXML.py
# Created on: 31 January 2022 by benoit fricheteau
# edited on: 
#
# Parameter: none
# 
# ---------------------------------------------------------------------------

from lxml import etree
import os
import inspect
import copy
import pandas

localisation_script=localisation_script = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
templates=localisation_script+"\\"+"templates"


CharacterStringXML=templates+"\\"+"CharacterString.xml"
IntegerXML=templates+"\\"+"Integer.xml"
DistanceXML=templates+"\\"+"Distance.xml"
BooleanXML=templates+"\\"+"Boolean.xml"
LocalisedCharacterStringXML=templates+"\\"+"LocalisedCharacterString.xml"
MD_MetadataXML=templates+"\\"+"MD_Metadata.xml"
DateTimeXML=templates+"\\"+"DateTime.xml"
DateXML=templates+"\\"+"Date.xml"
PT_LocaleXML=templates+"\\"+"PT_Locale.xml"
CI_ResponsiblePartyXML=templates+"\\"+"CI_ResponsibleParty.xml"
CI_ContactXML=templates+"\\"+"CI_Contact.xml"
CI_CitationXML=templates+"\\"+"CI_Citation.xml"
CI_DateXML=templates+"\\"+"CI_Date.xml"
RS_IdentifierXML=templates+"\\"+"RS_Identifier.xml"
CI_AddressXML=templates+"\\"+"CI_Address.xml"
CI_OnlineResourceXML=templates+"\\"+"CI_OnlineResource.xml"
MD_ResolutionXML=templates+"\\"+"MD_Resolution.xml"
MD_RepresentativeFractionXML=templates+"\\"+"MD_RepresentativeFraction.xml"
MD_KeywordsXML=templates+"\\"+"MD_Keywords.xml"
MD_LegalConstraintsXML=templates+"\\"+"MD_LegalConstraints.xml"
MD_BrowseGraphicXML=templates+"\\"+"MD_BrowseGraphic.xml"
EX_GeographicBoundingBoxXML=templates+"\\"+"EX_GeographicBoundingBox.xml"
EX_ExtentXML=templates+"\\"+"EX_Extent.xml"
URLXML=templates+"\\"+"URL.xml"
MD_DataIdentificationXML=templates+"\\"+"MD_DataIdentification.xml"
MD_DistributionXML=templates+"\\"+"MD_Distribution.xml"
MD_FormatXML=templates+"\\"+"MD_Format.xml"
MD_DigitalTransferOptionsXML=templates+"\\"+"MD_DigitalTransferOptions.xml"
DQ_DataQualityXML=templates+"\\"+"DQ_DataQuality.xml"
DQ_ScopeXML=templates+"\\"+"DQ_Scope.xml"
DQ_DomainConsistencyXML=templates+"\\"+"DQ_DomainConsistency.xml"
DQ_ConformanceResultXML=templates+"\\"+"DQ_ConformanceResult.xml"
MD_ScopeDescriptionXML=templates+"\\"+"MD_ScopeDescription.xml"
MD_ScopeCodeXML=templates+"\\"+"MD_ScopeCode.xml"
MD_CharacterSetCodeXML=templates+"\\"+"MD_CharacterSetCode.xml"
LanguageCodeXML=templates+"\\"+"LanguageCode.xml"
PT_FreeTextXML=templates+"\\"+"PT_FreeText.xml"
CI_OnLineFunctionCodeXML=templates+"\\"+"CI_OnLineFunctionCode.xml"
MD_MaintenanceInformationXML=templates+"\\"+"MD_MaintenanceInformation.xml"
DecimalXML=templates+"\\"+"Decimal.xml"
LI_LineageXML=templates+"\\"+"LI_Lineage.xml"
MD_ReferenceSystemXML=templates+"\\"+"MD_ReferenceSystem.xml"
SV_ServiceIdentificationXML=templates+"\\"+"SV_ServiceIdentification.xml"
LocalNameXML=templates+"\\"+"LocalName.xml"
SV_OperationMetadataXML=templates+"\\"+"SV_OperationMetadata.xml"
SV_CoupledResourceXML=templates+"\\"+"SV_CoupledResource.xml"
MD_TopicCategoryCodeXML=templates+"\\"+"MD_TopicCategoryCode.xml"




schemas = {
    "gmd": "http://"+"www.isotc211.org/2005/gmd",
    "gco": "http://"+"www.isotc211.org/2005/gco",
    "gmx": "http://"+"www.isotc211.org/2005/gmx",
    "xlink": "http://www.w3.org/1999/xlink",
    'atom': "http://www.w3.org/2005/Atom",
    'wfs': "http://www.opengis.net/wfs/2.0",
    'srv': 'http://www.isotc211.org/2005/srv',
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'spdx':"http://spdx.org/rdf/terms#",
    'owl':"http://www.w3.org/2002/07/owl#",
    'dc':"http://purl.org/dc/elements/1.1/",
    'adms':"http://www.w3.org/ns/adms#",
    'xs':"http://www.w3.org/2001/XMLSchema",
    'sr':"http://www.w3.org/2005/sparql-results#",
    'locn':"http://www.w3.org/ns/locn#",
    'xsi':"http://www.w3.org/2001/XMLSchema-instance",
    'rdfs':"http://www.w3.org/2000/01/rdf-schema#",
    'foaf':"http://xmlns.com/foaf/0.1/",
    'fn':"http://www.w3.org/2005/xpath-functions",
    'dct':"http://purl.org/dc/terms/",
    'gco':"http://www.isotc211.org/2005/gco",
    'vcard':"http://www.w3.org/2006/vcard/ns#",
    'dcat':"http://www.w3.org/ns/dcat#",
    'schema':"http://schema.org/",
    'dqv':"http://www.w3.org/ns/dqv#",
    'geodcat':"http://data.europa.eu/930/",
    'xml':'http://www.w3.org/XML/1998/namespace',
    'skos':"http://www.w3.org/2004/02/skos/core#"
}


def findpreflabel (URI, language):
        concept=etree.parse(URI)
        
        preflabel=concept.xpath('//skos:prefLabel[@xml:lang=' +"'" + language +"']", namespaces=schemas)[0]
        return preflabel.text

def findinScheme (URI):
        concept=etree.parse(URI)
        
        inScheme=concept.xpath('//skos:inScheme', namespaces=schemas)[0]
        return inScheme.get("{"+schemas['rdf']+"}"+'resource')
        
        
        
class genericalClass(object):           #ajouter une fonction pour détruire les balises correspondant à des attributs spécifiés (i.e. balises vides)
    def __init__(self, xmlinput, PathFileExcel):
        self.xml=etree.parse(xmlinput)
        self.PATHfile=PathFileExcel
        self.Path=pandas.read_excel(localisation_script+"\\"+"templates"+"\\"+"19139Paths.xlsx", sheet_name=self.PATHfile, index_col ='Mnemotique')
    def MultilingualTag (self, tag, python):
        if python is not None:
            self.tag=tag
            input=CharacterString(CharacterStringXML, "CharacterString")
            input.create(python)
            self.tag.insert(0, input.CharacterString[0])
            if python.FR is not None:
                self.tag.set("{"+schemas['xsi']+"}"+'type',"gmd:PT_FreeText_PropertyType")
                input=PT_FreeText(PT_FreeTextXML, "PT_FreeText")
                input.create(python)
                self.tag.insert(1, input.PT_FreeText[0])       
    
    def MultiplyTag (self, attribute, number):
        value=getattr(self,attribute)
        self.tag=value[0]
        i=self.tag.getparent().index(self.tag)
        copie=copy.deepcopy(self.tag)
        self.parent=self.tag.getparent()
        self.parent.remove(self.tag)
        for j in number : 
            local=copy.deepcopy(copie)
            self.parent.insert(i, local)
        setattr(self, attribute, self.xml.xpath(self.Path.loc[attribute,'XPATH'],namespaces=schemas))

    def CodeListClass(self, attribute, Class, codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#", nameSpace="gmd",  codeValue=None,):
        if codeValue is not None:
        
            self.tag=attribute
            self.Class=etree.Element('{'+schemas[nameSpace]+'}'+Class)
            self.Class.set('codeListValue',codeValue)
            self.Class.set('codeList',codeList)            
            if codeList=="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#":
                codeList=codeList+Class
            self.tag.insert(0, self.Class)


    
    def deleteEmpytTags(self):
        emptyTags=self.xml.xpath('//*[not(text()) and not(@*) and not(node())]', namespaces=schemas)
        for tag in emptyTags:
            tag.getparent().remove(tag)
            


class CharacterString(genericalClass):
    def __init__(self, xmlinput, PathFileExcel):
        super(CharacterString, self).__init__(xmlinput,PathFileExcel)
        self.CharacterString=self.xml.xpath(self.Path.loc['CharacterString','XPATH'],namespaces=schemas)        

    def create(self,python): 
        self.CharacterString[0].text=python.EN
        if python.URI is not None :
            self.CharacterString[0].tag="{"+schemas["gmx"]+"}"+"Anchor"
            self.CharacterString[0].set("{"+schemas['xlink']+"}"+'href',python.URI)
        if python.type is not None:
            self.CharacterString[0].tag="{"+schemas["gmx"]+"}"+"MimeFileType"
            self.CharacterString[0].set('type',python.type)
            
class Integer(genericalClass):
    def __init__(self, xmlinput, PathFileExcel):
    
        super(Integer, self).__init__(xmlinput,PathFileExcel)
        self.Integer=self.xml.xpath(self.Path.loc['Integer','XPATH'],namespaces=schemas)        

    def create(self,python):    
        self.Integer[0].text=python 
        
class Decimal(genericalClass):
    def __init__(self, xmlinput, PathFileExcel):
        super(Decimal, self).__init__(xmlinput,PathFileExcel)
        self.Decimal=self.xml.xpath(self.Path.loc['Decimal','XPATH'],namespaces=schemas)        

    def create(self,python):    
        self.Decimal[0].text=python 
        
        
class Distance (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(Distance, self).__init__(xmlinput,PathFileExcel)
        self.Distance=self.xml.xpath(self.Path.loc['Distance','XPATH'],namespaces=schemas)        

        
    def create(self,python):    
        self.Distance[0].text=python
        self.Distance[0].set('uom', 'm')
        
class Boolean (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(Boolean, self).__init__(xmlinput,PathFileExcel)
        self.Boolean=self.xml.xpath(self.Path.loc['Boolean','XPATH'],namespaces=schemas)        

        
    def create(self,python):    
        self.Boolean[0].text=python 
   
        
class LocalisedCharacterString(genericalClass):

    def __init__(self, xmlinput, PathFileExcel):
        super(LocalisedCharacterString, self).__init__(xmlinput,PathFileExcel)
        self.LocalisedCharacterString=self.xml.xpath(self.Path.loc['LocalisedCharacterString','XPATH'],namespaces=schemas)        

    def create(self,language, text):    
        self.LocalisedCharacterString[0].text=text                 
        self.LocalisedCharacterString[0].set('locale',language)

class PT_FreeText(genericalClass):     
    def __init__(self, xmlinput, PathFileExcel):    
        super(PT_FreeText, self).__init__(xmlinput,PathFileExcel)
        self.PT_FreeText=self.xml.xpath(self.Path.loc['PT_FreeText','XPATH'],namespaces=schemas)        
        self.textGroup=self.xml.xpath(self.Path.loc['textGroup','XPATH'], namespaces=schemas)[0]    
    def create(self,python):
        copie=copy.deepcopy(self.textGroup)
        self.PT_FreeText[0].remove(self.textGroup)
        for lang in ['EN', 'FR', 'NL']:
            local=copy.deepcopy(copie)               
            input=LocalisedCharacterString(LocalisedCharacterStringXML, "LocalisedCharacterString")
            input.create("#"+lang,getattr(python,lang))
            local.insert(0, input.LocalisedCharacterString[0]) 
            self.PT_FreeText[0].insert(0,local)

    
class MD_Metadata (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(MD_Metadata, self).__init__(xmlinput,PathFileExcel)
        self.MD_Metadata=self.xml.xpath(self.Path.loc['MD_Metadata','XPATH'],namespaces=schemas)        
        self.fileIdentifier=self.xml.xpath(self.Path.loc['fileIdentifier','XPATH'], namespaces=schemas)
        self.language=self.xml.xpath(self.Path.loc['language','XPATH'], namespaces=schemas)
        self.characterSet=self.xml.xpath(self.Path.loc['characterSet','XPATH'], namespaces=schemas)
        self.hierarchyLevel=self.xml.xpath(self.Path.loc['hierarchyLevel','XPATH'], namespaces=schemas)
        self.hierarchyLevelName=self.xml.xpath(self.Path.loc['hierarchyLevelName','XPATH'], namespaces=schemas)
        self.contact=self.xml.xpath(self.Path.loc['contact','XPATH'], namespaces=schemas)
        self.dateStamp=self.xml.xpath(self.Path.loc['dateStamp','XPATH'], namespaces=schemas)
        self.metadataStandardName=self.xml.xpath(self.Path.loc['metadataStandardName','XPATH'], namespaces=schemas)
        self.metadataStandardVersion=self.xml.xpath(self.Path.loc['metadataStandardVersion','XPATH'], namespaces=schemas)
        self.locale=self.xml.xpath(self.Path.loc['locale','XPATH'], namespaces=schemas)
        self.identificationInfo=self.xml.xpath(self.Path.loc['identificationInfo','XPATH'], namespaces=schemas)
        self.distributionInfo=self.xml.xpath(self.Path.loc['distributionInfo','XPATH'], namespaces=schemas)
        self.dataQualityInfo=self.xml.xpath(self.Path.loc['dataQualityInfo','XPATH'], namespaces=schemas)
        self.referenceSystemInfo=self.xml.xpath(self.Path.loc['referenceSystemInfo','XPATH'], namespaces=schemas)
        
    
    
    def create(self,python):    

        self.MultilingualTag(self.fileIdentifier[0], python.fileIdentifier)
        self.CodeListClass(self.language[0],"LanguageCode" ,"http://www.loc.gov/standards/iso639-2/", codeValue=python.language)
        self.CodeListClass(self.characterSet[0], "MD_CharacterSetCode", codeValue=python.characterSet)
        self.CodeListClass(self.hierarchyLevel[0],  "MD_ScopeCode", codeValue=python.hierarchyLevel)
        self.MultilingualTag(self.hierarchyLevelName[0], python.hierarchyLevelName)         
        input=CI_ResponsibleParty(CI_ResponsiblePartyXML, "CI_ResponsibleParty")
        input.create(python.contact)
        self.contact[0].insert(0, input.CI_ResponsibleParty[0])         
        input=DateTime(DateTimeXML, "DateTime")
        input.create(python.dateStamp)
        self.dateStamp[0].insert(0, input.DateTime[0])        
        self.MultilingualTag(self.metadataStandardName[0], python.metadataStandardName) 
        self.MultilingualTag(self.metadataStandardVersion[0], python.metadataStandardVersion)        
        i=self.MD_Metadata[0].index(self.locale[0])
        copie=copy.deepcopy(self.locale)        
        self.MultiplyTag('locale', range(len(python.locale)))       
        for i,j in zip(python.locale,self.locale):
            input=PT_Locale(PT_LocaleXML, "PT_Locale")
            input.create(i)
            j.insert(0, input.PT_Locale[0]) 
        if python.hierarchyLevel=="service":
            input=MD_DataIdentification(SV_ServiceIdentificationXML, "SV_ServiceIdentification")
            input.createService(python.identificationInfo)
        else:
            input=MD_DataIdentification(MD_DataIdentificationXML, "MD_DataIdentification")
            input.createDataset(python.identificationInfo)

        self.identificationInfo[0].insert(0, input.MD_DataIdentification[0])            
        input=MD_Distribution(MD_DistributionXML, "MD_Distribution")
        input.create(python.distributionInfo)
        self.distributionInfo[0].insert(0, input.MD_Distribution[0])
        if python.dataQualityInfo is not None:
        
            input=DQ_DataQuality(DQ_DataQualityXML, "DQ_DataQuality")
            input.create(python.dataQualityInfo)
            self.dataQualityInfo[0].insert(0, input.DQ_DataQuality[0])  
        
        if python.referenceSystemInfo is not None:
            self.MultiplyTag('referenceSystemInfo', range(len(python.referenceSystemInfo)))       
            for i,j in zip(python.referenceSystemInfo,self.referenceSystemInfo):
                input=MD_ReferenceSystem(MD_ReferenceSystemXML, "MD_ReferenceSystem")
                input.create(i)
                j.insert(0, input.MD_ReferenceSystem[0]) 
        self.deleteEmpytTags()  


class DateTime (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(DateTime, self).__init__(xmlinput,PathFileExcel)
        self.DateTime=self.xml.xpath(self.Path.loc['DateTime','XPATH'],namespaces=schemas)  
        
    def create(self,python):    
        self.DateTime[0].text=python
        
        
class Date (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(Date, self).__init__(xmlinput,PathFileExcel)
        self.Date=self.xml.xpath(self.Path.loc['Date','XPATH'],namespaces=schemas)  
        
    def create(self,python):    
        self.Date[0].text=python 


class MD_ReferenceSystem (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(MD_ReferenceSystem, self).__init__(xmlinput,PathFileExcel)
        self.MD_ReferenceSystem=self.xml.xpath(self.Path.loc['MD_ReferenceSystem','XPATH'],namespaces=schemas)  
        self.referenceSystemIdentifier=self.xml.xpath(self.Path.loc['referenceSystemIdentifier','XPATH'],namespaces=schemas)  
        
    def create(self,python):    
        input=RS_Identifier(RS_IdentifierXML, "RS_Identifier")
        input.create(python)
        self.referenceSystemIdentifier[0].insert(0, input.RS_Identifier[0])  

    
class PT_Locale (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(PT_Locale, self).__init__(xmlinput,PathFileExcel)
        self.PT_Locale=self.xml.xpath(self.Path.loc['PT_Locale','XPATH'],namespaces=schemas)  
        self.languageCode=self.xml.xpath(self.Path.loc['languageCode','XPATH'],namespaces=schemas)  
        self.characterEncoding=self.xml.xpath(self.Path.loc['characterEncoding','XPATH'],namespaces=schemas)  
        
    def create(self,python): 
        self.PT_Locale[0].set('id', python.internalID)
        self.CodeListClass(self.languageCode[0], "LanguageCode", "http://www.loc.gov/standards/iso639-2/", codeValue=python.languageCode)
        self.CodeListClass(self.characterEncoding[0], "MD_CharacterSetCode", codeValue=python.characterEncoding)     
        
        
class CI_ResponsibleParty (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(CI_ResponsibleParty, self).__init__(xmlinput,PathFileExcel)
        self.CI_ResponsibleParty=self.xml.xpath(self.Path.loc['CI_ResponsibleParty','XPATH'],namespaces=schemas)        
        self.individualName=self.xml.xpath(self.Path.loc['individualName','XPATH'], namespaces=schemas)
        self.organisationName=self.xml.xpath(self.Path.loc['organisationName','XPATH'], namespaces=schemas)
        self.contactInfo=self.xml.xpath(self.Path.loc['contactInfo','XPATH'], namespaces=schemas)
        self.role=self.xml.xpath(self.Path.loc['role','XPATH'], namespaces=schemas)

        
        
    def create(self,python):
        self.MultilingualTag(self.individualName[0], python.individualName)     
        self.MultilingualTag(self.organisationName[0], python.organisationName)
        input=CI_Contact(CI_ContactXML, "CI_Contact")
        input.create(python.contactInfo)
        self.contactInfo[0].insert(0, input.CI_Contact[0])        
        self.CodeListClass(self.role[0], "CI_RoleCode", codeValue=python.role)
        self.deleteEmpytTags()  


class CI_Contact (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(CI_Contact, self).__init__(xmlinput,PathFileExcel)
        self.CI_Contact=self.xml.xpath(self.Path.loc['CI_Contact','XPATH'],namespaces=schemas)        
        self.address=self.xml.xpath(self.Path.loc['address','XPATH'], namespaces=schemas)
        self.onlineResource=self.xml.xpath(self.Path.loc['onlineResource','XPATH'], namespaces=schemas)
        
        
    def create(self,python):    
        input=CI_Address(CI_AddressXML, "CI_Address")
        input.create(python.address)
        self.address[0].insert(0, input.CI_Address[0])
        input=CI_OnlineResource(CI_OnlineResourceXML, "CI_OnlineResource")
        input.create(python.onlineResource)
        self.onlineResource[0].insert(0, input.CI_OnlineResource[0])
        self.deleteEmpytTags()  

class CI_Citation (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(CI_Citation, self).__init__(xmlinput,PathFileExcel)
        self.CI_Citation=self.xml.xpath(self.Path.loc['CI_Citation','XPATH'],namespaces=schemas)        
        self.title=self.xml.xpath(self.Path.loc['title','XPATH'], namespaces=schemas)
        self.date=self.xml.xpath(self.Path.loc['date','XPATH'], namespaces=schemas)
        self.identifier=self.xml.xpath(self.Path.loc['identifier','XPATH'], namespaces=schemas)
        
        
    def create(self,python):    
        self.MultilingualTag(self.title[0], python.title)
        
                
        if python.date is not None:
            self.MultiplyTag('date', range(len(python.date)))
            for i,j in zip(python.date,self.date):
                input=CI_Date(CI_DateXML, "CI_Date")
                input.create(i)
                j.insert(0, input.CI_Date[0]) 
        
        if python.identifier is not None:
            input=RS_Identifier(RS_IdentifierXML, "RS_Identifier")
            input.create(python.identifier)
            self.identifier[0].insert(0, input.RS_Identifier[0])
        self.deleteEmpytTags()  

class CI_Date (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(CI_Date, self).__init__(xmlinput,PathFileExcel)
        self.CI_Date=self.xml.xpath(self.Path.loc['CI_Date','XPATH'],namespaces=schemas)        
        self.date=self.xml.xpath(self.Path.loc['date','XPATH'], namespaces=schemas)
        self.dateType=self.xml.xpath(self.Path.loc['dateType','XPATH'], namespaces=schemas)
        
        
    def create(self,python):  
        input=Date(DateXML, "Date")
        input.create(python.date)
        self.date[0].insert(0, input.Date[0])        
        self.CodeListClass(self.dateType[0], "CI_DateTypeCode"  , codeValue=python.dateType)
        
class RS_Identifier (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(RS_Identifier, self).__init__(xmlinput,PathFileExcel)
        self.RS_Identifier=self.xml.xpath(self.Path.loc['RS_Identifier','XPATH'],namespaces=schemas)        
        self.code=self.xml.xpath(self.Path.loc['code','XPATH'], namespaces=schemas)
        self.codeSpace=self.xml.xpath(self.Path.loc['codeSpace','XPATH'], namespaces=schemas)
        
        
    def create(self,python):    
        self.MultilingualTag(self.code[0], python.code)     
        self.MultilingualTag(self.codeSpace[0], python.codeSpace)   
        
class MD_MaintenanceInformation (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(MD_MaintenanceInformation, self).__init__(xmlinput,PathFileExcel)
        self.MD_MaintenanceInformation=self.xml.xpath(self.Path.loc['MD_MaintenanceInformation','XPATH'],namespaces=schemas)        
        self.maintenanceAndUpdateFrequency=self.xml.xpath(self.Path.loc['maintenanceAndUpdateFrequency','XPATH'], namespaces=schemas)
        
        
    def create(self,python):    
        self.CodeListClass(self.maintenanceAndUpdateFrequency[0], "MD_MaintenanceFrequencyCode", codeValue=python)

    
class CI_Address (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(CI_Address, self).__init__(xmlinput,PathFileExcel)
        self.CI_Address=self.xml.xpath(self.Path.loc['CI_Address','XPATH'],namespaces=schemas)        
        self.deliveryPoint=self.xml.xpath(self.Path.loc['deliveryPoint','XPATH'], namespaces=schemas)
        self.city=self.xml.xpath(self.Path.loc['city','XPATH'], namespaces=schemas)
        self.postalCode=self.xml.xpath(self.Path.loc['postalCode','XPATH'], namespaces=schemas)
        self.country=self.xml.xpath(self.Path.loc['country','XPATH'], namespaces=schemas)
        self.electronicMailAddress=self.xml.xpath(self.Path.loc['electronicMailAddress','XPATH'], namespaces=schemas)
        
        
    def create(self,python):    
        self.MultilingualTag(self.deliveryPoint[0], python.deliveryPoint)
        self.MultilingualTag(self.postalCode[0], python.postalCode)        
        self.MultilingualTag(self.city[0], python.city)
        self.MultilingualTag(self.country[0], python.country)
        self.MultilingualTag(self.electronicMailAddress[0], python.electronicMailAddress)
        self.deleteEmpytTags()  

        
class CI_OnlineResource (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(CI_OnlineResource, self).__init__(xmlinput,PathFileExcel)
        self.CI_OnlineResource=self.xml.xpath(self.Path.loc['CI_OnlineResource','XPATH'],namespaces=schemas)        
        self.linkage=self.xml.xpath(self.Path.loc['linkage','XPATH'], namespaces=schemas)
        self.name=self.xml.xpath(self.Path.loc['name','XPATH'], namespaces=schemas)
        self.protocol=self.xml.xpath(self.Path.loc['protocol','XPATH'], namespaces=schemas)
        self.description=self.xml.xpath(self.Path.loc['description','XPATH'], namespaces=schemas)
        self.function=self.xml.xpath(self.Path.loc['function','XPATH'], namespaces=schemas)
        
        
    def create(self,python):    
    
        input=URL(URLXML, "URL")
        input.create(python.linkage)
        self.linkage[0].insert(0, input.URL[0])
        # if python.function is not None:
        self.CodeListClass(self.function[0], "CI_OnLineFunctionCode", codeValue=python.function)
        self.MultilingualTag(self.name[0], python.name)
        self.MultilingualTag(self.protocol[0], python.protocol)        
        self.MultilingualTag(self.description[0], python.description)
        self.deleteEmpytTags()  

        
class MD_Resolution (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(MD_Resolution, self).__init__(xmlinput,PathFileExcel)
        self.MD_Resolution=self.xml.xpath(self.Path.loc['MD_Resolution','XPATH'],namespaces=schemas)        
        self.equivalentScale=self.xml.xpath(self.Path.loc['equivalentScale','XPATH'],namespaces=schemas)        
        self.distance=self.xml.xpath(self.Path.loc['distance','XPATH'],namespaces=schemas)        

        
    def create(self,python):    
        if python.equivalentScale is not None:
            input=MD_RepresentativeFraction(MD_RepresentativeFractionXML, "MD_RepresentativeFraction")
            input.create(python.equivalentScale)
            self.equivalentScale[0].insert(0, input.MD_RepresentativeFraction[0])        
       
        if python.distance is not None:
            input=Distance (DistanceXML, "Distance")
            input.create(python.distance)
            self.distance[0].insert(0, input.Distance[0])
        self.deleteEmpytTags()  

        
class MD_RepresentativeFraction (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(MD_RepresentativeFraction, self).__init__(xmlinput,PathFileExcel)
        self.MD_RepresentativeFraction=self.xml.xpath(self.Path.loc['MD_RepresentativeFraction','XPATH'],namespaces=schemas)        
        self.denominator=self.xml.xpath(self.Path.loc['denominator','XPATH'],namespaces=schemas)        

        
    def create(self,python):    
        input=Integer(IntegerXML, "Integer")
        input.create(python.denominator)
        self.denominator[0].insert(0, input.Integer[0])  
        self.deleteEmpytTags()  
        
        
class MD_Keywords (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(MD_Keywords, self).__init__(xmlinput,PathFileExcel)
        self.MD_Keywords=self.xml.xpath(self.Path.loc['MD_Keywords','XPATH'],namespaces=schemas)        
        self.keyword=self.xml.xpath(self.Path.loc['keyword','XPATH'],namespaces=schemas)
        self.type=self.xml.xpath(self.Path.loc['type','XPATH'],namespaces=schemas)        
        self.thesaurusName=self.xml.xpath(self.Path.loc['thesaurusName','XPATH'],namespaces=schemas)        

        
    def create(self,python): 

        self.MultiplyTag('keyword', range(len(python.keyword)))
        for i,j in zip(python.keyword,self.keyword):
            self.MultilingualTag(j,i)
        
        self.CodeListClass(self.type[0], "MD_KeywordTypeCode", codeValue=python.type)
        if python.thesaurusName is not None:

            input=CI_Citation(CI_CitationXML, "CI_Citation")
            input.create(python.thesaurusName)
            self.thesaurusName[0].insert(0, input.CI_Citation[0])  
        self.deleteEmpytTags()  
                
        
class MD_LegalConstraints (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(MD_LegalConstraints, self).__init__(xmlinput,PathFileExcel)
        self.MD_LegalConstraints=self.xml.xpath(self.Path.loc['MD_LegalConstraints','XPATH'],namespaces=schemas)        
        self.useConstraints=self.xml.xpath(self.Path.loc['useConstraints','XPATH'],namespaces=schemas)        
        self.accessConstraints=self.xml.xpath(self.Path.loc['accessConstraints','XPATH'],namespaces=schemas)        
        self.otherConstraints=self.xml.xpath(self.Path.loc['otherConstraints','XPATH'],namespaces=schemas)        

        
    def create(self,python):    
        self.CodeListClass(self.useConstraints[0], "MD_RestrictionCode" , codeValue=python.useConstraints)
        self.CodeListClass(self.accessConstraints[0], "MD_RestrictionCode" , codeValue=python.accessConstraints)
        self.MultilingualTag(self.otherConstraints[0], python.otherConstraints)
        self.deleteEmpytTags()  

            
class MD_BrowseGraphic (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(MD_BrowseGraphic, self).__init__(xmlinput,PathFileExcel)
        self.MD_BrowseGraphic=self.xml.xpath(self.Path.loc['MD_BrowseGraphic','XPATH'],namespaces=schemas)        
        self.fileName=self.xml.xpath(self.Path.loc['fileName','XPATH'],namespaces=schemas)       
        
    def create(self,python):    
        self.MultilingualTag(self.fileName[0], python.fileName)
        
class MD_TopicCategoryCode (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(MD_TopicCategoryCode, self).__init__(xmlinput,PathFileExcel)
        self.MD_TopicCategoryCode=self.xml.xpath(self.Path.loc['MD_TopicCategoryCode','XPATH'],namespaces=schemas)        
        
    def create(self,python):    
        self.MD_TopicCategoryCode[0].text=python
        

class SV_CoupledResource (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(SV_CoupledResource, self).__init__(xmlinput,PathFileExcel)
        self.SV_CoupledResource=self.xml.xpath(self.Path.loc['SV_CoupledResource','XPATH'],namespaces=schemas)        
        self.operationName=self.xml.xpath(self.Path.loc['operationName','XPATH'],namespaces=schemas)       
        self.identifier=self.xml.xpath(self.Path.loc['identifier','XPATH'],namespaces=schemas)       
        
    def create(self,python):    
        self.MultilingualTag(self.identifier[0], python.identifier)
        self.MultilingualTag(self.operationName[0], python.operationName)
        
class SV_OperationMetadata (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(SV_OperationMetadata, self).__init__(xmlinput,PathFileExcel)
        self.SV_OperationMetadata=self.xml.xpath(self.Path.loc['SV_OperationMetadata','XPATH'],namespaces=schemas)        
        self.operationName=self.xml.xpath(self.Path.loc['operationName','XPATH'],namespaces=schemas)       
        self.DCP=self.xml.xpath(self.Path.loc['DCP','XPATH'],namespaces=schemas)       
        self.connectPoint=self.xml.xpath(self.Path.loc['connectPoint','XPATH'],namespaces=schemas)       
        
    def create(self,python):    
        self.MultilingualTag(self.operationName[0], python.operationName)
        self.CodeListClass(self.DCP[0], "DCPList",nameSpace="srv", codeValue=python.DCP)
        input=CI_OnlineResource(CI_OnlineResourceXML, "CI_OnlineResource")
        input.create(python.connectPoint)
        self.connectPoint[0].insert(0, input.CI_OnlineResource[0])



        
        
class EX_GeographicBoundingBox (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(EX_GeographicBoundingBox, self).__init__(xmlinput,PathFileExcel)
        self.EX_GeographicBoundingBox=self.xml.xpath(self.Path.loc['EX_GeographicBoundingBox','XPATH'],namespaces=schemas)        
        self.westBoundLongitude=self.xml.xpath(self.Path.loc['westBoundLongitude','XPATH'],namespaces=schemas)        
        self.eastBoundLongitude=self.xml.xpath(self.Path.loc['eastBoundLongitude','XPATH'],namespaces=schemas)        
        self.southBoundLongitude=self.xml.xpath(self.Path.loc['southBoundLongitude','XPATH'],namespaces=schemas)        
        self.northBoundLongitude=self.xml.xpath(self.Path.loc['northBoundLongitude','XPATH'],namespaces=schemas)        

        
    def create(self,python):
        input=Decimal(DecimalXML, "Decimal")
        input.create(python.westBoundLongitude)
        self.westBoundLongitude[0].insert(0, input.Decimal[0])       
        input=Decimal(DecimalXML, "Decimal")
        input.create(python.eastBoundLongitude)
        self.eastBoundLongitude[0].insert(0, input.Decimal[0])              
        input=Decimal(DecimalXML, "Decimal")
        input.create(python.southBoundLongitude)
        self.southBoundLongitude[0].insert(0, input.Decimal[0])       
        input=Decimal(DecimalXML, "Decimal")
        input.create(python.northBoundLongitude)
        self.northBoundLongitude[0].insert(0, input.Decimal[0])      
    
        
class EX_Extent (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(EX_Extent, self).__init__(xmlinput,PathFileExcel)
        self.EX_Extent=self.xml.xpath(self.Path.loc['EX_Extent','XPATH'],namespaces=schemas)        
        self.description=self.xml.xpath(self.Path.loc['description','XPATH'],namespaces=schemas)        
        self.geographicElement=self.xml.xpath(self.Path.loc['geographicElement','XPATH'],namespaces=schemas)        

        
    def create(self,python):    
        self.MultilingualTag(self.description[0], python.description)
        input=EX_GeographicBoundingBox(EX_GeographicBoundingBoxXML, "EX_GeographicBoundingBox")
        input.create(python.geographicElement)
        self.geographicElement[0].insert(0, input.EX_GeographicBoundingBox[0])  

class URL (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(URL, self).__init__(xmlinput,PathFileExcel)
        self.URL=self.xml.xpath(self.Path.loc['URL','XPATH'],namespaces=schemas)   
    
    def create(self,python):        
        self.URL[0].text=python
       
class LocalName (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(LocalName, self).__init__(xmlinput,PathFileExcel)
        self.LocalName=self.xml.xpath(self.Path.loc['LocalName','XPATH'],namespaces=schemas)   
    
    def create(self,python):        
        self.LocalName[0].text=python
        self.LocalName[0].set("codeSpace", "http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceType")
        
        
class MD_DataIdentification (genericalClass):
     
    def __init__(self, xmlinput, PathFileExcel):
    
        super(MD_DataIdentification, self).__init__(xmlinput,PathFileExcel)
        self.MD_DataIdentification=self.xml.xpath(self.Path.loc[PathFileExcel,'XPATH'],namespaces=schemas)   
        self.citation=self.xml.xpath(self.Path.loc['citation','XPATH'],namespaces=schemas)
        self.abstract=self.xml.xpath(self.Path.loc['abstract','XPATH'],namespaces=schemas)   
        self.pointOfContact=self.xml.xpath(self.Path.loc['pointOfContact','XPATH'],namespaces=schemas)           
        self.resourceMaintenance=self.xml.xpath(self.Path.loc['resourceMaintenance','XPATH'],namespaces=schemas)   
        self.graphicOverview=self.xml.xpath(self.Path.loc['graphicOverview','XPATH'],namespaces=schemas)   
        self.descriptiveKeywords=self.xml.xpath(self.Path.loc['descriptiveKeywords','XPATH'],namespaces=schemas)   
        self.resourceConstraints=self.xml.xpath(self.Path.loc['resourceConstraints','XPATH'],namespaces=schemas)  
        self.extent=self.xml.xpath(self.Path.loc['extent','XPATH'],namespaces=schemas)  
    
    def _selectDatasetTags(self):
        self.status=self.xml.xpath(self.Path.loc['status','XPATH'],namespaces=schemas)   
        self.spatialRepresentationType=self.xml.xpath(self.Path.loc['spatialRepresentationType','XPATH'],namespaces=schemas)  
        self.spatialResolution=self.xml.xpath(self.Path.loc['spatialResolution','XPATH'],namespaces=schemas)   
        self.characterSet=self.xml.xpath(self.Path.loc['characterSet','XPATH'],namespaces=schemas)   
        self.language=self.xml.xpath(self.Path.loc['language','XPATH'],namespaces=schemas)   
        self.topicCategory=self.xml.xpath(self.Path.loc['topicCategory','XPATH'],namespaces=schemas)       
    
    def _selectServiceTags(self):
        self.serviceType=self.xml.xpath(self.Path.loc['serviceType','XPATH'],namespaces=schemas)   
        self.coupledResource=self.xml.xpath(self.Path.loc['coupledResource','XPATH'],namespaces=schemas)   
        self.couplingType=self.xml.xpath(self.Path.loc['couplingType','XPATH'],namespaces=schemas) 
        self.operatesOn=self.xml.xpath(self.Path.loc['operatesOn','XPATH'],namespaces=schemas)   
        self.containsOperations=self.xml.xpath(self.Path.loc['containsOperations','XPATH'],namespaces=schemas)   

    def _createCommon(self, python):
        input=CI_Citation(CI_CitationXML, "CI_Citation")
        input.create(python.citation)
        self.citation[0].insert(0, input.CI_Citation[0])        
        self.MultilingualTag(self.abstract[0], python.abstract)
        input=CI_ResponsibleParty(CI_ResponsiblePartyXML, "CI_ResponsibleParty")
        input.create(python.pointOfContact)
        self.pointOfContact[0].insert(0, input.CI_ResponsibleParty[0])                
        input=MD_MaintenanceInformation(MD_MaintenanceInformationXML, "MD_MaintenanceInformation")
        input.create(python.resourceMaintenance)
        self.resourceMaintenance[0].insert(0, input.MD_MaintenanceInformation[0]) 
        if python.graphicOverview is not None:        
            input=MD_BrowseGraphic(MD_BrowseGraphicXML, "MD_BrowseGraphic")
            input.create(python.graphicOverview)
            self.graphicOverview[0].insert(0, input.MD_BrowseGraphic[0])         
        self.MultiplyTag('descriptiveKeywords', range(len(python.descriptiveKeywords)))
        for i,j in zip(python.descriptiveKeywords,self.descriptiveKeywords):
            input=MD_Keywords(MD_KeywordsXML, "MD_Keywords")
            input.create(i)
            j.insert(0, input.MD_Keywords[0])
        self.MultiplyTag('resourceConstraints', range(len(python.resourceConstraints)))
        for i,j in zip(python.resourceConstraints,self.resourceConstraints):
            input=MD_LegalConstraints(MD_LegalConstraintsXML, "MD_LegalConstraints")
            input.create(i)
            j.insert(0, input.MD_LegalConstraints[0])
            
        input=EX_Extent(EX_ExtentXML, "EX_Extent")
        input.create(python.extent)
        self.extent[0].insert(0, input.EX_Extent[0])
    
    def createDataset(self,python):        
        self._createCommon(python)
        self._selectDatasetTags()
        self.CodeListClass(self.status[0], "MD_ProgressCode", codeValue=python.status)
        self.CodeListClass(self.spatialRepresentationType[0], "MD_SpatialRepresentationTypeCode" , codeValue=python.spatialRepresentationType)
        if python.spatialResolution is not None:
            input=MD_Resolution(MD_ResolutionXML, "MD_Resolution")
            input.create(python.spatialResolution)
            self.spatialResolution[0].insert(0, input.MD_Resolution[0]) 
        if python.characterSet is not None:
            self.MultiplyTag('characterSet', range(len(python.characterSet)))
            for i,j in zip(python.characterSet,self.characterSet) :
                self.CodeListClass(j, "MD_CharacterSetCode" , codeValue=i)        
        self.MultiplyTag('language', range(len(python.language)))
        for i,j in zip(python.language,self.language) :
            self.CodeListClass(j, "LanguageCode" , "http://www.loc.gov/standards/iso639-2/", codeValue=i)
        # self.CodeListClass(self.topicCategory[0], "MD_TopicCategoryCode", codeValue=python.topicCategory)  
        input=MD_TopicCategoryCode(MD_TopicCategoryCodeXML, "MD_TopicCategoryCode")
        input.create(python.topicCategory)
        self.topicCategory[0].insert(0, input.MD_TopicCategoryCode[0]) 
        self.deleteEmpytTags()  

    def createService(self,python):        
        self._createCommon(python)
        self._selectServiceTags()
        input=LocalName(LocalNameXML, "LocalName")
        input.create(python.serviceType)
        self.serviceType[0].insert(0, input.LocalName[0])         
        self.MultiplyTag('coupledResource', range(len(python.coupledResource)))
        for i,j in zip(python.coupledResource,self.coupledResource) :
            input=SV_CoupledResource(SV_CoupledResourceXML, "SV_CoupledResource")
            input.create(i)
            j.insert(0, input.SV_CoupledResource[0]) 
            
        input=SV_OperationMetadata(SV_OperationMetadataXML, "SV_OperationMetadata")
        input.create(python.containsOperations)
        self.containsOperations[0].insert(0, input.SV_OperationMetadata[0])  

        self.CodeListClass(self.couplingType[0], "SV_CouplingType",  nameSpace="srv", codeValue=python.couplingType)     
        self.MultiplyTag('operatesOn', range(len(python.operatesOn)))
        for i,j in zip(python.operatesOn,self.operatesOn) :
            j.set('uuidref', i)
            j.set("{"+schemas['xlink']+'}href', python.csw+i) #construire une vraie requête http au lieu de concaténer
        self.deleteEmpytTags()  


        
        
class MD_Distribution(genericalClass):
    def __init__(self, xmlinput, PathFileExcel):
    
        super(MD_Distribution, self).__init__(xmlinput,PathFileExcel)
        self.MD_Distribution=self.xml.xpath(self.Path.loc['MD_Distribution','XPATH'],namespaces=schemas)   
        self.distributionFormat=self.xml.xpath(self.Path.loc['distributionFormat','XPATH'],namespaces=schemas)   
        self.transferOptions=self.xml.xpath(self.Path.loc['transferOptions','XPATH'],namespaces=schemas)   
    
    def create(self,python):
        if python.distributionFormat is not None:
            self.MultiplyTag('distributionFormat', range(len(python.distributionFormat)))
            for i,j in zip(python.distributionFormat,self.distributionFormat):
                input=MD_Format(MD_FormatXML, "MD_Format")
                input.create(i)
                j.insert(0, input.MD_Format[0])        
            
        self.MultiplyTag('transferOptions', range(len(python.transferOptions)))
        for i,j in zip(python.transferOptions,self.transferOptions):
            input=MD_DigitalTransferOptions(MD_DigitalTransferOptionsXML, "MD_DigitalTransferOptions")
            input.create(i)
            j.insert(0, input.MD_DigitalTransferOptions[0]) 
        self.deleteEmpytTags()  

            
class MD_Format(genericalClass):
    def __init__(self, xmlinput, PathFileExcel):
    
        super(MD_Format, self).__init__(xmlinput,PathFileExcel)
        self.MD_Format=self.xml.xpath(self.Path.loc['MD_Format','XPATH'],namespaces=schemas)   
        self.name=self.xml.xpath(self.Path.loc['name','XPATH'],namespaces=schemas)   
        self.version=self.xml.xpath(self.Path.loc['version','XPATH'],namespaces=schemas)   
    
    def create(self,python): 
        self.MultilingualTag(self.name[0], python.name)
        if python.version is not None:
            self.MultilingualTag(self.version[0], python.version)
        else:
            self.version[0].set("{"+schemas["gco"]+"}"+"nilReason","inapplicable")
        self.deleteEmpytTags()  

class MD_DigitalTransferOptions(genericalClass):
    def __init__(self, xmlinput, PathFileExcel):
    
        super(MD_DigitalTransferOptions, self).__init__(xmlinput,PathFileExcel)
        self.MD_DigitalTransferOptions=self.xml.xpath(self.Path.loc['MD_DigitalTransferOptions','XPATH'],namespaces=schemas)   
        self.onLine=self.xml.xpath(self.Path.loc['onLine','XPATH'],namespaces=schemas)   
    
    def create(self,python):
        input=CI_OnlineResource(CI_OnlineResourceXML, "CI_OnlineResource")
        input.create(python.onLine)
        self.onLine[0].insert(0, input.CI_OnlineResource[0])
        self.deleteEmpytTags()  
       

class LI_Lineage(genericalClass):
    def __init__(self, xmlinput, PathFileExcel):
    
        super(LI_Lineage, self).__init__(xmlinput,PathFileExcel)
        self.LI_Lineage=self.xml.xpath(self.Path.loc['LI_Lineage','XPATH'],namespaces=schemas)   
        self.statement=self.xml.xpath(self.Path.loc['statement','XPATH'],namespaces=schemas)   
    
    def create(self,python):
        self.MultilingualTag(self.statement[0], python.statement)

        
class DQ_DataQuality(genericalClass):
    def __init__(self, xmlinput, PathFileExcel):
    
        super(DQ_DataQuality, self).__init__(xmlinput,PathFileExcel)
        self.DQ_DataQuality=self.xml.xpath(self.Path.loc['DQ_DataQuality','XPATH'],namespaces=schemas)   
        self.scope=self.xml.xpath(self.Path.loc['scope','XPATH'],namespaces=schemas)   
        self.report=self.xml.xpath(self.Path.loc['report','XPATH'],namespaces=schemas)   
        self.lineage=self.xml.xpath(self.Path.loc['lineage','XPATH'],namespaces=schemas)   
    
    def create(self,python):
        if python.scope is not None:
        

            input=DQ_Scope(DQ_ScopeXML, "DQ_Scope")
            input.create(python.scope)
            self.scope[0].insert(0, input.DQ_Scope[0])       
        if python.report is not None:
            self.MultiplyTag('report', range(len(python.report)))
            for i,j in zip(python.report,self.report):
                input=DQ_DomainConsistency(DQ_DomainConsistencyXML, "DQ_DomainConsistency")
                input.create(i)
                j.insert(0, input.DQ_DomainConsistency[0]) 
        if python.lineage is not None:
            input=LI_Lineage(LI_LineageXML, "LI_Lineage")
            input.create(python.lineage)
            self.lineage[0].insert(0, input.LI_Lineage[0])
        self.deleteEmpytTags()  

        
class DQ_Scope(genericalClass):
    def __init__(self, xmlinput, PathFileExcel):
    
        super(DQ_Scope, self).__init__(xmlinput,PathFileExcel)
        self.DQ_Scope=self.xml.xpath(self.Path.loc['DQ_Scope','XPATH'],namespaces=schemas)   
        self.level=self.xml.xpath(self.Path.loc['level','XPATH'],namespaces=schemas)   
        self.levelDescription=self.xml.xpath(self.Path.loc['levelDescription','XPATH'],namespaces=schemas)   
    
    def create(self,python):
        self.CodeListClass(self.level[0], "MD_ScopeCode", codeValue=python.level)
        if python.levelDescription is not None:
            input=MD_ScopeDescription(MD_ScopeDescriptionXML, "MD_ScopeDescription")
            input.create(python.levelDescription)
            self.levelDescription[0].insert(0, input.MD_ScopeDescription[0])
        self.deleteEmpytTags()  
        
        
class DQ_DomainConsistency(genericalClass):
    def __init__(self, xmlinput, PathFileExcel):
    
        super(DQ_DomainConsistency, self).__init__(xmlinput,PathFileExcel)
        self.DQ_DomainConsistency=self.xml.xpath(self.Path.loc['DQ_DomainConsistency','XPATH'],namespaces=schemas)   
        self.nameOfMeasure =self.xml.xpath(self.Path.loc['nameOfMeasure','XPATH'],namespaces=schemas)   
        self.result=self.xml.xpath(self.Path.loc['result','XPATH'],namespaces=schemas)   
    
    def create(self,python):
        self.MultilingualTag(self.nameOfMeasure[0], python.nameOfMeasure)
        input=DQ_ConformanceResult(DQ_ConformanceResultXML, "DQ_ConformanceResult")
        input.create(python.result)
        self.result[0].insert(0, input.DQ_ConformanceResult[0]) 
        self.deleteEmpytTags()  
       
class DQ_ConformanceResult(genericalClass):
    def __init__(self, xmlinput, PathFileExcel):
    
        super(DQ_ConformanceResult, self).__init__(xmlinput,PathFileExcel)
        self.DQ_ConformanceResult=self.xml.xpath(self.Path.loc['DQ_ConformanceResult','XPATH'],namespaces=schemas)   
        self.specification =self.xml.xpath(self.Path.loc['specification','XPATH'],namespaces=schemas)   
        self.passtest=self.xml.xpath(self.Path.loc['passtest','XPATH'],namespaces=schemas)   
        self.explanation=self.xml.xpath(self.Path.loc['explanation','XPATH'],namespaces=schemas)   
    
    def create(self,python):
        input=CI_Citation(CI_CitationXML, "CI_Citation")
        input.create(python.specification)
        self.specification[0].insert(0, input.CI_Citation[0]) 
        
        input=Boolean (BooleanXML, "Boolean")
        input.create(python.passtest)
        self.passtest[0].insert(0, input.Boolean[0])
        
        self.MultilingualTag(self.explanation[0], python.explanation)
        self.deleteEmpytTags()  

class MD_ScopeDescription(genericalClass):
    def __init__(self, xmlinput, PathFileExcel):
    
        super(MD_ScopeDescription, self).__init__(xmlinput,PathFileExcel)
        self.MD_ScopeDescription=self.xml.xpath(self.Path.loc['MD_ScopeDescription','XPATH'],namespaces=schemas)   
        self.other=self.xml.xpath(self.Path.loc['other','XPATH'],namespaces=schemas)   
    
    def create(self,python):
        self.MultilingualTag(self.other[0], python)
        self.deleteEmpytTags()  
      






    