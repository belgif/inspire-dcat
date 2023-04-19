**Table of content**

- [Federal DCAT AP profile](#federal-dcat-ap-profile)
  - [Introduction](#introduction)
  - [II. Detailed presentation of the classes](#ii-detailed-presentation-of-the-classes)
    - [A.	Class dcat:Catalog](#aclass-dcatcatalog)
      - [Class profile](#class-profile)
      - [Instantiation from [INSPIRE] elements](#instantiation-from-inspire-elements)
      - [Instantiation without [INSPIRE] element](#instantiation-without-inspire-element)
    - [B. Class dcat: Dataset](#b-class-dcat-dataset)
      - [Class profile](#class-profile-1)
      - [Instantiation from [INSPIRE] elements](#instantiation-from-inspire-elements-1)
      - [Instantiation without [INSPIRE] element](#instantiation-without-inspire-element-1)
    - [C. Classe dcat:DataService](#c-classe-dcatdataservice)
      - [Class profile](#class-profile-2)
      - [Instantiation from [INSPIRE] elements](#instantiation-from-inspire-elements-2)
      - [Instantiation without [INSPIRE] element](#instantiation-without-inspire-element-2)
    - [D. Class dcat:Distribution](#d-class-dcatdistribution)
      - [Class profile](#class-profile-3)
      - [Instantiation from [INSPIRE] elements](#instantiation-from-inspire-elements-3)
      - [Instantiation without [INSPIRE] element](#instantiation-without-inspire-element-3)
    - [E. Class foaf:Organization](#e-class-foaforganization)
    - [F. Class dcat:catalogRecord](#f-class-dcatcatalogrecord)
      - [Remarks concerning the attributes of the class](#remarks-concerning-the-attributes-of-the-class)
      - [Remarks concerning the content of the class](#remarks-concerning-the-content-of-the-class)
    - [G. Class locn:Address](#g-class-locnaddress)
    - [H. Class skos:Concept](#h-class-skosconcept)
      - [Class profile](#class-profile-4)
      - [Instantiation from [INSPIRE] elements](#instantiation-from-inspire-elements-4)
      - [Instantiation without [INSPIRE] element](#instantiation-without-inspire-element-4)
    - [I. Class dct:PeriodOfTime](#i-class-dctperiodoftime)
      - [Class profile](#class-profile-5)
      - [Instantiation from [INSPIRE] elements](#instantiation-from-inspire-elements-5)
      - [Instantiation without [INSPIRE] element](#instantiation-without-inspire-element-5)
    - [J. Class dqv:QualityMeasurement](#j-class-dqvqualitymeasurement)
      - [Class profile](#class-profile-6)
      - [Instantiation from [INSPIRE] elements](#instantiation-from-inspire-elements-6)
      - [Instantiation without [INSPIRE] element](#instantiation-without-inspire-element-6)
    - [K. Class dct:Location](#k-class-dctlocation)
      - [Class profile](#class-profile-7)
      - [Instantiation from [INSPIRE] elements](#instantiation-from-inspire-elements-7)
      - [Instantiation without [INSPIRE] element](#instantiation-without-inspire-element-7)
    - [L. Class skos:ConceptScheme](#l-class-skosconceptscheme)
    - [M. Class vcard:Organization](#m-class-vcardorganization)
      - [Class profile](#class-profile-8)
      - [Instantiation from [INSPIRE] elements](#instantiation-from-inspire-elements-8)
      - [Instantiation without [INSPIRE] element](#instantiation-without-inspire-element-8)
    - [N. Class vcard:Address](#n-class-vcardaddress)
      - [Class profile](#class-profile-9)
      - [Instantiation from [INSPIRE] elements](#instantiation-from-inspire-elements-9)
      - [Instantiation without [INSPIRE] element](#instantiation-without-inspire-element-9)
  - [Referenced standards](#referenced-standards)
- [Annexe I](#annexe-i)
  - [A. dcat:Catalog](#a-dcatcatalog)
  - [B. dcat:Dataset](#b-dcatdataset)
  - [C. dcat:DataService](#c-dcatdataservice)
  - [D. dcat:Distribution](#d-dcatdistribution)
  - [E. foaf:Organization](#e-foaforganization)
  - [F. dcat:CatalogRecord](#f-dcatcatalogrecord)
  - [G. locn:Address](#g-locnaddress)
  - [H. skos:Concept](#h-skosconcept)
  - [I. dct:PeriodOfTime](#i-dctperiodoftime)
  - [J. dqv:QualityMeasurement](#j-dqvqualitymeasurement)
    - [Instantiation of dqv:QualityMeasurement in an attribute describing a vector resource](#instantiation-of-dqvqualitymeasurement-in-an-attribute-describing-a-vector-resource)
    - [Instantiation of dqv:QualityMeasurement in an attribute describing a raster resource](#instantiation-of-dqvqualitymeasurement-in-an-attribute-describing-a-raster-resource)
  - [K. dct:Location](#k-dctlocation)
  - [L. skos:ConceptScheme](#l-skosconceptscheme)
  - [M. vcard:Organization](#m-vcardorganization)
  - [N. vcard:Address](#n-vcardaddress)
  - [O. dct:LicenseDocument](#o-dctlicensedocument)
  - [P. rdf:Description](#p-rdfdescription)
- [Annexe II](#annexe-ii)

# Federal DCAT AP profile

## Introduction
This document establishes the [federal DCAT AP 2 profile](#DCATAP2fédéral), developed by the federal administrations involved in the implementation of the INSPIRE directive. This profile complies with the [DCAT AP 2](#DCATAP2) standard. On the one hand, it specifies and restricts this standard by specifying the rules governing the instantiation of its classes. On the other hand, it implements rules applicable to the content of the classes and their respective attributes.
The [federal DCAT AP 2](#DCATAP2fédéral) has the primary objective of integrating the semantic richness of the metadata elements from TG 2.0 and exploiting the semantic opportunities offered by the [TG relating to download services](#TGrelativesauxservicesdetéléchargement).
Therefore, the federal DCAT AP 2 restricts the multiplicity of some attributes and adds others foreign to [DCAT AP 2](#DCATAP2) in order to match these attributes to metadata elements from [TG 2.0](#TG2). Similarly, the [federal DCAT AP 2](#DCATAP2fédéral) standardises the content of its attributes to include, where appropriate, the content of metadata elements from TG 2.0.



The [federal DCAT AP 2](#DCATAP2fédéral) includes all the classes and attributes required by [DCAT AP 2](#DCATAP2). In a complementary and non-imperative way, the attributes specific to [GEO DCAT AP 2](#GEODCATAP2) and [STAT DCAT AP 1](#STATDCATAP1) were integrated insofar as they met the needs expressed by the federal administrations. It includes the classes presented below. Classes in bold are mandatory in any [federal DCAT AP 2](#DCATAP2fédéral) compliant catalogue:

- **dcat:Catalog** which represents and describes catalogues;
- **dcat:Dataset** which represents and describes datasets;
- dcat:Dataservice which represents and describes services (or applications or APIs) providing access to one or more datasets;
- **foaf:Organization** which represents and describes organizations;
- dcat:Distribution which represents and describes accessible files of a dataset;
- dcat:CatalogRecord which represents and describes any object in the catalogue (a dataset, a service or a catalogue); locn:Address which represents and describes postal addresses of a foaf agent;
- skos:Concept which represents and describes concepts; dct:PeriodOfTime which represents and describes periods of time;
- dqv:QualityMeasurement which represents and describes the spatial resolution of resources; dct:Location which represents and describes geographical areas;
- skos:ConceptScheme which represents and describes thesauri; 
- vcard:Organization which represents Organizations; vcard:Address which represents and describes postal addresses.
The following diagram presents the classes and the attributes specific to [federal DCAT AP 2](#DCATAP2fédéral).


![DCATAPfederal](https://user-images.githubusercontent.com/87412262/180747799-287ac27e-a6eb-4766-87fc-4c402d8a81a1.png)


Section II, and the associated annexed tables, specify the specific attributes of each class. It also specifies the rules applicable to the content of the attributes of each class, as well as the element of the [ISO 19139](#ISO19139) form to be used in the event of conversion. In all the tables in Annex I, the following elements are listed for each attribute:
1.	URI: this element corresponds to the unique identifier of the attribute considered;
2.	Name: this element corresponds to the French name of the attribute considered;
3.	Description: this element corresponds to the description of the attribute considered;
4.	Requirement: this element corresponds to one of the four requirement[^1] levels specific to the attribute considered;
5.	Multiplicity: this element corresponds to the minimum and maximum number of attributes of this type allowed;
6.	Range: this element corresponds to the acceptable values that can be included in the attribute considered. If the acceptable values belong to one or more restricted groups (i.e. a thesaurus), then the optional, recommended and mandatory set(s) is/are listed in Annex II;
7.	Source: this element corresponds to the XPATH of the element that must be used as the value of the attribute considered if the class to which it belongs is matched to an [ISO 19115 class](#ISO19115) and if its range corresponds to a unilingual value, a multilingual value or a URL. If its range corresponds to another class in this profile, the source corresponds to the [ISO 19115](#ISO19115) class matched with the class in this profile.
The "multilingual" range attributes must be completed in German, French, Dutch and English. Wherever possible, the range attributes
"Multilingual URL" must be completed in German, French, Dutch and English.

[^1]: Applicable levels are mandatory (M), recommended (R), optional (O) and prohibited (W). This last case is only applicable for the attributes of the classes dcat:Catalog and dcat:Dataset which are instantiated in the same class, to avoid cascading instantiations.

## II. Detailed presentation of the classes

###  A.	Class dcat:Catalog
The dcat:Catalog class corresponds to a catalogue, i.e. a particular set of one or more datasets and possibly services identified and documented consistently.
According to these specifications, the class can instantiate itself in the root element on the one hand, and in the dct:hasPart, dct:isPartOf and dcat:catalog attributes on the other hand. The instance of the dcat:Catalog class present in the root element corresponds to the DCAT catalogue considered. This instantiation is mandatory and unique.
The instance(s) of the dcat:Catalog class present in the three above-mentioned attributes correspond to catalogues that can somehow be associated with the catalogue in which they instantiate. These instantiations are **optional** and **potentially multiple**.

#### Class profile

This profile provides different specifications depending on the attribute within which the class instantiates. These arise essentially from the need to prevent an infinite staging of instantiations from the class and from the specific purposes of each type of instantiation. The first instantiation aims to identify and exhaustively describe the catalogue considered, whereas the following instantiations aim exclusively to identify the catalogue considered.
 
The attributes specific to the instance present in the root element are specified in Table 1 in the annex. The attributes specific to the other instances are specified in Table 2 in the annex.
The specifications applicable to the class, regardless of where it is instantiated, provide the possibility of making explicit how the described catalogue is acquired by means of the dcat:Distribution attribute. This is an addition to the [DCAT AP 2](#DCATAP2) standard.

#### Instantiation from [INSPIRE] elements

Only the content of [ISO 19139](#ISO19139) records describing a CSW can be converted into instances of the dcat:Catalog class. In such cases, these specifications require that the content of each attribute of the dcat: Catalog class be provided from its associated [ISO 19139](#ISO19139) element in Table 1.
The content of multilingual or unilingual attributes must be provided from the content of the associated [ISO 19139](#ISO19139) element. The content of the attributes whose domain corresponds to a class is equal to one or more instantiations of that class conforming to the specifications of this profile. These instantiations take the content of the associated [ISO 19139](#ISO19139) element.
As an exception, some attributes are not matched with [ISO 19139](#ISO19139) elements. In this case, the following rules apply:

1.	The content of the foaf:homepage attribute must refer to a human readable version of the catalogue;
2.	The content of the dcat :themeTaxonomy attribute must be generated a posteriori¸ as soon as all the attributes of all the classes are provided, so as to list all the thesauri actually used in the catalogue considered;
3.	The content of the dct:identifier attribute is yet to be determined. It could correspond to the XML serialisation URL of the catalogue considered;
4.	The content of the dcat:dataset attribute is generated from all records describing static datasets, series or maps accessible via [CSW](#CSW);
5.	The content of the dcat:service attribute is generated from all records describing services or applications accessible via [CSW](#CSW);

#### Instantiation without [INSPIRE] element

If the instance of the dcat: Catalog class is not matched with an [ISO 19139](#ISO19139) record describing a [CSW](#CSW), then these specifications nonetheless provide that the content of the multilingual or unilingual domain attributes be populated according to the terminology and syntax rules of the [federal metadata profile](#profildemétadonnéesfédéral) applicable to its associated [ISO 19139](#ISO19139) element in Table 2.
These specifications also provide that the content of the attributes whose domain corresponds to a class is equal to one or more instantiations of that class conforming to the specifications of this profile.
As an exception, some attributes are not matched with [ISO 19139](#ISO19139) elements or classes. In this case, the following rules apply:
1.	The content of the foaf:homepage attribute must refer to a human readable version of the catalogue;
2.	The content of the dcat :themeTaxonomy attribute must be generated a posteriori¸ as soon as all the attributes of all the classes are provided, so as to list all the thesauri actually used in the catalogue considered;
3.	The content of the dct:identifier attribute is yet to be determined. It could correspond to the XML serialisation URL of the catalogue considered;
4.	The content of the dcat:dataset attribute is generated from the actual datasets integrated from the catalogue;
5.	The content of the dcat:dataset attribute is generated from the actual services integrated from the catalogue.


### B. Class dcat: Dataset

The dcat:Dataset class corresponds to the description of a dataset, i.e. a datatset, identified and maintained by an organization and accessible in one or several formats.
According to these specifications, the class can instantiate in the attributes dcat:dataset, dct:source, dcat:servesDataset and foaf:isPrimaryTopicOf. The instance(s) of the dcat:Dataset class present in the dcat:dataset attribute correspond to the description of the dataset(s) referenced in the catalogue. These instantiations are **mandatory** and **potentially multiple**.
The instance(s) of the dcat :Dataset class present in the attribute dct :source correspond to the dataset at the origin of the described dataset. These instantiations are **recommended** and **potentially multiple**.
The instance(s) of the dcat :Dataset class present in the attribute dcat :servesDataset correspond to the datasets accessible through the described service. These instantiations are **recommended** and **potentially multiple**.
The instances of the class dcat :Dataset present in the attribute foaf :isPrimaryTopic correspond to its identification. These instantiations are **mandatory** and
**potentially multiple** when the class dcat:CatalogRecord is instantiated.

#### Class profile

This profile provides different specifications depending on the attribute within which the class instantiates. These arise essentially from the need to prevent an infinite staging of instantiations from the class and from the specific purposes of each type of instantiation. The first instantiation aims to identify and exhaustively describe the dataset considered, whereas the following instantiations aim exclusively to identify the dataset considered.
The attributes specific to the instances present in the attribute dcat :dataset are specified in Table 3 in the annex. The attributes specific to the other instances are specified in Table 4 in the annex.
The specifications applicable to the class provide that the versions of the same dataset correspond to as many different instances of the dcat class
:Distribution. Therefore, they do not provide for the version-related attributes proposed by [DCAT AP 2.0](#DCATAP2).

The specifications for the class include the attributes dct:license and adms:representationTechnique because, according to [TG 2.0](#TG2) and [ISO 19115](#ISO19115), they characterise datasets and not a particular distribution of a dataset.
The specifications applicable to class require that the instances present in the dcat:dataset attribute have at least one attribute duly provided among the following attributes (dct:created, dct:modified or dct:issued).
The specifications applicable to the class require that instances in the dcat:dataset attribute have at least one of the following attributes (dct:publisher, geodcat:custodian, dct:creator, geodcat:distributor, geodcat:originator, geodcat:principalInvestigator, geodcat:processor, geodcat
:resourceProvider, geodcat :user or dct :rightsHolder).

#### Instantiation from [INSPIRE] elements

Only the content of the ISO 19139 records describing a dataset, a series or a static map can be converted into instances of the dcat:Dataset class. In such cases, these specifications require that the content of each attribute of the dcat: Dataset class be provided from its associated ISO 19139 element in Table 3.
The content of multilingual or unilingual attributes must be provided from the content of the associated [ISO 19139](#ISO19139) element. The content of the attributes whose domain corresponds to a class is equal to one or more instantiations of that class conforming to the specifications of this profile. These instantiations take the content of the associated [ISO 19139](#ISO19139) element.

#### Instantiation without [INSPIRE] element

If the instance of the dcat: Dataset class is not matched with an [ISO 19139](#ISO19139) record describing a dataset, then these specifications nonetheless provide that the content of the multilingual or unilingual domain attributes be populated according to the terminology and syntax rules of the [federal metadata profile](#profildemétadonnéesfédéral) applicable to its associated [ISO 19139](#ISO19139) element in Table 4.
These specifications also provide that the content of the attributes whose domain corresponds to a class is equal to one or more instantiations of that class conforming to the specifications of this profile.


### C. Classe dcat:DataService
The dcat : DataService class corresponds to the description of a data service, i.e. a web service, an application or an API identified and maintained by an organization and providing access to one or more identified datasets.
According to these specifications, the class can instantiate in the attributes dcat:service and foaf:isPrimaryTopicOf. The instance(s) of the class of the dcat:DataService in the attribute dcat:service correspond to the description of the service or services referenced in the catalogue. These instantiations are
**recommended** and **potentially multiple**.

The instances of the class dcat :DataService present in the attribute foaf :isPrimaryTopic correspond to its identification. These instantiations are **mandatory** and
**potentially multiple** when the class dcat:CatalogRecord is instantiated.

#### Class profile

This profile provides different specifications depending on the attribute within which the class instantiates. These are essentially derived from the specific purposes of each type of instantiation. The first instantiation aims to identify and exhaustively describe the service considered, whereas the following instantiation aims exclusively to identify the service considered.
The attributes specific to the instances present in the attribute dcat :service are specified in Table 5 in the annex. The attributes specific to the other instances are specified in Table 6 in the annex.
The specifications applicable to the class include the attributes dct:license and dct:conformsTo because, according to [TG 2.0](#TG2) and [ISO 19115](#ISO19115), they characterise the services.

The specifications applicable to class require that the instances present in the dcat:service attribute have at least one attribute duly provided among the following attributes (dct:created, dct:modified or dct:issued).
The specifications applicable to the class require that instances in the dcat:service attribute have at least one of the following attributes (dct:publisher, geodcat:custodian, dct:creator, geodcat:distributor, geodcat:originator, geodcat:principalInvestigator, geodcat:processor, geodcat
:resourceProvider, geodcat :user or dct :rightsHolder).

#### Instantiation from [INSPIRE] elements

Only the content of [ISO 19139](#ISO19139) records describing a view service, a download service or an application can be converted into instances of the dcat:DataService class. In such cases, these specifications require that the content of each attribute of the dcat: DataService class be provided from its associated [ISO 19139](#ISO19139) element in Table 5. The content of records describing an outcrop service cannot be converted into instances of the class dcat : DataService.
The content of multilingual or unilingual attributes must be provided from the content of the associated [ISO 19139](#ISO19139) element. The content of the attributes whose domain corresponds to a class is equal to one or more instantiations of that class conforming to the specifications of this profile. These instantiations take the content of the associated [ISO 19139](#ISO19139) element.
In addition, the federal DCAT AP 2 specification calls for instantiating, for each dataset accessible through the described services, the dcat:Dataset class in the dcat:Catalog class. It is necessary to explicitly instantiate in any DCAT AP catalogue the datasets accessible via the services considered by means of the class dcat:Dataset.

#### Instantiation without [INSPIRE] element

If the instance of the dcat: DataService class is not matched with an [ISO 19139](#ISO19139) record describing an eligible service, then these specifications nonetheless provide that the content of the multilingual or unilingual domain attributes be populated according to the terminology and syntax rules of the federal metadata profile applicable to its associated [ISO 19139](#ISO19139) element in Table 6.



### D. Class dcat:Distribution
The dcat:Distribution class corresponds to the description of a particular digital file of a given resource, i.e. a digital file in a particular format.
According to these specifications, the class can instantiate in the attribute dcat:distribution.

#### Class profile

This profile provides independent specifications of the attribute within which the class instantiates. The attributes specific to all the instances of the class are specified in Table 7 in the annex.
The specifications applicable to the class include the attributes dct:temporal and dct:spatial in order to specify, if necessary, the temporal coverage of the distributed file (i.e. the version) and its geographical territory.

#### Instantiation from [INSPIRE] elements

Only the content of the [ATOMFeed](#ATOMFeed) describing the download links of a dataset can be converted into instances of the dcat:Distribution class. In such cases, these specifications require that the contents of each attribute of the dcat:Distribution class be provided from its associated [ATOMFeed](#ATOMFeed) element in Table 7. Instances of the class present in an instance of dcat:Catalog are not generated from an [INSPIRE](#INSPIRE) element.
The content of multilingual or unilingual attributes must be provided from the content of the associated [ATOMFeed](#ATOMFeed) element. The content of the attributes whose domain corresponds to a class is equal to one or more instantiations of that class conforming to the specifications of this profile. These instantiations take the content of the associated [ATOMFeed](#ATOMFeed) element.

#### Instantiation without [INSPIRE] element

If the instance of the dcat: Distribution class is not matched with an [ATOMFeed](#ATOMFeed), then these specifications nonetheless provide that the content of the multilingual or unilingual domain attributes be populated according to the terminology and syntax rules of the federal metadata profile applicable to its associated ATOMFeed element in Table 7.
These specifications also provide that the content of the attributes whose domain corresponds to a class is provided via one or more instantiations of that class conforming to the specifications of this profile.



### E. Class foaf:Organization

The foaf:Organization class corresponds to the description of an organization, i.e. a structured set of people with one or more determined goals.

According to these specifications, the class can be instantiated in the attributes dct :publisher, geodcat :custodian, dct :creator, geodcat :distributor, geodcat : originator, geodcat :principalInvestigator, geodcat :processor, geodcat :resourceProvider, geodcat :user or dct :rightsHolder.

Class profile

This profile provides independent specifications of the attribute within which the class instantiates. The attributes specific to all the instances of the class are specified in Table 8 in the annex.

Instantiation from [INSPIRE] elements

Only the content of the instances of the [ISO 19139](#ISO19139) class relating to organizations can be converted into instances of the foaf:Organization class. In such cases, these specifications require that the content of each attribute of the foaf: Organization class be provided from its associated [ISO 19139](#ISO19139) element in Table 8.
The content of multilingual or unilingual attributes must be provided from the content of the associated [ISO 19139](#ISO19139) element. The content of the attributes whose domain corresponds to a class is equal to one or more instantiations of that class conforming to the specifications of this profile. These instantiations take the content of the associated ISO 19139 element.
As an exception, some attributes are not matched with [ISO 19115](#ISO19115) elements or classes. In this case, the following rules apply:
a) The content of the attribute dct:type is not associated with any [ISO 19115](#ISO19115) element. Therefore, it is not provided for the instances present in the classes that correspond to the result of the conversion of an [ISO 19139](#ISO19139) record.

Instantiation without [INSPIRE] element

If the instance of the foaf: Organization class is not matched with an instance of the [ISO 19139]](#ISO19139) record relating to an organization, then these specifications nonetheless provide that the content of the multilingual or unilingual domain attributes be populated according to the terminology and syntax rules of the [federal metadata profile](#profildemétadonnéesfédéral) applicable to its associated [ISO 19139](#ISO19139) element in Table 8.
These specifications also provide that the content of the attributes whose domain corresponds to a class is provided via one or more instantiations of that class conforming to the specifications of this profile.



### F. Class dcat:catalogRecord
The class dcat:CatalogRecord corresponds to the identification of particular instances of the classes dcat :Dataset, dcat :DataService (dcat :Catalog). According to these specifications, the class can instantiate in the class dcat :Catalog. The instances are **recommended** and **potentially multiple**.

#### Remarks concerning the attributes of the class

This class aims to identify and exhaustively describe the classes considered. Consequently, the attributes specific to this class are specified in Table 9 in the annex.

#### Remarks concerning the content of the class

If a dcat: CatalogRecord class refers to any class that is not matched with an [ISO 19139](#ISO19139) record, then these specifications provide that the content of the attributes of the dcat: CatalogRecord classes be populated according to the terminology and syntax rules of the federal metadata profile applicable to those same elements.
If a dcat:CatalogRecord class refers to any class that is matched with an [ISO 19139](#ISO19139) record, then these specifications require the content of the attributes to come from the [ISO 19139](#ISO19139) record elements referenced in the XPATH Source column.
Some attributes are not matched with the [ISO 19115](#ISO19115) elements. In such cases, these specifications provide for alternative sources. In this case, the rules relating to the following attributes apply:
a) The content of the foaf :primaryTopic attribute must be generated a posteriori¸ as soon as all classes have been instantiated, so as to reference all of them.



### G. Class locn:Address
The class locn :Address corresponds to the description of the postal address of a foaf agent. According to these specifications, the class can instantiate in the attribute locn:address.
Class profile

This profile provides independent specifications of the attribute within which the class instantiates. The attributes specific to the instances are specified in Table 9 in the annex.

Instantiation from [INSPIRE] elements

Only the content of the instances of the [ISO 19115](#ISO19115) class relating to postal addresses can be converted into instances of the locn:Address class. In such cases, these specifications require that each attribute of the locn :Address class be provided from its associated [ISO 19139](#ISO19139) element in Table 9.

Instantiation without [INSPIRE] element

If the instance of the locn :Address class is not matched with an instance of the [ISO 19139](#ISO19139) record relating to an organization, then these specifications nonetheless provide that the content of the multilingual or unilingual domain attributes be populated according to the terminology and syntax rules of the [federal metadata profile](#profildemétadonnéesfédéral) applicable to its associated [ISO 19139](#ISO19139) element in Table 9.




### H. Class skos:Concept
The skos :Concept class corresponds to the description of a concept, i.e. a notion univocally identified and named in at least one language.

According to these specifications, the class can instantiate in the attributes dcat:theme, dct:language, dct:subject, dct:adms:representationTechnique, dct:type, adms:status and sdmx-attribute:unitMeasure.

#### Class profile

This profile provides independent specifications of the attribute within which the class instantiates. The attributes of all instances of the class skos:Concept are specified in table 10 in the annex.

#### Instantiation from [INSPIRE] elements

Only the content of the instances of the [ISO 19139](#ISO19139) class relating to keywords from thesauri and duly identified by a URI can be directly converted into instances of the skos:Concept class.
In such cases, these specifications require that each attribute of the skos:Concept class be provided from its associated [ISO 19139](#ISO19139) element in Table 10.
The content of the instances of the [ISO 19139](#ISO19139) classes relating to languages, [ISO 19115](#ISO19115) themes, spatial representation type, spatial resolution of raster resources and service type can also be converted into instances of the skos:Concept class.
In such cases, these specifications provide that each attribute of the skos:Concept class be provided on the basis of concepts from SKOS thesauri that are semantically identical to the [ISO 19139](#ISO19139) elements considered. Annex II proposes an identical skos concept for each value of these [ISO 19139](#ISO19139) elements.

#### Instantiation without [INSPIRE] element

If the instance of the skos:Concept class is not matched with an [ISO 19139](#ISO19139) element, these specifications require that the content of the attributes be provided by concepts from the SKOS thesaurus. For each attribute where the skos:Concept class can be instantiated, annex II proposes a list of mandatory, recommended or optional thesauri.

### I. Class dct:PeriodOfTime
The class dct:PeriodOfTime corresponds to the description of a temporal sequence, i.e. a bounded time interval. According to these specifications, the class can instantiate in the dcat :temporal attribute.

#### Class profile

This profile provides independent specifications of the attribute within which the class instantiates. The attributes specific to all the instances of the dct:PeriodOfTime class are specified in Table 11 in the annex.

#### Instantiation from [INSPIRE] elements

Only the content of the instances of the [ISO 19139](#ISO19139) class relating to temporal sequences can be converted into instances of the dct:PeriodOfTime class. In such cases, these specifications require that each attribute of the dct :PeriodOfTime class be provided from its associated [ISO 19139](#ISO19139) element in Table 11.

#### Instantiation without [INSPIRE] element

If the instance of the dct:PeriodOfTime class is not matched with an instance of the [ISO 19139](#ISO19139) record relating to a temporal sequence, then these specifications nonetheless provide that the content of the multilingual or unilingual domain attributes be populated according to the terminology and syntax rules of the federal metadata profile applicable to its associated [ISO 19139](#ISO19139) element in Table 11.

### J. Class dqv:QualityMeasurement
The dqv: QualityMeasurement class corresponds to the spatial resolution of the resource considered, i.e. the level of detail of the resource.

According to these specifications, the class can instantiate in the attribute dqv:hasQualityMeasurement and dcat:spatialResolutionInMeters. In both cases, instantiation is **recommended** and **unique**.

#### Class profile

This profile provides different specifications depending on the place in which the class instantiates. These are mainly based on the need to describe the spatial resolution using concepts adapted to the type of resource.
The attributes specific to the instances relating to the vector resources are specified in Table 12 in the annex. The attributes specific to all the instances relating to the raster resources are specified in Table 13 in the annex.

#### Instantiation from [INSPIRE] elements

Only the content of the instances of the [ISO 19139](#ISO19139) class relating to the spatial resolution can be converted into instances of the dqv:QualityMeasurement class. In such cases, these specifications require that each attribute be provided from its associated [ISO 19139](#ISO19139) element in the annex.

#### Instantiation without [INSPIRE] element

If the instance of the dqv:QualityMeasurement class is not matched with an [ISO 19139](#ISO19139) element relating to spatial resolution, then these specifications nonetheless provide that the content of the multilingual or unilingual domain attributes be populated according to the terminology and syntax rules of the [federal metadata profile](#profildemétadonnéesfédéral) applicable to its associated [ISO 19139](#ISO19139) element in the annex.


### K. Class dct:Location
The dct: Location class corresponds to the description of a geographical area, i.e. a bounded portion of the earth's surface. According to these specifications, the class can instantiate in the attribute dct :location.

####  Class profile

This profile provides independent specifications of the attribute within which the class instantiates. The attributes of all instances of the class dct:Location are specified in table 14 in the annex.

In the absence of truly common standards, the specifications applicable to the class include the attributes locn:geometry and dcat:bbox. The content of these two attributes must be strictly identical and refer to the description of the resource's territory in a specific format. The two attributes must be scored four times to specify the territory in the following formats:
- [Well Know Text ](http://www.opengis.net/ont/geosparql#wktLiteral);
- [Geographic Markup Language](http://www.opengis.net/ont/geosparql#gmlLiteral); 
- GeoJSON using:
  - The [IANA identifier](https://www.iana.org/assignments/media-types/application/vnd.geo+json); 
  - The [opengis identifier](http://www.opengis.net/ont/geosparql#geoJSONLiteral).

####  Instantiation from [INSPIRE] elements

Only the content of the instances of the [ISO 19139](#ISO19139) class relating to the spatial resolution can be converted into instances of the dct :Location class. In such cases, these specifications require that each attribute be provided from its associated [ISO 19139](#ISO19139) element in the annex.

####  Instantiation without [INSPIRE] element
If the instance of the dct:Location class is not matched with an instance of the [ISO 19139](#ISO19139) record relating to an organization, then these specifications nonetheless provide that the content of the multilingual or unilingual domain attributes be populated according to the terminology and syntax rules of the [federal metadata profile](#profildemétadonnéesfédéral) applicable to its associated [ISO 19139](#ISO19139) element in Table 14.


### L. Class skos:ConceptScheme
The skos:ConceptScheme class corresponds to the description of a thesaurus, i.e. a structured set of related concepts. According to these specifications, the class can instantiate in the attribute dcat:themeTaxonomy.
Class profile

This profile provides independent specifications of the attribute within which the class instantiates. The attributes specific to all the instances of the skos:ConceptScheme class are specified in Table 15 in the annex.

Instantiation from [INSPIRE] elements

No [ISO 19115](#ISO19115) class can be converted into an instance of the skos:ConceptScheme class.

Instantiation without [INSPIRE] element

These specifications provide that the skos:ConceptScheme class is instantiated a posteriori, while all other classes have been duly instantiated. These specifications provide that the skos :ConceptScheme class be instantiated on the basis of the URLs present in the skos:inScheme attributes of the instances of the class skos:Concept.


### M. Class vcard:Organization
The vcard:Organization class corresponds to the description of an organization, i.e. a structured set of people with one or more determined goals. According to these specifications, the class can instantiate in the attributes dcat:contactPoint.

#### Class profile

This profile provides independent specifications of the attribute within which the class instantiates. The attributes specific to all the instances of the vcard:Organization class are specified in Table 16 in the annex.

#### Instantiation from [INSPIRE] elements

Only the content of the instances of the [ISO 19139](#ISO19139) class relating to bodies can be converted into instances of the vcard:Organization class. In such cases, these specifications require that each attribute of the vcard: Organization class be provided from its associated [ISO 19139](#ISO19139) element in Table 16.
These specifications also provide that the attributes whose domain corresponds to a class be provided via one or more instantiations of that class conforming to the specifications of this profile.

#### Instantiation without [INSPIRE] element

If the instance of the vcard: Organization class is not matched with an instance of the [ISO 19139](#ISO19139) record relating to an organization, then these specifications nonetheless provide that the content of the multilingual or unilingual domain attributes be populated according to the terminology and syntax rules of the [federal metadata profile](#profildemétadonnéesfédéral) applicable to its associated [ISO 19139](#ISO19139) element in Table 8.
These specifications also provide that the content of the attributes whose domain corresponds to a class is provided via one or more instantiations of that class conforming to the specifications of this profile.


### N. Class vcard:Address
The class vcard :Address corresponds to the description of a postal address of a vcard agent. According to these specifications, the class can instantiate in the class vcard:Organization.

#### Class profile

This profile provides independent specifications of the attribute within which the class instantiates. The attributes of all instances of the class vcard:Address are specified in table 17 in the annex.

#### Instantiation from [INSPIRE] elements

Only the content of the instances of the [ISO 19139](#ISO19139) class relating to postal addresses can be converted into instances of the vcard : Address class. In such cases, these specifications require that each attribute of the vcard :Address class be provided from its associated [ISO 19139](#ISO19139) element in Table 17.

#### Instantiation without [INSPIRE] element

If the instance of the vcard:Address class is not matched with an instance of the [ISO 19139](#ISO19139) record relating to an organization, then these specifications nonetheless provide that the content of the multilingual or unilingual domain attributes be populated according to the terminology and syntax rules of the [federal metadata profile](#profildemétadonnéesfédéral) applicable to its associated [ISO 19139](#ISO19139) element in Table 17.


## Referenced standards

<a id="ISO19115"></a>
[ISO 19115](https://www.iso.org/standard/26020.html) : 

ISO standard for metadata of geographic datasets and services used to implement the [INSPIRE directive](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32007L0002&from=FR)

<a id="ISO19139"></a>
[ISO 19139](https://www.iso.org/fr/standard/32557.htm) : 

ISO standard for the XML implementation of the [ISO 19115](#ISO19115) standard used to implement the [INSPIRE directive](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32007L0002&from=FR)

<a id="TG2"></a>
[TG 2.0](https://inspire.ec.europa.eu/id/document/tg/metadata-iso19139) : 

implementation standard for INSPIRE metadata based on [ISO 19115](#ISO19115) and [ISO 19139](#ISO19139)

<a id="profildemétadonnéesfédéral"></a>
profil de métadonnées fédéral :

unofficial federal standard compliant with [TG 2.0](#TG2)

<a id="CSW"></a>
[CSW](https://portal.ogc.org/files/?artifact_id=20555) : 

OGC standard for metadata publishing

<a id="TGrelativesauxservicesdedécouverte"></a>
TG relatives aux services de découverte : 

standard for implementing INSPIRE discovery services

<a id="DCAT"></a>
[DCAT](https://www.w3.org/TR/vocab-dcat-1/) : 

W3C standard to standardise dataset catalogues on the web

<a id="DCAT2"></a>
[DCAT 2](https://www.w3.org/TR/vocab-dcat-1/) : 

W3C standard to standardise dataset catalogues on the web 

<a id="DCATAP1"></a>
[DCAT AP 1](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/11) : 

ISA implementing and conforming to the [DCAT](#DCAT) standard for describing the public datasets distributed in the Union 

<a id="DCATAP2"></a>
[DCAT AP 2](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/200) : 

ISA implementing and conforming to the [DCAT 2](#DCAT2) standard for describing the public datasets distributed in the Union 

<a id="GeoDCATAP2"></a>
[Geo DCAT AP 2](https://semiceu.github.io/GeoDCAT-AP/drafts/latest/#properties-for-distribution) : 

ISA implementing and conforming to the [DCAT AP 2](#DCATAP2) standard for describing public geographic datasets distributed in the Union

<a id="StatDCATAP1"></a>
[Stat DCAT AP 1](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/statdcat-application-profile-data-portals-europe/release/100) :

ISA implementing and conforming to the [DCAT AP 1](#DCATAP1) standard for describing public statistical datasets distributed in the Union 

<a id="DCATAP2fédéral"></a>
DCAT AP 2 fédéral : 

informal federal standard contained in this document that conforms to [DCAT AP 2](#DCATAP2)

<a id="ATOM"></a>
[ATOM](https://tools.ietf.org/html/rfc4287) : 

IETF standard on content syndication 

<a id="TGrelativesauxservicesdetéléchargement"></a>
[TG relatives aux services de téléchargement](https://inspire.ec.europa.eu/documents/technical-guidance-implementation-inspire-download-services) : 

implementation standard for INSPIRE download services based on the [WFS] and [ATOM](#ATOM) standards 

# Annexe I

## A. dcat:Catalog

### Instantiation of dcat:Catalog

| URI                 | Name                                 | Description                                                                               | Requirement first instantiation (root element) | Requirement in any other instantiation | Cardinality | Range              | Source                                                                                                                                                                                                                                                            |
| ------------------- | ------------------------------------ | ----------------------------------------------------------------------------------------- | ------------------------------- | -------------------------------------- | ----------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dct:title           | title                                | Title of the catalogue considered                                                         | M                               | M                                      | 1           | multilingual       | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:title                                                                                                                                                                                             |
| dct:description     | description                          | description of the catalogue considered                                                   | M                               | O                                      | 1           | multilingual       | //\*/gmd:identificationInfo/\*/gmd:abstract                                                                                                                                                                                                                       |
| dct:publisher       | publisher                            | Organization responsible for the publication of the catalogue considered                  | M                               | O                                      | 1           | foaf:Organization  | //\*/gmd:contact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue=’publisher’]]                                                                                                                                                                    |
| dcat:dataset        | dataset                              | Informatie over de dataset(s) referenced in the catalogue considered                      | R                               | W                                      | 0-n         | dcat:Dataset       | [if catalogue generated from a CSW --> getrecords with type = dataset <> if catalogue generated from wizard: a posteriori creation based on mentioned datasets](https://github.com/marielleadam/inspire-dcat/edit/main/DCATAPprofil.en.md#CSW)                    |
| dcat:service        | service                              | Related information to the service(s) referenced in the catalogue considered              | R                               | W                                      | 0-n         | dcat:DataService   | [if catalogue generated from a CSW --> getrecords with type service/application provided <> if catalogue generated from wizard: a posteriori creation based on mentioned services](https://github.com/marielleadam/inspire-dcat/edit/main/DCATAPprofil.en.md#CSW) |
| foaf:homepage       | homepage                             | Human readable version of the catalogue considered                                        | R                               | R                                      | 0-4         | rdf:Description    | [No XPATH: https://www.geo.be/home (or homepage of catalogue specific to the institution if it's harvested)](https://www.geo.be/home)                                                                                                                             |
| dct:language        | language                             | Language(s) in which the catalog can be consulted                                         | M                               | O                                      | 1-4           | skos:Concept       | //\*/gmd:locale/gmd:PT_Locale/gmd:languageCode/gmd:LanguageCode/@codeListValue                                                                                                                                                                                    |
| dct:issued          | date of first publication            | Date of first publication of the catalogue                                                | R                               | O                                      | 0-1         | date (YYYY-MM-DD)  | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='publication']]/gmd:date                                                                                                         |
| dct:spatial         | spatial coverage                     | Description of the cover space of the resources included in the catalogue                 | R                               | O                                      | 0-n         | dct:Location       | //\*/gmd :identificationInfo/\*/gmd :extent/gmd :EX_Extent/gmd :geographicElement                                                                                                                                                                                 |
| dcat:themeTaxonomy | controlled vocabulary                | Information on thesauri including the keywords describing the datasets that are extracted | O                               | W                                      | 0-n         | skos:ConceptScheme | a posteriori generation by listing all thesauri referenced in Dataset and DataService classes                                                                                                                                                                     |
| dct:hasPart         | catalogue included                   | Information relating to the catalogue(s) including in the catalgue considered             | O                               | W                                      | 0-n         | dcat:Catalog       | if catalogue generated from a CSW --> nihil <> if catalogue generated from wizard: indien catalogus gegenereerd vanuit een CSW --> nihil <> if catalogue generated from wizard: foresee field                                                                     |
| dct:isPartOf        | catalogue including                  | Information relating to the catalogue(s) including in the catalogue considered            | O                               | W                                      | 0-n         | dcat:Catalog       | [if catalogue generated from CSW --> ID of the catalogue of BOSA + ID of the DCAT main catalogue of the NGI <> if catalog genrated from wizard : foresee field](https://github.com/marielleadam/inspire-dcat/edit/main/DCATAPprofil.en.md#CSW)                    |
| dcat:record         | signaletics                          | Instances listed in the catalogue considered                                              | R                               | W                                      | 0-n         | dcat:CatalogRecord | a posteriori generation by indetifying the CatalogRecord instances                                                                                                                                                                                                |
| dcat:distribution   | distribution                         | Information on how to acquire the catalogue                                               | R                               | R                                      | 0-n         | dcat:Distribution  | \--> to generate with link to XML seralisation (en possibly JSON)                                                                                                                                                                                                 |
| dcat:catalog        | catalogus                            | Catalogue whose content is interesting in the context of the described catalogue          | O                               | W                                      | 0-n         | dcat:Catalog       | [if catalogue generated from CSW --> nihil <> if catalogue generated from wizard: foresee field](https://github.com/marielleadam/inspire-dcat/edit/main/DCATAPprofil.en.md#CSW)                                                                                   |
| dcat:contactPoint   | point of contact of the catalogue    | Information relating to the modalities of contact abot the catalogue                      | R                               | R                                      | 0-1         | vcard:Organization | //\*/ gmd:contact/ gmd:CI_ResponsibleParty[ gôleole/ gmd:CI_RoleCode[@codeListValue=’publisher’]]                                                                                                                                                                 |
| dct:identifier      | identifier                           | Unique alphanumeric identifier of the catalogue                                           | M                               | M                                      | 1           | unilingual           | No XPATH: XML serialisation?                                                                                                                                                                                                                                      |
| dcat:theme          | keyword from a controlled vocabulary | Keyword from a thesaurus describing the dataset                                           | O                               | W                                      | 0-n         | skos:Concept       | //\*/ gmd:identificationInfo/\*/ gmd:descriptiveKeywords/ gmd:MD_Keywords[ gmd:thesaurusName/ gmd:CI_Citation/ gmd:title/\*={}]/ gmd:keyword/\*                                                                                                                   |

**Table 1 : dcat:Catalog class instantiation**

## B. dcat:Dataset

### Instantiation of dcat:Dataset

| URI                           | Name                                 | Description                                                                                                                                                    | Requirement instanciation in the dcat:dataset attribute | Requirement instanciation in any other attribute | Cardinality | Range                   | Source                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------ | ----------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dct:title                     | title                                | Title of the dataset considered                                                                                                                                | M                                                       | M                                                | 1           | multilingual            | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:title/\* (title genomen overeenkomstig de specificaties van het federaal profiel)                                                                                                                                                                                                                                                             |
| dct:description               | description                          | Description of the dataset considered                                                                                                                          | M                                                       | O                                                | 1           | multilingual            | //\*/gmd:identificationInfo/\*/gmd:abstract/\*                                                                                                                                                                                                                                                                                                                                                                |
| dcat:contactPoint             | point of contact                     | Information relating to the modalities of contact about the dataset                                                                                            | O                                                       | O                                                | 0-n         | vcard:Organization      | //\*/gmd:contact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='pointOfContact']]                                                                                                                                                                                                                                                                                                           |
| dcat:distribution             | distribution                         | Information relating the modalities of acquisition of the dataset considered                                                                                   | R                                                       | W                                                | 0-n         | dcat:Distribution       | [If dataset generates from ISO 19139 record --> the content of the ATOM FEED that refers to this record <> if dataset generated from wizard: generate by manual filling of the ad hoc field](https://github.com/marielleadam/inspire-dcat/edit/main/DCATAPprofil.en.md#ISO19139)                                                                                                                              |
| dcat:keyword                  | keyword                              | free keyword describing the set of data considered                                                                                                             | O                                                       | W                                                | 0-n         | multilingual            | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD_Keywords[not(./gmd:thesaurusName)]/gmd:keyword/\*                                                                                                                                                                                                                                                                                               |
| dcat:theme                    | keyword of a controlled vocabulary   | Keyword from a thesaurus describing the dataset                                                                                                                | M                                                       | W                                                | 1-n         | skos:Concept            | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD_Keywords[gmd:thesaurusName/gmd:CI_Citation/gmd:title/\*={}]/gmd:keyword/\*                                                                                                                                                                                                                                                                      |
| dct:subject                   | ISO category                         | [Information relating to the category ISO 19115 of the dataset considered](https://github.com/marielleadam/inspire-dcat/edit/main/DCATAPprofil.en.md#ISO19115) | O                                                       | W                                                | 0-n         | skos:Concept            | //\*/gmd:identificationInfo/\*/gmd:topicCategory/\*                                                                                                                                                                                                                                                                                                                                                           |
| dct:spatial                   | spatial coverage                     | information relating to the geographic region that is convered by the dataset considered                                                                       | R                                                       | W                                                | 0-n         | dct:Location            | //\*/gmd:identificationInfo/\*/gmd:extent/gmd:EX_Extent/gmd:geographicElement                                                                                                                                                                                                                                                                                                                                 |
| dct:temporal                  | temporal converage                   | information relating to a temporal period that the dataset considered convers                                                                                  | R                                                       | W                                                | 0-n         | dct:PeriodOfTime        | //\*/gmd:identificationInfo/\*/gmd:extent/gmd:EX_Extent/gmd:temporalElement                                                                                                                                                                                                                                                                                                                                   |
| dct:created                   | date of creation                     | Date of creation of the dataset considered                                                                                                                     | R                                                       | W                                                | 0-1         | date (YYYY-MM-DD)       | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='creation']]/gmd:date                                                                                                                                                                                                                                                        |
| dct:modified                  | update date                          | most recent date on which the dataset considered was modified                                                                                                  | R                                                       | W                                                | 0-1         | date (YYYY-MM-DD)       | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='revision']]/gmd:date                                                                                                                                                                                                                                                        |
| dct:issued                    | release date                         | date of first publication of dataset                                                                                                                           | O                                                       | W                                                | 0-1         | date (YYYY-MM-DD)       | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='publication']]/gmd:date                                                                                                                                                                                                                                                     |
| foaf:page                     | metadata page                 | Informations relatives au(x) lien(s) détaillant le contenu du jeu de données                                                                                   | R                                                       | R                                                | 0-1         | URL multilingue         | //\*/gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource[gmd:protocol/\*={WWW:LINK-1.0-http--link} and gmd:function/\*/@codeListValue={'information'}]/gmd:linkage/gmd:name                                                                                                                                                           |
| dct:accrualPeriodicity        | updatefrequency                      | Information on the updatefrequency of the dataset considered                                                                                                   | R                                                       | W                                                | 0-1         | skos:Concept            | //\*/gmd:identificationInfo/\*/gmd:resourceMaintenance/gmd:MD_MaintenanceInformation/gmd:maintenanceAndUpdateFrequency/gmd:MD_MaintenanceFrequencyCode/@codeListValue                                                                                                                                                                                                                                         |
| dct:identifier                | identifier                           | Alphanumeric identifier unique to the dataset considered dataset                                                                                               | M                                                       | M                                                | 1           | unilingual            | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:identifier/\*/gmd:code/\*                                                                                                                                                                                                                                                                                                                     |
| dcat:landingPage              | homepage                             | Original HTML metadata page                                                                                                                                    | R                                                       | R                                                | 0-4         | rdf:Description         | [https://www.geo.be/catalog/details/ + //\*/gmd:fileIdentifier](https://www.geo.be/catalog/details/)                                                                                                                                                                                                                                                                                                          |
| dct:language                  | language                             | Information relating to the language(s) of the dataset considered                                                                                              | R                                                       | W                                                | 0-4         | skos:Concept            | //\*/gmd:identificationInfo/\*/gmd:language/gmd:LanguageCode/@codeListValue                                                                                                                                                                                                                                                                                                                                   |
| dct:provenance                | origin                               | Information relating to the origin of the dataset considered                                                                                                   | O                                                       | W                                                | 0-1         | dct:ProvenanceStatement | //\*/gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:statement                                                                                                                                                                                                                                                                                                                          |
| dct:conformsTo                | specification or rule of structuring | Information relating to the standards of dataset quality                                                                                                       | O                                                       | W                                                | 0-n         | dct:Standard            | //\*/gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:report/gmd:DQ_DomainConsistency/gmd:result/gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation ET //\*/gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource[gmd:protocol/\*={WWW:LINK-1.0-http--link} and gmd:function/\*/@codeListValue={'information'}]/gmd:linkage/gmd:name  |
| dct:source                    | source dataset                       | Information relating to the concepetual scale of the dataset considered                                                                                        | O                                                       | W                                                | 0-1         | dcat:Dataset            | [if dataset generated from ISO 19139 fiche --> use the XPATH //\*/gmd:identificationInfo/\*/gmd:aggregationInfo <> if dataset generated from wizard: generate by manual selection in ad-hoc field](https://github.com/marielleadam/inspire-dcat/edit/main/DCATAPprofil.en.md#ISO19139)                                                                                                                        |
| dqv:hasQualityMeasurement     | spatial resolution                   | Information relating to the conceptual scale of the dataset considered                                                                                         | R                                                       | W                                                | 0-1         | dqv:QualityMeasurement  | //\*/gmd:identificationInfo/\*/gmd:spatialResolution/gmd:MD_Resolution                                                                                                                                                                                                                                                                                                                                        |
| dct:accessRights              | accessiblity                         | Information relating to restrictions on the use of the dataset                                                                                                 | M                                                       | W                                                | 1           | dct:RightsStatement     | [//\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD_LegalConstraints[\*/gmd:MD_RestrictionCode[@codeListValue='otherRestrictions']]/gmd:otherConstraints[gco:CharacterString or gmx:Anchor[not(starts-with(@xlink:href, 'http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))\\]\\]](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))%5C%5D%5C%5D) |
| adms:sample                   | distribution example                 | Reference to an example of the distribution of the dataset                                                                                                     | O                                                       | W                                                | 0-1         | dcat:Distribution       | no XPATH specified                                                                                                                                                                                                                                                                                                                                                                                            |
| dct:publisher                 | publisher                            | Information relating to the organization responsible for the availability of the dataset                                                                       | R                                                       | W                                                | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='publisher']]                                                                                                                                                                                                                                                                               |
| geodcat:custodian             | maintainer                           | Information relating to the organization responsible for the dataset and the maintenance of the resource                                                       | O                                                       | W                                                | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='custodian']]                                                                                                                                                                                                                                                                               |
| dct:creator                   | creator                              | Information relating to the organization responsible for the production of the dataset considered                                                              | O                                                       | W                                                | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='author']]                                                                                                                                                                                                                                                                                  |
| geodcat:distributor           | diffuser                             | Information relating to the organization responsible for the distribution of the dataset                                                                       | O                                                       | W                                                | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='distributor']]                                                                                                                                                                                                                                                                             |
| geodcat:originator            | author                               | Information relating to the organization responsible for the creation of the dataset                                                                           | O                                                       | W                                                | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='originator']]                                                                                                                                                                                                                                                                              |
| geodcat:principalInvestigator | collector                            | Information relating to the organization responsible for the collection of research information                                                                | O                                                       | W                                                | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='principalInvestigator']]                                                                                                                                                                                                                                                                   |
| geodcat:processor             | processor                            | Information relating to the organization that has modified the resource after processing the data                                                              | O                                                       | W                                                | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='processor']]                                                                                                                                                                                                                                                                               |
| geodcat:resourceProvider      | provider                             | Information relating to the organization which provides the dataset                                                                                            | O                                                       | W                                                | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='resourceProvider']]                                                                                                                                                                                                                                                                        |
| geodcat:user                  | user                                 | Information relating to the organization that uses the dataset                                                                                                 | O                                                       | W                                                | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='user']]                                                                                                                                                                                                                                                                                    |
| dct:rightsHolder              | rights holder                        | Information relating to the organisation holding rights on the dataset to rights                                                                               | O                                                       | W                                                | 0-1         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='user']]/gmd:organisationName                                                                                                                                                                                                                                                               |
| dct:license                   | conditions of use                  | Information on the conditions of use specific to this distribution                                                                                             | M                                                       | W                                                | 1           | dct:LicenseDocument     | [//\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD_LegalConstraints[\*/gmd:MD_RestrictionCode[@codeListValue='otherRestrictions']]/gmd:otherConstraints[gco:CharacterString or gmx:Anchor[not(starts-with(@xlink:href, 'http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))\\]\\]](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))%5C%5D%5C%5D) |
| adms:representationTechnique  | type dataset                         | Information relating to the spatial representation type of the dataset                                                                                         | R                                                       | W                                                | 1           | skos:Concept            | //\*/gmd:identificationInfo/\*/gmd:spatialRepresentationType                                                                                                                                                                                                                                                                                                                                                  |

**Table 2 : Class dcat:Dataset**

## C. dcat:DataService

### Instantiation of dcat:Dataservice
| URI                           | Name                                 | Description                                                                                                           | Requirement instanciation in dcat:service | Requirement instanciation in any other attribute | Cardinality | Range               | Source                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------ | ----------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dct:title                     | title                                | Title of the service considered                                                                                       | M                                         | M                                                | 1           | multilingual        | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:title/\*                                                                                                                                                                                                                                                                                                                                      |
| dct:description               | description                          | description of the service considered                                                                                 | M                                         | M                                                | 1           | multilingual        | //\*/gmd:identificationInfo/\*/gmd:abstract/\*                                                                                                                                                                                                                                                                                                                                                                |
| dcat:endpointURL              | URL of the service                   | URL of the service considered                                                                                         | M                                         | M                                                | 1-n         | URL                 | Te bekijken                                                                                                                                                                                                                                                                                                                                                                                                   |
| dcat:servesDataset            | accessible dataset                   | Identification of the dataset(s) accessible via the service considered                                                | R                                         | R                                                | 0-n         | dcat:Dataset        | [if the dataservice generated from ISO 19139 file --> use the list of identifiers of the datasets present in the getcapabilities <> if dataservice generated from a wizard--> generation by manual selection of the ad-hocfield containing the already documented datasets](https://github.com/marielleadam/inspire-dcat/edit/main/DCATAPprofil.en.md#ISO19139)                                               |
| dct:accessRights              | restricted access                    | Information relating to restrictions on the use of the service considered                                             | M                                         | M                                                | 1           | dct:RightsStatement | [//\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD_LegalConstraints[gmd:accessConstraints/gmd:MD_RestrictionCode[@codeListValue='otherRestrictions']]/gmd:otherConstraints[gmx:Anchor[starts-with(@xlink:href,'http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess')\\]\\]](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess')%5C%5D%5C%5D)            |
| dcat:keyword                  | keyword                              | Free keyword describing the service considered                                                                        | R                                         | R                                                | 0-n         | multilingual        | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD_Keywords[not(./gmd:thesaurusName)]/gmd:keyword/\*                                                                                                                                                                                                                                                                                               |
| dcat:theme                    | keyword from a controlled vocabulary | Keyword from a thesaurus describing the service                                                                       | R                                         | R                                                | 0-n         | skos:Concept        | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD_Keywords[gmd:thesaurusName/gmd:CI_Citation/gmd:title/\*={}]/gmd:keyword/\*                                                                                                                                                                                                                                                                      |
| dct:created                   | date of creation                     | Date of creation of the service considered                                                                            | R                                         | R                                                | 0-1         | date (YYYY-MM-DD)   | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='creation']]/gmd:date                                                                                                                                                                                                                                                        |
| dct:modified                  | update date                          | most recent date on which the service considered was modified                                                         | R                                         | R                                                | 0-1         | date (YYYY-MM-DD)   | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='revision']]/gmd:date                                                                                                                                                                                                                                                        |
| dct:issued                    | release date                         | Date of first publication of the service                                                                              | O                                         | O                                                | 0-1         | date (YYYY-MM-DD)   | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='publication']]/gmd:date                                                                                                                                                                                                                                                     |
| dct:conformsTo                | specification or structuring rule    | Information on service quality standards of the service                                                               | O                                         | O                                                | 0-n         | dct:Standard        | //\*/gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:report/gmd:DQ_DomainConsistency/gmd:result/gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation                                                                                                                                                                                                                                                         |
| dct:type                      | type of service                      | Information relating to the type of service                                                                           | R                                         | R                                                | 0-1           | skos:Concept        | //\*/gmd:identificationInfo/\*/srv:serviceType                                                                                                                                                                                                                                                                                                                                                                |
| geodcat:distributor           | diffuser                             | Information relating to the organization responsible for the distribution of the resource                             | O                                         | O                                                | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='publisher']]                                                                                                                                                                                                                                                                               |
| geodcat:originator            | author                               | Information relating to the organization responsible for the collection of research information                       | O                                         | O                                                | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='custodian']]                                                                                                                                                                                                                                                                               |
| geodcat:principalInvestigator | principal investigator               | Information relating to the organization responsible for gathering information and conducting reaearch                | O                                         | O                                                | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='author']]                                                                                                                                                                                                                                                                                  |
| geodcat:processor             | processor                            | Information relating to the organization that processed the data in a manner sich that the resource has been modified | O                                         | O                                                | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='distributor']]                                                                                                                                                                                                                                                                             |
| geodcat:resourceProvider      | provider                             | Information relating to the organization that supply the resource                                                     | O                                         | O                                                | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='originator']]                                                                                                                                                                                                                                                                              |
| geodcat:user                  | user                                 | Information relating to the organization that uses the resource                                                       | O                                         | O                                                | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='principalInvestigator']]                                                                                                                                                                                                                                                                   |
| dct:creator                   | creator                              | Information relating to the organization responsible of the production of the service considered                      | O                                         | O                                                | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='processor']]                                                                                                                                                                                                                                                                               |
| geodcat:custodian             | maintainer                           | Information relating to the organization responible for the data and maintenance                                      | O                                         | O                                                | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='resourceProvider']]                                                                                                                                                                                                                                                                        |
| dct:rightsHolder              | rightsholder                         | Information relating to the organization holding the rights on the service                                            | O                                         | O                                                | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='user']]                                                                                                                                                                                                                                                                                    |
| dct:license                   | conditions of use                    | Information on the conditions of use of this distribution                                                             | M                                         | M                                                | 1           | dct:LicenseDocument | [//\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD_LegalConstraints[\*/gmd:MD_RestrictionCode[@codeListValue='otherRestrictions']]/gmd:otherConstraints[gco:CharacterString or gmx:Anchor[not(starts-with(@xlink:href, 'http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))\\]\\]](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))%5C%5D%5C%5D) |
| dct:conformsTo                | geographical projection system       | Information relating to the geographical projection system                                                            | R                                         | R                                                | 0-n         | codedValue          | //\*gmd:referenceSystemInfo/gmd:MD_ReferenceSystem/gmd:referenceSystemIdentifier/gmd:RS_Identifier/gmd:code                                                                                                                                                                                                                                                                                                   |

**Table 3 : dcat:Service class**

## D. dcat:Distribution

### Any instantiation of dcat:Distribution
| URI                 | Name                           | Description                                                                         | Requirement | Cardinality | Range                 | Source                                    |
| ------------------- | ------------------------------ | ----------------------------------------------------------------------------------- | ----------- | ----------- | --------------------- | ----------------------------------------- |
| dct:title           | title                          | Title of the distribution considered                                                | O           | 0-1         | multilingual          | //atom:feed/atom :title                   |
| dcat:accessURL      | access URL                     | Web address of the relevant distribution of the dataset                             | M           | 1           | URL                   | //atom:feed/atom:entry/atom:link          |
| dct:description     | description                    | Description of the features of this distribution                                    | O           | 0-1         | multilingual          | //atom:feed/atom:entry/atom:subtitle      |
| dct:format          | format                         | Information relating to the particular format of this distribution                  | M           | 1           | dct:MediaTypeOrExtent | //atom:feed/atom:entry/atom:link/@type    |
| dcat:mediaType      | format type                    | Format type/support distribution (IANA)                                             | O           | 0-1         | dct:MediaType         | //atom:feed/atom:entry/atom:link/@type    |
| dcat:downloadURL    | download URL                   | Webaddress for directly downloading the distribution concerned                      | O           | 0-1         | URL                   | //atom:feed/atom:entry/atom:link          |
| dcat:compressFormat | compressed format              | Information relating to the compressed format specific to this distribution (IANA)  | O           | 0-1         | dct:MediaType         | //atom :feed/atom :entry/atom :link/@type |
| dct:conformsTo      | geographical projection system | Information relating to the particular projection of this distribution              | O           | 0-1         | dct:Standard          | //atom:feed/atom:entry/atom:category      |
| dcat:byteSize       | size                           | Size of the distribution in bytes                                                   | O           | 0-1         | xsd:decimal           | no XPATH specified                        |
| adms:status         | status                         | Information relating to the maturity of the distribution                            | O           | 1           | skos:Concept          | no XPATH specified                        |
| dct:spatial         | spatial coverage               | Information relating to the geographical area covered by the distribution concerned | O           | 0-1         | dct:Location          | //atom:feed/atom:entry/georss:box         |
| dct:temporal        | temporal coverage              | Information relating to the time interval covered by the distribution concerned     | R           | 0-1         | dct:PeriodOfTime      | //atom:feed/atom:entry/atom:link/@time    |
| dct:type            | type of distribution           | Link to a distribution type                                                         | O           | 0-n         | skos:Concept          | no XPATH specified                        |
| dct:language        | language                       | Information relating to the language(s) used in the distribution                    | R           | 0-4         | skos:Concept          | no XPATH specified                        |


**Table 4 : dcat:DataService class instantiated in any attribute**

## E. foaf:Organization


### Instantiation of foaf:Organization in any attribute
| URI                    | Name           | Description                                           | Requirement | Cardinality | Range           | Source                                                                                  |
| ---------------------- | -------------- | ----------------------------------------------------- | ----------- | ----------- | --------------- | --------------------------------------------------------------------------------------- |
| foaf:name              | name           | Name vof the organization                             | M           | 1-n         | multilingual    | ./gmd:organisationName                                                                  |
| dct:type               | type           | Indicates the type of organization                    | O           | 0-1         | skos:Concept    | no XPATH specified                                                               |
| foaf:mbox              | address mail   | Email address of the organization (using URI mailto:) | R           | 0-1         | URI      | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address/gmd:electronicMailAddress |
| foaf:workplaceHomepage | Website        | Website of the organization                           | R           | 1-4         | rdf:Description | ./gmd:contactInfo/gmd:CI\_Contact/gmd:onlineResource/gmd:CI\_OnlineResource/gmd:linkage |
| locn:address           | Postal address | Postal address of the organization                    | O           | 0-1         | locn:Address    | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address                           |

**Table 5 : class foaf:Organization instanciated in any attribute**

## F. dcat:CatalogRecord

### Instantiation of dcat:CatalogRecord in any attribute
| URI               | Name                                 | Description                                                                                                      | Requirement | Cardinality | Range              | Source                                                                                                                                                                  |
| ----------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------- | ----------- | ----------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| foaf:primaryTopic | instance to which the record relates | Information relating to the dataset, service or catalogue                                                        | M           | 1           | dcat:Dataset       | dcat:Dataservice                                                                                                                                                        | dcat:Catalog | a posteriori generation with integration of all ID's of all primary instantiations (i.e. the instances that do not match the value of an attribute of the same class)
| dct:modified      | update date                          | most recent date on which the service considered was modified                                                    | M           | 1           | date (YYYY-MM-DD)  | //\* /gmd:dateStamp/\*                                                                                                                                                  |
| dct:language      | language                             | Information relating to the language(s) used in the metadata of the dataset or service                           | M           | 1-4         | skos:Concept      | //\*/gmd:locale/gmd:PT\_Locale/gmd:languageCode/gmd:LanguageCode\[@codeListValue={}\]                                                                                   |
| dcat:contactPoint | point of contact                     | Information relating to the organization that can be contacted for sending comments about the dataset or service | M           | 1           | vcard:Organization | //\*/gmd:contact/gmd:CI\_ResponsibleParty                                                                                                                               |
| dct:identifier    | identifier                           | Unique alphanumeric identifier of the catalogrecord                                                              | M           | 1           | unilingual         | //\*/gmd:fileIdentifier                                                                                                                                                 |
| dct:source        | Catalogrecord source                 | Information relating to the original metadata file of the dataset or service                                     | O           | 0-1         | dct:CatalogRecord         | http://csw.geo.be/eng/csw?request=GetRecordById&service=CSW&version=2.0.2&elementSetName=full&outputSchema=http://www.isotc211.org/2005/gmd&id=+//\*/gmd:fileIdentifier |
| dcat:landingPage  | home page                            | Human readable version of the original metadata file of the dataset of service                                   | O           | 0-4         | rdf:Description    | https://www.geo.be/catalog/details/ + //*/gmd:fileIdentifier                                                                                                            |

**Table 6 : class dcat:CatalogRecord instantiated in any attribute**

## G. locn:Address

### Instantiation of locn:Address in any attribute
| URI               | Name           | Description                | Requirement | Cardinality | Range        | Source                |
| ----------------- | -------------- | -------------------------- | ----------- | ----------- | ------------ | --------------------- |
| locn:thoroughfare | postal address | Street and policy number   | M           | 1           | multilingual | ./gmd:deliveryPoint |
| locn:postName     | municipality   | Name of the municipality   | M           | 1           | multilingual | ./gmd:city          |
| locn:postCode     | postal code    | Postal code of the address | M           | 1           | unilingual   | ./gmd:postalCode      |
| locn:adminUnitL1  | country        | Country                    | M           | 1           | multilingual | ./gmd:country         |

**Table 7 : locn:Address in any attribute**

## H. skos:Concept

### Instantiation of skos:Concept in any attribute
| URI           | Name                | Description                                 | Requirement | Cardinality | Range      | Source                                           |
| ------------- | ------------------- | ------------------------------------------- | ----------- | ----------- | ---------- | ------------------------------------------------ |
| rdf:type      | type of concept     | Type of concept                             | O           | 0-1         | unilingual | none                                             |
| skos:inScheme | thesaurus of origin | Thesaurus from which the concept originates | R           | 0-1         | URL        | .  /gmd:thesaurusName/gmd:CI\_Citation/gmd:title |

**Table 8 : class skos:Concept instanciated in any attribute**

## I. dct:PeriodOfTime

### Instantiation of skos:PeriodOfTime in any attribute
| URI            | Name       | Description                 | Requirement | Cardinality | Range      | Source                                                                  |
| -------------- | ---------- | --------------------------- | ----------- | ----------- | ---------- | ----------------------------------------------------------------------- |
| dcat:startDate | dtart date | Start of the period of time | M           | 1           | unilingual | /gmd:EX_TemporalExtent/gmd :extent/gml32:TimePeriod/gml32:beginPosition |
| dcat:endDate   | end date   | End of the period of time   | M           | 1           | unilingual | ./gmd:EX_TemporalExtent/gmd :extent/gml32:TimePeriod/gml32:endPosition  |

**Table 9 : class dct:PeriodOfTime instanciated in any attribute**

## J. dqv:QualityMeasurement

### Instantiation of dqv:QualityMeasurement in an attribute describing a vector resource
| URI                              | Name                                        | Description                                 | Requirement | Cardinality | Range        | Source                                                                                                 |
| -------------------------------- | ------------------------------------------- | ------------------------------------------- | ----------- | ----------- | ------------ | ------------------------------------------------------------------------------------------------------ |
| dqv:isMeasurementOf              | measured scalar quantity                    | Measured scalar quantity                    | O           | 0-1         | multilingual | hardcoded value depending on the type of dataset                                                       |
| geodcat:spatialResolutionAsScale | conceptual scale of the dataset             | Conceptual scale of the dataset             | M           | 1           | unilingual   | ./gmd :MD\_Resolution/gmd:equivalentScale/ gmd:MD\_RepresentativeFraction/ gmd:denominator/gco:Integer |

**Table 10 : class dqv:QualityMeasurement referring to the description of a vector resource**

### Instantiation of dqv:QualityMeasurement in an attribute describing a raster resource
| URI                              | Name                                        | Description                                 | Requirement | Cardinality | Range        | Source                                                                                                 |
| -------------------------------- | ------------------------------------------- | ------------------------------------------- | ----------- | ----------- | ------------ | ------------------------------------------------------------------------------------------------------ |
| dqv:isMeasurementOf              | measured scalar quantity                    | Measured scalar quantity                    | O           | 0-1         | multilingual | hardcoded value depending on the type of dataset                                                       |
| sdmx-attribut:unitMeasure        | unit of measurement of the scalar quantity  | Unit of measurement of the scalar quantity  | R           | 1           | skos:Concept | ./gmd :MD\_Resolution/gmd:distance/gco:Distance/@uom                                                   |
| dqv:value                        | value of measurement of the scalar quantity | Value of measurement of the scalar quantity | M           | 1           | unilingual   | ./gmd :MD\_Resolution /gmd:distance/gco:Distance                                                       |

**Table 11 : class dqv:QualityMeasurement  referring to the description of a raster resource**

## K. dct:Location

### Instantiation of dct:Location in any attribute
| URI             | Name                                | Description                         | Requirement | Cardinality | Range        | Source |
| --------------- | ----------------------------------- | ----------------------------------- | ----------- | ----------- | ------------ | ------ |
| locn:geometry   | geometry                            | Coordinates of he resource geometry | M           | 1-4         | unilingual   |        |
| dcat:bbox       | geographic bounding box             | Coordinates of he resource geometry | M           | 1-4         | unilingual   |        |
| skos:prefLabel  | name of the geographical entity     | name of the geographical entity     | R           | 0-1         | multilingual |        |
| dct:identifier  | identifier of the geographic entity | Identifier of the geographic entity | R           | 0-1         | codedValue   |        |

**Table 12 : class dct:Location instantiated in any attribute**

## L. skos:ConceptScheme

### Instantiation of skos:ConceptScheme in any attribute
| URI            | Name                        | Description                 | Requirement | Cardinality | Range        | Source                                                                                                                                                                                  |
| -------------- | --------------------------- | --------------------------- | ----------- | ----------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dct:title      | Title of the thesaurus      | Title of the thesaurus      | M           | 1           | multilingual | Generation on the basis of the URLs provided in the skos:inScheme properties of the instances of the skos:Concept (it must have the inScheme propoerty and have a machine-readable URL) |
| dct:issued     | release date                | Date of first publication   | O           | 0-1         | date         | Generation on the basis of the URLs provided in the skos:inScheme properties of the instances of the skos:Concept (it must have the inScheme propoerty and have a machine-readable URL) |
| dct:identifier | Identifier of the thesaurus | Identifier of the thesaurus | M           | 1           | URL          | Generation on the basis of the URLs provided in the skos:inScheme properties of the instances of the skos:Concept (it must have the inScheme propoerty and have a machine-readable URL) |

**Table 13 : class skos:ConceptScheme instantiated in any attribute**

## M. vcard:Organization

### Instantiation of vcard:Organization in any attribute

| URI                     | Name           | Description                                          | Requirement | Cardinality | Range           | Source                                                                                  |
| ----------------------- | -------------- | ---------------------------------------------------- | ----------- | ----------- | --------------- | --------------------------------------------------------------------------------------- |
| vcard:organization-name | name           | Name of the organization                             | M           | 1-n         | multilingual    | ./gmd:organisationName                                                                  |
| vcard:hasEmail          | address mail   | Emailaddress of the organization (using URI mailto:) | R           | 0-1         | unilingual      | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address/gmd:electronicMailAddress |
| vcard:hasURL            | website        | Website of the organisation                          | R           | 0-4         | rdf:Description | ./gmd:contactInfo/gmd:CI\_Contact/gmd:onlineResource/gmd:CI\_OnlineResource/gmd:linkage |
| vcard:hasAddress        | postal address | Postal address of the organisation                   | O           | 0-1         | vcard:Address   | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address                           |

**Table 14 : class vcard:Organization instantiated in any attribute**

## N. vcard:Address

### Instantiation of vcard:Address in any attribute

| URI                  | Name           | Description                | Requirement | Cardinality | Range        | Source                |
| -------------------- | -------------- | -------------------------- | ----------- | ----------- | ------------ | --------------------- |
| vcard:street-address | postal address | Street en huisnummer       | M           | 1           | multilingual | ./gmd:deliveryPoint |
| Vcard :locality      | municipality   | Name of the municipality   | M           | 1           | multilingual | ./gmd:city          |
| vcard:postal-code    | postal code    | Postal code of the address | M           | 1           | unilingual   | ./gmd:postalCode      |
| vcard:country-name   | country        | Country                    | M           | 1           | multilingual | ./gmd:country         |

**Table 15 : class vcard:Address instantiated in any attribute**

## O. dct:LicenseDocument

### Instantiation of dct:LicenseDocument in any attribute

| URI             | Name                        | Description                 | Requirement | Cardinality | Range        | Source |
| --------------- | --------------------------- | --------------------------- | ----------- | ----------- | ------------ | ------ |
| dct:type        | type of document            | Type of document            | M           | 1           | URI          |        |
| dct:title       | title of the document       | Title of the document       | M           | 1           | multilingual |        |
| dct:description | description of the document | Description of the document | O           | 0-1         | multilingual |        |

**Table 16 : class dct:LicenseDocument instantiated in any attribute**

## P. rdf:Description

### Instantiation of rdf:Description in any attribute

| URI          | Name                     | Description              | Requirement | Cardinality | Domain     | Source                               |
| ------------ | ------------------------ | ------------------------ | ----------- | ----------- | ---------- | ------------------------------------ |
| dct:language | language of the document | Language of the document | M           | 1           | codedValue | /gmd:LocaliseCharacterString/@locale |

**Table 17 : class rdf:Description instantiated in any attribute**

# Annexe II

| Concerned class | Concerned attribute | Proposed thesaurus | Requirement |
| --------------- | ------------------- | ------------------ | ----------- |
| Catalog            | dcat:theme                   | [http://inspire.ec.europa.eu/theme](http://inspire.ec.europa.eu/theme)                                                                                                                                                                                 | O   |
| Catalog            | dct:language                 | [http://publications.europa.eu/resource/authority/language](http://publications.europa.eu/resource/authority/language)                                                                                                                                 | M   |
| Catalog            | dct:spatial                  | [http://publications.europa.eu/resource/authority/place](http://publications.europa.eu/resource/authority/place)                                                                                                                                       | R   |
| Dataset            | dcat:theme                   | [http://publications.europa.eu/resource/authority/data-theme](http://publications.europa.eu/resource/authority/data-theme)                                                                                                                             | M   |
| Dataset            | dcat:theme                   | [http://inspire.ec.europa.eu/theme](http://inspire.ec.europa.eu/theme)                                                                                                                                                                                 | R   |
| Dataset            | dcat:theme                   | [http://inspire.ec.europa.eu/featureconcept](http://inspire.ec.europa.eu/featureconcept)                                                                                                                                                               | O   |
| Dataset            | dcat:theme                   | [https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurovoc](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurovoc) | O   |
| Dataset            | dct:subject                  | http://inspire.ec.europa.eu/metadata-codelist/TopicCategory                                                                                                                                                                                            | O   |
| Dataset            | dct:accrualPeriodicity       | http://publications.europa.eu/resource/authority/frequency                                                                                                                                                                                             | M   |
| Dataset            | dct:accrualPeriodicity       | http://inspire.ec.europa.eu/metadata-codelist/MaintenanceFrequency                                                                                                                                                                                     | R   |
| Dataset            | dct:language                 | [http://publications.europa.eu/resource/authority/language](http://publications.europa.eu/resource/authority/language)                                                                                                                                 | M   |
| Dataset            | dct:accessRights             | [http://publications.europa.eu/resource/authority/access-right](http://publications.europa.eu/resource/authority/access-right)                                                                                                                         | R   |
| Dataset            | dct:accessRights             | [http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess](https://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess)                                                                                                    | R   |
| Dataset            | dct:license                  | https://creativecommons.org/licenses/                                                                                                                                                                                                                  | R   |
| Dataset            | adms:representationTechnique | [http://inspire.ec.europa.eu/metadata-codelist/SpatialRepresentationType](http://inspire.ec.europa.eu/metadata-codelist/SpatialRepresentationType)                                                                                                     | R   |
| DataService        | dct:accessRights             | [http://publications.europa.eu/resource/authority/access-right](http://publications.europa.eu/resource/authority/access-right)                                                                                                                         | R   |
| DataService        | dct:accessRights             | [http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess](https://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess)                                                                                                    | R   |
| DataService        | dct:type                     | https://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceType                                                                                                                                                                                  | R   |
| DataService        | dct:type                     | https://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceCategory                                                                                                                                                                              | R   |
| DataService        | dcat:theme                   | [http://publications.europa.eu/resource/authority/data-theme](http://publications.europa.eu/resource/authority/data-theme)                                                                                                                             | M   |
| DataService        | dcat:theme                   | [http://inspire.ec.europa.eu/theme](http://inspire.ec.europa.eu/theme)                                                                                                                                                                                 | R   |
| DataService        | dcat:theme                   | [http://inspire.ec.europa.eu/featureconcept](http://inspire.ec.europa.eu/featureconcept)                                                                                                                                                               | O   |
| DataService        | dcat:theme                   | [https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurovoc](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurovoc) | O   |
| DataService        | dct:license                  | https://creativecommons.org/licenses/                                                                                                                                                                                                                  | R   |
| DataService        | dct:conformsTo               | http://www.opengis.net/def/crs/EPSG/0/                                                                                                                                                                                                                 | M   |
| Distribution       | dct:format                   | http://publications.europa.eu/resource/authority/file-type                                                                                                                                                                                             | R   |
| Distribution       | dcat:mediaType               | [http://www.iana.org/assignments/media-types](http://www.iana.org/assignments/media-types)                                                                                                                                                             | R   |
| Distribution       | dct:conformsTo               | http://www.opengis.net/def/crs/EPSG/0/                                                                                                                                                                                                                 | M   |
| Distribution       | adms:status                  | [http://inspire.ec.europa.eu/metadata-codelist/SpatialRepresentationType](http://inspire.ec.europa.eu/metadata-codelist/SpatialRepresentationType)                                                                                                     | R   |
| Distribution       | dct:type                     | http://publications.europa.eu/resource/authority/distribution-type                                                                                                                                                                                     | O   |
| Distribution       | dcat:compressFormat          | [http://www.iana.org/assignments/media-types](http://www.iana.org/assignments/media-types)                                                                                                                                                             | O   |
| foaf:Organization  | dct:type                     | http://publications.europa.eu/resource/authority/corporate-body                                                                                                                                                                                        | O   |
| CatalogRecord      | dct:language                 | [http://publications.europa.eu/resource/authority/language](http://publications.europa.eu/resource/authority/language)                                                                                                                                 | M   |
| QualityMeasurement | sdmx-attribut:unitMeasure    | http://www.qudt.org/vocab/unit/                                                                                                                                                                                                                        | M   |
| Location           | dct:identifier               | http://publications.europa.eu/resource/authority/country                                                                                                                                                                                               | M   |
| Location           | dct:identifier               | belgif UA + thésuarus cadastre in progess                                                                                                                                                                                                              | O   |

**List 1: thesaurus**
