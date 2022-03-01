Profil fédéral DCAT AP

# Introduction

Le présent document institue le profil [DCAT AP 2 fédéral], élaboré par les administrations fédérales impliquées dans l&#39;implémentation de la directive INSPIRE. Ce profil est , conforme à la norme [DCAT AP 2]. D&#39;une part, il [DCAT AP 2 fédéral] spécifie et restreint ladite norme en précisant les règles régissant l&#39;instanciation de ses classes. D&#39;autre part, il dispose met en place des règles relatives applicavles au contenu des classes et de leurs attributs respectifs.

En effet, [DCAT AP 2 fédéral] a pour objectif premier d&#39;intégrer la richesse sémantique les éléments de métadonnées issus des [TG 2.0] ainsi que d&#39;exploiter les opportunités sémantiques offertes par les [TG relatives aux services de téléchargement].

Dès lors, [DCAT AP 2 fédéral] restreint la cardinalité de certains attributs, en ajoute d&#39;autres étrangers à [DCAT AP 2] de sorte de mettre en correspondance ces attributs à des éléments de métadonnées issus des [TG 2.0]. De la même manière, [DCAT AP 2 fédéral] norme le contenu de ses attributs de manière à y intégrer, s&#39;il échet, le contenu des éléments de métadonnées issus des [TG 2.0].

1.
# Présentation générale des classes

[DCAT AP 2 fédéral] inclut toutes les classes et tous les attributs requis par [DCAT AP 2]. De manière complémentaire et non-impérative, les attributs propres à [GEO DCAT AP 2] et à [STAT DCAT AP 1] ont été intégrés dans la mesure où ils répondaient aux besoins exprimés par les administrations fédérales. Il comprend les classes présentées ci-dessous. Les classes reprises en gras sont obligatoires dans tout catalogue conforme à [DCAT AP 2 fédéral] :

- **dcat:Catalog** qui représente et décrit des catalogues ;
- **dcat:Dataset** qui représente et décrit des jeux de données ;
- dcat:Dataservice qui représente et décrit des services (ou des applications oudes API) donnant accès à un ou plusieurs jeux de données ;
- **foaf:Organization** qui représente et décrit des organisations ;
-
- dcat:Distribution qui représente et décrit des fichiers accessibles d&#39;un jeu de données ;
- dcat:CatalogRecord qui représente et décrit un objet quelconque du catalogue (un jeu de données, un service ou un catalogue) ;.
- locn :Address qui représente et décrit des adresses postales d&#39;un agent foaf ;
- skos :Concept qui représente et décrit des concepts ;
- dct :PeriodOfTime qui représente et décrit des périodes temporelles ;
- dqv :QualityMeasurement qui représente et décrit la résolution spatiale de ressources ;
- dct :Location qui représente et décrit des zones géographiques ;
- skos :ConceptScheme qui représente et décrit des thésaurus ;
- vcard :Organization qui représente des organisations ;
- vcard :Address qui représente et décrit des adresses postale.

En outre, certaines classes supplémentaires, non détaillées dans le présent document, sont également partie intégrante de [DCAT AP 2 fédéral]. Il s&#39;agit des classes dont les spécifications définies par [DCAT AP 2] apparaissent pleinement satisfaisantes. Afin de limiter la redondance, elles ne sont donc pas reprises ici. Il convient de se référer directement aux spécifications de [DCAT AP 2] qui leur sont applicables.

Le diagramme suivant présentes les classes ainsi que les attributs propres à [DCAT AP 2 fédéral].

![](RackMultipart20220301-4-1246a4o_html_cc6918eab17a5cc1.png)

Le point II, ainsi que les tableaux en annexes qui lui sont associés, Les points A à F , ainsi que les tableaux en annexes qui leur sont associées, précisent les règles applicablesattributs propres à chaque classe. Le point III, ainsi que les tableaux en annexe qui lui sont associés Il , précise en outre les règles applicables au contenu des attributs de chaque classeables lors de l&#39;instanciation de chaque classe, etainsi que notamment, les règles applicables lorsl&#39;élément de de la génération la fiche [ISO 19139] à utiliser en cas de conversion.

En outre, dans cha Dans tous les tableaux que tableau de l&#39;annexe Iannexé, figurent, pour chaque attribut, les éléments suivants :

1. URI : cet élément correspond à l&#39;identifiant unique de l&#39;attribut considéré ;
2. Nom : cet élément correspond au nom français de l&#39;attribut considéré  ;
3. Description  : cet élément correspond à la description de l&#39;attribut considéré ;
4. Exigence : cet élément correspond à l&#39;un des quatre niveaux d&#39;exigence
# 1
 propre à l&#39;attribut considéré ;
5. Cardinalité : cet élément correspond aux nombres minimal et maximal d&#39;attributs de ce type autorisés ;
6. Domaine : cet élément correspond aux valeurs acceptables que peut prendre comprendre l&#39;attribut considéré. Si les valeurs acceptables sont comprises dansappartiennent à un ou plusieurs ensembles limités (i.e. un thésaurus), alors le lien vers ledit ensemble est spécifié dans le tableaule ou les ensembles optionnels, recommandés et obligatoires sont repris à l&#39;annexe II  ;
7.
8. Source : cet élément correspond au XPATH de l&#39;élément de métadonnées **impérativement utilisé** comme valeur de l&#39;attribut considérési la classe à laquelle il appartient est mise en correspondance avec une source classe INSPIRE [ISO 19115] et si son domaine correspond à une valeur unilingue, à une valeur multilingue ou à un URL. Si son domaine ne correspond pas à une autre classe du présent profilou à un ensemble de classes.

Dans ce cas, cet la source élément correspond aux instructions nécessaires pour obtenir le contenu des instances à produirà la classe [ISO 19115] mise en correspondance avec la classe du présent profil.e

1.

Les attributs de domaine « multilingue » doivent être remplis en allemand, en français, en néerlandais et en anglais. Dans la mesure du possible, les attributs de domaine « URL multilingue » doivent être remplis en allemand, en français, en néerlandais et en anglais.

1. Présentation détaillée des classes

## A.Classe dcat: Catalog

La classe dcat :Catalog correspond à un catalogue, c&#39;est-à-dire à un ensemble particulier d&#39;un ou de plusieurs jeux de données et éventuellement de services identifiés et documentés de manière cohérente.

Conformément aux à ces spécifications [DCAT AP 2 fédéral], la classe peut s&#39;instancier à deux endroits : dans l&#39;élément racine d&#39;une part, et dans les attributs dct :hasPart, dct :isPartOf et dcat :catalog d&#39;autre la classe dcat :Catalog d&#39;autre partpart. L&#39;instance de la classe dcat :Catalog présente dans l&#39;élément racine correspond au catalogue DCAT considéré. Cette instance instanciation est **obligatoire** et **unique**.

La ou les instances de la classe dcat :Catalog présentes dans une autre instance de la même classe dans les trois attributs susmentionnés correspondent à des catalogues qui peuvent d&#39;une manière ou d&#39;une autre être associés au catalogue dans lequel ils s&#39;instancient. Ces instances instanciations sont **optionnelles** et **potentiellement**** multiples**.

### Remarques concernant les attributs de la classe Profil de la classe

Le présent profil prévoit des spécifications différentes en fonction de l&#39;attribut où la classe l&#39;attribut au sein duquel la classe s&#39;instancie. Celles-ci découlent pour l&#39;essentiel de la nécessité de prévenir une séquence infinie d&#39;instanciations de la classe et des finalités propres à chaque type d&#39; de finalité entre elleinstanciations. En effet, la première instanciation vise à identifier et à décrire exhaustivement le catalogue considéré, alors que les instanciations suivantes visent exclusivement à identifier les catalogues considérés.

Les attributs propres à l&#39;instance présente dans l&#39;élément racine sont spécifiés dans le tableau 1 présent en annexe. Les attributs propres aux autres instances sont spécifiés dans le tableau 2 présent en annexe.

Les spécifications applicables à la classe, indépendamment de l&#39;endroit où elle s&#39;instancie, prévoient la possibilité d&#39;expliciter les modalités d&#39;acquisition du catalogue décrit au moyen de l&#39;attribut dcat :Distribution. Il s&#39;agit d&#39;un ajout par rapport à la norme [DCAT AP 2].

### Instanciation à partir d&#39;éléments [INSPIRE]

Seul le contenu des fiches [ISO 19139] décrivant un jeu de [CSW] peut être converti en instances de la classe dcat :Catalog. En pareil cas, ces spécifications prévoient que le contenu de chaque attribut de de la classe dcat : Catalog soit pourvu à partir de l&#39;élément [ISO 19139] qui lui est associé dans le tableau 1en annexe.

Le contenu des attributs multilingues ou unilingues doit être pourvu à partir du contenu de l&#39;élément [ISO 19139] associé. Le contenu des attributs dont le domaine est une classe domaine correspond à une classe est pourvu au moyen d&#39;une ou de plusieurs instanciations est égal à une ou plusieurs instanciations de ladite classe conforme(s) aux spécifications du présent profil. Ces instanciations reprennent le contenu de l&#39;élément [ISO 19139] associé.

De manière dérogatoire, certains attributs ne sont pas mis en correspondance avec des éléments o [ISO 19139]. En l&#39;espèce, les règles suivantes sont d&#39;application :

1. Le contenu de l&#39;attribut foaf:homepage doit renvoyer vers une version human readable du catalogue ;
2. Le contenu de l&#39;attribut dcat :themeTaxonomy doit être généré _a posteriori¸_ dès que tous les attributs de toutes les classes sont pourvus, de manière à recenser tous les thésaurus effectivement utilisés dans le catalogue considéré ;
3. Le contenu de l&#39;attribut dct :identifier reste à déterminer. Il pourrait correspondre à l&#39;URL de sérialisation XML du catalogue considéré.
4. Le contenu de l&#39;attribut dcat :dataset est généré à partir de toutes les fiches décrivant des jeux de données, séries ou cartes statiques accessibles via le [CSW] ;
5. Le contenu de l&#39;attribut dcat :service est généré à partir de toutes les fiches décrivant des services ou des applications accessibles via le [CSW].

###


### Les différences entre les règles applicables aux deux types d&#39;instances découlent pour l&#39;essentiel de la volonté de prévenir une séquence infinie d&#39;instanciations et découlent des différences de finalité entre elles. En effet, la première instanciation vise à identifier et à décrire exhaustivement le catalogue considéré, alors que les instanciations suivantes visent exclusivement à identifier le catalogue considéré.

### Les attributs propres à l&#39;instance de la classe dcat:Catalog présente dans l&#39;élément racine sont spécifiés dans le tableau 1 présent en annexe. Les attributs propres aux instances éventuelles de la classe dcat:Catalog présentes dans une autre instance de la même classe sont spécifiés dans le tableau 2 présent en annexe.

### Remarques concernant le cInstanciation sansontenu de la classe élément [INSPIRE]

Si l&#39;instance de la classe dcat : Catalog n&#39;est pas mise en correspondance avec une fiche [ISO 19139] décrivant un [CSW], alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à l&#39;élément [ISO 19139] qui lui est associé dans le tableau 2 en annexe.

Ces spécifications prévoient également que le contenu des attributs dont le domaine est une classe domaine correspond à une classe soit égalpourvu àau moyen d&#39;une ou de plusieurs instanciations de ladite classe conformes aux spécifications du présent profil.

Si une classe dcat : Catalog n&#39;est pas mise en correspondance avec un CSW[CSW], alors ces spécifications prévoient que le contenu des attributs mis en correspondance avec des éléments INSPIRE soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à ces mêmes éléments

# 2
. Dans ce cas, il est requis de référencer le catalogue DCAT AP fédéral complet au moyen de l&#39;attribut dct :isPartOf.

De manière dérogatoire, certains attributs ne sont pas mis en correspondance avec des éléments ou des classes [ISO 1913915]. En l&#39;espèce, les règles suivantes sont d&#39;application :

1. Le contenu de l&#39;attribut foaf:homepage doit renvoyer vers une version human readable du catalogue ;
2. Le contenu de l&#39;attribut dcat :themeTaxonomy doit être généré _a posteriori¸_ dès que tous les attributs de toutes les classes sont pourvus, de manière à recenser tous les thésaurus effectivement utilisés dans le catalogue considéré ;
3. Le contenu de l&#39;attribut dct :identifier reste à déterminer. Il pourrait correspondre à l&#39;URL de sérialisation XML du catalogue considéré.
4. Le contenu de l&#39;attribut dcat :dataset est généré à partir des jeux de données effectivement intégrés à partir du catalogue ;
5. Le contenu de l&#39;attribut dcat :dataset est généré à partir des services effectivement intégrés à partir du catalogue.

## B.Si une classe dcat : Catalog est mise en correspondance avec un CSW[CSW] entier, alors ces spécifications prévoient que le contenu des attributs provienne, dans la mesure du possible, des éléments de métadonnées de la fiche [[ISO 19139]] décrivant le CSW[CSW] référencés dans la colonne XPATH Source. Dans ce cas, il est requis de référencer le catalogue DCAT AP fédéral complet au moyen de l&#39;attribut dct :isPartOf.

## C.Certains attributs ne sont pas mis en correspondance avec des élément [[ISO 19115]]. En pareil cas, ces spécifications prévoient des sources alternatives. En l&#39;espèce, les règles relatives aux attributs suivants sont d&#39;application :

## D.Le contenu de l&#39;attribut foaf:homepage doit être hardcodé pour chaque instance ;

## E.Le contenu de l&#39;attribut dcat :themeTaxonomy doit être généré _a posteriori¸_ dès que tous les attributs de toutes les classes sont pourvus, de manière à recenser tous les thésaurus effectivement utilisés dans le catalogue considéré ;

## F.Le contenu de l&#39;attribut dct :identifier reste à déterminer. Il pourrait correspondre à l&#39;URL de sérialisation XML du catalogue considéré.

## G.Classe dcat: Dataset

La classe dcat :Dataset correspond à la description d&#39;un jeu de données, c&#39;est-à-dire à un ensemble de données, identifié et maintenu par une organisation, accessible dans une ou plusieurs représentationsformats.

Conformément à ces spécifications, la classe peut s&#39;instancier dans les classes attributs dcat :dataset, dct :source, dcat :servesDataset et foaf :isPrimaryTopicOf. dcat :Catalog, dcat :Dataservice, dcat :Dataset et dcat :CatalogRecord.

La ou les instances de la classe de la classe dcat :Dataset présentes dans la classe dcat :Catalogl&#39;attribut dcat :dataset correspondent aux à la description du ou des descriptions des jeux de données référencés dans le catalogue. Ces instanciations instances est sont **obligatoires** et **potentiellement multiples**.

La ou les instances de la classe dcat :Dataset présentes dans la classe dcat :Dataservice correspondent aux références des jeux de données accessible via le service considéré. Ces instances sont **recommandées** et **potentiellement**** multiples**.

La ou les &#39;instances a ou les instances de la classe dcat :Dataset présentess dans l&#39;attribut la dct :source correspondent classe même classe correspondent aux jeux de donnéesau jeu de données à l&#39;origine du jeu de données décrit qui peuvent d&#39;une manière ou d&#39;une autre être associés au jeu de données dans lequel elles s&#39;instancient. Ces instanciations sont Cettees instanciation instances sont est **recommandéess** et **potentiellement multiplesunique**** potentiellement ****multiples**.

