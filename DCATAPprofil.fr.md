**Table des matières**

- [Profil fédéral DCAT AP](#profil-fédéral-dcat-ap)
  - [Introduction](#introduction)
  - [I. Présentation générale des classes](#i-présentation-générale-des-classes)
  - [II. Présentation détaillée des classes](#ii-présentation-détaillée-des-classes)
    - [A. Classe dcat:Catalog](#a-classe-dcatcatalog)
      - [Profil de la classe](#profil-de-la-classe)
      - [Instanciation à partir d&#39;éléments [INSPIRE]](#instanciation-à-partir-déléments-inspire)
      - [Instanciation sans élément [INSPIRE]](#instanciation-sans-élément-inspire)
    - [B. Classe dcat:Dataset](#b-classe-dcatdataset)
      - [Profil de la classe](#profil-de-la-classe-1)
      - [Instanciation à partir d&#39;éléments [INSPIRE]](#instanciation-à-partir-déléments-inspire-1)
      - [Instanciation sans élément [INSPIRE]](#instanciation-sans-élément-inspire-1)
    - [C. Classe dcat:DataService](#c-classe-dcatdataservice)
      - [Profil de la classe](#profil-de-la-classe-2)
      - [Instanciation à partir d'éléments [INSPIRE]](#instanciation-à-partir-déléments-inspire-2)
      - [Instanciation sans élément [INSPIRE]](#instanciation-sans-élément-inspire-2)
    - [D. Classe dcat:Distribution](#d-classe-dcatdistribution)
      - [Profil de la classe](#profil-de-la-classe-3)
      - [Instanciation à partir d'éléments [INSPIRE]](#instanciation-à-partir-déléments-inspire-3)
      - [Instanciation sans élément [INSPIRE]](#instanciation-sans-élément-inspire-3)
    - [E. Classe foaf:Organization](#e-classe-foaforganization)
      - [Profil de la classe](#profil-de-la-classe-4)
      - [Instanciation à partir d'éléments [INSPIRE]](#instanciation-à-partir-déléments-inspire-4)
      - [Instanciation sans élément [INSPIRE]](#instanciation-sans-élément-inspire-4)
    - [F. Classe dcat:catalogRecord](#f-classe-dcatcatalogrecord)
      - [Remarques concernant les attributs de la classe](#remarques-concernant-les-attributs-de-la-classe)
      - [Remarques concernant le contenu de la classe](#remarques-concernant-le-contenu-de-la-classe)
    - [G. Classe locn:Address](#g-classe-locnaddress)
      - [Profil de la classe](#profil-de-la-classe-5)
        - [Instanciation à partir d'éléments [INSPIRE]](#instanciation-à-partir-déléments-inspire-5)
      - [Instanciation sans élément [INSPIRE]](#instanciation-sans-élément-inspire-5)
    - [H. Classe skos:Concept](#h-classe-skosconcept)
      - [Profil de la classe](#profil-de-la-classe-6)
      - [Instanciation à partir d'éléments [INSPIRE]](#instanciation-à-partir-déléments-inspire-6)
      - [Instanciation sans élément [INSPIRE]](#instanciation-sans-élément-inspire-6)
    - [I. Classe dct:PeriodOfTime](#i-classe-dctperiodoftime)
      - [Profil de la classe](#profil-de-la-classe-7)
      - [Instanciation à partir d'éléments [INSPIRE]](#instanciation-à-partir-déléments-inspire-7)
      - [Instanciation sans élément [INSPIRE]](#instanciation-sans-élément-inspire-7)
    - [J. Classe dqv:QualityMeasurement](#j-classe-dqvqualitymeasurement)
      - [Profil de la classe](#profil-de-la-classe-8)
      - [Instanciation à partir d'éléments [INSPIRE]](#instanciation-à-partir-déléments-inspire-8)
      - [Instanciation sans élément [INSPIRE]](#instanciation-sans-élément-inspire-8)
    - [K. Classe dct:Location](#k-classe-dctlocation)
      - [Profil de la classe](#profil-de-la-classe-9)
      - [Instanciation à partir d'éléments [INSPIRE]](#instanciation-à-partir-déléments-inspire-9)
      - [Instanciation sans élément [INSPIRE]](#instanciation-sans-élément-inspire-9)
    - [L. Classe skos:ConceptScheme](#l-classe-skosconceptscheme)
      - [Profil de la classe](#profil-de-la-classe-10)
      - [Instanciation à partir d'éléments [INSPIRE]](#instanciation-à-partir-déléments-inspire-10)
      - [Instanciation sans élément [INSPIRE]](#instanciation-sans-élément-inspire-10)
    - [M. Classe vcard:Organization](#m-classe-vcardorganization)
      - [Profil de la classe](#profil-de-la-classe-11)
      - [Instanciation à partir d'éléments [INSPIRE]](#instanciation-à-partir-déléments-inspire-11)
      - [Instanciation sans élément [INSPIRE]](#instanciation-sans-élément-inspire-11)
    - [N. Classe vcard:Address](#n-classe-vcardaddress)
      - [Profil de la classe](#profil-de-la-classe-12)
      - [Instanciation à partir d'éléments [INSPIRE]](#instanciation-à-partir-déléments-inspire-12)
      - [Instanciation sans élément [INSPIRE]](#instanciation-sans-élément-inspire-12)
  - [Normes référencées](#normes-référencées)
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
    - [Instanciation de dqv:QualityMeasurement dans un attribut décrivant une ressource vectorielle](#instanciation-de-dqvqualitymeasurement-dans-un-attribut-décrivant-une-ressource-vectorielle)
    - [Instanciation de dqv:QualityMeasurement dans un attribut décrivant une ressource matricielle](#instanciation-de-dqvqualitymeasurement-dans-un-attribut-décrivant-une-ressource-matricielle)
  - [K. dct:Location](#k-dctlocation)
  - [L. skos:ConceptScheme](#l-skosconceptscheme)
  - [M. vcard:Organization](#m-vcardorganization)
  - [N. vcard:Address](#n-vcardaddress)
  - [O. dct:LicenseDocument](#o-dctlicensedocument)
  - [P. rdf:Description](#p-rdfdescription)
- [Annexe II](#annexe-ii)


# Profil fédéral DCAT AP
## Introduction

Le présent document institue le profil [DCAT AP 2 fédéral](#DCATAP2fédéral), élaboré par les administrations fédérales impliquées dans l&#39;implémentation de la directive INSPIRE. Ce profil est conforme à la norme [DCAT AP 2](#DCATAP2). D&#39;une part, il spécifie et restreint ladite norme en précisant les règles régissant l&#39;instanciation de ses classes. D&#39;autre part, il met en place des règles applicables au contenu des classes et de leurs attributs respectifs.

En effet, [DCAT AP 2 fédéral](#DCATAP2fédéral) a pour objectif premier d&#39;intégrer la richesse sémantique les éléments de métadonnées issus des [TG 2.0](#TG2) ainsi que d&#39;exploiter les opportunités sémantiques offertes par les [TG relatives aux services de téléchargement](#TGrelativesauxservicesdetéléchargement).

Dès lors, [DCAT AP 2 fédéral](#DCATAP2fédéral) restreint la cardinalité de certains attributs, en ajoute d&#39;autres étrangers à [DCAT AP 2](#DCATAP2) de sorte de mettre en correspondance ces attributs à des éléments de métadonnées issus des [TG 2.0](#TG2). De la même manière, [DCAT AP 2 fédéral](#DCATAP2fédéral) norme le contenu de ses attributs de manière à y intégrer, s&#39;il échet, le contenu des éléments de métadonnées issus des [TG 2.0](#TG2).

## I. Présentation générale des classes

[DCAT AP 2 fédéral](#DCATAP2fédéral) inclut toutes les classes et tous les attributs requis par [DCAT AP 2](#DCATAP2). De manière complémentaire et non-impérative, les attributs propres à [GEO DCAT AP 2](#GEODCATAP2) et à [STAT DCAT AP 1](#STATDCATAP1) ont été intégrés dans la mesure où ils répondaient aux besoins exprimés par les administrations fédérales. Il comprend les classes présentées ci-dessous. Les classes reprises en gras sont obligatoires dans tout catalogue conforme à [DCAT AP 2 fédéral](#DCATAP2fédéral) :

- **dcat:Catalog** qui représente et décrit des catalogues ;
- **dcat:Dataset** qui représente et décrit des jeux de données ;
- dcat:Dataservice qui représente et décrit des services (ou des applications oudes API) donnant accès à un ou plusieurs jeux de données ;
- **foaf:Organization** qui représente et décrit des organisations ;
- dcat:Distribution qui représente et décrit des fichiers accessibles d&#39;un jeu de données ;
- dcat:CatalogRecord qui représente et décrit un objet quelconque du catalogue (un jeu de données, un service ou un catalogue) ;
- locn:Address qui représente et décrit des adresses postales d&#39;un agent foaf ;
- skos:Concept qui représente et décrit des concepts ;
- dct:PeriodOfTime qui représente et décrit des périodes temporelles ;
- dqv:QualityMeasurement qui représente et décrit la résolution spatiale de ressources ;
- dct:Location qui représente et décrit des zones géographiques ;
- skos:ConceptScheme qui représente et décrit des thésaurus ;
- vcard:Organization qui représente des organisations ;
- vcard:Address qui représente et décrit des adresses postale.

Le diagramme suivant présentes les classes ainsi que les attributs propres à [DCAT AP 2 fédéral](#DCATAP2fédéral).

![DCATAPfederal](https://user-images.githubusercontent.com/87412262/180747799-287ac27e-a6eb-4766-87fc-4c402d8a81a1.png)


Le point II, ainsi que les tableaux en annexes qui lui sont associés, précise les attributs propres à chaque classe. Il précise en outre les règles applicables au contenu des attributs de chaque classe, ainsi que notamment, l&#39;élément de la fiche [ISO 19139](#ISO19139) à utiliser en cas de conversion. Dans tous les tableaux de l&#39;annexe I, figurent, pour chaque attribut, les éléments suivants :

1. URI : cet élément correspond à l&#39;identifiant unique de l&#39;attribut considéré ;
2. Nom : cet élément correspond au nom français de l&#39;attribut considéré ;
3. Description : cet élément correspond à la description de l&#39;attribut considéré ;
4. Exigence : cet élément correspond à l&#39;un des quatre niveaux d&#39;exigence[^1] propre à l&#39;attribut considéré ;
5. Cardinalité : cet élément correspond aux nombres minimal et maximal d&#39;attributs de ce type autorisés ;
6. Domaine : cet élément correspond aux valeurs acceptables que peut comprendre l&#39;attribut considéré. Si les valeurs acceptables appartiennent à un ou plusieurs ensembles limités (i.e. un thésaurus), alors le ou les ensembles optionnels, recommandés et obligatoires sont repris à l&#39;annexe II  ;
7. Source : cet élément correspond au XPATH de l&#39;élément **impérativement utilisé** comme valeur de l&#39;attribut considérési la classe à laquelle il appartient est mise en correspondance avec une classe [ISO 19115](#ISO19115) et si son domaine correspond à une valeur unilingue, à une valeur multilingue ou à un URL. Si son domaine correspond à une autre classe du présent profil, la source correspond à la classe [ISO 19115](#ISO19115) mise en correspondance avec la classe du présent profil.

Les attributs de domaine « multilingue » doivent être remplis en allemand, en français, en néerlandais et en anglais. Dans la mesure du possible, les attributs de domaine « URL multilingue » doivent être remplis en allemand, en français, en néerlandais et en anglais.

[^1]: Les niveaux applicables sont obligatoire (M), recommandé (R), optionnel (O) et interdit (W). Ce dernier cas de figure n&#39;est applicable que pour les attributs des classes dcat :Catalog et dcat :Dataset qui s&#39;instancient dans la même classe, pour éviter des instanciations en cascade.

## II. Présentation détaillée des classes

### A. Classe dcat:Catalog

La classe dcat :Catalog correspond à un catalogue, c&#39;est-à-dire à un ensemble particulier d&#39;un ou de plusieurs jeux de données et éventuellement de services identifiés et documentés de manière cohérente.

Conformément à ces spécifications, la classe peut s&#39;instancier dans l&#39;élément racine d&#39;une part, et dans les attributs dct :hasPart, dct :isPartOf et dcat :catalog d&#39;autre part. L&#39;instance de la classe dcat :Catalog présente dans l&#39;élément racine correspond au catalogue DCAT considéré. Cette instanciation est **obligatoire** et **unique**.

La ou les instances de la classe dcat :Catalog présentes dans les trois attributs susmentionnés correspondent à des catalogues qui peuvent d&#39;une manière ou d&#39;une autre être associés au catalogue dans lequel ils s&#39;instancient. Ces instanciations sont **optionnelles** et **potentiellement** **multiples**.

#### Profil de la classe

Le présent profil prévoit des spécifications différentes en fonction de l&#39;attribut au sein duquel la classe s&#39;instancie. Celles-ci découlent pour l&#39;essentiel de la nécessité de prévenir une séquence infinie d&#39;instanciations de la classe et des finalités propres à chaque type d&#39;instanciation. En effet, la première instanciation vise à identifier et à décrire exhaustivement le catalogue considéré, alors que les suivantes visent exclusivement à identifier le catalogue considéré.

Les attributs propres à l&#39;instance présente dans l&#39;élément racine sont spécifiés dans le tableau 1 présent en annexe. Les attributs propres aux autres instances sont spécifiés dans le tableau 2 présent en annexe.

Les spécifications applicables à la classe, indépendamment de l&#39;endroit où elle s&#39;instancie, prévoient la possibilité d&#39;expliciter les modalités d&#39;acquisition du catalogue décrit au moyen de l&#39;attribut dcat :Distribution. Il s&#39;agit d&#39;un ajout par rapport à la norme [DCAT AP 2](#DCATAP2).

#### Instanciation à partir d&#39;éléments [INSPIRE]

Seul le contenu de fiches [ISO 19139](#ISO19139) décrivant un [CSW](#CSW) peut être converti en instances de la classe dcat :Catalog. En pareil cas, ces spécifications prévoient que le contenu de chaque attribut de de la classe dcat : Catalog soit pourvu à partir de l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 1.

Le contenu des attributs multilingues ou unilingues doit être pourvu à partir du contenu de l&#39;élément [ISO 19139](#ISO19139) associé. Le contenu des attributs dont le domaine correspond à une classe est égal à une ou plusieurs instanciations de ladite classe conforme(s) aux spécifications du présent profil. Ces instanciations reprennent le contenu de l&#39;élément [ISO 19139](#ISO19139) associé.

De manière dérogatoire, certains attributs ne sont pas mis en correspondance avec des éléments [ISO 19139](#ISO19139). En l&#39;espèce, les règles suivantes sont d&#39;application :

1. Le contenu de l&#39;attribut foaf:homepage doit renvoyer vers une version human readable du catalogue ;
2. Le contenu de l&#39;attribut dcat :themeTaxonomy doit être généré _a posteriori¸_ dès que tous les attributs de toutes les classes sont pourvus, de manière à recenser tous les thésaurus effectivement utilisés dans le catalogue considéré ;
3. Le contenu de l&#39;attribut dct :identifier reste à déterminer. Il pourrait correspondre à l&#39;URL de sérialisation XML du catalogue considéré ;
4. Le contenu de l&#39;attribut dcat :dataset est généré à partir de toutes les fiches décrivant des jeux de données, séries ou cartes statiques accessibles via le [CSW](#CSW);
5. Le contenu de l&#39;attribut dcat :service est généré à partir de toutes les fiches décrivant des services ou des applications accessibles via le [CSW](#CSW).

#### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe dcat : Catalog n&#39;est pas mise en correspondance avec une fiche [ISO 19139](#ISO19139) décrivant un [CSW](#CSW), alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral](#profildemétadonnéesfédéral) applicables à l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 2.

Ces spécifications prévoient également que le contenu des attributs dont le domaine correspond à une classe soit égal à une ou plusieurs instanciations de ladite classe conformes aux spécifications du présent profil.

De manière dérogatoire, certains attributs ne sont pas mis en correspondance avec des éléments ou des classes [ISO 19139](#ISO19139). En l&#39;espèce, les règles suivantes sont d&#39;application :

1. Le contenu de l&#39;attribut foaf:homepage doit renvoyer vers une version human readable du catalogue ;
2. Le contenu de l&#39;attribut dcat :themeTaxonomy doit être généré _a posteriori¸_ dès que tous les attributs de toutes les classes sont pourvus, de manière à recenser tous les thésaurus effectivement utilisés dans le catalogue considéré ;
3. Le contenu de l&#39;attribut dct :identifier reste à déterminer. Il pourrait correspondre à l&#39;URL de sérialisation XML du catalogue considéré ;
4. Le contenu de l&#39;attribut dcat :dataset est généré à partir des jeux de données effectivement intégrés à partir du catalogue ;
5. Le contenu de l&#39;attribut dcat :dataset est généré à partir des services effectivement intégrés à partir du catalogue.


### B. Classe dcat:Dataset

La classe dcat :Dataset correspond à la description d&#39;un jeu de données, c&#39;est-à-dire à un ensemble de données, identifié et maintenu par une organisation, accessible dans un ou plusieurs formats.

Conformément à ces spécifications, la classe peut s&#39;instancier dans les attributs dcat :dataset, dct :source, dcat :servesDataset et foaf :isPrimaryTopicOf. La ou les instances de la classe dcat :Dataset présentes dans l&#39;attribut dcat :dataset correspondent à la description du ou des jeux de données référencés dans le catalogue. Ces instanciations sont **obligatoires** et **potentiellement multiples**.

La ou les instances de la classe dcat :Dataset présentes dans l&#39;attribut dct :source correspondent au jeu de données à l&#39;origine du jeu de données décrit. Ces instanciations sont **recommandées** et **potentiellement multiples**.

La ou les instances de la classe dcat :Dataset présentes dans l&#39;attribut dcat :servesDataset correspondent aux jeux de données accessible au travers du service décrit. Ces instanciations sont **recommandées** et **potentiellement** **multiples**.

Les instances de la classe dcat :Dataset présentes dans l&#39;attribut foaf :isPrimaryTopic correspond à son identification. Ces instanciations sont **obligatoires** et **potentiellement multiples** dès lors que la classe dcat :CatalogRecord est instanciée.

#### Profil de la classe

Le présent profil prévoit des spécifications différentes en fonction de l&#39;attribut au sein duquel la classe s&#39;instancie. Celles-ci découlent pour l&#39;essentiel de la nécessité de prévenir une séquence infinie d&#39;instanciations de la classe et des finalités propres à chaque type d&#39;instanciation. En effet, la première instanciation vise à identifier et à décrire exhaustivement le jeu de données considéré, alors que les suivantes visent exclusivement à identifier le jeu de données considéré.

Les attributs propres aux instances présentes dans l&#39;attribut dcat :dataset sont spécifiés dans le tableau 3 présent en annexe. Les attributs propres aux autres instances sont spécifiés dans le tableau 4 présent en annexe.

Les spécifications applicables à la classe prévoient que les versions d&#39;un même jeu de données correspondent à autant d&#39;instances différentes de la classe dcat :Distribution. Elles ne prévoient dès lors pas les attributs afférents à la version proposés par [DCAT AP 2.0](#DCATAP2).

Les spécifications applicables à la classe incluent les attributs dct :license et adms :representationTechnique car, selon les [TG 2.0](#TG2) et [ISO 19115](#ISO19115), ils caractérisent les jeux de données et non une distribution particulière d&#39;un jeu de données.

Les spécifications applicables à classe prévoient que les instances présentes dans l&#39;attribut dcat :dataset aient au moins un attribut dûment pourvu parmi les attributs suivants (dct :created, dct :modified ou dct :issued).

Les spécifications applicables à la classe prévoient que les instances présentes dans l&#39;attribut dcat :dataset aient au moins un attribut dûment pourvu parmi les attributs suivants (dct :publisher, geodcat :custodian, dct :creator, geodcat :distributor, geodcat : originator, geodcat :principalInvestigator, geodcat :processor, geodcat :resourceProvider, geodcat :user ou dct :rightsHolder).

#### Instanciation à partir d&#39;éléments [INSPIRE]

Seul le contenu des fiches [ISO 19139](#ISO19139) décrivant un jeu de données, une série ou une carte statique peut être converti en instances de la classe dcat :Dataset. En pareil cas, ces spécifications prévoient que le contenu de chaque attribut de de la classe dcat : Dataset soit pourvu à partir de l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 3.

Le contenu des attributs multilingues ou unilingues doit être pourvu à partir du contenu de l&#39;élément [ISO 19139](#ISO19139) associé. Le contenu des attributs dont le domaine correspond à une classe est égal à une ou plusieurs instanciations de ladite classe conforme(s) aux spécifications du présent profil. Ces instanciations reprennent le contenu de l&#39;élément [ISO 19139](#ISO19139) associé.

#### Instanciation sans élément [INSPIRE]
Si l&#39;instance de la classe dcat : Dataset n&#39;est pas mise en correspondance avec une fiche [ISO 19139](#ISO19139) décrivant un jeu de données, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral](#profildemétadonnéesfédéral) applicables à l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 4.

Ces spécifications prévoient également que le contenu des attributs dont le domaine correspond à une classe soit égal à une ou plusieurs instanciations de ladite classe conformes aux spécifications du présent profil.


### C. Classe dcat:DataService

La classe dcat : DataService correspond à la description d&#39;un service de données, c&#39;est-à-dire à un service web, une application ou une API identifié et maintenu par une organisation et donnant accès à un ou plusieurs jeux de données identifiés.

Conformément à ces spécifications, la classe peut s&#39;instancier dans les attributs dcat :service et foaf :isPrimaryTopicOf. La ou les instances de la classe de la classe dcat :DataService présentes dans l&#39;attribut dcat :service correspondent à la description du ou des services référencés dans le catalogue. Ces instanciations sont **recommandées** et **potentiellement multiples**.

Les instances de la classe dcat : DataService présentes dans l&#39;attribut foaf :isPrimaryTopic correspond à son identification. Ces instanciations sont **obligatoires** et **potentiellement multiples** dès lors que la classe dcat :CatalogRecord est instanciée.

#### Profil de la classe

Le présent profil prévoit des spécifications différentes en fonction de l&#39;attribut au sein duquel la classe s&#39;instancie. Celles-ci découlent pour l&#39;essentiel des finalités propres à chaque type d&#39;instanciation. En effet, la première instanciation vise à identifier et à décrire exhaustivement le service considéré, alors que l&#39;instanciation suivante vise exclusivement à identifier le service considéré.

Les attributs propres aux instances présentes dans l&#39;attribut dcat :service sont spécifiés dans le tableau 5 présent en annexe. Les attributs propres aux autres instances sont spécifiés dans le tableau 6 présent en annexe.

Les spécifications applicables à la classe incluent les attributs dct :license et dct :conformsTo car, selon les [TG 2.0](#TG2) et [ISO 19115](#ISO19115), ils caractérisent les services.

Les spécifications applicables à classe prévoient que les instances présentes dans l&#39;attribut dcat :service ait au moins un attribut dûment pourvu parmi les attributs suivants (dct :created, dct :modified ou dct :issued).

Les spécifications applicables à la classe prévoient que les instances présentes dans l&#39;attribut dcat :service ait au moins un attribut dûment pourvu parmi les attributs suivants (dct :publisher, geodcat :custodian, dct :creator, geodcat :distributor, geodcat : originator, geodcat :principalInvestigator, geodcat :processor, geodcat :resourceProvider, geodcat :user ou dct :rightsHolder).

#### Instanciation à partir d'éléments [INSPIRE]

Seul le contenu des fiches [ISO 19139](#ISO19139) décrivant un service de visualisation, un service de téléchargement ou une application peut être converti en instances de la classe dcat :DataService. En pareil cas, ces spécifications prévoient que le contenu de chaque attribut de de la classe dcat: DataService soit pourvu à partir de l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 5. Le contenu de fiches décrivant un service de découverte ne peut être converti en instances de la classe dcat : DataService.

Le contenu des attributs multilingues ou unilingues doit être pourvu à partir du contenu de l&#39;élément [ISO 19139](#ISO19139) associé. Le contenu des attributs dont le domaine correspond à une classe est égal à une ou plusieurs instanciations de ladite classe conforme(s) aux spécifications du présent profil. Ces instanciations reprennent le contenu de l&#39;élément [ISO 19139](#ISO19139) associé.

En outre, les spécifications de [DCAT AP 2 fédéral](#DCATAP2fédéral) prévoient d&#39;instancier, pour chaque jeu de données accessibles au moyen des services décrits, la classe dcat :Dataset dans la classe dcat :Catalog. En effet, il est nécessaire d&#39;instancier explicitement dans tout catalogue [DCAT AP](#DCATAP) les jeux de données au moyen de la classe dcat :Dataset accessibles via les services considérés.

#### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe dcat :DataService n&#39;est pas mise en correspondance avec une fiche [ISO 19139](#ISO19139) décrivant un service éligible, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral](#profildemétadonnéesfédéral) applicables à l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 6.

Ces spécifications prévoient également que le contenu des attributs dont le domaine correspond à une classe soit égal à une ou plusieurs instanciations de ladite classe conformes aux spécifications du présent profil.


### D. Classe dcat:Distribution

La classe dcat : Distribution correspond à la description d&#39;un fichier numérique particulier d&#39;une ressource considérée, c&#39;est-à-dire un fichier numérique dans un format particulier.

Conformément à ces spécifications, la classe peut s&#39;instancier dans l&#39;attribut dcat :distribution.

#### Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe sont spécifiés dans le tableau 7 présent en annexe.

Les spécifications applicables à la classe incluent les attributs dct :temporal et dct : spatial de manière à spécifier, s&#39;il échet, la couverture temporelle du fichier distribué (i.e. la version) et son emprise géographique.

#### Instanciation à partir d'éléments [INSPIRE]

Seul le contenu des [ATOMFeed] décrivant les liens de téléchargement d&#39;un jeu de données peut être converti en instances de la classe dcat :Distribution. En pareil cas, ces spécifications prévoient que le contenu de chaque attribut de la classe dcat :Distribution soit pourvu à partir de l&#39;élément [ATOMFeed](#ATOMFeed) qui lui est associé dans le tableau 7. Les instances de la classe présentes dans une instance de dcat :Catalog ne sont pas générées à partir d&#39;un élément [INSPIRE](#INSPIRE).

Le contenu des attributs multilingues ou unilingues doit être pourvu à partir du contenu de l&#39;élément [ATOMFeed](#ATOMFeed) associé. Le contenu des attributs dont le domaine correspond à une classe est égal à une ou plusieurs instanciations de ladite classe conforme(s) aux spécifications du présent profil. Ces instanciations reprennent le contenu de l&#39;élément [ATOMFeed](#ATOMFeed) associé.

#### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe dcat :Distribution n&#39;est pas mise en correspondance avec un [ATOMFeed](#ATOMFeed), alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral](#profildemétadonnéesfédéral) applicables à l&#39;élément de l&#39;[ATOMFeed](#ATOMFeed) qui lui est associé dans le tableau 7.

Ces spécifications prévoient également que le contenu des attributs dont le domaine correspond à une classe soit pourvu au moyen d&#39;une ou de plusieurs instanciations de ladite classe conformes aux spécifications du présent profil.


### E. Classe foaf:Organization

La classe foaf :Organization correspond à la description d&#39;une organisation, c&#39;est-à-dire un ensemble structuré de personnes ayant un ou des buts déterminés.

Conformément à ces spécifications, la classe peut s&#39;instancier dans les attributs dct :publisher, geodcat :custodian, dct :creator, geodcat :distributor, geodcat : originator, geodcat :principalInvestigator, geodcat :processor, geodcat :resourceProvider, geodcat :user ou dct :rightsHolder.

#### Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe sont spécifiés dans le tableau 8 présent en annexe.

#### Instanciation à partir d'éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 19139](#ISO19139) relative aux organisations peut être converti en instances de la classe foaf :Organization. En pareil cas, ces spécifications prévoient que le contenu de chaque attribut de de la classe foaf : Organization soit pourvu à partir de l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 8.

Le contenu des attributs multilingues ou unilingues doit être pourvu à partir du contenu de l&#39;élément [ISO 19139](#ISO19139) associé. Le contenu des attributs dont le domaine correspond à une classe est égal à une ou plusieurs instanciations de ladite classe conforme(s) aux spécifications du présent profil. Ces instanciations reprennent le contenu de l&#39;élément [ISO 19139](#ISO19139) associé.

De manière dérogatoire, certains attributs ne sont pas mis en correspondance avec des éléments ou des classes [ISO 19115](#ISO19115). En l&#39;espèce, les règles suivantes sont d&#39;application :

a) Le contenu de l&#39;attribut dct :type n&#39;est mis en association avec aucun élément [ISO 19115](#ISO19115). Dès lors, il n&#39;est pas pourvu pour les instances présentes dans les classes qui correspondent au résultat de la conversion d&#39;une fiche [ISO 19139](#ISO19139).

#### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe foaf : Organization n&#39;est mise en correspondance avec un instance de la classe [ISO 19139](#ISO19139) relative à une organisation, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral](#profildemétadonnéesfédéral) applicables à l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 8.

Ces spécifications prévoient également que le contenu des attributs dont le domaine correspond à une classe soit pourvu au moyen d&#39;une ou de plusieurs instanciations de ladite classe conformes aux spécifications du présent profil.


### F. Classe dcat:catalogRecord

La classe dcat :CatalogRecord correspond à l&#39;identification des instances particulières des classes dcat :Dataset, dcat :DataService (dcat :Catalog).

Conformément à ces spécifications, la classe peut s&#39;instancier dans la classe dcat :Catalog. Les instances sont **recommandées** et **potentiellement** **multiple**.

#### Remarques concernant les attributs de la classe

Cette classe vise à identifier et à décrire exhaustivement les classes considérées. Dès lors, les attributs propres à cette classe sont spécifiés dans le tableau 9 présent en annexe.

#### Remarques concernant le contenu de la classe

Si une classe dcat : CatalogRecord se rapporte à une classe quelconque qui n&#39;est pas mise en correspondance avec une fiche [ISO 19139](#ISO19139), alors ces spécifications prévoient que le contenu des attributs des classes dcat : CatalogRecord soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral](#profildemétadonnéesfédéral) applicables à ces mêmes éléments.

Si une classe dcat : CatalogRecord se rapporte à une classe quelconque qui est mise en correspondance avec une fiche [ISO 19139](#ISO19139), alors ces spécifications prévoient que le contenu des attributs provienne des éléments de la fiche [ISO 19139](#ISO19139) référencés dans la colonne XPATH Source.

Certains attributs ne sont pas mis en correspondance avec les élément [ISO 19115](#ISO19115). En pareil cas, ces spécifications prévoient des sources alternatives. En l&#39;espèce, les règles relatives aux attributs suivants sont d&#39;application :

a) Le contenu de l&#39;attribut foaf :primaryTopic doit être généré _a posteriori¸_ dès que toutes les classes ont été instanciées, de manière à toutes les référencer.


### G. Classe locn:Address

La classe locn :Address correspond à la description de l&#39;adresse postale d&#39;un agent foaf.

Conformément à ces spécifications, la classe peut s&#39;instancier dans l&#39;attribut locn:address.

#### Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres aux instances sont spécifiés dans le tableau 9 présent en annexe.

##### Instanciation à partir d'éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 19115](#ISO19115) relative aux adresses postales peut être converti en instances de la classe locn : Address. En pareil cas, ces spécifications prévoient que chaque attribut de la classe locn :Address soit pourvu à partir de l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 9.

#### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe locn : Address n&#39;est mise en correspondance avec un instance de la classe [ISO 19139](#ISO19139) relative à une organisation, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral](#profildemétadonnéesfédéral) applicables à l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 9.


### H. Classe skos:Concept

La classe skos :Concept correspond à la description d&#39;un concept, c&#39;est-à-dire une notion identifiée de manière univoque et nommée en au moins une langue.

Conformément à ces spécifications, la classe peut s&#39;instancier dans les attributs dcat :theme, dct :language, dct :subject, dct : adms:representationTechnique, dct :type, adms :status et sdmx-attribut:unitMeasure.

#### Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe skos :Concept sont spécifiés dans le tableau 10 présent en annexe.

#### Instanciation à partir d'éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 19139](#ISO19139) relatives à des mots-clés issus de thésaurus et dûment identifiées par une URI peut être directement converti en instances de la classe skos : Concept.

En pareil cas, ces spécifications prévoient que chaque attribut de la classe skos :Concept soit pourvu à partir de l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 10.

Le contenu des instances des classes [ISO 19139](#ISO19139) relatives aux langues, aux thèmes [ISO 19115](#ISO19115), au type de représentation spatiale, à la résolution spatiale des ressources matricielles et au type de service peut également être converti en instances de la classe skos:Concept.

En pareil cas, ces spécifications prévoient que chaque attribut de la classe skos :Concept soit pourvu sur base de concepts issus de thésaurus SKOS sémantiquement identiques aux éléments [ISO 19139](#ISO19139) considérés. L&#39;annexe II propose pour chaque valeur de ces éléments [ISO 19139](#ISO19139), un concept skos identique.

#### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe skos :Concept n&#39;est mise en correspondance avec un élément [ISO 19139](#ISO19139), alors ces spécifications prévoient que le contenu des attributs soit pourvu par des concepts issus de thésaurus SKOS. L&#39;annexe II propose, pour chaque attribut où peut s&#39;instancier la classe skos :Concept, une liste de thésaurus obligatoires, recommandés ou optionnels.


### I. Classe dct:PeriodOfTime

La classe dct:PeriodOfTime correspond à la description d&#39;une séquence temporelle, c&#39;est-à-dire un intervalle de temps borné.

Conformément à ces spécifications, la classe peut s&#39;instancier dans l&#39;attribut dct :temporal.

#### Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe dct:PeriodOfTime sont spécifiés dans le tableau 11 présent en annexe.

#### Instanciation à partir d'éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 19139](#ISO19139) relative aux séquences temporelles peut être converti en instances de la classe dct : PeriodOfTime. En pareil cas, ces spécifications prévoient que chaque attribut de la classe dct :PeriodOfTime soit pourvu à partir de l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 11.

#### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe dct : PeriodOfTime n&#39;est mise en correspondance avec un instance de la classe [ISO 19139](#ISO19139) relative à une séquence temporelle, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral](#profildemétadonnéesfédéral) applicables à l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 11.


### J. Classe dqv:QualityMeasurement

La classe dqv: QualityMeasurement correspond à la résolution spatiale de la ressource considérée, c&#39;est-à-dire au niveau de détail de la ressource.

Conformément à ces spécifications, la classe peut s&#39;instancier dans l&#39;attribut dqv:hasQualityMeasurement. L&#39;instanciation est **recommandée** et **unique**.

#### Profil de la classe

Le présent profil prévoit des spécifications différentes en fonction de l&#39;endroit où la classe s&#39;instancie. Celles-ci découlent pour l&#39;essentiel de la nécessité de décrire la résolution spatiale au moyen de notions adaptés au type de ressource.

Les attributs propres aux instances relatives aux ressources vectorielles sont spécifiés dans le tableau 12 présent en annexe. Les attributs propres à toutes les instances relatives aux ressources matricielles sont spécifiés dans le tableau 13 présent en annexe.

#### Instanciation à partir d'éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 19139](#ISO19139) relative à la résolution spatiale peut être converti en instances de la classe dqv : QualityMeasurement. En pareil cas, ces spécifications prévoient que chaque attribut soit pourvu à partir de l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau en annexe.

#### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe dqv : QualityMeasurement n&#39;est mise en correspondance avec un élément [ISO 19139](#ISO19139) relatif à la résolution spatiale, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral](#profildemétadonnéesfédéral) applicables à l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau en annexe.


### K. Classe dct:Location

La classe dct : Location correspond à la description d&#39;une zone géographique, c&#39;est-à-dire une portion bornée de la surface terrestre.

Conformément à ces spécifications, la classe peut s&#39;instancier dans l&#39;attribut dct :location.

#### Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe dct :Location sont spécifiés dans le tableau 14 présent en annexe.

En l&#39;absence de standards réellement communs, les spécifications applicables à la classe incluent les attributs locn :geometry et dcat :bbox. Le contenu de ces deux attributs doit être rigoureusement identiques et renvoyer vers la description de l&#39;emprise au sol de la ressource dans un format spécifique. Les deux attributs doivent être notés quatre fois, de manière à spécifier l&#39;emprise au sol selon les formats suivants :

- [Well Know Text ](http://www.opengis.net/ont/geosparql#wktLiteral);
- [Geographic Markup Language ](http://www.opengis.net/ont/geosparql#gmlLiteral);
- GeoJSON au moyen de :
  - L&#39;[identifiant IANA](https://www.iana.org/assignments/media-types/application/vnd.geo+json) ;
  - L&#39;[identifiant opengis](http://www.opengis.net/ont/geosparql#geoJSONLiteral).

#### Instanciation à partir d'éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 19139](#ISO19139) relative à la résolution spatiale peut être converti en instances de la classe dct :Location. En pareil cas, ces spécifications prévoient que chaque attribut soit pourvu à partir de l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau en annexe.

#### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe dct :Location n&#39;est mise en correspondance avec un instance de la classe [ISO 19139](#ISO19139) relative à une organisation, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral](#profildemétadonnéesfédéral) applicables à l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 14.


### L. Classe skos:ConceptScheme

La classe skos:ConceptSchemecorrespond à la description d&#39;un thésaurus, c&#39;est-à-dire un ensemble structuré de concepts mis en relation.

Conformément à ces spécifications, la classe peut s&#39;instancier dans l&#39;attribut dcat:themeTaxonomy.

#### Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe skos : ConceptSchemesont spécifiés dans le tableau 15 présent en annexe.

#### Instanciation à partir d'éléments [INSPIRE]

Aucune classe [ISO 19115](#ISO19115) ne peut être convertie en une instance de la classe skos :ConceptScheme.

#### Instanciation sans élément [INSPIRE]

Ces spécifications prévoient que la classe skos : ConceptScheme soit instanciée _a posteriori_, alors que toutes les autres classes ont été dûment instanciées. Ces spécifications prévoient que la classe skos :ConceptScheme soit instanciée sur base des URL présents dans les attributs skos :inScheme des instances de la classe skos :Concept.


### M. Classe vcard:Organization

La classe vcard :Organization correspond à la description d&#39;une organisation, c&#39;est-à-dire un ensemble structuré de personnes ayant un ou des buts déterminés.

Conformément à ces spécifications, la classe peut s&#39;instancier dans les attributs dcat:contactPoint.

#### Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe vcard: Organization sont spécifiés dans le tableau 16 présent en annexe.

#### Instanciation à partir d'éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 19139](#ISO19139) relative aux organismes peut être converti en instances de la classe vcard :Organization. En pareil cas, ces spécifications prévoient que chaque attribut de la classe vcard : Organization soit pourvu à partir de l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 16.

Ces spécifications prévoient également que les attributs dont le domaine correspond à une classe soient pourvus au moyen d&#39;une ou de plusieurs instanciations de ladite classe conformes aux spécifications du présent profil.

#### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe vcard :Organization n&#39;est mise en correspondance avec un instance de la classe [ISO 19139](#ISO19139) relative à une organisation, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral](#profildemétadonnéesfédéral) applicables à l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau en annexe.

Ces spécifications prévoient également que le contenu des attributs dont le domaine correspond à une classe soit pourvu au moyen d&#39;une ou de plusieurs instanciations de ladite classe conformes aux spécifications du présent profil.


### N. Classe vcard:Address

La classe vcard :Address correspond à la description d&#39;une adresse postale d&#39;un agent vcard.

Conformément à ces spécifications, la classe peut s&#39;instancier dans la classe vcard :Organization.

#### Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe vcard :Address sont spécifiés dans le tableau 17 présent en annexe.

#### Instanciation à partir d'éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 19139](#ISO19139) relative aux adresses postales peut être converti en instances de la classe vcard : Address. En pareil cas, ces spécifications prévoient que chaque attribut de la classe vcard :Address soit pourvu à partir de l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 17.

#### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe vcard : Address n&#39;est mise en correspondance avec un instance de la classe [ISO 19139](#ISO19139) relative à une organisation, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral](#profildemétadonnéesfédéral) applicables à l&#39;élément [ISO 19139](#ISO19139) qui lui est associé dans le tableau 17.

## Normes référencées

<a id="ISO19115"></a>
[ISO 19115](https://www.iso.org/standard/26020.html) : 

norme ISO relative aux métadonnées de jeux de données et de services à caractère géographique utilisée pour implémenter la [directive INSPIRE](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32007L0002&from=FR)

<a id="ISO19139"></a>
[ISO 19139](https://www.iso.org/fr/standard/32557.htm) : 

norme ISO relative à l&#39;implémentation XML de la norme [ISO 19115](#ISO19115) utilisée pour implémenter la [directive INSPIRE](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32007L0002&from=FR)

<a id="TG2"></a>
[TG 2.0](https://inspire.ec.europa.eu/id/document/tg/metadata-iso19139) : 

norme d&#39;implémentation des métadonnées INSPIRE basée sur les normes [ISO 19115](#ISO19115) et [ISO 19139](#ISO19139)

<a id="profildemétadonnéesfédéral"></a>
profil de métadonnées fédéral :

norme fédérale non-officielle conforme aux [TG 2.0](#TG2)

<a id="CSW"></a>
[CSW](https://portal.ogc.org/files/?artifact_id=20555) : 

norme OGC relative à la publication de métadonnées

<a id="TGrelativesauxservicesdedécouverte"></a>
TG relatives aux services de découverte : 

norme d&#39;implémentation des services de découverte INSPIRE

<a id="DCAT"></a>
[DCAT](https://www.w3.org/TR/vocab-dcat-1/) : 

norme W3C pour standardiser les catalogues de jeux de données sur le web

<a id="DCAT2"></a>
[DCAT 2](https://www.w3.org/TR/vocab-dcat-1/) : 

norme W3C pour standardiser les catalogues de jeux de données sur le web

<a id="DCATAP1"></a>
[DCAT AP 1](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/11) : 

norme ISA implémentant le standard [DCAT](#DCAT) et lui étant conforme pour décrire les jeux de données publics distribués dans l&#39;Union

<a id="DCATAP2"></a>
[DCAT AP 2](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/200) : 

norme ISA implémentant le standard [DCAT 2](#DCAT2) et lui étant conforme pour décrire les jeux de données publics distribués dans l&#39;Union

<a id="GeoDCATAP2"></a>
[Geo DCAT AP 2](https://semiceu.github.io/GeoDCAT-AP/drafts/latest/#properties-for-distribution) : 

norme ISA implémentant le standard [DCAT AP 2](#DCATAP2) et lui étant conforme pour décrire les jeux de données publics géographiques distribués dans l&#39;Union

<a id="StatDCATAP1"></a>
[Stat DCAT AP 1](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/statdcat-application-profile-data-portals-europe/release/100) :

norme ISA implémentant le standard [DCAT AP 1](#DCATAP1) et lui étant conforme pour décrire les jeux de données publics statistiques distribués dans l&#39;Union

<a id="DCATAP2fédéral"></a>
DCAT AP 2 fédéral : 

norme fédérale informelle contenue dans le présent document conforme à [DCAT AP 2](#DCATAP2)

<a id="ATOM"></a>
[ATOM](https://tools.ietf.org/html/rfc4287) : 

norme IETF relative à la syndication de contenus

<a id="TGrelativesauxservicesdetéléchargement"></a>
[TG relatives aux services de téléchargement](https://inspire.ec.europa.eu/documents/technical-guidance-implementation-inspire-download-services) : 

norme d&#39;implémentation des services de téléchargement INSPIRE basée sur les normes [WFS] et [ATOM](#ATOM)

# Annexe I

## A. dcat:Catalog

### Instanciation de dcat:Catalog
| URI                 | Nom                                     | Description                                                                                         | Exigence première instanciation | Exigence autre instanciation | Cardinalité | Domaine             | Source                                                                                                                                                                                                                                                       |
| ------------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------- | ---------------------------- | ----------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| dct:title           | titre                                   | Titre du catalogue considéré                                                                        | M                               | M                            | 1           | multilingue         | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:title                                                                                                                                                                                        |
| dct:description     | description                             | Description du catalogue considéré                                                                  | M                               | O                            | 1           | multilingue         | //\*/gmd:identificationInfo/\*/gmd:abstract                                                                                                                                                                                                                  |
| dct:publisher       | éditeur                                 | Organisation responsable de la publication du catalogue considéré                                   | M                               | O                            | 1           | foaf:Organization   | //\*/gmd:contact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue=’publisher’]]                                                                                                                                                               |
| dcat:dataset        | jeu de données                          | Informations relatives au(x) jeu(x) de données référencés dans le catalogue considéré               | R                               | W                            | 0-n         | dcat:Dataset        | [si catalogue généré à partir d'un CSW --> getrecords avec type = dataset <> si catalogue généré par wizard : génération a posteriori sur base des datasets renseignés](https://github.com/belgif/inspire-dcat/blob/main/DCATAPprofil.fr.md#CSW)             |
| dcat:service        | service                                 | Informations relatives au(x)service(s) référencés dans le catalogue considéré                       | R                               | W                            | 0-n         | dcat:DataService    | [si catalogue généré à partir d'un CSW --> getrecords avec type = service/application <> si catalogue généré par wizard : génération a posteriori sur base des services renseignés](https://github.com/belgif/inspire-dcat/blob/main/DCATAPprofil.fr.md#CSW) |
| foaf:homepage       | page d'acceuil                          | Version human readable du catalogue considéré                                                       | R                               | R                            | 0-4         | rdf:Description     | [Pas de XPATH : https://www.geo.be/home (ou homepage du catalogue propre à l'institution si celui-ci est harvesté)](https://www.geo.be/home)                                                                                                                 |
| dct:language        | langue                                  | Langue(s) dans le(s)quelle(s) on peut consulter le catalogue considéré                              | M                               | O                            | 1-4           | skos:Concept        | //\*/gmd:locale/gmd:PT_Locale/gmd:languageCode/gmd:LanguageCode/@codeListValue                                                                                                                                                                               |
| dct:issued          | date de première publication            | Date de première publication du catalogue                                                           | R                               | O                            | 0-1         | date (YYYY-MM-DD)   | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='publication']]/gmd:date                                                                                                    |
| dct:spatial         | couverture spatiale                     | Description de la couverture spatiale des ressources comprises dans le catalogue                    | R                               | O                            | 0-n         | dct:Location        | //\*/gmd :identificationInfo/\*/gmd :extent/gmd :EX_Extent/gmd :geographicElement                                                                                                                                                                            |
| dcat:themeTaxonomy | vocabulaire contrôlé                    | Informations relatives aux thésaurus dont sont extraits les mots clés décrivant les jeux de données | O                               | W                            | 0-n         | skos :ConceptScheme | génération a posteriori en recensant tous les thésaurus référencés dans les classes Dataset et DataService                                                                                                                                                   |
| dct:hasPart        | catalogue inclus                        | Informations relatives au(x) catalogue(s) compris dans le catalogue considéré                       | O                               | W                            | 0-n         | dcat:Catalog        | [si catalogue généré à partir d’un CSW --> néant <> si catalogue généré par wizard : prévoir champ](https://github.com/belgif/inspire-dcat/blob/main/DCATAPprofil.fr.md#CSW)                                                                                 |
| dct:isPartOf        | catalogue incluant                      | Informations relatives au(x) catalogue(s) comprenant dans le catalogue considéré                    | O                               | W                            | 0-n         | dcat:Catalog        | [si catalogue généré à parti’ d'un CSW --> ID du catalogue de BOSA + ID du catalogue suprême DCAT de l'IGN <> si catalogue généré par wizard : prévoir champ](https://github.com/belgif/inspire-dcat/blob/main/DCATAPprofil.fr.md#CSW)                       |
| dcat:record         | signalétique                            | Informations relatives aux instances figurant dans le catalogue considéré                           | R                               | W                            | 0-n         | dcat:CatalogRecord  | génération a posteriori en recensant toutes les instances CatalogRecord                                                                                                                                                                                      |
| dcat:distribution   | distribution                            | Informations relatives aux modalité’ d'acquisition du catalogue                                     | R                               | R                            | 0-n         | dcat:Distribution   | \--> générer en utilisant le lien vers la sérialisation XML (et éventuellement JSON)                                                                                                                                                                         |
| dcat:catalog        | catalogue                               | Catalogue dont le contenu est intéressant dans le contexte du catalogue décrit                      | O                               | W                            | 0-n         | dcat:Catalog        | [si catalogue généré à parti’ d'un CSW --> néant <> si catalogue généré par wiz rd : prévoir champ](https://github.com/belgif/inspire-dcat/blob/main/DCATAPprofil.fr.md#CSW)                                                                                 |
| dcat:contactPoint   | point de contact du catalogue considéré | Informations relatives aux modalités de prise de contact à propos du catalogue                      | R                               | R                            | 0-1         | vcard:Organization  | //\*/ gmd:contact/ gmd:CI_ResponsibleParty[ gôleole/ gmd:CI_RoleCode[@codeListValue=’publisher’]]                                                                                                                                                            |
| dct:identifier      | identifiant                             | Identifiant alphanumérique unique du catalogue                                                      | M                               | M                            | 1           | unilingue           | Pas de XPATH : sérialisation X ML ?                                                                                                                                                                                                                          |
| dcat:theme          | mot-clé issu d'un vocabulaire contrôlé  | Mot clé iss’ d'un thésaurus décrivant le jeu de données                                             | O                               | W                            | 0-n         | skos:Concept        | //\*/ gmd:identificationInfo/\*/ gmd:descriptiveKeywords/ gmd:MD_Keywords[ gmd:thesaurusName/ gmd:CI_Citation/ gmd:title/\*={}]/ gmd:keyword/\*                                                                                                              |

**Tableau  1 : classe dcat:Catalog**

## B. dcat:Dataset

### Instanciation de dcat:Dataset
| URI                           | Nom                                     | Description                                                                                                                                                       | Exigence instanciée dans l'attribut dcat:dataset | Exigence dans tout autre attribut | Cardinalité | Domaine                 | Source                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | --------------------------------- | ----------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dct:title                     | titre                                   | Titre du jeu de données considéré                                                                                                                                 | M                                                | M                                 | 1           | multilingue             | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:title/\* (titre saisi conformément aux spécifications du profil fédéral)                                                                                                                                                                                                                                                                      |
| dct:description               | description                             | Description du jeu de données considéré                                                                                                                           | M                                                | O                                 | 1           | multilingue             | //\*/gmd:identificationInfo/\*/gmd:abstract/\*                                                                                                                                                                                                                                                                                                                                                                |
| dcat:contactPoint             | point de contact                        | Informations relatives aux modalités de prise de contact à propos du jeu de données                                                                               | O                                                | O                                 | 0-n         | vcard:Organization      | //\*/gmd:contact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='pointOfContact']]                                                                                                                                                                                                                                                                                                           |
| dcat:distribution             | distribution                            | Informations relatives aux modalités d'acquisition du jeu de données considéré                                                                                    | R                                                | W                                 | 0-n         | dcat:distribution       | [si dataset généré à partir d'une fiche ISO 19139 --> utiliser contenu de l'ATOM FEED référencé dans la dite fiche <> si dataset généré par wizard : générer par saisie manuelle dans un champ ad hoc](https://github.com/marielleadam/inspire-dcat/edit/main/DCATAPprofil.fr.md#ISO19139)                                                                                                                    |
| dcat:keyword                  | mot-clé                                 | Mot-clé libre décrivant le jeu de données considéré                                                                                                               | O                                                | W                                 | 0-n         | multilingue             | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD_Keywords[not(./gmd:thesaurusName)]/gmd:keyword/\*                                                                                                                                                                                                                                                                                               |
| dcat:theme                    | mot-clé issu d'un vocabulaire contrôlé  | Mot-clé issu d'un thésaurus décrivant le jeu de données                                                                                                           | M                                                | W                                 | 1-n         | skos:concept            | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD_Keywords[gmd:thesaurusName/gmd:CI_Citation/gmd:title/\*={}]/gmd:keyword/\*                                                                                                                                                                                                                                                                      |
| dct:subject                   | catégorie ISO                           | [Informations relatives à la catégorie ISO 19115 du jeu de données considéré](https://github.com/marielleadam/inspire-dcat/edit/main/DCATAPprofil.fr.md#ISO19115) | O                                                | W                                 | 0-n         | skos:Concept            | //\*/gmd:identificationInfo/\*/gmd:topicCategory/\*                                                                                                                                                                                                                                                                                                                                                           |
| dct:spatial                   | couverture spatiale                     | Informations relatives à la région géographique visée par le jeu de données concerné                                                                              | R                                                | W                                 | 0-n         | dct:location            | //\*/gmd:identificationInfo/\*/gmd:extent/gmd:EX_Extent/gmd:geographicElement                                                                                                                                                                                                                                                                                                                                 |
| dct:temporal                  | couverture temporelle                   | Informations relatives au(x) laps de temps couvert(s) par le jeu de données concerné                                                                              | R                                                | W                                 | 0-n         | dct:PeriodOfTime        | //\*/gmd:identificationInfo/\*/gmd:extent/gmd:EX_Extent/gmd:temporalElement                                                                                                                                                                                                                                                                                                                                   |
| dct:created                   | date de création                        | Date de création du jeu de données considéré                                                                                                                      | R                                                | W                                 | 0-1         | date (YYYY-MM-DD)       | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='creation']]/gmd:date                                                                                                                                                                                                                                                        |
| dct:modified                  | date de mise à jour                     | Date de dernière modification du jeu de données                                                                                                                   | R                                                | W                                 | 0-1         | date (YYYY-MM-DD)       | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='revision']]/gmd:date                                                                                                                                                                                                                                                        |
| dct:issued                    | date de première publication            | Date de première publication du jeu de données                                                                                                                    | O                                                | W                                 | 0-1         | date (YYYY-MM-DD)       | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='publication']]/gmd:date                                                                                                                                                                                                                                                     |
| foaf:page                     | page des métadonnées                    | Informations relatives au(x) lien(s) détaillant le contenu du jeu de données                                                                                      | R                                                | R                                 | 0-1         | URL multilingue         | //\*/gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource[gmd:protocol/\*={WWW:LINK-1.0-http--link} and gmd:function/\*/@codeListValue={'information'}]/gmd:linkage/gmd:name                                                                                                                                                           |
| dct:accrualPeriodicity        | fréquence de mise à jour                | Informations relatives à la fréquence de mise à jour du jeu de données concerné                                                                                   | R                                                | W                                 | 0-1         | skos:Concept            | //\*/gmd:identificationInfo/\*/gmd:resourceMaintenance/gmd:MD_MaintenanceInformation/gmd:maintenanceAndUpdateFrequency/gmd:MD_MaintenanceFrequencyCode/@codeListValue                                                                                                                                                                                                                                         |
| dct:identifier                | identifiant                             | Identifiant alphanumérique unique du jeu de données concerné                                                                                                      | M                                                | M                                 | 1           | unilingue             | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:identifier/\*/gmd:code/\*                                                                                                                                                                                                                                                                                                                     |
| dcat:landingPage              | page d'accueil                          | Page de métadonnées HTML d’origine                                                                                                                                | R                                                | R                                 | 0-4         | rdf:Description         | [https://www.geo.be/catalog/details/ + //\*/gmd:fileIdentifier](https://www.geo.be/catalog/details/)                                                                                                                                                                                                                                                                                                          |
| dct:language                  | langue                                  | Informations relatives au(x) langue(s) du jeu de données considéré                                                                                                | R                                                | W                                 | 0-4         | skos:Concept            | //\*/gmd:identificationInfo/\*/gmd:language/gmd:LanguageCode/@codeListValue                                                                                                                                                                                                                                                                                                                                   |
| dct:provenance                | origine                                 | Informations relatives à l'origine du jeu de données considéré                                                                                                    | O                                                | W                                 | 0-1         | dct:ProvenanceStatement | //\*/gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:statement                                                                                                                                                                                                                                                                                                                          |
| dct:conformsTo                | spécification ou règle de structuration | Informations relative(s) aux normes de qualité du jeu de données                                                                                                  | O                                                | W                                 | 0-n         | dct:Standard            | //\*/gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:report/gmd:DQ_DomainConsistency/gmd:result/gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation ET //\*/gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource[gmd:protocol/\*={WWW:LINK-1.0-http--link} and gmd:function/\*/@codeListValue={'information'}]/gmd:linkage/gmd:name  |
| dct:source                    | jeu de données source                   | Informations relatives à un jeu de données source                                                                                                                 | O                                                | W                                 | 0-1         | dcat:Dataset            | [si dataset généré à partir d'une fiche ISO 19139 --> utiliser le XPATH //\*/gmd:identificationInfo/\*/gmd:aggregationInfo <> si dataset généré par wizard : générer par sélection manuelle dans un champ ad hoc](https://github.com/marielleadam/inspire-dcat/edit/main/DCATAPprofil.fr.md#ISO19139)                                                                                                         |
| dqv:hasQualityMeasurement     | résolution spatiale                     | Informations relatives à l’échelle conceptuelle du jeu de données considéré                                                                                       | R                                                | W                                 | 0-1         | dqv:QualityMeasurement  | //\*/gmd:identificationInfo/\*/gmd:spatialResolution/gmd:MD_Resolution                                                                                                                                                                                                                                                                                                                                        |
| dct:accessRights              | accessibilité                           | Informations relatives aux restrictions concernant l'utilisation du jeu de données                                                                                | M                                                | W                                 | 1           | dct:rightsStatement     | [//\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD_LegalConstraints[\*/gmd:MD_RestrictionCode[@codeListValue='otherRestrictions']]/gmd:otherConstraints[gco:CharacterString or gmx:Anchor[not(starts-with(@xlink:href, 'http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))\\]\\]](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))%5C%5D%5C%5D) |
| adms:sample                   | exemple de distribution                 | Référence à un exemple de distribution du jeu de données                                                                                                          | O                                                | W                                 | 0-1         | dcat:Distribution       | pas de XPATH spécifié                                                                                                                                                                                                                                                                                                                                                                                         |
| dct:publisher                 | éditeur                                 | Informations relatives à l'organisation responsable de la disponibilité du jeu de données                                                                         | R                                                | W                                 | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='publisher']]                                                                                                                                                                                                                                                                               |
| geodcat:custodian             | mainteneur                              | Informations relatives à l'organisation responsable de la données et de la maintenance de la ressource                                                            | O                                                | W                                 | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='custodian']]                                                                                                                                                                                                                                                                               |
| dct:creator                   | créateur                                | Informations relatives à l'organisation responsable de la production du jeu de données considéré                                                                  | O                                                | W                                 | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='author']]                                                                                                                                                                                                                                                                                  |
| geodcat:distributor           | diffuseur                               | Informations relatives à l'organisation responsable de la distribution de la ressource                                                                            | O                                                | W                                 | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='distributor']]                                                                                                                                                                                                                                                                             |
| geodcat:originator            | auteur                                  | Informations relatives à l'organisation responsable de la création de la ressource                                                                                | O                                                | W                                 | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='originator']]                                                                                                                                                                                                                                                                              |
| geodcat:principalInvestigator | collecteur                              | Informations relatives à l'organisation responsable de la collecte d'information de recherche                                                                     | O                                                | W                                 | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='principalInvestigator']]                                                                                                                                                                                                                                                                   |
| geodcat:processor             | processeur                              | Informations relatives à l'organisation ayant modifié la ressource après traitement des données                                                                   | O                                                | W                                 | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='processor']]                                                                                                                                                                                                                                                                               |
| geodcat:resourceProvider      | fournisseur                             | Informations relatives à l'organisation qui fournit la ressource                                                                                                  | O                                                | W                                 | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='resourceProvider']]                                                                                                                                                                                                                                                                        |
| geodcat:user                  | utilisateur                             | Informations relatives à l'organisation qui utilise la ressource                                                                                                  | O                                                | W                                 | 0-n         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='user']]                                                                                                                                                                                                                                                                                    |
| dct:rightsHolder              | ayant droits                            | Organisation détenteur de droits sur le dataset                                                                                                                   | O                                                | W                                 | 0-1         | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='user']]/gmd:organisationName                                                                                                                                                                                                                                                               |
| dct:license                   | conditions d'utilisation                | Informations relatives aux conditions d'utilisation particulières de cette distribution                                                                           | M                                                | W                                 | 1           | dct:LicenseDocument     | [//\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD_LegalConstraints[\*/gmd:MD_RestrictionCode[@codeListValue='otherRestrictions']]/gmd:otherConstraints[gco:CharacterString or gmx:Anchor[not(starts-with(@xlink:href, 'http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))\\]\\]](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))%5C%5D%5C%5D) |
| adms:representationTechnique  | type de jeu de données                  | Informations relatives à la représentation spatiale du jeu de données                                                                                             | R                                                | W                                 | 0-1           | skos:Concept            | //\*/gmd:identificationInfo/\*/gmd:spatialRepresentationType                                                                                                                                                                                                                                                                                                                                                  |

**Tableau 2 : Classe dcat:Dataset instanciée dans l'attribut dcat:dataset**

## C. dcat:DataService

### Instanciation de dcat:Dataservice dans l'attribut dcat:service
| URI                           | Nom                                     | Description                                                                                            | Exigence instanciée dans l'attribut dcat:service | Exigence instanciée dans tout autre attribut | Cardinalité | Domaine             | Source                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------ | -------------------------------------------- | ----------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dct:title                     | titre                                   | Titre du service renseigné                                                                             | M                                                | M                                            | 1           | multilingue         | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:title/\*                                                                                                                                                                                                                                                                                                                                      |
| dct:description               | description                             | Description du service renseigné                                                                       | M                                                | M                                            | 1           | multilingue         | //\*/gmd:identificationInfo/\*/gmd:abstract/\*                                                                                                                                                                                                                                                                                                                                                                |
| dcat:endpointURL              | URL du service                          | URL du service considéré                                                                               | M                                                | M                                            | 1-n         | URL                 | A voir                                                                                                                                                                                                                                                                                                                                                                                                        |
| dcat:servesDataset            | jeu de données accessible               | Identification du ou des jeux de données accessibles via le service considéré                          | R                                                | R                                            | 0-n         | dcat:Dataset        | si dataservice généré à partir d'une fiche ISO 19139 --> utiliser la liste des identifiants de datasets présents le getcapabilties <> si dataservice généré par wizard : générer par sélection manuelle dans un champ ad hoc des datasets déjà documentés                                                                                                                                                     |
| dct:accessRights              | restriction d'accès                     | Informations relatives aux restrictions concernant l'utilisation du service considéré                  | M                                                | M                                            | 1           | dct:RightsStatement | [//\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD_LegalConstraints[gmd:accessConstraints/gmd:MD_RestrictionCode[@codeListValue='otherRestrictions']]/gmd:otherConstraints[gmx:Anchor[starts-with(@xlink:href,'http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess')\\]\\]](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess')%5C%5D%5C%5D)            |
| dcat:keyword                  | mot-clé                                 | Mot-clé libre décrivant le service considéré                                                           | R                                                | R                                            | 0-n         | multilingue         | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD_Keywords[not(./gmd:thesaurusName)]/gmd:keyword/\*                                                                                                                                                                                                                                                                                               |
| dcat:theme                    | mot-clé issu d'un vocabulaire contrôlé  | Mot clé issu d'un thésaurus décrivant le service                                                       | R                                                | R                                            | 0-n         | skos:Concept        | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD_Keywords[gmd:thesaurusName/gmd:CI_Citation/gmd:title/\*={}]/gmd:keyword/\*                                                                                                                                                                                                                                                                      |
| dct:created                   | date de création                        | Date de création du service considéré                                                                  | R                                                | R                                            | 0-1         | date (YYYY-MM-DD)   | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='creation']]/gmd:date                                                                                                                                                                                                                                                        |
| dct:modified                  | date de mise à jour                     | Date de dernière modification du service                                                               | R                                                | R                                            | 0-1         | date (YYYY-MM-DD)   | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='revision']]/gmd:date                                                                                                                                                                                                                                                        |
| dct:issued                    | date de première publication            | Date de première publication du service                                                                | O                                                | O                                            | 0-1         | date (YYYY-MM-DD)   | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='publication']]/gmd:date                                                                                                                                                                                                                                                     |
| dct:conformsTo                | spécification ou règle de structuration | Informations relative(s) aux normes de qualité du service                                              | O                                                | O                                            | 0-n         | dct:Standard        | //\*/gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:report/gmd:DQ_DomainConsistency/gmd:result/gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation                                                                                                                                                                                                                                                         |
| dct:type                      | type de service                         | Informations relatives au type de service                                                              | R                                                | R                                            | 0-1           | skos:Concept        | //\*/gmd:identificationInfo/\*/srv:serviceType                                                                                                                                                                                                                                                                                                                                                                |
| geodcat:distributor           | diffuseur                               | Informations relatives à l'organisation responsable de la distribution de la ressource                 | O                                                | O                                            | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='publisher']]                                                                                                                                                                                                                                                                               |
| geodcat:originator            | auteur                                  | Informations relatives à l'organisation responsable de la création de la ressource                     | O                                                | O                                            | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='custodian']]                                                                                                                                                                                                                                                                               |
| geodcat:principalInvestigator | collecteur                              | Informations relatives à l'organisation responsable de la collecte d'information de recherche          | O                                                | O                                            | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='author']]                                                                                                                                                                                                                                                                                  |
| geodcat:processor             | processeur                              | Informations relatives à l'organisation ayant modifié la ressource après traitement des données        | O                                                | O                                            | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='distributor']]                                                                                                                                                                                                                                                                             |
| geodcat:resourceProvider      | fournisseur                             | Informations relatives à l'organisation qui fournit la ressource                                       | O                                                | O                                            | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='originator']]                                                                                                                                                                                                                                                                              |
| geodcat:user                  | utilisateur                             | Informations relatives à l'organisation qui utilise la ressource                                       | O                                                | O                                            | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='principalInvestigator']]                                                                                                                                                                                                                                                                   |
| dct:creator                   | créateur                                | Informations relatives à l'organisation responsable de la production du service considéré              | O                                                | O                                            | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='processor']]                                                                                                                                                                                                                                                                               |
| geodcat:custodian             | mainteneur                              | Informations relatives à l'organisation responsable de la données et de la maintenance de la ressource | O                                                | O                                            | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='resourceProvider']]                                                                                                                                                                                                                                                                        |
| dct:rightsHolder              | ayant droits                            | Organisation déteneur de droits sur le service                                                         | O                                                | O                                            | 0-1         | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='user']]                                                                                                                                                                                                                                                                                    |
| dct:license                   | conditions d'utilisation                | Informations relatives aux conditions d'utilisation particulières de cette distribution                | M                                                | M                                            | 1           | dct:LicenseDocument | [//\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD_LegalConstraints[\*/gmd:MD_RestrictionCode[@codeListValue='otherRestrictions']]/gmd:otherConstraints[gco:CharacterString or gmx:Anchor[not(starts-with(@xlink:href, 'http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))\\]\\]](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))%5C%5D%5C%5D) |
| dct:conformsTo                | système de projection géographique      | Informations relatives aux systèmes de référence spatiaux ou temporels                                 | R                                                | R                                            | 0-n         | dct:Standard          | //\*gmd:referenceSystemInfo/gmd:MD_ReferenceSystem/gmd:referenceSystemIdentifier/gmd:RS_Identifier/gmd:code                                                                                                                                                                                                                                                                                                   |

**Tableau 3 : classe dcat:DataService instanciée dans l'attribut dcat:service**

## D. dcat:Distribution

### Toute instanciation de dcat:Distribution
| URI                 | Nom                                | Description                                                                            | Exigence | Cardinalité | Domaine               | Source                                    |
| ------------------- | ---------------------------------- | -------------------------------------------------------------------------------------- | -------- | ----------- | --------------------- | ----------------------------------------- |
| dct:title           | titre                              | Titre de la distribution concernée                                                     | O        | 0-1         | multilingue           | //atom:feed/atom :title                   |
| dcat:accessURL      | URL d’accès                        | Adresse web de la distribution concernée du jeu de données                             | M        | 1           | URL                   | //atom:feed/atom:entry/atom:link          |
| dct:description     | description                        | Description des particularités de cette description                                    | O        | 0-1         | multilingue           | //atom:feed/atom:entry/atom:subtitle      |
| dct:format          | format                             | Informations relatives au format particulier de cette distribution                     | M        | 1           | dct:MediaTypeOrExtent | //atom:feed/atom:entry/atom:link/@type    |
| dcat:mediaType      | type de format                     | Type de format/support de la distribution (IANA)                                       | O        | 0-1         | dct:MediaType         | //atom:feed/atom:entry/atom:link/@type    |
| dcat:downloadURL    | URL de téléchargement              | Adresse web pour télécharger directement la distribution concernée                     | O        | 0-1         | URL                   | //atom:feed/atom:entry/atom:link          |
| dcat:compressFormat | format comprimé                    | Informations relatives au format comprimé particulier de cette distribution (IANA)     | O        | 0-1         | dct:MediaType        | //atom :feed/atom :entry/atom :link/@type |
| dct:conformsTo      | système de projection géographique | Informations relatives à la projection particulière de cette distribution              | O        | 0-1         | dct:Standard          | //atom:feed/atom:entry/atom:category      |
| dcat:byteSize       | taille                             | Taille de la distribution en bytes                                                     | O        | 0-1         | xsd:decimal          | pas de XPATH spécifié                     |
| adms:status         | statut                             | Informations relatives à la maturité de la distribution                                | O        | 0-1           | skos:Concept          | pas de XPATH spécifié                     |
| dct:spatial         | couverture spatiale                | Informations relatives à la région géographique couverte par la distribution concernée | O        | 0-1         | dct:Location          | //atom:feed/atom:entry/georss:box         |
| dct:temporal        | couverture temporelle              | Informations relatives à l’intervalle temporelle couvert par la distribution concernée | R        | 0-1         | dct:PeriodOfTime      | //atom:feed/atom:entry/atom:link/@time    |
| dct:type            | type de distribution               | Lien vers un type de distribution                                                      | O        | 0-n         | skos:Concept          | pas de XPATH spécifié                     |
| dct:language        | langue                             | Informations relatives au(x) langue(s) utilisés dans la distribution                   | R        | 0-4         | skos:Concept          | pas de XPATH spécifié                     |

**Tableau 4 : classe dcat:Distribution instanciée dans tout attribut**

## E. foaf:Organization

### Instanciation de foaf:Organization dans tout attribut
| URI                    | Nom             | Description                                               | Exigence | Cardinalité | Domaine         | Source                                                                                  |
| ---------------------- | --------------- | --------------------------------------------------------- | -------- | ----------- | --------------- | --------------------------------------------------------------------------------------- |
| foaf:name              | nom             | Nom de l'organisation                                     | M        | 1-n         | Multilingue     | ./gmd:organisationName                                                                  |
| dct:type               | type            | Indique le type d'organisation                            | O        | 0-1         | skos:Concept    | pas de XPATH spécifié                                                                   |
| foaf:mbox              | adresse mail    | adresse mail de l'organisation (en utilisant URI mailto:) | R        | 0-1         | URI       | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address/gmd:electronicMailAddress |
| foaf:workplaceHomepage | Site web        | Site web de l’organisation                                | R        | 0-4         | rdf:Description | ./gmd:contactInfo/gmd:CI\_Contact/gmd:onlineResource/gmd:CI\_OnlineResource/gmd:linkage |
| locn:address           | Adresse postale | Adresse postale de l’organisation                         | O        | 0-1         | locn:Address    | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address                           |

**Tableau 5 : classe foaf:Organization instanciée dans tout attribut**

## F. dcat:CatalogRecord

### Instanciation de dcat:CatalogRecord dans tout attribut
| URI               | Nom                                      | Description                                                                                            | Exigence | Cardinalité | Domaine            | Source                                                                                                                                                                  |
| ----------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------- | ----------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| foaf:primaryTopic | instance à laquelle la fiche se rapporte | Information relative au jeu de données, service ou catalogue                                           | M        | 1           | dcat:Dataset       | dcat:Dataservice                                                                                                                                                        | dcat:Catalog | génération a posteriori en intégrant tous les ID de toutes instanciations primaires (i.e. les instances qui ne correspondent à la valeur d'un attribut de la même classe)
| dct:modified      | date de mise à jour                      | Date de dernière mise à jour du Catalog Record                                                         | M        | 1           | date (YYYY-MM-DD)  | //\* /gmd:dateStamp/\*                                                                                                                                                  |
| dct:language      | langue                                   | Informations relatives au(x) langue(s) utilisés dans les metadonnées du jeu de données                 | M        | 1-4         | skos:Concept      | //\*/gmd:locale/gmd:PT\_Locale/gmd:languageCode/gmd:LanguageCode\[@codeListValue={}\]                                                                                   |
| dcat:contactPoint | Point de contact                         | Informations relatives aux modalités de prise de contact à propos du service                           | M        | 1           | vcard:Organization | //\*/gmd:contact/gmd:CI\_ResponsibleParty                                                                                                                               |
| dct:identifier    | identifiant                              | Identifiant alphanumérique unique du catalogrecord concerné                                            | M        | 1           | unilingue          | //\*/gmd:fileIdentifier                                                                                                                                                 |
| dct:source        | Catalogrecord source                     | Informations relative(s) à la fiche de métadonnées originale décrivant le jeu de données ou service    | O        | 0-1         | dct:CatalogRecord          | http://csw.geo.be/eng/csw?request=GetRecordById&service=CSW&version=2.0.2&elementSetName=full&outputSchema=http://www.isotc211.org/2005/gmd&id=+//\*/gmd:fileIdentifier |
| dcat:landingPage  | page d'acceuil                           | Informations relative(s) à la fiche de métadonnées HTML originale décrivant le jeu de données concerné | O        | 0-4         | rdf:Description    | https://www.geo.be/catalog/details/ + //*/gmd:fileIdentifier                                                                                                            |

**Tableau 6 : classe dcat:CatalogRecord instanciée dans tout attribut**

## G. locn:Address

### Instanciation de locn :Address dans tout attribut
| URI               | Nom             | Description              | Exigence | Cardinalité | Domaine     | Source                |
| ----------------- | --------------- | ------------------------ | -------- | ----------- | ----------- | --------------------- |
| locn:thoroughfare | adresse postale | Rue et numéro de police  | M        | 1           | multilingue | .  /gmd:deliveryPoint |
| locn:postName     | commune         | Nom de la commune        | M        | 1           | multilingue | .  /gmd:city          |
| locn:postCode     | code postal     | Code postal de l’adresse | M        | 1           | unilingue   | ./gmd:postalCode      |
| locn:adminUnitL1  | pays            | Pays                     | M        | 1           | multilingue | ./gmd:country         |

**Tableau 7 : classe locn:Address instanciée dans tout attribut**

## H. skos:Concept

### Instanciation de skos:Concept dans tout attribut
| URI           | Nom                | Description                        | Exigence | Cardinalité | Domaine     | Source                                           |
| ------------- | ------------------- | ---------------------------------- | ----------- | ----------- | --------- | ------------------------------------------------ |
| rdf:type      | type de concept     | Type de concept                    | O           | 0-1         | unilingue | néant                                            |
| skos:inScheme | thésaurus d’origine | Thésaurus dont est issu le concept | R           | 0-1         | URL       | .  /gmd:thesaurusName/gmd:CI\_Citation/gmd:title |

**Tableau 8 : classe skos:Concept instanciée tout attribut**

## I. dct:PeriodOfTime

### Instanciation de dct:PeriodOfTime dans tout attribut
| URI            | Nom           | Description                            | Exigence | Cardinalité | Domaine   | Source                                                                  |
| -------------- | ------------- | -------------------------------------- | -------- | ----------- | --------- | ----------------------------------------------------------------------- |
| dcat:startDate | date de début | Date de début de la période temporelle | M        | 1           | Unilingue | /gmd:EX_TemporalExtent/gmd :extent/gml32:TimePeriod/gml32:beginPosition |
| dcat:endDate   | date de fin   | Date de fin de la période temporelle   | M        | 1           | Unilingue | ./gmd:EX_TemporalExtent/gmd :extent/gml32:TimePeriod/gml32:endPosition  |

**Tableau 9 : classe dct:PeriodOfTime instanciée dans tout attribut**

## J. dqv:QualityMeasurement

### Instanciation de dqv:QualityMeasurement dans un attribut décrivant une ressource vectorielle
| URI                              | Nom                                         | Description                                 | Exigence | Cardinalité | Domaine      | Source                                                                                                 |
| -------------------------------- | ------------------------------------------- | ------------------------------------------- | -------- | ----------- | ------------ | ------------------------------------------------------------------------------------------------------ |
| dqv:isMeasurementOf              | grandeur scalaire mesurée                   | Grandeur scalaire mesurée                   | O        | 0-1         | multilingue  | Valeur hardcodée en fonction du type de jeu de données                                                 |
| geodcat:spatialResolutionAsScale | échelle conceptuelle de la ressource        | Échelle conceptuelle de la ressource        | M        | 1           | unilingue    | ./gmd :MD\_Resolution/gmd:equivalentScale/ gmd:MD\_RepresentativeFraction/ gmd:denominator/gco:Integer |

**Tableau 10 : classe dqv:QualityMeasurement se rapportant à la description d&#39;une ressource vectorielle**

### Instanciation de dqv:QualityMeasurement dans un attribut décrivant une ressource matricielle
| URI                              | Nom                                         | Description                                 | Exigence | Cardinalité | Domaine      | Source                                                                                                 |
| -------------------------------- | ------------------------------------------- | ------------------------------------------- | -------- | ----------- | ------------ | ------------------------------------------------------------------------------------------------------ |
| dqv:isMeasurementOf              | grandeur scalaire mesurée                   | Grandeur scalaire mesurée                   | O        | 0-1         | multilingue  | Valeur hardcodée en fonction du type de jeu de données                                                 |
| sdmx-attribut:unitMeasure        | unité de mesure des grandeurs scalaires     | Unité de mesure des grandeurs scalaires     | R        | 0-1           | skos:Concept | ./gmd :MD\_Resolution/gmd:distance/gco:Distance/@uom                                                   |
| dqv:value                        | valeur de la mesure de la grandeur scalaire | Valeur de la mesure de la grandeur scalaire | M        | 1           | unilingue    | ./gmd :MD\_Resolution /gmd:distance/gco:Distance                                                       |

**Tableau 11 : classe dqv:QualityMeasurement se rapportant à la description d&#39;une ressource matricielle**

## K. dct:Location

### Instanciation de dct:Location dans tout attribut
| URI             | Nom                                    | Description                                 | Exigence | Cardinalité | Domaine     | Source |
| --------------- | -------------------------------------- | ------------------------------------------- | -------- | ----------- | ----------- | ------ |
| locn:geometry   | géométrie                              | Coordonnées de la géométrie de la ressource | M        | 1-4           | Unilingue   |        |
| dcat:bbox       | rectangle de délimitation géographique | Coordonnées de la géométrie de la ressource | M        | 1-4           | Unilingue   |        |
| skos:prefLabel  | nom de l’entité géographique           | Nom de l’entité géographique                | R        | 0-1         | multilingue |        |
| dct:identifier  | identifiant de l’entité géographique   | Identifiant de l’entité géographique        | R        | 0-1         | codedValue  |        |

**Tableau 12 : classe dct:Location instanciée dans tout attribut**

## L. skos:ConceptScheme

### Instanciation de skos :ConceptScheme dans tout attribut
| URI            | Nom                          | Description                  | Exigence | Cardinalité | Domaine     | Source                                                                                                                                                                                                       |
| -------------- | ---------------------------- | ---------------------------- | -------- | ----------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| dct:title      | Titre du thésaurus           | Titre du thésaurus           | M        | 1           | multilingue | Génération sur base des URL fournies dans les propriétés skos:inScheme des instances de la classe skos :Concept (il faut donc la propriété inScheme et que celle-ci soit pourvue d’une URL machine-readable) |
| dct:issued     | Date de première publication | Date de première publication | O        | 0-1         | date        | Génération sur base des URL fournies dans les propriétés skos:inScheme des instances de la classe skos :Concept (il faut donc la propriété inScheme et que celle-ci soit pourvue d’une URL machine-readable) |
| dct:identifier | Identifiant du thésaurus     | Identifiant du thésaurus     | M        | 1           | URL         | Génération sur base des URL fournies dans les propriétés skos:inScheme des instances de la classe skos :Concept (il faut donc la propriété inScheme et que celle-ci soit pourvue d’une URL machine-readable) |

**Tableau 13 : classe skos:ConceptScheme instanciée dans tout attribut**

## M. vcard:Organization

### Instanciation de vcard:Organization dans tout attribut

| URI                     | Nom             | Description                                               | Exigence | Cardinalité | Domaine         | Source                                                                                  |
| ----------------------- | --------------- | --------------------------------------------------------- | -------- | ----------- | --------------- | --------------------------------------------------------------------------------------- |
| vcard:organization-name | nom             | Nom de l'organisation                                     | M        | 1-n         | Multilingue     | ./gmd:organisationName                                                                  |
| vcard:hasEmail          | adresse mail    | Adresse mail de l'organisation (en utilisant URI mailto:) | R        | 0-1         | Unilingue       | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address/gmd:electronicMailAddress |
| vcard:hasURL            | dite web        | Site web de l’organisation                                | R        | 0-4         | rdf:Description | ./gmd:contactInfo/gmd:CI\_Contact/gmd:onlineResource/gmd:CI\_OnlineResource/gmd:linkage |
| vcard:hasAddress        | adresse postale | Adresse postale de l’organisation                         | O        | 0-1         | vcard:Address   | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address                           |

**Tableau 14 : classe vcard:Organization instanciée dans tout attribut**

## N. vcard:Address

### Instanciation de vcard:Address dans tout attribut

| URI                  | Nom             | Description              | Exigence | Cardinalité | Domaine     | Source                |
| -------------------- | --------------- | ------------------------ | -------- | ----------- | ----------- | --------------------- |
| vcard:street-address | adresse postale | Rue et numéro de police  | M        | 1           | multilingue | .  /gmd:deliveryPoint |
| vcard:locality      | commune         | Nom de la commune        | M        | 1           | multilingue | .  /gmd:city          |
| vcard:postal-code    | code postal     | Code postal de l’adresse | M        | 1           | unilingue   | ./gmd:postalCode      |
| vcard:country-name   | pays            | Pays                     | M        | 1           | multilingue | ./gmd:country         |

**Tableau 15 : classe vcard:Address instanciée dans tout attribut**

## O. dct:LicenseDocument

### Instanciation de dct:LicenseDocument dans tout attribut

| URI             | Nom                     | Description             | Exigence | Cardinalité | Domaine     | Source |
| --------------- | ----------------------- | ----------------------- | -------- | ----------- | ----------- | ------ |
| dct:type        | type de document        | Type de document        | M        | 1           | URI         |        |
| dct:title       | titre du document       | Titre du document       | M        | 1           | multilingue |        |
| dct:description | description du document | Description du document | O        | 0-1         | multilingue |        |

**Tableau 16 : classe dct:LicenseDocument instanciée dans tout attribut**

## P. rdf:Description

### Instanciation de rdf:Description dans tout attribut

| URI          | Nom                | Description        | Exigence | Cardinalité | Domaine    | Source                               |
| ------------ | ------------------ | ------------------ | -------- | ----------- | ---------- | ------------------------------------ |
| dct:language | langue du document | Langue du document | M        | 1           | codedValue | /gmd:LocaliseCharacterString/@locale |

**Tableau 17 : classe rdf:Description instanciée dans tout attribut**

# Annexe II

| Classe concernée | Attribut concerné | Thésaurus proposés | Exigence |
| ---------------- | ----------------- | ------------------ | -------- |
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

**Liste 1: thésaurus**