La ou les instances de la classe dcat :Dataset présentes dans l&#39;attribut dcat :servesDataset correspondent aux jeux de données accessible au travers du le service décrit. Ces instanciations sont Ces instances sont **recommandées** et **potentiellement**** multiples**.

L&#39;instance Les instances de la classe dcat :Dataset présentes dans dans la classe l&#39;attribut foaf :isPrimaryTopicdcat :CatalogRecord correspond à son identification. Ces instanciations sont Cette instanciation instance est **obligatoires** et **unique potentiellement multiples** dès lors que la classe dcat :CatalogRecord est instanciée.

### Remarques concernant les attributs de la classe Profil de la classe

Le présent profil prévoit des spécifications différentes en fonction de l&#39;attribut où la classe l&#39;attribut au sein duquel la classe s&#39;instancie. Celles-ci découlent pour l&#39;essentiel de la nécessité de prévenir une séquence infinie d&#39;instanciations de la classe et des finalités propres à chaque type d&#39;instanciation. En effet, la première instanciation vise à identifier et à décrire exhaustivement le jeu de données considéré, alors que les instanciations les suivantes visent exclusivement à identifier les jeux de données considérés.

Les différences entre les règles applicables aux types d&#39;instances découlent pour l&#39;essentiel de la volonté de prévenir une séquence infinie d&#39;instanciations et découlent des différences de finalité entre elles. En effet, les instanciations dans la classe dcat :Catalog visent à identifier et à décrire exhaustivement les jeux de données compris, alors que les autres instanciations visent exclusivement à identifier le jeu de données considéré.Les attributs propres aux instances présentes dans l&#39;attribut dcat :dataset sont spécifiés dans le tableau 3 présent en annexe. Les attributs propres aux autres instances sont spécifiés dans le tableau 4 présent en annexe.

Les attributs propres aux instances dcat:Dataset présentes dans la classe dcat :Catalog sont spécifiés dans le tableau 3 présent en annexe. Les attributs propres aux autres instances sont spécifiés dans le tableau 4 en annexe.

Les spécifications de [DCAT AP 2 fédéral]applicables à la classe prévoient que les versions d&#39;un même jeu de données correspondent à autant d&#39;instances différentes de la classe dcat :Distribution. Elles ne prévoient dès lors pas de remplir les attributs afférents à la version proposésrepris par [DCAT AP 2.0] pour spécifier la version considérée.

Les spécifications applicables à la classe incluent les attributs dct :license et adms :representationTechnique car, selon les [TG 2.0] et [ISO 1911515], ils caractérisent les jeux de données et non une distribution particulière d&#39;un jeu de données.

Les spécifications applicables à classe prévoient que les instances présentes dans l&#39;attribut dcat :dataset aient au moins un attribut dûment pourvu parmi les attributs suivants (dct :created, dct :modified ou dct :issued).

Les spécifications applicables à la classe prévoient que les instances présentes dans l&#39;attribut dcat :dataset aient au moins un attribut dûment pourvu parmi les attributs suivants (dct :publisher, geodcat :custodian, dct :creator, geodcat :distributor, geodcat : originator, geodcat :principalInvestigator, geodcat :processor, geodcat :resourceProvider, geodcat :user ou dct :rightsHolder).

### Instanciation à partir d&#39;éléments [INSPIRE]

Seul le contenu des fiches [ISO 19139] décrivant un jeu de données, une série ou une carte statique peut être converti en instances de la classe dcat :Dataset. En pareil cas, ces spécifications prévoient que le contenu de chaque attribut de de la classe dcat : Dataset soit pourvu à partir de l&#39;élément [ISO 19139] qui lui est associé dans le tableau 3 en annexe.

Le contenu des attributs multilingues ou unilingues doit être pourvu à partir du contenu de l&#39;élément [ISO 19139] associé. Le contenu des attributs dont le domaine est une classe domaine correspond à une classe est pourvu au moyen d&#39;une ou de plusieurs instanciations est égal à une ou plusieurs instanciations de ladite classe conforme(s) aux spécifications du présent profil. Ces instanciations reprennent le contenu de l&#39;élément [ISO 19139] associé.

### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe dcat : Dataset n&#39;est pas mise en correspondance avec une fiche [ISO 19139] décrivant un jeu de données, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à l&#39;élément [ISO 19139] qui lui est associé dans le tableau en annexe 4.

Ces spécifications prévoient également que le contenu des attributs dont le domaine est une classe domaine correspond à une classe soit égalpourvu à au moyen d&#39;uune ou de plusieurs instanciations de ladite classe conformes aux spécifications du présent profil.

## H.

## I.Les règles concernant les attributs cités ci-dessous s&#39;appliquent aux instanciations dans la classe dcat :Catalog :

## J.Les attributs dct :license et adms :representationTechnique y sont inclus car, selon les [TG 2.0], ils caractérisent les jeux de données ;

## K.L&#39;un des attributs suivants doit être pourvu (dct :created, dct :modified ou dct :issued). En outre, les attributs dct :created et dct :modified devraient être pourvus.

## L.L&#39;un des attributs suivants doit être pourvu (dct :publisher, geodcat :custodian, dct :creator, geodcat :distributor, geodcat : originator, geodcat :principalInvestigator, geodcat :processor, geodcat :resourceProvider, geodcat :user ou dct :rightsHolder) ;

## M.Un des attributs suivants doit être pourvu (dcat :spatialResolutionInMeters ou dqv :hasQualityMeasurement) : le premier doit être pourvu dans le cas des jeux de données raster alors que le second doit être pourvu dans le cas des jeux de données vectoriels.

## N.Remarques concernant le contenu de la classe

## O.Si une classe dcat :Dataset n&#39;est pas mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs mis en correspondance avec des éléments INSPIRE soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à ces mêmes éléments.

## P.Si une classe dcat :Dataset est mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs provienne des éléments de la fiche [ISO 19139] référencés dans la colonne XPATH Source. Les règles concernant les attributs cités ci-dessous s&#39;appliquent aux instanciations dans la classe dcat :Catalog :

## Q.Les attributs dct :license et adms :representationTechnique y sont inclus car, selon les [TG 2.0], ils caractérisent les jeux de données ;

## R.L&#39;un des attributs suivants doit être pourvu (dct :created, dct :modified ou dct :issued). En outre, les attributs dct :created et dct :modified devraient être pourvus.

## S.L&#39;un des attributs suivants doit être pourvu (dct :publisher, geodcat :custodian, dct :creator, geodcat :distributor, geodcat : originator, geodcat :principalInvestigator, geodcat :processor, geodcat :resourceProvider, geodcat :user ou dct :rightsHolder) ;

## T.Un des attributs suivants doit être pourvu (dcat :spatialResolutionInMeters ou dqv :hasQualityMeasurement) : le premier doit être pourvu dans le cas des jeux de données raster alors que le second doit être pourvu dans le cas des jeux de données vectoriels.

## U.

## V.Classe DataService

## W.Classe dcat: DataService

La classe dcat : DataService correspond à la description d&#39;un service de données, c&#39;est-à-dire à un service web, une application ou une API identifié et maintenu par une organisation et donnant accès à un ou plusieurs jeux de données identifiés.

Conformément à ces spécifications, la classe peut s&#39;instancier dans les attributs dcat :service et foaf :isPrimaryTopicOf. La ou les instances de la classe de la classe dcat :DataService présentes dans l&#39;attribut dcat :service correspondent à la description du ou des services référencés dans le catalogue. Ces instanciations sont **recommandéeobligatoires** et **potentiellement multiples**.

Les instances de la classe dcat : DataService présentes dans l&#39;attribut foaf :isPrimaryTopic correspond à son identification. Cestte instanciations sontest **obligatoires** et **potentiellement multiples** dès lors que la classe dcat :CatalogRecord est instanciée.

###


### Dès lors, seules les fiches [ISO 19139] décrivant un service de visualisation, un service de téléchargement ou une application peuvent être converties en classes DataService. Les fiches décrivant un service de découverte ne peuvent être converties en classes DataService.

### La ou les instances de la classe de la classe dcat :Dataservicet présentes dans la classe dcat :Catalog correspondent aux descriptions des servicesjeux de données référencés. Ces instances sont **recommandéesobligatoires** et **potentiellement multiples**.

### L&#39;instance de la classe dcat : DataService présente dans la classe dcat :CatalogRecord correspond à son identification. Cette instance est **obligatoire** et **unique** dès lors que la classe dcat :CatalogRecord est instanciée.

### Remarques concernant les attributs de la classeProfil de la classe

Le présent profil prévoit des spécifications différentes en fonction de l&#39;attribut où la classe l&#39;attribut au sein duquel la classe s&#39;instancie. Celles-ci découlent pour l&#39;essentiel des finalités propres à chaque type d&#39;instanciation. En effet, la première instanciation vise à identifier et à décrire exhaustivement le jeu de donnéesservice considéré, alors que l&#39;instanciation suivante vise exclusivement à identifier les services considérés.

Les attributs propres aux instances présentes dans l&#39;attribut dcat :service sont spécifiés dans le tableau 5 présent en annexe. Les attributs propres aux autres instances sont spécifiés dans le tableau 6 présent en annexe.

Les spécifications applicables à la classe incluent les attributs dct :license et dct :confoormsTo car, selon les [TG 2.0] et [ISO 19115], ils caractérisent également les services.

Les spécifications applicables à classe prévoient que les instances présentes dans l&#39;attribut dcat :service ait au moins un attribut dûment pourvu parmi les attributs suivants (dct :created, dct :modified ou dct :issued).

Les spécifications applicables à la classe prévoient que les instances présentes dans l&#39;attribut dcat :service ait au moins un attribut dûment pourvu parmi les attributs suivants (dct :publisher, geodcat :custodian, dct :creator, geodcat :distributor, geodcat : originator, geodcat :principalInvestigator, geodcat :processor, geodcat :resourceProvider, geodcat :user ou dct :rightsHolder).

### 2)

### Conversion depuis des éléments [INSPIRE]

Seul le contenu des fiches [ISO 19139] décrivant un service de visualisation, un service de téléchargement ou une application peut être converti en instances de la classe dcat :DataService. Le contenu de fiches décrivant un service de découverte ne peut être converti en instances de la classe dcat : DataService. En pareil cas, ces spécifications prévoient que le contenu de chaque attribut de de la classe dcat : DataService soit pourvu à partir de l&#39;élément [ISO 19139] qui lui est associé dans le tableau 5en annexe. Le contenu de fiches décrivant un service de découverte ne peut être converti en instances de la classe dcat : DataService.

Le contenu des attributs multilingues ou unilingues doit être pourvu à partir du contenu de l&#39;élément [ISO 19139] associé. Le contenu des attributs dont le domaine correspond àest une classe est pourvu au moyen d&#39;une ou de plusieurs instanciations est égal à une ou plusieurs instanciations de ladite classe conforme(s) aux spécifications du présent profil. Ces instanciations reprennent le contenu de l&#39;élément [ISO 19139] associé.

En outre, les spécifications de [DCAT AP 2 fédéral]  prévoient d&#39;instancier, pour chaque jeu de données accessibles au moyen des services décrits, la classe dcat :Dataset dans la classe dcat :Catalog. En effet, il est nécessaire d&#39;instancier explicitement dans tout catalogue [DCAT AP] les jeux de données au moyen de la classe dcat :Dataset accessibles via les services considérés.

### Les différences entre les règles applicables aux types d&#39;instances découlent des différences de finalité entre elles. En effet, les instanciations dans la classe dcat :Catalog visent à identifier et à décrire exhaustivement les services de données compris, alors que l&#39;autre instanciation vise exclusivement à identifier le service de données considéré.

### Les attributs propres aux instances dcat:Dataservice présentes dans la classe dcat :Catalog sont spécifiés dans le tableau 5 présent en annexe. Les attributs propres aux autres instances sont spécifiés dans le tableau 6 en annexe.

### Les règles concernant les attributs cités ci-dessous s&#39;appliquent aux instanciations dans la classe dcat :Catalog :

### Les attributs dct :conformsTo et dct :license y sont inclus car, selon les [TG 2.0], ils caractérisent les jeux de données ;

### L&#39;un des attributs suivants doit être pourvu (dct :created, dct :modified ou dct :issued). En outre, les attributs dct :created et dct :modified devraient être pourvus.

### L&#39;un des attributs suivants doit être pourvus (dct :publisher, geodcat :custodian, dct :creator, geodcat :distributor, geodcat :originator, geodcat :principalInvestigator, geodcat :processor, geodcat :resourceProvider, geodcat :user ou dct :rightsHolder).

### Instanciation sans élément [INSPIRE]

Remarques concernant le contenu de la classeDès lors, seules les fiches [ISO 19139] décrivant un service de visualisation, un service de téléchargement ou une application peuvent être converties en classes DataService. Les fiches décrivant un service de découverte ne peuvent être converties en classes DataService.

Si l&#39;instance de la classe dcat :DataService n&#39;est pas mise en correspondance avec une fiche [ISO 19139] décrivant un service éligible, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à l&#39;élément [ISO 19139] qui lui est associé dans le tableau 6 en annexe.

Ces spécifications prévoient également que le contenu des attributs dont le domaine est une classe domaine correspond à une classe soit égalpourvu àau moyen d&#39;une une ou de plusieurs instanciations de ladite classe conformes aux spécifications du présent profil.

## X.

## Y.Si une classe dcat : DataService n&#39;est pas mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs mis en correspondance avec des éléments INSPIRE soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à ces mêmes éléments.

## Z.Si une classe dcat : DataService est mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs provienne des éléments de la fiche [ISO 19139] référencés dans la colonne XPATH Source.

## AA.En outre, les spécifications de [DCAT AP 2 fédéral]  prévoient d&#39;instancier, pour chaque jeu de données accessibles au moyen des services décrits, la classe dcat :Dataset dans la classe dcat :Catalog. En effet, il est nécessaire d&#39;instancier explicitement dans tout catalogue [DCAT AP] les jeux de données au moyen de la classe dcat :Dataset accessibles via les services considérés.

## BB.Classe dcat :Distribution

La classe dcat : Distribution correspond à la description d&#39;un fichier numérique particulier d&#39;une ressource considéréed&#39;un jeu de données considéré, c&#39;est-à-dire un fichier numérique dans un format particulier..

Conformément à ces spécifications, la classe peut s&#39;instancier dans l&#39;attribut la classe dcat :Datasetdistribution. Les Cette instanciation instances sont est **recommandées** et **potentiellement**** multiples**.

### Profil de la classeRemarques concernant les attributs de la classe

### Cette classe vise à identifier et à décrire exhaustivement la distribution considérée. Dès lors, les attributs propres à cette classe sont spécifiés dans le tableau 7 présent en annexe.

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut où la classe l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe sont spécifiés dans le tableau 7 présent en annexe.

Les spécifications applicables à la classe incluent les attributs dct :temporal et dct : spatial de manière à spécifier, s&#39;il échet, la couverture temporelle du fichier distribué (i.e. la version) et son emprise géographique.

### Conversion depuis des éléments [INSPIRE]

Seul le contenu des [ATOMFeed] décrivreprenant les liens de téléchargement d&#39;un jeu de données peut être convertis en instances de la classe dcat :Distribution. Les instances de la classe présentes dans une instance de dcat :Catalog ne sont pas générées à partir d&#39;un élément [INSPIRE]. En pareil cas, ces spécifications prévoient que le contenu de chaque attribut de de la classe dcat : Distribution soit pourvu à partir de l&#39;élément [ATOMFeed] qui lui est associé dans le tableau en annexe7. Les instances de la classe présentes dans une instance de dcat :Catalog ne sont pas générées à partir d&#39;un élément [INSPIRE].

Le contenu des attributs multilingues ou unilingues doit être pourvu à partir du contenu de l&#39;élément [ATOMFeed] associé. Le contenu des attributs dont le domaine est une classe domaine correspond à une classe est pourvu au moyen d&#39;une ou de plusieurs instanciations est égal à une ou plusieurs instanciations de ladite classe conforme(s) aux spécifications du présent profil. Ces instanciations reprennent le contenu de l&#39;élément [ATOMFeed] associé.

###


### Les règles particulières concernant les attributs cités ci-dessous s&#39;appliquent :

### Les attributs dct :temporal et dct : spatial sont ajoutés à la classe dcat :Distribution car ils caractérisent un fichier distribué du jeu de données considéré, correspondant à une version et éventuellement à un sous-ensemble géographique spécifiques.

### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe dcat : Distribution n&#39;est pas mise en correspondance avec une fiche [Aun [ATOMFeed] décrivant un service, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à l&#39;élément de l&#39;un [ATOMFeed] qui lui est associé dans le tableau en annexe 7.

Ces spécifications prévoient également que le contenu des attributs dont le domaine est une classe domaine correspond à une classe soit pourvu au moyen d&#39;une ou de plusieurs instanciations de ladite classe conformes aux spécifications du présent profil.

## CC.Remarques concernant le contenu de la classe

## DD.Si une classe dcat : Distribution ne s&#39;instancie pas dans une instance de dcat :Dataset mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs mis en correspondance avec des éléments INSPIRE soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral des ATOMFeed] applicables à ces mêmes éléments.

## EE.Si une classe dcat : Distribution s&#39;instancie dans une instance de dcat :Dataset mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs provienne des éléments des ATOM du jeu de données décrit par la fiche [ISO 19139] référencés dans la colonne XPATH Source.

## FF.Classe foaf: Organizsation

La classe foaf :Organization correspond à la description d&#39;une organisation, c&#39;est-à-dire un ensemble structuré de personnes ayant un ou des buts déterminés.

Conformément à ces spécifications, la classe peut s&#39;instancier dans les classes attributs dct :publisher, geodcat :custodian, dct :creator, geodcat :distributor, geodcat : originator, geodcat :principalInvestigator, geodcat :processor, geodcat :resourceProvider, geodcat :user ou dct :rightsHolderdcat :Catalog, dcat ;DataService et dcat :Dataset. L&#39;instanciation dans la première est **obligatoire** et **unique**. Dans les deux autres, l&#39;instanciationCes instanciations sont est **obligatoire**** recommandées **et** potentiellement multiple**.

### Remarques concernant les attributs de la classe Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut où la classe l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe sont spécifiés dans le tableau 8 présent en annexe.

### Conversion depuis des éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 1913915] relative aux organisations organismes peut être converti en instances de la classe foaf :Organization. En pareil cas, ces spécifications prévoient que le contenu de chaque attribut de de la classe foaf : Organization soit pourvu à partir de l&#39;élément [ISO 19139] qui lui est associé dans le tableau 8en annexe.

Le contenu des attributs multilingues ou unilingues doit être pourvu à partir du contenu de l&#39;élément [ISO 19139] associé. Le contenu des attributs dont le domaine est une classe domaine correspond à une classe est pourvu au moyen d&#39;une ou de plusieurs instanciations est égal à une ou plusieurs instanciations de ladite classe conforme(s) aux spécifications du présent profil. Ces instanciations reprennent le contenu de l&#39;élément [ISO 19139] associé.

Cette classe vise à identifier et à décrire exhaustivement l&#39;organisation considérée, indépendamment de l&#39;endroit où elle s&#39;instancie. Dès lors, les attributs propres à cette classe sont constants et spécifiés dans le tableau 8 présent en annexe.

De manière dérogatoire, certains attributs ne sont pas mis en correspondance avec des éléments ou des classes [ISO 19115]. En l&#39;espèce, les règles suivantes sont d&#39;application :

1. Le contenu de l&#39;attribut dct :type n&#39;est mis en association avec aucun élément [ISO 19115]. Dès lors, il n&#39;est pas pourvu pour les instances présentes dans les classes qui correspondent au résultat de la conversion d&#39;une fiche [ISO 19139].Remarques concernant le contenu de la classe
2.

### Instanciation sans élément [INSPIRE]

###


Si l&#39;instance de la classe foaf : Organization n&#39;est mise en correspondance avec un élément [ISO 19139] relatif correspondance avec un instance de la classe [ISO 19139] relative à une organisation, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à l&#39;élément un élément [ISO 19139] qui lui est associé dans le tableau 8au en annexe.

Ces spécifications prévoient également que le contenu des attributs dont le domaine est une classe domaine correspond à une classe soit pourvu au moyen d&#39;une ou de plusieurs instanciations de ladite classe conformes aux spécifications du présent profil.

## GG.Si une classe foaf : Organization ne s&#39;instancie pas dans une instance mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs mis en correspondance avec des éléments INSPIRE soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à ces mêmes éléments.

## HH.Si classe foaf : Organization s&#39;instancie dans une instance mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs provienne des éléments de la fiche [ISO 19139] de la ressource référencée dans la colonne XPATH Source.

## II.Certains attributs ne sont pas mis en correspondance avec les élément [ISO 19115]. En l&#39;espèce, les règles relatives aux attributs suivants sont d&#39;application :

## JJ.Le contenu de l&#39;attribut dct :type n&#39;est mis en association avec aucun élément [ISO 19115]. Dès lors, il n&#39;est pas pourvu pour les instances présentes dans les classes qui correspondent au résultat de la conversion d&#39;une fiche [ISO 19139].

## KK.Classe catalogRecord

La classe dcat :CatalogRecord correspond à l&#39;identification des instances particulières des classes dcat :Dataset, dcat :DataService (dcat :Catalog).

Conformément à ces spécifications, la classe peut s&#39;instancier dans la classe dcat :Catalog. Les instances sont **recommandées** et **potentiellement**** multiple**.

### Remarques concernant les attributs de la classe

Cette classe vise à identifier et à décrire exhaustivement les classes considérées. Dès lors, les attributs propres à cette classe sont spécifiés dans le tableau 9 présent en annexe.

### Remarques concernant le contenu de la classe

###


Si une classe dcat : CatalogRecord se rapporte à une classe quelconque qui n&#39;est pas mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs des classes dcat : CatalogRecord soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à ces mêmes éléments.

Si une classe dcat : CatalogRecord se rapporte à une classe quelconque qui est mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs provienne des éléments de la fiche [ISO 19139] référencés dans la colonne XPATH Source.

Certains attributs ne sont pas mis en correspondance avec les élément [ISO 19115]. En pareil cas, ces spécifications prévoient des sources alternatives. En l&#39;espèce, les règles relatives aux attributs suivants sont d&#39;application :

1. Le contenu de l&#39;attribut foaf :primaryTopic doit être généré _a posteriori¸_ dès que toutes les classes ont été instanciées, de manière à toutes les référencer.

## LL.Classe locn:Address

La classe locn :Address correspond à la description d&#39;unede l&#39;a adresse postale d&#39;un agent foaf, c&#39;est-à-dire un ensemble structuré de personnes ayant un ou des buts déterminés.

Conformément à ces spécifications, la classe peut s&#39;instancier dans la&#39;attribut locn:address classe foaf :Organization. L&#39;instanciation dans celle-ciCette instanciation est **recommandée** et **unique**.

### Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut où la classe l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres aux instances sont spécifiés dans le tableau 9 présent en annexe.

### Conversion depuis des éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 19115] relative aux adresses postales peut être converti en instances de la classe locn : Address. En pareil cas, ces spécifications prévoient que chaque attribut de la classe locn :Address soit pourvu à partir de l&#39;élément [ISO 19139] qui lui est associé dans le tableau 9leau en annexe.

### Instanciation sans élément [INSPIRE]

1.
### Remarques concernant les attributs de la classe

### Cette classe vise à identifier et à décrire exhaustivement l&#39;adresse considérée, indépendamment de l&#39;endroit où elle s&#39;instancie. Dès lors, les attributs propres à cette classe sont constants et spécifiés dans le tableau 8 présent en annexe.

Si l&#39;instance de la classe locn : Address n&#39;est mise en correspondance avec un élément [ISO 19139] relatif correspondance avec un instance de la classe [ISO 19139] relative à une organisation, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à l&#39;élément un élément [ISO 19139] qui lui est associé dans le tableau 9 en annexe.

## MM.Remarques concernant le contenu de la classe

## NN.Si une classe locn :Address ne s&#39;instancie pas dans une instance mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs mis en correspondance avec des éléments INSPIRE soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à ces mêmes éléments.

## OO.Si classe locn :Address s&#39;instancie dans une instance mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs provienne des éléments de la fiche [ISO 19139] de la ressource référencée dans la colonne XPATH Source.

## PP.Classe skos: Concept

La classe skos :Concept correspond à la description d&#39;un concept, c&#39;est-à-dire une notion identifiée de manière univoque et nommée en au moins une langue.

Conformément à ces spécifications, la classe peut s&#39;instancier dans les attributs dcat :theme, dct :language, dct :subject, dct : adms:representationTechnique, dct :type, adms :status et sdmx-attribut:unitMeasure. L&#39;instanciationCes instanciations dans ceux-ci estsont **recommandées** et **potentiellement multiples**.

### Profil de la classe

1.
### Remarques concernant les attributs de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut où la classe l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe skos :Concept sont spécifiés dans le tableau 10 présent en annexe.

### Conversion depuis des éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 1911539] relatives à des mots-clés issus de thésaurus et dûment identifiées par une URI peut être directement converti en instances de la classe skos : Concept.

En pareil cas, ces spécifications prévoient que chaque attribut de la classe skos :Concept soit pourvu à partir de l&#39;élément [ISO 19139] qui lui est associé dans le tableau 10en annexe.

Le contenu des instances des classes [ISO 19139] relatives aux langues, aux thèmes [ISO 19115], au type de représentation spatiale, à la résolution spatiale des ressources matricielles et, au type de service peut également être converti en instances de la classe skos:Concept.

En pareil cas, ces spécifications prévoient que chaque attribut de la classe skos :Concept soit pourvu sur base de concepts issus de thésaurus SKOS sémantiquement identiques aux éléments [ISO 19139] considérés. L&#39;annexe II propose pour chaque valeur de ces éléments [ISO 19139], un concept skos identique.

### Cette classe vise à identifier et à décrire exhaustivement le concept considéré, indépendamment de l&#39;endroit où il s&#39;instancie. Dès lors, les attributs propres à cette classe sont constants et spécifiés dans le tableau 8 présent en annexe.

### Instanciation sans élément [INSPIRE]

### Remarques concernant le contenu de la classe

Si l&#39;instance de la classe skos : Concept n&#39;est mise en correspondance avec un élément [ISO 19139], alors ces spécifications prévoient que le contenu des attributs soit pourvu par des concepts issus de thésaurus SKOS. L&#39;annexe II propose, pour chaque attribut où peut s&#39;instancier la classe skos :Concept, une liste de thésaurus obligatoires, recommandés ou optionnels.

## QQ.Si la classe skos :Concept s&#39;instancie dans un attribut mis en correspondance avec un élément d&#39;une fiche [ISO 19139] identifié par l&#39;URI d&#39;un concept issus d&#39;un [thésaurus SKOS], alors ces spécifications prévoient que le contenu des attributs soit pourvu sur base du concept issu du [thésaurus SKOS] mis en correspondance.

## RR.Si la classe skos :Concept s&#39;instancie dans un attribut mis en correspondance avec un élément d&#39;une fiche [ISO 19139] qui n&#39;est pas identifié par l&#39;URI d&#39;un concept issus d&#39;un [thésaurus SKOS], alors ces spécifications prévoient que le contenu des attributs soit pourvu sur base de concepts issus de [thésaurus SKOS] pertinents et de manière à refléter l&#39;élément de la fiche [ISO 19139].

## SS.Si la classe skos :Concept s&#39;instancie dans un attribut qui n&#39;est pas mis en correspondance avec un élément d&#39;une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs soit pourvu sur base de concepts issus de [thésaurus SKOS] pertinents.

## TT.L&#39;annexe II propose une liste de [thésaurus SKOS] pertinents en fonction de l&#39;attribut où s&#39;instancie la classe skos:Concept.

## UU.Classe dct: PeriodOfTime

La classe dct :PeriodOfTime correspond à la description d&#39;une séquence temporelle, c&#39;est-à-dire un intervalle de temps borné.

Conformément à ces spécifications, la classe peut s&#39;instancier dans l&#39;attribut dct :temporal. L&#39;instanciationCette instanciation dans celle-ci est **recommandée** et **potentiellement multiple**.

### Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut où la classe l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe dct : PeriodOfTime sont spécifiés dans le tableau 11 présent en annexe.

### Conversion depuis des éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 1911539] relative aux séquences temporelles peut être converti en instances de la classe dct  : PeriodOfTime. En pareil cas, ces spécifications prévoient que chaque attribut de la classe dct  :PeriodOfTime soit pourvu à partir de l&#39;élément [ISO 19139] qui lui est associé dans le tableau 11 en annexe.

### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe dct : PeriodOfTime n&#39;est mise en correspondance avec un élément [ISO 19139] relatif correspondance avec un instance de la classe [ISO 19139] relative à une organisation une séquence temporelle, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à l&#39;élément un élément [ISO 19139] qui lui est associé dans le tableau en annexe 11.

## VV.

## WW.Remarques concernant les attributs de la classe

## XX.Cette classe vise à identifier et à décrire exhaustivement la période de temps considérée, indépendamment de l&#39;endroit où elle s&#39;instancie. Dès lors, les attributs propres à cette classe sont constants et spécifiés dans le tableau 8 présent en annexe.

## YY.Remarques concernant le contenu de la classe

## ZZ.Si la classe dct : PeriodOfTime ne s&#39;instancie pas dans un attribut mis en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs mis en correspondance avec des éléments INSPIRE soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à ces mêmes éléments.

## AAA.Si la classe dct : PeriodOfTime s&#39;instancie dans un attribut mis en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs de l&#39;instance considérée provienne des éléments de la fiche [ISO 19139] dans la colonne XPATH Source.

## BBB.Classe dqv: QualityMeasurement

La classe dqv: QualityMeasurement correspond à la résolution spatiale de la ressource considérée, c&#39;est-à-dire au niveau de détail de la ressource. .

Conformément à ces spécifications, la classe peut s&#39;instancier dans l&#39;attribut dqv:hasQualityMeasurement et dcat :spatialResolutionInMeters. Dans les deux cas, l&#39;L&#39;instanciation dans le premier est celle-ci est **recommandée** et **unique**. dans le cas de ressources vectorielles, alors que l&#39;instanciation dans . le second est **obligatoire** et **unique** dans le cas de ressources matricielles.

### Profil de la classe

Le présent profil prévoit des spécifications différentes en fonction de l&#39;endroit où la classe s&#39;instancie. Celles-ci découlent pour l&#39;essentiel de la nécessité de décrire la résolution spatiale au moyen de notionsconcepts adaptés au type de ressource.

Les attributs propres aux instances relatives aux ressources vectorielles sont spécifiés dans le tableau 1212 présent en annexe. Les attributs propres à toutes les instances relatives aux ressources matricielles sont spécifiés dans le tableau 13 13 présent en annexe.

### Conversion depuis des éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 19139] relative à la résolution spatiale peut être converti en instances de la classe dqv : QualityMeasurement. En pareil cas, ces spécifications prévoient que chaque attribut soit pourvu à partir de l&#39;élément [ISO 19139] qui lui est associé dans le tableau en annexe.

### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe dqv : QualityMeasurement n&#39;est mise en correspondance avec un élément [ISO 19139] relatif à la résolution spatialeune organisation, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à l&#39;élément un élément [ISO 19139] qui lui est associé dans le tableau en annexe.

## CCC.

## DDD.Remarques concernant les attributs de la classe

## EEE.Cette classe vise à identifier et à décrire exhaustivement la résolution spatiale de la ressource. Dès lors, les attributs propres à cette classe varient en fonction de la nature de la ressource considérée.

## FFF.Les différences entre les règles applicables aux types de ressources découlent de la nécessité de préciser la résolution spatiale de manière adaptée. En effet, la résolution spatiale des ressources matricielles se mesure au moyen de l&#39;emprise au sol des pixel, là où la résolution spatiale des ressources vectorielles se mesure au moyen de leur échelle de conception. Les attributs sémantiquement nécessaires pour l&#39;instanciation varient en fonction de la ressource considérée.

## GGG.Dès lors, les attributs propres à la classe instanciée pour décrire une ressource matricielle sont spécifiés dans le tableau .... présent en annexe. Les attributs propres à la classe instanciée pour décrire une ressource verctorielle sont spécifiés dans le tableau .... présent annexe.

## HHH.Remarques concernant le contenu de la classe

## III.Si la classe dqv: QualityMeasurement ne s&#39;instancie pas dans un attribut mis en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs mis en correspondance avec des éléments INSPIRE soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à ces mêmes éléments.

## JJJ.Si la classe dqv: QualityMeasurement s&#39;instancie dans un attribut mis en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs de l&#39;instance considérée provienne des éléments de la fiche [ISO 19139] dans la colonne XPATH Source.

## KKK.Classe dct: Location

La classe dct : Location correspond à la description d&#39;une zone géographique, c&#39;est-à-dire une portion bornée de la surface terrestre.

Conformément à ces spécifications, la classe peut s&#39;instancier dans l&#39;attribut dct :location. Cette L&#39;instanciation dans celle-ci est **recommandée** et **unique**.

### Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut où la classe l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe dct :Location dct : PeriodOfTime sont spécifiés dans le tableau 14 14 présent en annexe.

En l&#39;absence de standards réellement communs, les spécifications applicables à la classe incluent les attributs locn :geometry et dcat :bbox. Le contenu de ces deux attributs doit être rigoureusement identiques et renvoyer vers la description de l&#39;emprise au sol de la ressource dans un format spécifique. Les deux attributs doivent être notés quatre fois, de manière à spécifier l&#39;emprise au sol selon les formats suivants :

- [Well Know Text ](http://www.opengis.net/ont/geosparql#wktLiteral);
- [Geographic Markup Language ](http://www.opengis.net/ont/geosparql#gmlLiteral);
- GeoJSON au moyen de :.
  - L&#39;[identifiant IANA](https://www.iana.org/assignments/media-types/application/vnd.geo+json) ;
  - L&#39;[identifiant opengis](http://www.opengis.net/ont/geosparql#geoJSONLiteral).

L&#39;emprise au sol en GeoJSON doit être notée deux fois, de manière à l&#39;identifier au moyen de son [identifiant IANA](https://www.iana.org/assignments/media-types/application/vnd.geo+json) et de son [identifiant opengis](http://www.opengis.net/ont/geosparql#geoJSONLiteral).

### Conversion depuis des éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 1913915] relative à la résolution spatiale peut être converti en instances de la classe dct :Location dct : PeriodOfTime. En pareil cas, ces spécifications prévoient que chaque attribut soit pourvu à partir de l&#39;élément [ISO 19139] qui lui est associé dans le tableau en annexe.

### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe dct :Location dct : PeriodOfTime n&#39;est mise en correspondance avec un élément [ISO 19139] relatif correspondance avec un instance de la classe [ISO 19139] relative à une organisation, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à l&#39;élément un élément [ISO 19139] qui lui est associé dans le tableau 14en annexe.

## LLL.

## MMM.Remarques concernant les attributs de la classe

## NNN.Cette classe vise à identifier et à décrire de différentes manières la zone géographique couverte par la ressource, indépendamment de l&#39;endroit où elle s&#39;instancie. Dès lors, les attributs propres à cette classe sont constants et spécifiés dans le tableau 8 présent en annexe.

## OOO.L&#39;absence de réels standards en la matière a conduit ces spécifications à fixer la cardinalité des attributs locn :geometry et dcat :bbox à quatre. Ces attributs doivent être également remplis avec la géométrie de la zone géographique spécifiée selon les normes suivantes :

## PPP.http://www.opengis.net/ont/geosparql#wktLiteral (Well Known Text) ;

## QQQ.[http://www.opengis.net/ont/geosparql#gmlLiteral](http://www.opengis.net/ont/geosparql#gmlLiteral) (GML] ;

## RRR.[https://www.iana.org/assignments/media-types/application/vnd.geo+json](https://www.iana.org/assignments/media-types/application/vnd.geo+json) (GeoJSON);

## SSS.[http://www.opengis.net/ont/geosparql#geoJSONLiteral](http://www.opengis.net/ont/geosparql#geoJSONLiteral) (GeoJSON).

## TTT.Remarques concernant le contenu de la classe

## UUU.Si la classe dct : PeriodOfTime ne s&#39;instancie pas dans un attribut mis en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs mis en correspondance avec des éléments INSPIRE soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à ces mêmes éléments.

## VVV.Si la classe dct : PeriodOfTime s&#39;instancie dans un attribut mis en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs de l&#39;instance considérée provienne des éléments de la fiche [ISO 19139] dans la colonne XPATH Source.

## WWW.Classe ConceptScheme

La classe skos:ConceptScheme dct :PeriodOfTime correspond à la description d&#39;un thésaurus, c&#39;est-à-dire un ensemble structurés de concepts mis en relation.

Conformément à ces spécifications, la classe peut s&#39;instancier dans l&#39;attribut dcat:themeTaxonomy. L&#39; Cette instanciation dans celle-ci est **recommandée** et **potentiellement multiple**.

### Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut où la classe l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe skos : ConceptSchemesont spécifiés dans le tableau 157 présent en annexe.

### Conversion depuis des éléments [INSPIRE]

Aucune classe [ISO 19115] ne peut être convertie en une instance de la classe skos :ConceptScheme.

### Instanciation sans élément [INSPIRE]

Ces spécifications prévoient que la classe skos : ConceptScheme soit instanciée _a posteriori_, alors que toutes les autres classes ont été dûment instanciées. Ces spécifications prévoient que la classe skos :ConceptScheme soit instanciée sur base des URL présents dans les attributs skos :inScheme des instances de la classe skos :Concept.

## XXX.

## YYY.Remarques concernant les attributs de la classe

## ZZZ.Cette classe vise à identifier et à décrire exhaustivement les thésaurus dont proviennent les mots-clés présents dans l&#39;ensemble du catalogue. Dès lors, les attributs propres à cette classe sont constants et spécifiés dans le tableau 8 présent en annexe.

## AAAA.Remarques concernant le contenu de la classe

## BBBB.Ces spécifications prévoient que le contenu des attributs de ou des instances soient cohérents avec les thésaurus effectivement identifiés dans la ou les instances de la classe skos :Concept.

## CCCC.Classe vcard Organizartion

La classe vcard :Organization correspond à la description d&#39;une organisation, c&#39;est-à-dire un ensemble structuré de personnes ayant un ou des buts déterminés.

Conformément à ces spécifications, la classe peut s&#39;instancier dans les attributs dcat:contactPoint. Cette instanciation est **optionnelle** et **unique**.

### Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut où la classe l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe vcard: Organization sont spécifiés dans le tableau 167 présent en annexe.

### Conversion depuis des éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 1911539] relative aux organismes peut être converti en instances de la classe vcard :Organization. En pareil cas, ces spécifications prévoient que chaque attribut de la classe vcard : Organization soit pourvu à partir de l&#39;élément [ISO 19139] qui lui est associé dans le tableau 16en annexe.

Ces spécifications prévoient également que les attributs dont le domaine est une classe domaine correspond à une classe soient pourvus au moyen d&#39;une ou de plusieurs instanciations de ladite classe conformes aux spécifications du présent profil.

### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe f vcard  oaf : Organization n&#39;est mise en correspondance avec un élément [ISO 19139] relatif correspondance avec un instance de la classe [ISO 19139] relative à une organisation, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à l&#39;élément un élément [ISO 19139] qui l&#39;élément [ISO 19139] qui lui est associé dans le tableau en annexe.

Ces spécifications prévoient également que le contenu des attributs dont le domaine est une classe domaine correspond à une classe soit pourvu au moyen d&#39;une ou de plusieurs instanciations de ladite classe conformes aux spécifications du présent profil.

## DDDD.

## EEEE.La classe foaf :Organization correspond à la description d&#39;une organisation, c&#39;est-à-dire un ensemble structuré de personnes ayant un ou des buts déterminés.

## FFFF.Conformément à ces spécifications, la classe peut s&#39;instancier dans les attributs dcat:contactPoint. L&#39;instanciation est **optionnelle** et **unique**.

## GGGG.Remarques concernant les attributs de la classe

## HHHH.Cette classe vise à identifier et à décrire exhaustivement l&#39;organisation considérée, indépendamment de l&#39;endroit où elle s&#39;instancie. Dès lors, les attributs propres à cette classe sont constants et spécifiés dans le tableau 8 présent en annexe.

## IIII.Remarques concernant le contenu de la classe

## JJJJ.Si une classe vcard : Organization ne s&#39;instancie pas dans une instance mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs mis en correspondance avec des éléments INSPIRE soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à ces mêmes éléments.

## KKKK.Si classe vcard : Organization s&#39;instancie dans une instance mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs provienne des éléments de la fiche [ISO 19139] de la ressource référencée dans la colonne XPATH Source.

## LLLL.Classe vcard:Address

La classe vcard :Address correspond à la description d&#39;une adresse postale d&#39;un agent agent vcard .

Conformément à ces spécifications, la classe peut s&#39;instancier dans la classe vcard :Organization. Cette instanciation dans celle-ci est **recommandée** et **unique**.

### Profil de la classe

Le présent profil prévoit des spécifications indépendantes de l&#39;attribut où la classe l&#39;attribut au sein duquel la classe s&#39;instancie. Les attributs propres à toutes les instances de la classe vcard :Address sont spécifiés dans le tableau 177 présent en annexe.

### Conversion depuis des éléments [INSPIRE]

Seul le contenu des instances de la classe [ISO 1911539] relative aux adresses postales peut être converti en instances de la classe vcard : Address. En pareil cas, ces spécifications prévoient que chaque attribut de la classe vcard :Address soit pourvu à partir de l&#39;élément [ISO 19139] qui lui est associé dans le tableau 17 en annexe.

### Instanciation sans élément [INSPIRE]

Si l&#39;instance de la classe vcard : Address n&#39;est mise en correspondance avec un élément [ISO 19139] relatif correspondance avec un instance de la classe [ISO 19139] relative à une organisation, alors ces spécifications prévoient néanmoins que le contenu des attributs de domaine multilingue ou unilingue soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à l&#39;élément un élément [ISO 19139] qui l&#39;élément [ISO 19139] qui lui est associé dans le tableau 17en annexe.

La classe vcard :Address correspond à la description d&#39;une adresse postale d&#39;un agent vcard, c&#39;est-à-dire un ensemble structuré de personnes ayant un ou des buts déterminés.

Conformément à ces spécifications, la classe peut s&#39;instancier dans la classe vcard :Organization. L&#39;instanciation dans celle-ci est **recommandée** et **unique**.

1.
### Remarques concernant les attributs de la classe

Cette classe vise à identifier et à décrire exhaustivement l&#39;adresse considérée, indépendamment de l&#39;endroit où elle s&#39;instancie. Dès lors, les attributs propres à cette classe sont constants et spécifiés dans le tableau 8 présent en annexe.

### Remarques concernant le contenu de la classe

Si une classe vcard :Address ne s&#39;instancie pas dans une instance mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs mis en correspondance avec des éléments INSPIRE soit pourvu selon les règles terminologiques et syntaxiques du [profil de métadonnées fédéral] applicables à ces mêmes éléments.

Si classe vcard :Address s&#39;instancie dans une instance mise en correspondance avec une fiche [ISO 19139], alors ces spécifications prévoient que le contenu des attributs provienne des éléments de la fiche [ISO 19139] de la ressource référencée dans la colonne XPATH Source.

# Normes référencées

[ISO 19115] : norme ISO relative aux métadonnées de jeux de données et de services à caractère géographique utilisée pour implémenter la [directive INSPIRE] ([https://www.iso.org/standard/26020.html](https://www.iso.org/standard/26020.html))

[ISO 19139] : norme ISO relative à l&#39;implémentation XML de la norme [[ISO 19115]] utilisée pour implémenter la [directive INSPIRE] ([https://www.iso.org/fr/standard/32557.htm](https://www.iso.org/fr/standard/32557.htm))

[TG 2.0] : norme d&#39;implémentation des métadonnées INSPIRE basée sur les normes [[ISO 19115]] et [[ISO 19139]] ([https://inspire.ec.europa.eu/id/document/tg/metadata-iso19139](https://inspire.ec.europa.eu/id/document/tg/metadata-iso19139))

[profil de métadonnées fédéral] : norme fédérale non-officielle conforme aux TG 2.0

[[CSW]] : norme OGC relative à la publication de métadonnées ([https://portal.ogc.org/files/?artifact\_id=20555](https://portal.ogc.org/files/?artifact_id=20555))

[TG relatives aux services de découverte] : norme d&#39;implémentation des services de découverte INSPIRE

[CSW] : norme

[DCAT] : norme W3C pour standardiser les catalogues de jeux de données sur le web ([https://www.w3.org/TR/vocab-dcat-1/](https://www.w3.org/TR/vocab-dcat-1/))

[DCAT 2] : norme W3C pour standardiser les catalogues de jeux de données sur le web ([https://www.w3.org/TR/vocab-dcat-1/](https://www.w3.org/TR/vocab-dcat-1/))

[DCAT AP 1] : norme ISA implémentant le standard [DCAT] et lui étant conforme pour décrire les jeux de données publics distribués dans l&#39;Union ([https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/11](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/11))

[DCAT AP 2] : norme ISA implémentant le standard [DCAT 2] et lui étant conforme pour décrire les jeux de données publics distribués dans l&#39;Union ([https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/200](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/200))

[Geo DCAT AP 2] : norme ISA implémentant le standard [DCAT AP 2] et lui étant conforme pour décrire les jeux de données publics géographiques distribués dans l&#39;Union ([https://semiceu.github.io/GeoDCAT-AP/drafts/latest/#properties-for-distribution](https://semiceu.github.io/GeoDCAT-AP/drafts/latest/#properties-for-distribution))

[Stat DCAT AP 1] : norme ISA implémentant le standard [DCAT AP 1] et lui étant conforme pour décrire les jeux de données publics statistiques distribués dans l&#39;Union ([https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/statdcat-application-profile-data-portals-europe/release/100](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/statdcat-application-profile-data-portals-europe/release/100))

[DCAT AP 2 fédéral] : norme fédérale informelle contenue dans le présent document conforme à [DCAT AP 2]

[ATOM] : norme IETF relative à la syndication de contenus ([https://tools.ietf.org/html/rfc4287](https://tools.ietf.org/html/rfc4287))

[TG relatives aux services de téléchargement] : norme d&#39;implémentation des services de téléchargement INSPIRE basée sur les normes [WFS] et [ATOM] ([https://inspire.ec.europa.eu/documents/technical-guidance-implementation-inspire-download-services](https://inspire.ec.europa.eu/documents/technical-guidance-implementation-inspire-download-services))

# Annexe Is

1.
## dcat :Catalog

| Instanciation de dcat :Catalog dans l&#39;élément racineInstanciation : Feed |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| --- | --- | --- | --- | --- | --- | --- |
| dct:title | titre | Titre du catalogue considéré  | M  | 1  | multilingue | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:title  |
| dct:description | description | Description du catalogue considéré  | M  | 1  | multilingue | //\*/gmd:identificationInfo/\*/gmd:abstract  |
| --- | --- | --- | --- | --- | --- | --- |
| dct:publisher | éditeur | Organisation responsable de la publication du catalogue considéré  | M  | 1  | foaf:Organization | //\*/gmd:contact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;publisher&#39;]]  |
| --- | --- | --- | --- | --- | --- | --- |
| dcat:dataset | jeu de données | Informations relatives au(x) jeu(x) de données référencés dans le catalogue  considéré  | M  | 1-n  | dcat:Dataset | si catalogue généré à partir d&#39;un CSW[CSW] --\&gt; getrecords avec type = dataset
 si catalogue généré par wizard : génération _a posteriori_ sur base des datasets renseignés |
| --- | --- | --- | --- | --- | --- | --- |
| dcat:service | service | Informations relatives au(x)service(s) référencés dans le catalogue considéré  | RM  | 0-n  | dcat:DataService | si catalogue généré à partir d&#39;un CSW[CSW] --\&gt; getrecords avec type = service/application
 si catalogue généré par wizard : génération _a posteriori_ sur base des services renseignés |
| --- | --- | --- | --- | --- | --- | --- |
| foaf:homepage | page d&#39;acceuil | Version human readable du catalogue considéré  | R  | 0-1  | foaf:DocumentURL | Pas de XPATH : https://www.geo.be/home (ou homepage du catalogue propre à l&#39;institution si celui-ci est harvesté) |
| --- | --- | --- | --- | --- | --- | --- |
| dct:language | langue | Langue(s) du catalogue considéré  | M  | 4  | [codedValue](http://publications.europa.eu/resource/authority/language)codedValueskos:Concept | //\*/gmd:locale/gmd:PT\_Locale/gmd:languageCode/gmd:LanguageCode/@codeListValue |
| --- | --- | --- | --- | --- | --- | --- |
| dct:issued | date de première publication | Date de première publication du catalogue  | R  | 1  | date (YYYY-MM-DD) | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:date/gmd:CI\_Date[gmd:dateType/gmd:CI\_DateTypeCode[@codeListValue=&#39;publication&#39;]]/gmd:date  |
| --- | --- | --- | --- | --- | --- | --- |
| dct:spatial | couverture spatiale | Description de la couverture spatiale des ressources comprises dans le catalogue  | R  | 1-n  | dct :Location | //\*/gmd :identificationInfo/\*/gmd :extent/gmd :EX\_Extent/gmd :geographicElement  |
| --- | --- | --- | --- | --- | --- | --- |
| dcat :themeTaxonomy | vocabulaire contrôlé | Informations relatives aux thésaurus dont sont extraits les mots clés décrivant les jeux de données  | O  | 0-n  | [skos :ConceptScheme](http://publications.europa.eu/resource/authority/data-theme) | génération _a posteriori _en recensant tous les thésaurus référencés dans les classes Dataset et DataService |
| --- | --- | --- | --- | --- | --- | --- |
| dct :hasPart | catalogue inclus | Informations relatives au(x) catalogue(s) compris dans le catalogue considéré  | O  | 0-n  | dcat :Catalog | si catalogue généré à partir d&#39;&#39;un CSW[CSW] --\&gt; néant
 si catalogue généré par wiza rd : prévoir champ |
| --- | --- | --- | --- | --- | --- | --- |
|  dct:isPartOf | catalogue incluant | Informations relatives au(x) catalogue(s) comprenant dans le catalogue considéré  | O  | 0-n  | d cat:Catalog | si catalogue généré à partir&#39; d&#39;un CSW[CSW] --\&gt; ID du catalogue de BOSA+ ID du cataloguesuprême DCAT de&#39; l&#39;IGN
 si catalogue généré par wiza rd : prévoir champ |
| --- | --- | --- | --- | --- | --- | --- |
| dcat:record | signalétique | Informations relatives aux instances figurant dans le catalogue considéré  | R | 0-n  | d cat:CatalogRecord | génération _a posteriori _en recensant toutes les instances CatalogRecord  |
| --- | --- | --- | --- | --- | --- | --- |
| dcat:distribution | distribution | Informations relatives aux modalités&#39; d&#39;acquisition du catalogue  | R  | 0-n  | d cat:Distribution | --\&gt; générer en utilisant le lien vers la sérialisation XML (et éventuellement JSON) |
| --- | --- | --- | --- | --- | --- | --- |
| dcat:catalog | catalogue | un cCatalogue dont le contenu est intéréssantintéressant dans le contexte du catalogue décritconsidéré  | O  | 0-n  | d cat:Catalog | si catalogue généré à partir&#39; d&#39;un CSW[CSW] --\&gt; néant
 si catalogue généré par wiza rd : prévoir champ |
| --- | --- | --- | --- | --- | --- | --- |
| dcat:contactPoint | point de contact | Informations relatives aux modalités de prise de contact à propos du catalogue  | R  | 0-1  | vc ard:Kind | //\*/ gmd:contact/ gmd:CI\_ResponsibleParty[ gmd:rôleole/ gmd:CI\_RoleCode[@codeListValue=&#39;publisher&#39;]]  |
| --- | --- | --- | --- | --- | --- | --- |
|  dct:identifier | identifiant | Identifiant alphanumérique unique du catalogue  | M | 1  | unilingue | Pas de XPA TH :  sérialisation X ML ?  |
| --- | --- | --- | --- | --- | --- | --- |
| dcat:theme | mot-clé issu&#39; d&#39;un vocabulaire contrôlé | Mot clé issu&#39; d&#39;un thésaurus décrivant le jeu de données  | O  | 0-n  | s kos:Concept | //\*/ gmd:identificationInfo/\*/ gmd:descriptiveKeywords/ gmd:MD\_Keywords[ gmd:thesaurusName/ gmd:CI\_Citation/ gmd:title/\*={}]/ gmd:keyword/\*  |
| --- | --- | --- | --- | --- | --- | --- |

Tableau  1 : classe dc at :Catalog instanciée dans l&#39;élément racine

| Instanciation de d at :Catalog dans une autre instance de d at :CatalogInstanciation : Catalog |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
|  dct:title | titre | Titre du catalogue considéré  | M | 1  | multilingue | //\*/ gmd:identificationInfo/\*/ gmd:citation/ gmd:CI\_Citation/ gmd:title  |
|  dct:description | description | Description du catalogue considéré  | O | 1  | multilingue | //\*/ gmd:identificationInfo/\*/ gmd:abstract  |
|  dct:publisher | éditeur | Organisation responsable de la publication du catalogue considéré  | O | 1  | f oaf:Organization | //\*/ gmd:contact/ gmd:CI\_ResponsibleParty[ gmd:rôleole/ gmd:CI\_RoleCode[@codeListValue=&#39;publisher&#39;]]  |
| dcat:dataset | jeu de données | Informations relatives au(x) jeu(x) de données référencés dans le catalogue  considéré  | W | 0 | d cat:Dataset |   |
| dcat:service | service | Informations relatives au(x)service(s) référencés dans le catalogue considéré  | W | 0 | d cat:DataService |   |
| foaf:homepage | page&#39; d&#39;acceuil | Version human readable du catalogue considéré  | R | 0-1  | URL multilingue | Pas de XPA TH : ht tps://www.geo.be/home (ou homepage du catalogue propre à&#39; l&#39;institution si celui-ci est harvesté) |
|  dct:language | langue | Langue(s) du catalogue considéré  | O | 4  | skos :ConceptcodedValue | //\*/ gmd:locale/ gmd:PT\_Locale/ gmd:languageCode/ gmd:LanguageCode/@codeListValue |
|  dct:issued | date de première publication | Date de première publication du catalogue  | O | 1  | date (YYYY-MM-DD) | //\*/ gmd:identificationInfo/\*/ gmd:citation/ gmd:CI\_Citation/ gmd:date/ gmd:CI\_Date[ gmd:dateType/ gmd:CI\_DateTypeCode[@codeListValu&#39;e=&#39;publicati&#39;on&#39;]]/ gmd:date  |
|  dct:spatial | couverture spatiale | Description de la couverture spatiale des ressources comprises dans le catalogue  | O | 1-n  | dct:Location | //\*/gmd:identificationInfo/\*/gmd:extent/gmd:EX\_Extent/gmd:geographicElement  |
| dcat:themeTaxonomy | vocabulaire contrôlé | Informations relatives aux thésaurus dont sont extraits les mots clés décrivant les jeux de données  | W | 0 | [skos:ConceptScheme](http://publications.europa.eu/resource/authority/data-theme) | Pas de XPATH : généré _a posteriori _en recensant tous les thésaurus référencés dans les classes Dataset et DataService |
| dct:hasPart | catalogue inclus | Informations relatives au(x) catalogue(s) compris dans le catalogue considéré  | W | 0 | dcat:Catalog |   |
| dct:isPartOf | catalogue incluant | Informations relatives au(x) catalogue(s) comprenant dans le catalogue considéré  | W | 0 | dcat:Catalog |   |
| dcat:record | signalétique | Informations relatives aux instances figurant dans le catalogue considéré  | W | 0  | dcat:CatalogRecord |   |
| dcat:distribution | distribution | Informations relatives aux modalités d&#39;acquisition du catalogue  | R | 0-n  | dcat:Distribution | Instances renvoyant vers le lien d&#39;accès en XML + JSON si moyen  |
| dct:catalog | catalogue | un cCatalogue dont le contenu est intéréssantintéressant dans le contexte du catalogue considéré  | W | 0 | dcat:Catalog | Instance renvoyant vers un catalogue intéressant |
| dcat:contactPoint | point de contact | Informations relatives aux modalités de prise de contact à propos du catalogue  | R | 0-1  | vcard:OrganizationKind | //\*/gmd:contact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;publisher&#39;]]  |
| dct:identifier | identifiant | Identifiant alphanumérique unique du catalogue  | M | 1  | unilingue | Pas de XPATH :  sérialisation XML ?  |
| dcat:theme | mot-clé issu d&#39;un vocabulaire contrôlé | Mot clé issu d&#39;un thésaurus décrivant le jeu de données  | W | 0 | skos:Concept |   |

**Tableau 2 : classe dcat :Catalog instanciée dans une autre instance de la classe dcat :Catalog**

## B.dcat :Dataset

| Instanciation de dcat :Dataset dans une instance de dcat :CatalogInstanciation : Catalog |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| dct:title | titre | Ttitre du jeu de données considéré | M | 1 | multilingue | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:title/\*
 titre saisi conformément aux spécifications du profil fédéral |
| dct:description | description | Ddescription du jeu de données considéré | M | 1 | multilingue | //\*/gmd:identificationInfo/\*/gmd:abstract/\* |
| dcat:contactPoint | point de contact | Iinformations relatives aux modalités de prise de contact à propos du jeu de données | O | 0-n | vcard:OrganizationKind | //\*/gmd:contact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;pointOfContact&#39;]] |
| dcat:distribution | distribution | Iinformations relatives aux modalités d&#39;acquisition du jeu de données considéré | R | 0-n | dcat:Distribution | si dataset généré à partir d&#39;une fiche [ISO 19139] --\&gt; utiliser contenu de l&#39;ATOM FEED référencé dans la dite fiche
 si dataset généré par wizard : générer par saisie manuelle dans un champ ad hoc |
| dcat:keyword | mot-clé | Mmot-clé libre décrivant le jeu de données considéré | O | 0-n | multilingue | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD\_Keywords[not(./gmd:thesaurusName)]/gmd:keyword/\* |
| dcat:theme | mot-clé issu d&#39;un vocabulaire contrôlé | Mmot- clé issu d&#39;un thésaurus décrivant le jeu de données | M | 1-n | [skos:Concept](http://publications.europa.eu/resource/authority/data-theme) | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD\_Keywords[gmd:thesaurusName/gmd:CI\_Citation/gmd:title/\*={}]/gmd:keyword/\* |
| dct:subject | catégorie ISO | Iinformations relatives à la catégorie [ISO 19115] du jeu de données considéré | O | 0-n | [skos:Concept](http://inspire.ec.europa.eu/metadata-codelist/TopicCategory) | //\*/gmd:identificationInfo/\*/gmd:topicCategory/\* |
| dct:spatial | couverture spatiale | Iinformations relatives à la région géographique visée par le jeu de données concerné | R | 0-n | [dct:Location](http://publications.europa.eu/resource/authority/country) | //\*/gmd:identificationInfo/\*/gmd:extent/gmd:EX\_Extent/gmd:geographicElement |
| dct:temporal | couverture temporelle | Iinformations relatives au(x) laps de temps couvert(s) par le jeu de données concerné | R | 0-n | dct:PeriodOfTime | //\*/gmd:identificationInfo/\*/gmd:extent/gmd:EX\_Extent/gmd:temporalElement |
| dct:created | date de création | Ddate de création du jeu de données considéré | R | 0-1 | date (YYYY-MM-DD) | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:date/gmd:CI\_Date[gmd:dateType/gmd:CI\_DateTypeCode[@codeListValue=&#39;creation&#39;]]/gmd:date |
| dct:modified | date de mise à jour | Ddate de dernière modification du jeu de données | R | 0-1 | date (YYYY-MM-DD) | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:date/gmd:CI\_Date[gmd:dateType/gmd:CI\_DateTypeCode[@codeListValue=&#39;revision&#39;]]/gmd:date |
| dct:issued | date de première publication | Ddate de première publication du jeu de données | O | 0-1 | date (YYYY-MM-DD) | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:date/gmd:CI\_Date[gmd:dateType/gmd:CI\_DateTypeCode[@codeListValue=&#39;publication&#39;]]/gmd:date |
| foaf:page | page des métadonnéesspécifications techniques | Iinformations relatives au(x) lien(s) détaillant le contenu du jeu de données | R | 0-1 | URL multilinguefoaf:Document | //\*/gmd:distributionInfo/gmd:MD\_Distribution/gmd:transferOptions/gmd:MD\_DigitalTransferOptions/gmd:onLine/gmd:CI\_OnlineResource[gmd:protocol/\*={WWW:LINK-1.0-http--link} and gmd:function/\*/@codeListValue={&#39;information&#39;}]/gmd:linkage/gmd:name |
| dct:accrualPeriodicity | fréquence de mise à jour | Iinformations relatives à la fréquence de mise à jour du jeu de données concerné | R | 0-1 | [dct:Frequency](http://inspire.ec.europa.eu/metadata-codelist/MaintenanceFrequency) | //\*/gmd:identificationInfo/\*/gmd:resourceMaintenance/gmd:MD\_MaintenanceInformation/gmd:maintenanceAndUpdateFrequency/gmd:MD\_MaintenanceFrequencyCode/@codeListValue |
| dct:identifier | identifiant | Iidentifiant alphanumérique unique du jeu de données concerné | M | 1 | multilingue | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:identifier/\*/gmd:code/\* |
| dcat:landingPage | page d&#39;acceuilaccueil | informations relative(s) à la fiche de métadonnées HTML originale décrivant le jeu de données concernéPage de métadonnées HTML d&#39;origine | R | 0-1 | foaf:DocumentURL multilingue | [https://www.geo.be/catalog/details/ + //\*/gmd:fileIdentifier](https://www.geo.be/catalog/details/%20+%20/*/gmd:fileIdentifier) |
| dct:language | langue | Iinformations relatives au(x) langue(s) du jeu de données considéré | R | 0-4 | [codedValue](http://publications.europa.eu/resource/authority/language)skos :Concept | //\*/gmd:identificationInfo/\*/gmd:language/gmd:LanguageCode/@codeListValue |
| dct:provenance | origine | Iinformations relatives à l&#39;origine du jeu de données considéré | O | 0-1 | dct:ProvenanceStatement | //\*/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:lineage/gmd:LI\_Lineage/gmd:statement |
| dct:conformsTo | spécification ou règle de structuration | Iinformations relative(s) aux normes de qualité du jeu de données | O | 0-n | [dct:SStandard](http://www.opengis.net/def/crs/EPSG/0/) | //\*/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_DomainConsistency/gmd:result/gmd:DQ\_ConformanceResult/gmd:specification/gmd:CI\_Citation |
| dct:source | jeu de données source | Iinformations relatives à un jeu de données source | O | 0-1 | dcat:Dataset | si dataset généré à partir d&#39;une fiche [ISO 19139] --\&gt; utiliser le XPATH //\*/gmd:identificationInfo/\*/gmd:aggregationInfo
 si dataset généré par wizard : générer par sélection manuelle dans un champ ad hoc |
| dcat:spatialResolutionInMeters | résolution spatiale | iInformations relatives à la résolution spatiale du pixel du jeu de données considéré (raster) | RO | 0-1 | dqv :QualityMeasurementxsd:decimal | //\*/gmd:identificationInfo/\*/gmd:spatialResolution/gmd:MD\_Resolution/gmd:distance |
| dqv:hasQualityMeasurement | résolution spatiale | Iinformations relatives à l&#39;échelle conceptuelle du jeu de données considéréa résolution spatiale du jeu de données considéré | RO | 0-1 | dqv :QualityMeasurementdqv:QualityMeasurement | //\*/gmd:identificationInfo/\*/gmd:spatialResolution/gmd:MD\_Resolution/gmd:equivalentScale/gmd:MD\_RepresentativeFraction/gmd:denominator |
| dct:accessRights | accessibilité | Iinformations relatives aux restrictions concernant l&#39;utilisation du jeu de données | M | 1 | [dct:RightsStatement](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess) | //\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD\_LegalConstraints[\*/gmd:MD\_RestrictionCode[@codeListValue=&#39;otherRestrictions&#39;]]/gmd:otherConstraints[gco:CharacterString or gmx:Anchor[not(starts-with(@xlink:href, &#39;http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess&#39;))]] |
| adms:sample | exemple de distribution | Rréférence à un exemple de distribution du jeu de données | O | 0-1 | dcat:Distribution | pas de XPATH spécifié |
| dct:publisher | éditeur | Iinformations relatives à l&#39;organisation responsable de la disponibilité du jeu de données | O | 0-n | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;publisher&#39;]] |
| geodcat:custodian | mainteneur | Iinformations relatives à l&#39;organisation responsable de la données et de la maintenance de la ressource | O | 0-n | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;custodian&#39;]] |
| dct:creator | créateur | iInformations relatives à l&#39;organisation responsable de la production du jeu de données considéré | O | 0-n | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;author&#39;]] |
| geodcat:distributor | diffuseur | Iinformations relatives à l&#39;organisation responsable de la distribution de la ressource | O | 0-n | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;distributor&#39;]] |
| geodcat:originator | auteur | Iinformations relatives à l&#39;organisation responsable de la création de la ressource | O | 0-n | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;originator&#39;]] |
| geodcat:principalInvestigator | collecteur | Iinformations relatives à l&#39;organisation responsable de la collecte d&#39;information de recherche | O | 0-n | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;principalInvestigator&#39;]] |
| geodcat:processor | processeur | Iinformations relatives à l&#39;organisation ayant modifié la ressource après traitement des données | O | 0-n | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;processor&#39;]] |
| geodcat:resourceProvider | fournisseur | Iinformations relatives à l&#39;organisation qui fournit la ressource | O | 0-n | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;resourceProvider&#39;]] |
| geodcat:user | utilisateur | Iinformations relatives à l&#39;organisation qui utilise la ressource | O | 0-n | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;user&#39;]] |
| dct:rightsHolder | ayant droits | oOrganisation déteneurdétenteur de droits sur le service | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;user&#39;]]/gmd:organisationName |
| dct:license | conditions d&#39;utilisation | Informations relatives aux conditions d&#39;utilisation particulières de cette distribution | M | 1 | dct:LicenseDocument | //\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD\_LegalConstraints[\*/gmd:MD\_RestrictionCode[@codeListValue=&#39;otherRestrictions&#39;]]/gmd:otherConstraints[gco:CharacterString or gmx:Anchor[not(starts-with(@xlink:href, &#39;http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess&#39;))]] |
| adms:representationTechnique | type de jeu de données | Informations relatives à la représentation spatiale du jeu de données | R | 1 | [skos:Concept](http://inspire.ec.europa.eu/metadata-codelist/SpatialRepresentationType) | //\*/gmd:identificationInfo/\*/gmd:spatialRepresentationType |

**Tableau 3 : classe dcat :Dataset instanciée dans une instance de la classe dcat :Catalog**

| Instanciation de dcat :Dataset dans une autre instance toute autre classe que dcat :CatalogAutre instanciation |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| dct:title | titre | Ttitre du jeu de données considéré | M | 1 | multilingue | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:title/\* |
| dct:description | description | Ddescription du jeu de données considéré | O | 1 | multilingue | //\*/gmd:identificationInfo/\*/gmd:abstract/\* |
| dcat:contactPoint | point de contact | Iinformations relatives aux modalités de prise de contact à propos du jeu de données | O | 0-n | vcard:OrganizationKind | //\*/gmd:contact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;pointOfContact&#39;]] |
| dcat:distribution | distribution | Iinformations relatives aux modalités d&#39;acquisition du catalogue  | W | 0 | dcat:Distribution |   |
| dcat:keyword | mot-clé | Mmot-clé libre décrivant le jeu de données considéré | W | 0-n | multilingue |   |
| dcat:theme | vocabulaire contrôlé | Mot- clé issu d&#39;un thésaurus décrivant le jeu de données | W | 1-n | [skos:Concept](http://publications.europa.eu/resource/authority/data-theme) |   |
| dct:subject | catégorie ISO | Iinformations relatives à la catégorie [ISO 19115] du jeu de données considéré | W | 0-n | [skos:Concept](http://inspire.ec.europa.eu/metadata-codelist/TopicCategory) |   |
| dct:spatial | couverture spatiale | Iinformations relatives à la région géographique visée par le jeu de données concerné | W | 0-n | [dct:Location](http://publications.europa.eu/resource/authority/country) |   |
| dct:temporal | couverture temporelle | Iinformations relatives au(x) laps de temps couvert(s) par le jeu de données concerné | W | 0-n | dctdct:PeriodOfTime |   |
| dct:created | date de création | Ddate de création du jeu de données considéré | W | 0-1 | date (YYYY-MM-DD) |   |
| dct:modified | date de mise à jour | Ddate de dernière modification du jeu de données | W | 0-1 | date (YYYY-MM-DD) |   |
| dct:issued | date de première publication | Ddate de première publication du jeu de données | W | 0-1 | date (YYYY-MM-DD) |   |
| foaf:page | page des métadonnées | iInformations relatives au(x) lien(s) détaillant le contenu du jeu de données | R | 0-1 | URL multilingue | //\*/gmd:distributionInfo/gmd:MD\_Distribution/gmd:transferOptions/gmd:MD\_DigitalTransferOptions/gmd:onLine/gmd:CI\_OnlineResource[gmd:protocol/\*={WWW:LINK-1.0-http--link} and gmd:function/\*/@codeListValue={&#39;information&#39;}]/gmd:linkage/gmd:name |
| dct:accrualPeriodicity | fréquence de mise à jour | iInformations relatives à la fréquence de mise à jour du jeu de données concerné | W | 0-1 | [dct:Frequency](http://inspire.ec.europa.eu/metadata-codelist/MaintenanceFrequency) |   |
| dct:identifier | identifiant | Iidentifiant alphanumérique unique du jeu de données concerné | M | 1 | multilingue | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:identifier/\*/gmd:code/\* |
| dcat:landingPage | page d&#39;acceuil | Iinformations relative(s) à la fiche de métadonnées HTML originale décrivant le jeu de données concerné | R | 0-1 | URL multilingue | [https://www.geo.be/catalog/details/ + //\*/gmd:fileIdentifier](https://www.geo.be/catalog/details/%20+%20/*/gmd:fileIdentifier) |
| dct:language | langue | Iinformations relatives au(x) langue(s) du jeu de données considéré | W | 0-4 | [codedValue](http://publications.europa.eu/resource/authority/language) skos :Concept |   |
| dct:provenance | origine | Iinformations relatives à l&#39;origine du jeu de données considéré | W | 0-1 | dct:ProvenanceStatement |   |
| dct:conformsTo | spécification ou règle de structuration | Iinformations relative(s) aux normes de qualité du jeu de données | W | 0-n | [dct:Standard](http://www.opengis.net/def/crs/EPSG/0/) |   |
| dct:source | jeu de données source | Iinformations relatives à un jeu de données source | W | 0 | dcat:Dataset |   |
| dcat:spatialResolutionInMeters | résolution spatiale | Iinformations relatives à la résolution spatiale du jeu de données considéré | W | 0-1 | xsd:decimal |   |
| dqv:hasQualityMeasurement | résolution spatiale | Iinformations relatives à la résolution spatiale du jeu de données considéré | W | 0-1 | dqv:QualityMeasurement |   |
| dct:accessRights | accessibilité | Iinformations relatives aux restrictions concernant l&#39;utilisation du jeu de données | W | 1 | [dct:RightsStatement](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess) |   |
| adms:sample | exemple de distribution | Rréférence à un exemple de distribution du jeu de données | W | 0 | dcat:Distribution |   |
| dct:publisher | publieur | Iinformations relatives à l&#39;organisation responsable de la disponibilité du jeu de données | W | 0-n | foaf:Organization |   |
| geodcat:custodian | mainteneur | Iinformations relatives à l&#39;organisation responsable de la données et de la maintenance de la ressource | W | 0-n | foaf:Organization |   |
| dct:creator | créateur | Iinformations relatives à l&#39;organisation responsable de la production du jeu de données considéré | W | 0-n | foaf:Organization |   |
| geodcat:distributor | diffuseur | Iinformations relatives à l&#39;organisation responsable de la distribution de la ressource | W | 0-n | foaf:Organization |   |
| geodcat:originator | auteur | Iinformations relatives à l&#39;organisation responsable de la création de la ressource | W | 0-n | foaf:Organization |   |
| geodcat:principalInvestigator | collecteur | Iinformations relatives à l&#39;organisation responsable de la collecte d&#39;information de recherche | W | 0-n | foaf:Organization |   |
| geodcat:processor | processeur | Iinformations relatives à l&#39;organisation ayant modifié la ressource après traitement des données | W | 0-n | foaf:Organization |   |
| geodcat:resourceProvider | fournisseur | Iinformations relatives à l&#39;organisation qui fournit la ressource | W | 0-n | foaf:Organization |   |
| geodcat:user | utilisateur | Iinformations relatives à l&#39;organisation qui utilise la ressource | W | 0-n | foaf:Organization |   |
| dct:rightsHolder | ayant droits | Oorganisation déteneur de droits sur le service | W | 0-1 | foaf:Organization |   |
| dct:license | conditions d&#39;utilisation | Informations relatives aux conditions d&#39;utilisation particulières de cette distribution | W | 1 | dct:LicenseDocument |   |
| adms:representationTechnique | type de jeu de données | Informations relatives à la représentation spatiale du jeu de données | W | 0 | [skos:Concept](http://inspire.ec.europa.eu/metadata-codelist/SpatialRepresentationType) |   |

**Tableau 4 : classe dcat :Dataset instanciée dans une instance toute autre classe que dcat :Catalog**

## C.dcat :DataService

| Instanciation de dcat :Dataservice dans une instance de dcat :CatalogInstanciation : Catalog |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| dct:title | titre | Titre du service renseigné | M | 1 | multilingue | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:title/\* |
| dct:description | description | Description du service renseigné | M | 1 | multilingue | //\*/gmd:identificationInfo/\*/gmd:abstract/\* |
| dcat:endpointURL | URL du service | URL du service considéré | MR | 0-n | URL | A voir |
| dcat:servesDataset | jeu de données accessible | Identification du ou des jeux de données accessibles via le service considéré | R | 0-n | dcat:Dataset | si dataservice généré à partir d&#39;une fiche [ISO 19139] --\&gt; utiliser la liste des identifiants de datasets présents le getcapabilties
 si dataservice généré par wizard : générer par sélection manuelle dans un champ ad hoc des datasets déjà documentés |
| dct:accessRights | restriction d&#39;accès | Informations relatives aux restrictions concernant l&#39;utilisation du service considéré | M | 1 | [dct:RightsStatement](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess) | //\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD\_LegalConstraints[gmd:accessConstraints/gmd:MD\_RestrictionCode[@codeListValue=&#39;otherRestrictions&#39;]]/gmd:otherConstraints[gmx:Anchor[starts-with(@xlink:href, &#39;http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess&#39;)]] |
| dcat:keyword | mot-clé | Mot-clé libre décrivant le service considéré | R | 0-n | multilingue | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD\_Keywords[not(./gmd:thesaurusName)]/gmd:keyword/\* |
| dcat:theme | mot-clé issu d&#39;un vocabulaire contrôlé | Mot clé issu d&#39;un thésaurus décrivant le service | R | 0-n | [skos:Concept](http://inspire.ec.europa.eu/theme) | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD\_Keywords[gmd:thesaurusName/gmd:CI\_Citation/gmd:title/\*={}]/gmd:keyword/\* |
| dct:created | date de création | Date de création du service considéré | R | 0-1 | date (YYYY-MM-DD) | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:date/gmd:CI\_Date[gmd:dateType/gmd:CI\_DateTypeCode[@codeListValue=&#39;creation&#39;]]/gmd:date |
| dct:modified | date de mise à jour | Date de dernière modification du service | R | 0-1 | date (YYYY-MM-DD) | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:date/gmd:CI\_Date[gmd:dateType/gmd:CI\_DateTypeCode[@codeListValue=&#39;revision&#39;]]/gmd:date |
| dct:issued | date de première publication | Date de première publication du service | O | 0-1 | date (YYYY-MM-DD) | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:date/gmd:CI\_Date[gmd:dateType/gmd:CI\_DateTypeCode[@codeListValue=&#39;publication&#39;]]/gmd:date |
| dct:conformsTo | spécification ou règle de structuration | Informations relative(s) aux normes de qualité du jeu de donnéesInformations relatives aux systèmes de référence spatiaux ou temporels | O | 0-n | [dct:Standard](http://www.opengis.net/def/crs/EPSG/0/) | //\*/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_DomainConsistency/gmd:result/gmd:DQ\_ConformanceResult/gmd:specification/gmd:CI\_Citation |
| dct:type | type de service | Informations relatives au type de service | R | 1 | skos:Concept | //\*/gmd:identificationInfo/\*/srv:serviceType |
| geodcat:distributor | diffuseur | Informations relatives à l&#39;organisation responsable de la distribution de la ressource | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;publisher&#39;]] |
| geodcat:originator | auteur | Informations relatives à l&#39;organisation responsable de la création de la ressource | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;custodian&#39;]] |
| geodcat:principalInvestigator | collecteur | Informations relatives à l&#39;organisation responsable de la collecte d&#39;information de recherche | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;author&#39;]] |
| geodcat:processor | processeur | Iinformations relatives à l&#39;organisation ayant modifié la ressource après traitement des données | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;distributor&#39;]] |
| geodcat:resourceProvider | fournisseur | Iinformations relatives à l&#39;organisation qui fournit la ressource | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;originator&#39;]] |
| geodcat:user | utilisateur | Iinformations relatives à l&#39;organisation qui utilise la ressource | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;principalInvestigator&#39;]] |
| dct:creator | créateur | Informations relatives à l&#39;organisation responsable de la production du service considéré | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;processor&#39;]] |
| geodcat:custodian | mainteneur | Informations relatives à l&#39;organisation responsable de la données et de la maintenance de la ressource | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;resourceProvider&#39;]] |
| dct:rightsHolder | ayant droits | Oorganisation déteneur de droits sur le service | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;user&#39;]] |
| dct:license | conditions d&#39;utilisation | Informations relatives aux conditions d&#39;utilisation particulières de cette distribution | M | 1 | dct:LicenseDocument | //\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD\_LegalConstraints[\*/gmd:MD\_RestrictionCode[@codeListValue=&#39;otherRestrictions&#39;]]/gmd:otherConstraints[gco:CharacterString or gmx:Anchor[not(starts-with(@xlink:href, &#39;http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess&#39;))]] |
| dct:conformsTo | système de projection géographique | Informations relatives aux systèmes de référence spatiaux ou temporels | R | 0-n | [codedValue](https://inspire.ec.europa.eu/metadata-codelist/ProtocolValue) | //\*/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_DomainConsistency/gmd:result/gmd:DQ\_ConformanceResult/gmd:specification/gmd:CI\_Citation |

**Tableau 5 : classe dcat :DataService instanciée dans une instance de la classe dcat :Catalog**

| Instanciation de dcat :DataService dans une autre instance toute autre classe que dcat :CatalogAutre instanciation |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| dct:title | titre | Titre du service renseigné | M | 1 | multilingue | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:title/\* |
| dct:description | description | Description du service renseigné | M | 1 | multilingue | //\*/gmd:identificationInfo/\*/gmd:abstract/\* |
| dcat:endpointURL | URL du service | URL du service considéré | MR | 0-n | URL | A voir |
| dcat:servesDataset | jeu de données accessible | Identification du ou des jeux de données accessibles via le service considéré | R | 0-n | dcat:Dataset | si dataservice généré à partir d&#39;une fiche [ISO 19139] --\&gt; utiliser la liste des identifiants de datasets présents le getcapabilties
 si dataservice généré par wizard : générer par sélection manuelle dans un champ ad hoc des datasets déjà documentés |
| dct:accessRights | restriction d&#39;accès | Informations relatives aux restrictions concernant l&#39;utilisation du service considéré | M | 1 | [dct:RightsStatement](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess) | //\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD\_LegalConstraints[gmd:accessConstraints/gmd:MD\_RestrictionCode[@codeListValue=&#39;otherRestrictions&#39;]]/gmd:otherConstraints[gmx:Anchor[starts-with(@xlink:href, &#39;http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess&#39;)]] |
| dcat:keyword | mot-clé | Mot-clé libre décrivant le service considéré | R | 0-n | multilingue | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD\_Keywords[not(./gmd:thesaurusName)]/gmd:keyword/\* |
| dcat:theme | mot-clé issu d&#39;un vocabulaire contrôlé | Mot clé issu d&#39;un thésaurus décrivant le service | R | 0-n | [skos:Concept](http://inspire.ec.europa.eu/theme) | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD\_Keywords[gmd:thesaurusName/gmd:CI\_Citation/gmd:title/\*={}]/gmd:keyword/\* |
| dct:created | date de création | Date de création du service considéré | R | 0-1 | date (YYYY-MM-DD) | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:date/gmd:CI\_Date[gmd:dateType/gmd:CI\_DateTypeCode[@codeListValue=&#39;creation&#39;]]/gmd:date |
| dct:modified | date de mise à jour | Date de dernière modification du service | R | 0-1 | date (YYYY-MM-DD) | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:date/gmd:CI\_Date[gmd:dateType/gmd:CI\_DateTypeCode[@codeListValue=&#39;revision&#39;]]/gmd:date |
| dct:issued | date de première publication | Date de première publication du service | O | 0-1 | date (YYYY-MM-DD) | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI\_Citation/gmd:date/gmd:CI\_Date[gmd:dateType/gmd:CI\_DateTypeCode[@codeListValue=&#39;publication&#39;]]/gmd:date |
| dct:conformsTo | spécification ou règle de structuration | Informations relatives aux systèmes de référence spatiaux ou temporels | O | 0-n | [dct:Standard](http://www.opengis.net/def/crs/EPSG/0/) | //\*/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_DomainConsistency/gmd:result/gmd:DQ\_ConformanceResult/gmd:specification/gmd:CI\_Citation |
| dct:type | type de service | Informations relatives au type de service | R | 1 | skos:Concept | //\*/gmd:identificationInfo/\*/srv:serviceType |
| geodcat:distributor | diffuseur | Informations relatives à l&#39;organisation responsable de la distribution de la ressource | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;publisher&#39;]] |
| geodcat:originator | auteur | Informations relatives à l&#39;organisation responsable de la création de la ressource | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;custodian&#39;]] |
| geodcat:principalInvestigator | collecteur | Informations relatives à l&#39;organisation responsable de la collecte d&#39;information de recherche | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;author&#39;]] |
| geodcat:processor | processeur | informations relatives à l&#39;organisation ayant modifié la ressource après traitement des données | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;distributor&#39;]] |
| geodcat:resourceProvider | fournisseur | Iinformations relatives à l&#39;organisation qui fournit la ressource | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;originator&#39;]] |
| geodcat:user | utilisateur | Iinformations relatives à l&#39;organisation qui utilise la ressource | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;principalInvestigator&#39;]] |
| dct:creator | créateur | Informations relatives à l&#39;organisation responsable de la production du service considéré | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;processor&#39;]] |
| geodcat:custodian | mainteneur | Informations relatives à l&#39;organisation responsable de la données et de la maintenance de la ressource | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;resourceProvider&#39;]] |
| dct:rightsHolder | ayant droits | Oorganisation déteneur de droits sur le service | O | 0-1 | foaf:Organization | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI\_ResponsibleParty[gmd:role/gmd:CI\_RoleCode[@codeListValue=&#39;user&#39;]] |
| dct:license | conditions d&#39;utilisation | Informations relatives aux conditions d&#39;utilisation particulières de cette distribution | M | 1 | dct:LicenseDocument | //\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD\_LegalConstraints[\*/gmd:MD\_RestrictionCode[@codeListValue=&#39;otherRestrictions&#39;]]/gmd:otherConstraints[gco:CharacterString or gmx:Anchor[not(starts-with(@xlink:href, &#39;http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess&#39;))]] |
| dct:conformsTo | système de projection géographique | Informations relatives aux systèmes de référence spatiaux ou temporels | R | 0-n | [codedValue](https://inspire.ec.europa.eu/metadata-codelist/ProtocolValue) | //\*/gmd:dataQualityInfo/gmd:DQ\_DataQuality/gmd:report/gmd:DQ\_DomainConsistency/gmd:result/gmd:DQ\_ConformanceResult/gmd:specification/gmd:CI\_Citation |

Tableau 6 : classe dcat :DataService instanciée dans une instance de toute autre classe que dcat :Catalog

## D.

## E.

## F.dcat :Distribution

| Toute instanciation de dcat :DistributionInstanciation : Dataset |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| dct :title | titre | Titre de la distribution concernée | O | 0-1 | multilingue | //atom :feed/atom :title |
| dcat :accessURL | URL d&#39;&#39;accès | Adresse web de la distribution concernée du jeu de données | M | 1 | URL | //atom:feed/atom:entry/atom:id |
| dct :description | description | Description des particularités de cette description | O | 0-1 | multilingue | //atom:feed/atom:entry/atom:id |
| dct :format | format | Informations relatives au format particulier de cette distribution | M | 1 | [dct :MediaTypeOrExtent](http://publications.europa.eu/resource/authority/file-type) | //atom :feed/atom :entry/atom :link/@type |
| dcat :mediaType | type de format | Type de format/support de la distribution (IANA) | O | 0-1 | [dct :MediaType](http://www.iana.org/assignments/media-types) | //atom :feed/atom :entry/atom :link/@type |
| dcat :downloadURL | URL de téléchargement | Adresse web pour télécharger directement la distribution concernée | O | 0-1 | URL | //atom:feed/atom:entry/atom:id |
| dcat :compressFormat | format comprimé | Informations relatives au format comprimé particulier de cette distribution (IANA) | O | 0-1 | dct :MediaType | //atom :feed/atom :entry/atom :link/@type |
| dct :conformsTo | système de projection géographique | Informations relatives à la projection particulière de cette distribution | O | 0-1 | [dct :Standard](http://www.opengis.net/def/crs/EPSG/0/) | //atom:feed/atom:entry/atom:category |
| dcat :byteSize | taille | Taille de la distribution en bytes | O | 0-1 | xsd :decimal | pas de XPATH spécifié |
| adms :status | statut | Informations relatives à la maturité de la distribution | O | 1 | [skos :Concept](http://purl.org/adms/status/) | pas de XPATH spécifié |
| dct :spatial | couverture spatiale | Informations relatives à la région géographique couverte par la distribution concernée | O | 0-1 | dct :Location | //atom:feed/atom:entry/georss:box |
| dcterms :temporal | couverture temporelle | Informations relatives à l&#39;&#39;intervalle temporelle couvert par la distribution concernée | R | 0-1 | dcterms:PeriodOfTime | //atom:feed/atom:entry/atom:link/@time |
| dct:type | type de distribution | Lien vers un type de distribution | O | 0-n | skos:Concept URL |   |

**Tableau 7 : classe dcat :Distribution instanciée dans une instance de la classe dcat :Dataset**

## G.

|
## H.Instanciation : Catalog
 |
| --- |
|
## I.URI
 |
## J.Nom
 |
## K.Description
 |
## L.Exigence
 |
## M.Cardinalité
 |
## N.Domaine
 |
## O.Source
 |
|
## P.dct:title
 |
## Q.titre
 |
## R.Titre de la distribution concernée
 |
## S.O
 |
## T.0-1
 |
## U.multilingue
 |
## V.//atom:feed/atom:title
 |
|
## W.dcat:accessURL
 |
## X.URL d&#39;accès
 |
## Y.Adresse web de la distribution concernée du jeu de données
 |
## Z.M
 |
## AA.1
 |
## BB.URL
 |
## CC.//atom:feed/atom:entry/atom:id
 |
|
## DD.dct:description
 |
## EE.description
 |
## FF.Description des particularités de cette distribution
 |
## GG.O
 |
## HH.0-1
 |
## II.multilingue
 |
## JJ.//atom:feed/atom:entry/atom:id
 |
|
## KK.dct:format
 |
## LL.format
 |
## MM.Informations relatives au format particulier de cette distribution
 |
## NN.M
 |
## OO.1
 |
## PP.dct:MediaTypeOrExtent
 |
## QQ.//atom:feed/atom:entry/atom:link/@type
 |
|
## RR.dcat:mediaType
 |
## SS.type de format
 |
## TT.Type de format/support de la distribution (IANA)
 |
## UU.O
 |
## VV.0-1
 |
## WW.dct:MediaType
 |
## XX.//atom:feed/atom:entry/atom:link/@type
 |
|
## YY.dcat:downloadURL
 |
## ZZ.URL de téléchargement
 |
## AAA.Adresse web pour télécharger directement la distribution concernée
 |
## BBB.O
 |
## CCC.0-1
 |
## DDD.URL
 |
## EEE.//atom:feed/atom:entry/atom:id
 |
|
## FFF.dcat:compressFormat
 |
## GGG.format comprimé
 |
## HHH.Informations relatives au format comprimé particulier de cette distribution (IANA)
 |
## III.O
 |
## JJJ.0-1
 |
## KKK.dct:MediaType
 |
## LLL.//atom:feed/atom:entry/atom:link/@type
 |
|
## MMM.dct:conformsTo
 |
## NNN.système de projection géographique
 |
## OOO.Informations relatives à la projection particulière de cette distribution
 |
## PPP.W
 |
## QQQ.0
 |
## RRR.dct:Standard
 |
## SSS.//atom:feed/atom:entry/atom:category
 |
|
## TTT.dcat:byteSize
 |
## UUU.taille
 |
## VVV.taille de la distribution en bytes
 |
## WWW.O
 |
## XXX.0-1
 |
## YYY.xsd:decimal
 |
## ZZZ.pas de XPATH spécifié
 |
|
## AAAA.adms:status
 |
## BBBB.statut
 |
## CCCC.information relative à la maturité de la distribution: Completed, Deprecated, Under Development, Withdrawn
 |
## DDDD.W
 |
## EEEE.0
 |
## FFFF.skos:Concept
 |
## GGGG.pas de XPATH spécifié
 |
|
## HHHH.dct:spatial
 |
## IIII.couverture spatiale
 |
## JJJJ.Informations relatives à la région géographique couverte par la distribution concernée
 |
## KKKK.W
 |
## LLLL.0
 |
## MMMM.dct:Location
 |
## NNNN.//atom:feed/atom:entry/georss:box
 |
|
## OOOO.dcterms:temporal
 |
## PPPP.couverture temporelle
 |
## QQQQ.Informations relatives à l&#39;intervalle temporelle couvert par la distribution concernée
 |
## RRRR.O
 |
## SSSS.1
 |
## TTTT.dcterms:PeriodOfTime
 |
## UUUU.//atom:feed/atom:entry/atom:link/@time
 |
|
## VVVV.dct:type
 |
## WWWW.type de distribution
 |
## XXXX.Lien vers un type de distribution (visualisation; ex table, graphique qui représente les données)
 |
## YYYY.O
 |
## ZZZZ.0-n
 |
## AAAAA.rdfs:Resourceskos:Concept
 |
## BBBBB.pas de XPATH spécifié
 |

## CCCCC.Tableau 8 : classe dcat :Distribution instanciée dans une instance de la classe dcat :Catalog

## DDDDD.foaf :Organization

| Instanciation de foaf :Organization dans une instance de toute classe |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| foaf:name | nom | Nom de l&#39;organisation | M | 1-n | Multilingue | ./gmd:organisationName |
| dct:type | type | Indique le type d&#39;organisation | O | 0-1 | [skos:Concept](http://purl.org/adms/publishertype/) | pas de XPATH spécifié |
| foaf:mbox | adresse mail | adresse mail de l&#39;organisation (en utilisant URI mailto:) | RO | 0-1 |

Unilingue | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address/gmd:electronicMailAddress |
| foaf:workplaceHomepage | Site web | Site web de l&#39;organisation | R | 0-1 | Unilingue | ./gmd:contactInfo/gmd:CI\_Contact/gmd:onlineResource/gmd:CI\_OnlineResource/gmd:linkage |
| locn:address | Adresse postale | Adresse postale de l&#39;organisation | O | 0-1 | locn:Address | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address |

**Tableau 98 : classe foaf :Organization instanciée dans une instance de toute classe**

## EEEEE.dcat :CatalogRecord

| Iinstanciation de dcat :CatalogRecord dans une instance de dcat :Catalog |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| --- | --- | --- | --- | --- | --- | --- |
| foaf:primaryTopic | instance à laquelle la fiche se rapporte | Information relative au jeu de données, service ou catalogue | M | 1 | dcat:Dataset | dcat:Dataservice | dcat:Catalog | génération a posteriori en intégrant tous les ID de toutes instanciations primaires (i.e. les instances qui ne correspondent à la valeur d&#39;un attribut de la même classe) |
| --- | --- | --- | --- | --- | --- | --- |
| dct:modified | date de mise à jour | Ddate de dernière mise à jour du Catalog Record | M | 1 | date (YYYY-MM-DD) | //\* /gmd:dateStamp/\* |
| dct:language | langue | Informations relatives au(x) langue(s) utilisés dans les metadonnées du jeu de données | M | 1-n | skos :Concept[codedValue](http://publications.europa.eu/resource/authority/language) | //\*/gmd:locale/gmd:PT\_Locale/gmd:languageCode/gmd:LanguageCode[@codeListValue={}] |
| --- | --- | --- | --- | --- | --- | --- |
| dcat:contactPoint | Point de contact | Informations relatives aux modalités de prise de contact à propos du service | M | 1 | vcard:OrganizationKind | //\*/gmd:contact/gmd:CI\_ResponsibleParty |
| --- | --- | --- | --- | --- | --- | --- |
| dct:identifier | identifiant | Identifiant alphanumérique unique du catalogrecord concerné | M | 1 | unilingue | //\*/gmd:fileIdentifier |
| --- | --- | --- | --- | --- | --- | --- |

**Tableau 108 : classe dcat :CatalogRecord instanciée dans une instance de la classe dcat :Catalog**

## FFFFF.locn :Address

| Instanciation de locn :Address dans une instance de toute classe |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| locn:thoroughfare | Adresse postale | Rue et numéro de police | M | 1 | multilingue | . /gmd:deliveryPoint |
| locn:postName | Commune | Nom de la commune | M | 1 | multilingue | . /gmd:city |
| locn:postCode | Code postal | Code postal de l&#39;adresse | M | 1 | unilingue | ./gmd:postalCode |
| locn:adminUnitL1 | Pays | Pays | M | 1 | multilingue | ./gmd:country |

**Tableau 11 : classe locn :Address instanciée dans une instance de toute classe**

## GGGGG.skos :Concept

| Instanciation de skos :Concept dans une instance de toute classe |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| skos:prefLabel | Nom du concept | Nom du concept | M | 1 | multilingue | ./ gmd:keyword |
| rdf:type | Type de concept | Type de concept | O | 0-1 | unilingue | néant |
| skos:inScheme | Thésaurus d&#39;origine | Thésaurus dont est issu le concept | R | 0-1 | URL | . /gmd:thesaurusName/gmd:CI\_Citation/gmd:title |

**Tableau 12 : classe skos:Concept instanciée une instance de toute classe**

## HHHHH.dct :periodOfTime

## IIIII.

| Instanciation de dct :PperiodOfTime dans une instance de toute classe |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| dcat:startDate | Date de début | Date de début de la période temporelle | M | 1 | unilingue | ./gmd:EX\_TemporalExtent/gmd :extent/gml32:TimePeriod/gml32:beginPosition |
| dcat:endDate | Date de fin | Date de fin de la période temporelle | M | 1 | unilingue | ./gmd:EX\_TemporalExtent/gmd :extent/gml32:TimePeriod/gml32:endPosition |

**Tableau 13 : classe dct:PeriodOfTime instanciée une instance de toute classe**

## JJJJJ.dqv : QualityMeasurement QualityMeasurement

| Instanciation de dqv : QualityMeasurement QualityMeasurement – ressource vectorielledans une instance de toute classe |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| dqv:isMeasurementOf | Grandeur scalaire mesurée | Grandeur scalaire mesurée | O | 0-1 | multilingue | Valeur hardcodée en fonction du type de jeu de données |
| sdmx-attribut:unitMeasure | Unité de mesure des grandeurs scalaires | Unité de mesure des grandeurs scalaires | RW | 1 | skos:Concept | ./gmd :MD\_Resolution./gmd:distance/gco:Distance/@uom |
| dqv:value | Valeur de la mesure de la grandeur scalaire | Valeur de la mesure de la grandeur scalaire | MW\* | 0-1 | unilingue | ./gmd :MD\_Resolution /gmd:distance/gco:Distance |
| geodcat:spatialResolutionAsScale | Échelle conceptuelle de la ressource | Échelle conceptuelle de la ressource | M\*\* | 0-1 | unilingue | ./gmd :MD\_Resolution/gmd:equivalentScale/ gmd:MD\_RepresentativeFraction/ gmd:denominator/gco:Integer |

**Tableau 14 : classe dqv: QualityMeasurement QualityMeasurement instanciée dans une instance de dcat :Dataset. M\* : obligatoire si raster ; M\*\* : obligatoire si vecteur.se rapportant à la description d&#39;une ressource vectorielle**

**dqv : QualityMeasurement**

| Instanciation de dqv : QualityMeasurement – ressource matricielle |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| dqv:isMeasurementOf | Grandeur scalaire mesurée | Grandeur scalaire mesurée | O | 0-1 | multilingue | Valeur hardcodée en fonction du type de jeu de données |
| sdmx-attribut:unitMeasure | Unité de mesure des grandeurs scalaires | Unité de mesure des grandeurs scalaires | R | 1 | skos:Concept | ./gmd :MD\_Resolution/gmd:distance/gco:Distance/@uom |
| dqv:value | Valeur de la mesure de la grandeur scalaire | Valeur de la mesure de la grandeur scalaire | M | 1 | unilingue | ./gmd :MD\_Resolution /gmd:distance/gco:Distance |
| geodcat:spatialResolutionAsScale | Échelle conceptuelle de la ressource | Échelle conceptuelle de la ressource | W | 1 | unilingue | ./gmd :MD\_Resolution/gmd:equivalentScale/ gmd:MD\_RepresentativeFraction/ gmd:denominator/gco:Integer |

**Tableau 15 : classe dqv: QualityMeasurement se rapportant à la description d&#39;une ressource matricielle**

## KKKKK.

## LLLLL.dct :Location

| Instanciation de dct :Location dans une instance de toute classe |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| locn:geometry | géométrie | Coordonnées de la géométrie de la ressource | M | 1 | Unilingue |
 |
| dcat:bbox | Rectangle de délimitationgéographique | Coordonnées de la géométrie de la ressource | M | 1 | Unilingue |
 |
| Skos :prefLabel | Nom de l&#39;entité géographique | Nom de l&#39;entité géographique | R | 0-1 | multilingue |
 |
| dct:identifier | Identifiant de l&#39;entité géographique | Identifiant de l&#39;entité géographique | R | 0-1 | codedValue |
 |

Tableau 15 : classe dct :Location instanciée dans une instance de toute classe

## MMMMM.skos :ConceptScheme

| Instanciation de skos :ConceptScheme dans une instance de dcat :Catalog |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| dct:title | Titre du thésaurus | Titre du thésaurus | M | 1 | multilingue | Génération sur base des URL fournies dans les propriétés skos:inScheme des instances de la classe skos :Concept (il faut donc la propriété inScheme et que celle-ci soit pourvue d&#39;une URL machine-readable) |
| dct:issued | Date de première publication | Date de première publication | O | 0-1 | date |
|
 |
 |
 |
 |
 |
 |
| Dct:identifier | Identifiant du thésaurus | Identifiant du thésaurus | M | 1 | URL |

Tableau 16 : classe skos:ConceptScheme instanciée dans une instance de dcat :Catalog

## NNNNN.vcard :Organization

| Instanciation de vcard :Organization dans une instance de toute classe |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| vcard:organization-name | nom | Nom de l&#39;organisation | M | 1-n | Multilingue | ./gmd:organisationName |
| vcard:hasEmail | adresse mail | Adresse mail de l&#39;organisation (en utilisant URI mailto:) | R | 0-1 |

Unilingue | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address/gmd:electronicMailAddress |
| vcard:hasURL | Site web | Site web de l&#39;organisation | R | 0-1 | Unilingue | ./gmd:contactInfo/gmd:CI\_Contact/gmd:onlineResource/gmd:CI\_OnlineResource/gmd:linkage |
| vcard:hasAddress | Adresse postale | Adresse postale de l&#39;organisation | O | 0-1 | vcard:Address | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address |

Tableau 9 : classe vcard :Organization instanciée une instance de toute classe

## OOOOO.vcard :Address

| Instanciation de vcard :Address dans une instance de vcard :Organization |
| --- |
| URI | Nom | Description | Exigence | Cardinalité | Domaine | Source |
| vcard:street-address | Adresse postale | Rue et numéro de police | M | 1 | multilingue | . /gmd:deliveryPoint |
| Vcard :locality | Commune | Nom de la commune | M | 1 | multilingue | . /gmd:city |
| vcard:postal-code | Code postal | Code postal de l&#39;adresse | M | 1 | unilingue | ./gmd:postalCode |
| vcard:country-name | Pays | Pays | M | 1 | multilingue | ./gmd:country |

Tableau 11 : classe vcard:Address instanciée une instance de vcard :Organization

# Annexe II

| classe concernée | attribut concerné | thésaurus proposés | Exigence |
| --- | --- | --- | --- |
| catalogue | dcat:theme | [http://inspire.ec.europa.eu/theme](http://inspire.ec.europa.eu/theme) | O |
| catalogue | dcat:theme | [http://publications.europa.eu/resource/authority/data-theme](http://publications.europa.eu/resource/authority/data-theme) | M |
| catalogue | dct:language | [http://publications.europa.eu/resource/authority/language](http://publications.europa.eu/resource/authority/language) | M |
| catalogue | dct:spatial | [http://publications.europa.eu/resource/authority/place](http://publications.europa.eu/resource/authority/place) | R |
| dataset | dcat:theme | [http://publications.europa.eu/resource/authority/data-theme](http://publications.europa.eu/resource/authority/data-theme) | M |
| dataset | dcat:theme | [http://inspire.ec.europa.eu/theme](http://inspire.ec.europa.eu/theme) | R |
| dataset | dcat:theme | [http://inspire.ec.europa.eu/featureconcept](http://inspire.ec.europa.eu/featureconcept) | O |
| dataset | dcat:theme | [https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurovoc](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurovoc) | O |
| dataset | dct:subject | http://inspire.ec.europa.eu/metadata-codelist/TopicCategory | O |
| dataset | dct:accrualPeriodicity | http://publications.europa.eu/resource/authority/frequency | M |
| dataset | dct:accrualPeriodicity | http://inspire.ec.europa.eu/metadata-codelist/MaintenanceFrequency | R |
| dataset | dct:language | [http://publications.europa.eu/resource/authority/language](http://publications.europa.eu/resource/authority/language) | M |
| dataset | dct:accessRights | [http://publications.europa.eu/resource/authority/access-right](http://publications.europa.eu/resource/authority/access-right) | R |
| dataset | dct:accessRights | [http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess](https://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess) | R |
| dataset | dct:license | https://creativecommons.org/licenses/ | R |
| dataset | adms:representationTechnique | [http://inspire.ec.europa.eu/metadata-codelist/SpatialRepresentationType](http://inspire.ec.europa.eu/metadata-codelist/SpatialRepresentationType) | R |
| dataservice | dct:accessRights | [http://publications.europa.eu/resource/authority/access-right](http://publications.europa.eu/resource/authority/access-right) | R |
| dataservice | dct:accessRights | [http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess](https://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess) | R |
| dataservice | dct:type | https://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceType | R |
| dataservice | dct:type | https://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceCategory | R |
| dataservice | dcat:theme | [http://publications.europa.eu/resource/authority/data-theme](http://publications.europa.eu/resource/authority/data-theme) | M |
| dataservice | dcat:theme | [http://inspire.ec.europa.eu/theme](http://inspire.ec.europa.eu/theme) | R |
| dataservice | dcat:theme | [http://inspire.ec.europa.eu/featureconcept](http://inspire.ec.europa.eu/featureconcept) | O |
| dataservice | dcat:theme | [https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurovoc](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurovoc) | O |
| dataservice | dct:license | https://creativecommons.org/licenses/ | R |
| dataservice | dct:conformsTo | http://www.opengis.net/def/crs/EPSG/0/ | M |
| Distribution | dct:format | http://publications.europa.eu/resource/authority/file-type | R |
| Distribution | dcat:mediaType | [http://www.iana.org/assignments/media-types](http://www.iana.org/assignments/media-types) | R |
| Distribution | dct:conformsTo | http://www.opengis.net/def/crs/EPSG/0/ | M |
| Distribution | adms:status | [http://inspire.ec.europa.eu/metadata-codelist/SpatialRepresentationType](http://inspire.ec.europa.eu/metadata-codelist/SpatialRepresentationType) | R |
| Distribution | dct:type | http://publications.europa.eu/resource/authority/distribution-type | O |
| Distribution | dcat:compressFormat | [http://www.iana.org/assignments/media-types](http://www.iana.org/assignments/media-types) | O |
| foaf:organization | dct:type | http://publications.europa.eu/resource/authority/corporate-body | O |
| catalogrecord | dct:language | [http://publications.europa.eu/resource/authority/language](http://publications.europa.eu/resource/authority/language) | M |
| qualitymeasurement | sdmx-attribut:unitMeasure | http://www.qudt.org/vocab/unit/ | M |
| location | dct:identifier | http://publications.europa.eu/resource/authority/country | M |
| location | dct:identifier | belgif UA + thésuarus du cadastre en devenir | O |

Liste : thésaurus.

[1](#sdfootnote1anc) Les niveaux applicables sont obligatoire (M), recommandé (R), optionnel (O) et interdit (W). Ce dernier cas de figure n&#39;est applicable que pour les attributs des classes dcat :Catalog et dcat :Dataset qui s&#39;instancient dans la même classe, pour éviter des instanciations en cascade.

[2](#sdfootnote2anc) ou éventuellement hardcodé

11
