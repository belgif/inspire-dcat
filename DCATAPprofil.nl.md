**Inhoudstafel**

- [Federaal profiel DCAT AP](#federaal-profiel-dcat-ap)
  - [Inleiding](#inleiding)
  - [I. Algemene voorstelling van de klassen](#i-algemene-voorstelling-van-de-klassen)
  - [II. Gedetailleerde voorstelling van de klassen](#ii-gedetailleerde-voorstelling-van-de-klassen)
    - [A. Klasse dcat: Catalog](#a-klasse-dcat-catalog)
      - [Profiel van de klasse](#profiel-van-de-klasse)
      - [Instantiëring vertrekkend van [INSPIRE] elementen](#instantiëring-vertrekkend-van-inspire-elementen)
      - [Instantiëring zonder [INSPIRE] element](#instantiëring-zonder-inspire-element)
    - [B. Klasse dcat: Dataset](#b-klasse-dcat-dataset)
      - [Profiel van de klasse](#profiel-van-de-klasse-1)
      - [Instantiëring vertrekkend van [INSPIRE] elementen](#instantiëring-vertrekkend-van-inspire-elementen-1)
      - [Instantiëring zonder [INSPIRE] element](#instantiëring-zonder-inspire-element-1)
    - [Klasse dcat: DataService](#klasse-dcat-dataservice)
      - [Profiel van de klasse](#profiel-van-de-klasse-2)
      - [Omzetting vanuit [INSPIRE] elementen](#omzetting-vanuit-inspire-elementen)
      - [Instantiëring zonder [INSPIRE] element](#instantiëring-zonder-inspire-element-2)
    - [Klasse dcat:Distribution](#klasse-dcatdistribution)
      - [Profiel van de klasse](#profiel-van-de-klasse-3)
      - [Omzetting vanuit [INSPIRE] elementen](#omzetting-vanuit-inspire-elementen-1)
      - [Instantiëring zonder [INSPIRE] element](#instantiëring-zonder-inspire-element-3)
    - [Klasse foaf: Organization](#klasse-foaf-organization)
      - [Omzetting vanuit [INSPIRE] elementen](#omzetting-vanuit-inspire-elementen-2)
      - [Instantiëring zonder [INSPIRE] element](#instantiëring-zonder-inspire-element-4)
    - [Klasse catalogRecord](#klasse-catalogrecord)
      - [Opmerkingen over de attributen van de klasse](#opmerkingen-over-de-attributen-van-de-klasse)
      - [Opmerkingen over de inhoud van de klasse](#opmerkingen-over-de-inhoud-van-de-klasse)
    - [Klasse locn:Address](#klasse-locnaddress)
      - [Profiel van de klasse](#profiel-van-de-klasse-4)
        - [Omzetting vanuit [INSPIRE] elementen](#omzetting-vanuit-inspire-elementen-3)
        - [Instantiëring zonder [INSPIRE] element](#instantiëring-zonder-inspire-element-5)
    - [Klasse skos: Concept](#klasse-skos-concept)
      - [Omzetting vanuit [INSPIRE] elementen](#omzetting-vanuit-inspire-elementen-4)
      - [Instantiëring zonder [INSPIRE] element](#instantiëring-zonder-inspire-element-6)
    - [Klasse dct: PeriodOfTime](#klasse-dct-periodoftime)
      - [Profiel van de klasse](#profiel-van-de-klasse-5)
      - [Omzetting vanuit [INSPIRE] elementen](#omzetting-vanuit-inspire-elementen-5)
      - [Instantiëring zonder [INSPIRE] element](#instantiëring-zonder-inspire-element-7)
    - [Klasse dqv: QualityMeasurement](#klasse-dqv-qualitymeasurement)
      - [Profiel van de klasse](#profiel-van-de-klasse-6)
      - [Omzetting vanuit [INSPIRE] elementen](#omzetting-vanuit-inspire-elementen-6)
      - [Instantiëring zonder [INSPIRE] element](#instantiëring-zonder-inspire-element-8)
    - [Klasse dct: Location](#klasse-dct-location)
      - [Profiel van de klasse](#profiel-van-de-klasse-7)
      - [Omzetting vanuit [INSPIRE] elementen](#omzetting-vanuit-inspire-elementen-7)
      - [Instantiëring zonder [INSPIRE] element](#instantiëring-zonder-inspire-element-9)
    - [Klasse ConceptScheme](#klasse-conceptscheme)
      - [Profiel van de klasse](#profiel-van-de-klasse-8)
      - [Omzetting vanuit [INSPIRE] elementen](#omzetting-vanuit-inspire-elementen-8)
      - [Instantiëring zonder [INSPIRE] element](#instantiëring-zonder-inspire-element-10)
    - [Klasse vcard Organization](#klasse-vcard-organization)
      - [Omzetting vanuit [INSPIRE] elementen](#omzetting-vanuit-inspire-elementen-9)
      - [Instantiëring zonder [INSPIRE] element](#instantiëring-zonder-inspire-element-11)
    - [Klasse vcard:Address](#klasse-vcardaddress)
      - [Profiel van de klasse](#profiel-van-de-klasse-9)
      - [Omzetting vanuit [INSPIRE] elementen](#omzetting-vanuit-inspire-elementen-10)
      - [Instantiëring zonder [INSPIRE] element](#instantiëring-zonder-inspire-element-12)
  - [Normen waarnaar verwezen wordt](#normen-waarnaar-verwezen-wordt)
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
    - [Instantiëring van dqv: QualityMeasurement – vectoriële dataset](#instantiëring-van-dqv-qualitymeasurement--vectoriële-dataset)
    - [Instantiëring van dqv:QualityMeasurement – matriciële dataset](#instantiëring-van-dqvqualitymeasurement--matriciële-dataset)
  - [K. dct:Location](#k-dctlocation)
  - [L. skos:ConceptScheme](#l-skosconceptscheme)
  - [M. vcard:Organization](#m-vcardorganization)
  - [N. vcard:Address](#n-vcardaddress)
  - [O. dct:LicenseDocument](#o-dctlicensedocument)
  - [P. rdf:Description](#p-rdfdescription)
- [Annexe II](#annexe-ii)


# Federaal profiel DCAT AP
## Inleiding

Dit document stelt het [DCAT AP 2 fédéral](#DCATAP2fédéral) in dat werd uitgewerkt door de federale administraties die betrokken zijn bij de implementatie van de INSPIRE-richtlijn overeenkomstig [DCAT AP 2](#DCATAP2). Dit profiel voldoet aan de norm [DCAT AP 2](#DCATAP2). Enerzijds specificeert en beperkt het deze norm door de regels te preciseren voor de concretisering van zijn klassen. Anderzijds geeft het regels over de inhoud van de klassen en hun respectieve attributen.

[DCAT AP 2 fédéral](#DCATAP2fédéral) heeft immers als eerste doel de semantische rijkdom te integreren van de metadata-elementen afkomstig van de [TG 2.0](#TG2), alsook de semantische opportuniteiten te exploiteren die worden geboden door de [TG met betrekking tot de downloaddiensten](#TGrelativesauxservicesdetéléchargement). 

Bijgevolg beperkt [federaal DCAT AP 2](#DCATAP2fédéral) de kardinaliteit van bepaalde attributen, voegt het er andere toe die vreemd zijn aan [DCAT AP 2](#DCATAP2) zodat het deze attributen linkt aan metadata-elementen afkomstig van de [TG 2.0](#TG2). Op dezelfde manier legt [federaal DCAT AP 2](#DCATAP2fédéral) normen vast voor zijn attributen om er, als het nodig is, de inhoud van de elementen afkomstig van de [TG 2.0](#TG2) in te integreren.

## I. Algemene voorstelling van de klassen

[Federaal DCAT AP 2](#DCATAP2fédéral) omvat alle klassen en alle attributen die vereist zijn door [DCAT AP 2](#DCATAP2). Bovendien werden als aanvulling en zonder dat dit een verplichting is de attributen die eigen zijn aan [GEO DCAT AP 2](#GEODCATAP2) en aan [STAT DCAT AP 1](#STATDCATAP1) geïntegreerd voor zover ze beantwoordden aan de behoeften die werden uitgedrukt door de federale administraties. Het omvat alle klassen die hieronder vermeld staan. De in het vet vermelde klassen zijn verplicht in elke catalogus die conform [federaal DCAT AP 2](#DCATAP2fédéral) is:

- **dcat:Catalog** die de catalogi vermeldt en beschrijft;
- **dcat:Dataset** die de datasets vermeldt en beschrijft;
- dcat:Dataservice die diensten (of toepassingen of API's) vermeldt en beschrijft die toegang
geven tot een of meer datasets;
- **foaf:Organization** die organisaties vermeldt en beschrijft;
- dcat:Distribution die toegankelijke bestanden van een dataset vermeldt en beschrijft;
- dcat:CatalogRecord die een willekeurig element van de catalogus vermeldt en beschrijft (een
dataset, een service of een catalogus);
- locn:Address die de postadressen van een foaf-agent vermeldt en beschrijft;
- skos:Concept die concepten vermeldt en beschrijft;
- dct:PeriodOfTime die tijdsperiodes vermeldt en beschrijft;
- dqv:QualityMeasurement die de ruimtelijke resolutie van resources vermeldt en beschrijft;
- dct:Location die geografische zones vermeldt en beschrijft;
- skos:ConceptScheme die thesaurussen vermeldt en beschrijft;
- vcard:Organization die organisaties vermeldt;
- vcard:Address die postadressen vermeldt en beschrijft.
Het diagram hieronder toont de klassen en attributen die eigen zijn aan [federaal DCAT AP 2](#DCATAP2fédéral).

![DCATAPfederal](https://user-images.githubusercontent.com/87412262/180747799-287ac27e-a6eb-4766-87fc-4c402d8a81a1.png)


Punt II en de tabellen in bijlage die erbij horen, preciseren de attributen eigen aan elke klasse en daarnaast de regels die van toepassing zijn op de inhoud van de attributen van elke klasse, evenals meer bepaald het te gebruiken element van de [ISO 19139](#ISO19139) fiche in geval van omzetting. In alle tabellen van bijlage I staan voor elk attribuut de volgende elementen:

1. URI: dit element komt overeen met de unieke identifier van het betrokken attribuut;
2. Naam: dit element komt overeen met de naam van het betrokken attribuut;
3. Beschrijving: dit element komt overeen met de beschrijving van het betrokken attribuut;
4. Vereiste: dit element komt overeen met een van de vier vereist niveaus[^1] eigen aan het betrokken attribuut;
5. Kardinaliteit: dit element komt overeen met het minimaal en het maximaal aantal toegelaten attributen van dit type;
6. Type: dit element komt overeen met de aanvaardbare waarden die het betrokken attribuut kan aannemen. Als de aanvaardbare waarden opgenomen zijn in een of meer beperkt(e) geheel/gehelen (namelijk een thesaurus), dan is/zijn het/de optionele, aanbevolen en verplichte geheel/gehelen opgenomen in bijlage II;
7. Bron: dit element komt overeen met de XPATH van het element dat verplicht moet worden gebruikt als waarde van het betrokken attribuut als de klasse waartoe het behoort wordt gelinkt aan een [ISO 19115](#ISO19115) klasse en als zijn domein overeenstemt met een eentalige waarde, een meertalige waarde of een URL. Indien zijn domein overeenkomt met een andere klasse van het huidige profiel, komt de bron overeen met de [ISO 19115](#ISO19115) klasse die is gelinkt aan de klasse van het huidige profiel.

De "meertalige "domeinattributen moeten worden ingevuld in het Duits, Nederlands, Frans en Engels. In de mate van het mogelijke moeten de domeinattributen "meertalige URL" worden ingevuld in het Duits, Nederlands, Frans en Engels.

[^1]: De toepasselijke niveaus zijn verplicht (M), aanbevolen (R), optioneel (O) en verboden (W). Dat laatste geval is alleen van toepassing voor de attributen van de klassen dcat:Catalog en dcat:Dataset die zich in dezelfde klasse instantiëren, om instantiëringen in cascade te vermijden.

## II. Gedetailleerde voorstelling van de klassen

### A. Klasse dcat: Catalog

De klasse dcat:Catalog komt overeen met een catalogus, d.w.z. een welbepaald geheel van een of meerdere datasets en eventueel van diensten die op een coherente manier geïdentificeerd en gedocumenteerd zijn.

Overeenkomstig die specificaties kan de klasse zich enerzijds instantiëren in het root-element en anderzijds in de attributen dct:hasPart, dct:isPartOf en dcat:catalog. De instantie van de klasse dcat:Catalog die aanwezig is in het root-element komt overeen met de betrokken DCAT-catalogus. Deze instantie is **verplicht** en **uniek**.

De instantie(s) van de klasse dcat:Catalog die aanwezig is/zijn in de drie bovenvermelde attributen, komen overeen met catalogi die op de ene of andere manier geassocieerd kunnen worden met de catalogus waarin ze zich instantiëren. Deze instanties zijn **optioneel** en **potentieel meervoudig**.

#### Profiel van de klasse
Het huidige profiel voorziet in verschillende specificaties naar gelang van het attribuut waarbinnen de klasse zich instantieert. Die vloeien in hoofdzaak voort uit de noodzaak om een oneindige sequentie van instantiëringen van de klasse te voorkomen en uit de finaliteiten die eigen zijn aan ieder type instantiëring. De eerste instantiëring is immers bedoeld om de betrokken catalogus te identificeren en uitvoerig te beschrijven, terwijl de daarop volgende uitsluitend bedoeld zijn om de betrokken catalogus te identificeren.

De attributen eigen aan de instantie die aanwezig is in het root-element, worden gespecificeerd in tabel 1 in bijlage. De attributen eigen aan de andere instanties, worden gespecificeerd in tabel 2 in bijlage.
De specificaties die van toepassing zijn op de klasse, ongeacht de plaats waar zij zich instantieert, voorzien in de mogelijkheid om de modaliteiten te expliciteren voor de verwerving van de catalogus die beschreven wordt met het attribuut dcat:Distribution. Het gaat om een toevoeging ten opzichte van de norm [DCAT AP 2](#DCATAP2).

#### Instantiëring vertrekkend van [INSPIRE] elementen

Alleen de inhoud van fiches [ISO 19139](#ISO19139) die een [CSW](#CSW) beschrijven, kan omgezet worden in instanties van de klasse dcat:Catalog. In een dergelijk geval bepalen die specificaties dat de inhoud van elk attribuut van de klasse dcat: Catalog aangereikt wordt vanaf het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 1.

De inhoud van de meertalige of eentalige attributen moet worden aangereikt vanuit de inhoud van het verbonden [ISO 19139](#ISO19139) element. De inhoud van de attributen waarvan het domein overeenkomt met een klasse, is gelijk aan één of meer instantiëringen van die klasse, conform de specificaties van het huidige profiel. Deze instantiëringen nemen de inhoud van het gekoppelde [ISO 19139](#ISO19139) element over.

Bij wijze van afwijking worden bepaalde attributen niet gekoppeld met [ISO 19139](#ISO19139) elementen. In dat geval gelden de volgende regels:

1. De inhoud van het attribuut foaf:homepage moet verwijzen naar een human readable versie van de catalogus;
2. De inhoud van het attribuut dcat:themeTaxonomy moet a posteriori gegenereerd worden, zodra alle attributen van alle klassen ingevuld zijn, zodat men alle thesaurussen opneemt die effectief in de betrokken catalogus worden gebruikt;
3. De inhoud van het attribuut dct:identifier moet nog worden bepaald. Hij zou kunnen overeenkomen met de XML-serialisatie URL van de betrokken catalogus;
4. De inhoud van het attribuut dcat:dataset wordt gegenereerd vanuit alle fiches die via de [CSW](#CSW) toegankelijke datasets, reeksen of statische kaarten beschrijven;
5. De inhoud van het attribuut dcat:service wordt gegenereerd vanuit alle fiches die services of via de [CSW](#CSW) toegankelijke applicaties beschrijven.

#### Instantiëring zonder [INSPIRE] element
Als de instantie van de klasse dcat: Catalog niet wordt gekoppeld aan een fiche [ISO 19139](#ISO19139) die een [CSW](#CSW) beschrijft, dan bepalen deze specificaties toch dat in de inhoud van de meertalige of eentalige domeinattributen wordt voorzien volgens de terminologische en syntactische regels van het [federaal metadataprofiel](#profildemétadonnéesfédéral) die van toepassing zijn op het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 2.

Deze specificaties bepalen eveneens dat de inhoud van de attributen waarvan het domein overeenkomt met een klasse, gelijk is aan een of meer instantiëringen van die klasse, conform de specificaties van het huidige profiel.
Bij wijze van afwijking worden bepaalde attributen niet gekoppeld met [ISO 19139](#ISO19139) elementen of klassen. In dat geval gelden de volgende regels:

1. De inhoud van het attribuut foaf:homepage moet verwijzen naar een human readable versie van de catalogus;
2. De inhoud van het attribuut dcat:themeTaxonomy moet a posteriori gegenereerd worden, zodra alle attributen van alle klassen ingevuld zijn, zodat men alle thesaurussen opneemt die effectief in de betrokken catalogus worden gebruikt;
3. De inhoud van het attribuut dct:identifier moet nog worden bepaald. Hij zou kunnen overeenkomen met de XML-serialisatie URL van de betrokken catalogus.
4. De inhoud van het attribuut dcat:dataset wordt gegenereerd vanuit datasets die daadwerkelijk geïntegreerd zijn vanuit de catalogus;
5. De inhoud van het attribuut dcat:dataset wordt gegenereerd vanuit services die daadwerkelijk geïntegreerd zijn vanuit de catalogus.

### B. Klasse dcat: Dataset
De klasse dcat:Dataset komt overeen met de beschrijving van een dataset, d.w.z. een geheel van gegevens dat is geïdentificeerd en wordt onderhouden door een organisatie en toegankelijk is in een of meer weergaven.
Conform deze specificaties kan de klasse zich instantiëren in de attributen dcat:dataset, dct:source, dcat:servesDataset en foaf:isPrimaryTopicOf. De instantie(s) van de klasse dcat:Dataset die aanwezig is/zijn in het attribuut dcat:dataset, komt/komen overeen met de beschrijvingen van de datasets waarnaar verwezen wordt in de catalogus. Deze instanties zijn **verplicht** en **potentieel meervoudig**.

De instantie(s) van de klasse dcat:Dataset die aanwezig zijn in het attribuut dct:source, komen overeen met de dataset aan de basis van de beschreven dataset. Deze instanties zijn **aanbevolen** en **potentieel meervoudig**.

De instantie(s) van de klasse dcat:Dataset die aanwezig zijn in het attribuut dcat:servesDataset, komen overeen met de datasets die toegankelijk zijn via de beschreven service. Deze instanties zijn **aanbevolen** en **potentieel meervoudig**.

De instanties van de klasse dcat:Dataset die aanwezig zijn in het attribuut foaf:isPrimaryTopic komen overeen met hun identificatie. Deze instanties zijn **verplicht** en **potentieel meervoudig** zodra de klasse dcat:CatalogRecord geïnstantieerd is.

#### Profiel van de klasse
Het huidige profiel voorziet in verschillende specificaties naar gelang van het attribuut waarbinnen de klasse zich instantieert. Die vloeien in hoofdzaak voort uit de noodzaak om een oneindige sequentie van instantiëringen van de klasse te voorkomen en uit de finaliteiten die eigen zijn aan ieder type instantiëring. De eerste instantiëring is immers bedoeld om de betrokken dataset te identificeren en uitvoerig te beschrijven, terwijl de daarop volgende uitsluitend bedoeld zijn om de betrokken dataset te identificeren.
De attributen eigen aan de instanties die aanwezig zijn in het attribuut dcat:dataset, worden gespecificeerd in tabel 3 in bijlage. 

De attributen eigen aan de andere instanties, worden gespecificeerd in tabel 4 in bijlage.
De specificaties die op de klasse van toepassing zijn, bepalen dat de versies van eenzelfde dataset overeenkomen met evenveel verschillende instanties van de klasse dcat:Distribution. Bijgevolg bepalen ze niet de bij de versie behorende attributen die worden voorgesteld door [DCAT AP 2.0](#DCATAP2).

De specificaties die op de klasse van toepassing zijn, omvatten ook de attributen dct:license en adms:representationTechnique, want volgens de [TG 2.0](#TG2) en [ISO 19115](#ISO19115) kenmerken ze datasets en niet een welbepaalde verdeling van een dataset.
De specificaties die op de klasse van toepassing zijn, bepalen dat de instanties die aanwezig zijn in het attribuut dcat:dataset ten minste één naar behoren voorzien attribuut moeten hebben van de hierna volgende (dct:created, dct:modified of dct:issued). De specificaties die op de klasse van toepassing zijn, bepalen dat de instanties die aanwezig zijn in het attribuut dcat:dataset ten minste één naar behoren voorzien attribuut moeten hebben van de hierna volgende (dct:publisher, geodcat:custodian, dct:creator, geodcat:distributor, geodcat: originator, geodcat:principalInvestigator, geodcat:processor, geodcat:resourceProvider, geodcat:user of dct:rightsHolder).

#### Instantiëring vertrekkend van [INSPIRE] elementen
Alleen de inhoud van de [ISO 19139](#ISO19139) fiches die een dataset, een reeks of een statische kaart beschrijven, kan omgezet worden in instanties van de klasse dcat:Dataset. In een dergelijk geval bepalen die specificaties dat de inhoud van elk attribuut van de klasse dcat: Dataset aangereikt wordt vanaf het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 3.
De inhoud van de meertalige of eentalige attributen moet worden aangereikt vanuit de inhoud van het verbonden [ISO 19139](#ISO19139) element. De inhoud van de attributen waarvan het domein overeenkomt met een klasse, is gelijk aan één of meer instantiëringen van die klasse, conform de specificaties van het huidige profiel. Deze instantiëringen nemen de inhoud van het gekoppelde [ISO 19139](#ISO19139) element over.

#### Instantiëring zonder [INSPIRE] element
Als de instantie van de klasse dcat: Dataset niet wordt gekoppeld aan een fiche [ISO 19139](#ISO19139) die een dataset beschrijft, dan bepalen deze specificaties toch dat in de inhoud van de meertalige of eentalige domeinattributen wordt voorzien volgens de terminologische en syntactische regels van het [federaal metadataprofiel](#profildemétadonnéesfédéral) die van toepassing zijn op het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 4.

Deze specificaties bepalen eveneens dat de inhoud van de attributen waarvan het domein overeenkomt met een klasse, gelijk is aan een of meer instantiëringen van die klasse, conform de specificaties van het huidige profiel.

### Klasse dcat: DataService
De klasse dcat: DataService komt overeen met de beschrijving van een dataservice, d.w.z. een webservice, een applicatie of een API die werd geïdentificeerd en wordt onderhouden door een organisatie en die toegang geeft tot een of meer geïdentificeerde datasets.
Conform deze specificaties kan de klasse zich instantiëren in de attributen dcat:service en foaf:isPrimaryTopicOf. De instantie(s) van de klasse dcat:DataService die aanwezig is/zijn in het attribuut dcat:service, komt/komen overeen met de beschrijvingen van de service(s) waarnaar verwezen wordt in de catalogus. Deze instanties zijn **aanbevolen** en **potentieel meervoudig**.
De instanties van de klasse dcat:DataService die aanwezig zijn in het attribuut foaf:isPrimaryTopic komen overeen met hun identificatie. Deze instanties zijn **verplicht** en **potentieel meervoudig** zodra de klasse dcat:CatalogRecord geïnstantieerd is.
#### Profiel van de klasse
Het huidige profiel voorziet in verschillende specificaties naar gelang van het attribuut waarbinnen de klasse zich instantieert. Ze vloeien hoofdzakelijk voort uit de finaliteiten die eigen zijn aan elk type instantiëring. De eerste instantiëring is immers bedoeld om de betrokken service te identificeren en uitvoerig te beschrijven, terwijl de daarop volgende uitsluitend bedoeld zijn om de betrokken service te identificeren.
De attributen eigen aan de andere instanties die aanwezig zijn in het attribuut dcat:service, worden gespecificeerd in tabel 5 in bijlage. De attributen eigen aan de andere instanties, worden gespecificeerd in tabel 6 in bijlage.
De specificaties die op de klasse van toepassing zijn, omvatten ook de attributen dct:license en dct:comformsTo, want volgens de [TG 2.0](#TG2) en [ISO 19115](#ISO19115) kenmerken ze services.
De specificaties die op de klasse van toepassing zijn, bepalen dat de instanties die aanwezig zijn in het attribuut dcat:service ten minste één naar behoren voorzien attribuut moeten hebben van de hierna volgende (dct:created, dct:modified of dct:issued).
De specificaties die op de klasse van toepassing zijn, bepalen dat de instanties die aanwezig zijn in het attribuut dcat:service ten minste één naar behoren voorzien attribuut moeten hebben van de hierna volgende (dct:publisher, geodcat:custodian, dct:creator, geodcat:distributor, geodcat: originator, geodcat:principalInvestigator, geodcat:processor, geodcat:resourceProvider, geodcat:user of dct:rightsHolder).

#### Omzetting vanuit [INSPIRE] elementen
Alleen de inhoud van de [ISO 19139](#ISO19139) fiches die een visualiseringsservice, een downloadservice of een applicatie beschrijven, kan worden omgezet in instanties van de klasse dcat:DataService. In een dergelijk geval bepalen die specificaties dat de inhoud van elk attribuut van de klasse dcat: DataService aangereikt wordt vanaf het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 5. De inhoud van fiches die een ontdekkingsservice beschrijven kan niet worden omgezet in instanties van de klasse cat: DataService.
De inhoud van de meertalige of eentalige attributen moet worden aangereikt vanuit de inhoud van het verbonden [ISO 19139](#ISO19139) element. De inhoud van de attributen waarvan het domein overeenkomt met een klasse, is gelijk aan één of meer instantiëringen van die klasse, conform de specificaties van het huidige profiel. Deze instantiëringen nemen de inhoud van het gekoppelde [ISO 19139](#ISO19139) element over.
Bovendien voorzien de specificaties van [federaal DCAT AP 2] voor elke dataset die toegankelijk is via de beschreven services, in een instantiëring van de klasse dcat:Dataset in de klasse dcat:Catalog. Het is immers noodzakelijk om in elke [DCAT AP] catalogus expliciet de datasets die toegankelijk zijn via de betrokken services te instantiëren met de klasse dcat:Dataset.
#### Instantiëring zonder [INSPIRE] element
Als de instantie van de klasse dcat: DataService niet wordt gekoppeld aan een [ISO 19139](#ISO19139) fiche die een in aanmerking komende service beschrijft, dan bepalen deze specificaties toch dat in de inhoud van de meertalige of eentalige domeinattributen wordt voorzien volgens de terminologische en syntactische regels van het [federaal metadataprofiel](#profildemétadonnéesfédéral) die van toepassing zijn op het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 6.
Deze specificaties bepalen eveneens dat de inhoud van de attributen waarvan het domein overeenkomt met een klasse, gelijk is aan een of meer instantiëringen van die klasse, conform de specificaties van het huidige profiel.

### Klasse dcat:Distribution

De klasse dcat: Distribution komt overeen met de beschrijving van een welbepaald digitaal bestand van een betrokken resource, d.w.z. een digitaal bestand in een welbepaald formaat.
Conform deze specificaties kan de klasse zich instantiëren in het attribuut dcat:distribution.

#### Profiel van de klasse

Het huidige profiel voorziet in specificaties die onafhankelijk zijn van het attribuut waarbinnen de klasse zich instantieert. De attributen eigen aan alle instanties van de klasse, worden gespecificeerd in tabel 7 in bijlage.
De specificaties die van toepassing zijn op de klasse, omvatten de attributen dct:temporal en dct: spatial om indien nodig de bestreken tijdspanne van het verdeelde bestand (m.a.w. de versie) en het geografisch beslag ervan te specificeren.

#### Omzetting vanuit [INSPIRE] elementen

Alleen de inhoud van de [ATOMFeed](#ATOMFeed) die de downloadlinks van een dataset beschrijven, kan worden omgezet in instanties van de klasse dcat:Distribution. In een dergelijk geval bepalen die specificaties dat de inhoud van elk attribuut van de klasse dcat: Distributie aangereikt wordt vanaf het [ATOMFeed](#ATOMFeed) element dat eraan gekoppeld is in tabel 7. De instanties van de klasse die aanwezig zijn in een instantie van dcat:Catalog, worden niet gegenereerd vanuit een [INSPIRE](#INSPIRE) element.
De inhoud van de meertalige of eentalige attributen moet worden aangereikt vanuit de inhoud van het verbonden [ATOMFeed](#ATOMFeed) element. De inhoud van de attributen waarvan het domein overeenkomt met een klasse, is gelijk aan één of meer instantiëringen van die klasse, conform de specificaties van het huidige profiel. Deze instantiëringen nemen de inhoud van het gekoppelde [ATOMFeed](#ATOMFeed) element over.

#### Instantiëring zonder [INSPIRE] element

Als de instantie van de klasse dcat: Catalog niet wordt gekoppeld aan een [ATOMFeed](#ATOMFeed), dan bepalen deze specificaties toch dat in de inhoud van de meertalige of eentalige domeinattributen wordt voorzien volgens de terminologische en syntactische regels van het [federaal metadataprofiel](#profildemétadonnéesfédéral) die van toepassing zijn op het element van de [ATOMFeed](#ATOMFeed) dat eraan gekoppeld is in tabel 7.
Deze specificaties bepalen eveneens dat de inhoud van de attributen waarvan het domein overeenkomt met een klasse, wordt aangereikt door middel van een of meer instantiëringen van die klasse, conform de specificaties van het huidige profiel.

### Klasse foaf: Organization
De klasse foaf:Organization komt overeen met de beschrijving van een organisatie, d.w.z. een gestructureerd geheel van personen met een of meer welbepaalde doelen Overeenkomstig deze specificaties kan de klasse zich instantiëren in de attributen dct:publisher, geodcat:custodian, dct:creator, geodcat:distributor, geodcat: originator, geodcat:principalInvestigator, geodcat:processor, geodcat:resourceProvider, geodcat:user of dct:rightsHolder.
Profiel van de klasse
Het huidige profiel voorziet in specificaties die onafhankelijk zijn van het attribuut waarbinnen de klasse zich instantieert. De attributen eigen aan alle instanties van de klasse, worden gespecificeerd in tabel 8 in bijlage.
#### Omzetting vanuit [INSPIRE] elementen
Alleen de inhoud van de instanties van de [ISO 19139](#ISO19139) klasse met betrekking tot organisaties kan worden omgezet in instanties van de klasse foaf:Organization. In een dergelijk geval bepalen die specificaties dat de inhoud van elk attribuut van de klasse foaf: Organization aangereikt wordt vanaf het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 8.
De inhoud van de meertalige of eentalige attributen moet worden aangereikt vanuit de inhoud van het verbonden [ISO 19139](#ISO19139) element. De inhoud van de attributen waarvan het domein overeenkomt met een klasse, is gelijk aan één of meer instantiëringen van die klasse, conform de specificaties van het huidige profiel. Deze instantiëringen nemen de inhoud van het gekoppelde [ISO 19139](#ISO19139) element over.
Bij wijze van afwijking worden bepaalde attributen niet gekoppeld met [ISO 19115](#ISO19115) elementen of klassen. In dat geval gelden de volgende regels:
a) De inhoud van het attribuut dct:type wordt aan geen enkel [ISO 19115](#ISO19115) element gekoppeld. Bijgevolg is hij niet aanwezig voor de instanties die aanwezig zijn in de klassen die overeenkomen met het resultaat van de omzetting van een [ISO 19139](#ISO19139) fiche.
####  Instantiëring zonder [INSPIRE] element
Als de instantie van de klasse foaf: Organization niet wordt gekoppeld aan een instantie van de [ISO 19139](#ISO19139) klasse betreffende een organisatie, dan bepalen deze specificaties toch dat in de inhoud van de meertalige of eentalige domeinattributen wordt voorzien volgens de terminologische en syntactische regels van het [federaal metadataprofiel](#profildemétadonnéesfédéral) die van toepassing zijn op het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 8.
Deze specificaties bepalen eveneens dat de inhoud van de attributen waarvan het domein overeenkomt met een klasse, wordt aangereikt door middel van een of meer instantiëringen van die klasse, conform de specificaties van het huidige profiel.

### Klasse catalogRecord
De klasse dcat:CatalogRecord komt overeen met de identificatie van de bijzondere instanties van de klassen dcat:Dataset, dcat:DataService (dcat:Catalog).
Conform deze specificaties kan de klasse zich instantiëren in de klasse dcat:Catalog. De instanties zijn **aanbevolen** en **potentieel meervoudig**.

#### Opmerkingen over de attributen van de klasse

Het doel van deze klasse is de betrokken klassen te identificeren en exhaustief te beschrijven. Bijgevolg worden de attributen van deze klasse gespecificeerd in de bijgevoegde tabel 9.

#### Opmerkingen over de inhoud van de klasse

Als een dcat: CatalogRecord klasse verwijst naar om het even welke klasse die niet gekoppeld is aan een [ISO 19139](#ISO19139) fiche, dan bepalen deze specificaties dat de inhoud van de attributen van de dcat: CatalogRecord klassen wordt ingevuld volgens de terminologische en syntactische regels van het [federaal metadataprofiel ] die van toepassing zijn op deze elementen.
Als een dcat: CatalogRecord klasse verwijst naar om het even welke klasse die gekoppeld is aan een [ISO 19139](#ISO19139) fiche, dan bepalen deze specificaties dat de inhoud van de attributen afkomstig moet zijn van de elementen van de [ISO 19139](#ISO19139) fiche waarnaar verwezen wordt in de kolom XPATH Source.
Bepaalde attributen worden niet gekoppeld aan de [ISO 19115](#ISO19115) elementen. In dat geval voorzien deze specificaties in alternatieven. Concreet zijn de volgende regels met betrekking tot de attributen van toepassing:
a) De inhoud van het attribuut foaf:primaryTopic moet a posteriori gegenereerd worden, zodra alle klassen geïnstantieerd zijn, zodat naar alle klassen verwezen wordt.

### Klasse locn:Address
De klasse locn:Address komt overeen met de beschrijving van het postadres van een foaf-agent.
Conform deze specificaties kan de klasse zich instantiëren in het attribuut dcat:address.
#### Profiel van de klasse
Het huidige profiel voorziet in specificaties die onafhankelijk zijn van het attribuut waarbinnen de klasse zich instantieert. De attributen eigen aan de instanties, worden gespecificeerd in tabel 9 in bijlage.
##### Omzetting vanuit [INSPIRE] elementen
Alleen de inhoud van de instanties van de [ISO 19115](#ISO19115) klasse met betrekking tot postadressen kan worden omgezet in instanties van de klasse locn:Address. In een dergelijk geval bepalen die specificaties dat de inhoud van elk attribuut van de klasse locn:Address aangereikt wordt vanaf het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 9.
##### Instantiëring zonder [INSPIRE] element
Als de instantie van de klasse locn: Address niet wordt gekoppeld aan een instantie van de [ISO 19139](#ISO19139) klasse betreffende een organisatie, dan bepalen deze specificaties toch dat in de inhoud van de meertalige of eentalige domeinattributen wordt voorzien volgens de terminologische en syntactische regels van het [federaal metadataprofiel](#profildemétadonnéesfédéral) die van toepassing zijn op het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 8.

###  Klasse skos: Concept
De klasse skos:Concept komt overeen met de beschrijving van een concept, d.w.z. een begrip dat op een ondubbelzinnige manier geïdentificeerd en in ten minste één taal benoemd wordt.
Overeenkomstig deze specificaties kan de klasse zich instantiëren in de attributen dcat:theme, dct:language, dct:subject, dct: adms:representationTechnique, dct:type, adms:status en sdmx-attribut:unitMeasure.
Profiel van de klasse
Het huidige profiel voorziet in specificaties die onafhankelijk zijn van het attribuut waarbinnen de klasse zich instantieert. De attributen eigen aan alle instanties van de klasse skos:Concept worden gespecificeerd in tabel 10 in bijlage.
#### Omzetting vanuit [INSPIRE] elementen
Alleen de inhoud van de [ISO 19139](#ISO19139) klasse betreffende trefwoorden afkomstig uit thesaurussen en naar behoren geïdentificeerd door een URI, kan rechtstreeks worden omgezet in instanties van de klasse skos: Concept.
In een dergelijk geval bepalen die specificaties dat de inhoud van elk attribuut van de klasse skos:Concept aangereikt wordt vanaf het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 10.
De inhoud van de instanties van de klassen [ISO 19139](#ISO19139) met betrekking tot talen, tot [ISO 19115](#ISO19115) thema's, tot het soort ruimtelijke weergave, tot de ruimtelijke resolutie van de matriciële resources en tot het servicetype, kan eveneens worden omgezet in instanties van de klasse skos:Concept.
In dat geval bepalen deze specificaties dat ieder attribuut van de klasse skos:Concept wordt aangereikt op basis van concepten afkomstig uit SKOS thesaurussen die semantisch identiek zijn aan de betrokken [ISO 19139](#ISO19139) elementen. Bijlage II stelt voor elke waarde van deze [ISO 19139](#ISO19139) elementen een identiek skos-concept voor.
#### Instantiëring zonder [INSPIRE] element
Als de instantie van de klasse skos:Concept niet wordt gekoppeld aan een [ISO 19139](#ISO19139) element, dan bepalen deze specificaties dat de inhoud van de attributen wordt aangereikt door concepten uit SKOS-thesaurussen. Bijlage II stelt voor elk attribuut waar zich de klasse skos:Concept kan instantiëren, een lijst van verplichte, aanbevolen of optionele thesaurussen voor.

### Klasse dct: PeriodOfTime
De klasse dct:PeriodOfTime komt overeen met de beschrijving van een sequentie in de tijd, d.w.z. een beperkt tijdsinterval.
Conform deze specificaties kan de klasse zich instantiëren in het attribuut dct:temporal.
#### Profiel van de klasse
Het huidige profiel voorziet in specificaties die onafhankelijk zijn van het attribuut waarbinnen de klasse zich instantieert. De attributen eigen aan alle instanties van de klasse dct: PeriodOfTime worden gespecificeerd in tabel 11 in bijlage.
#### Omzetting vanuit [INSPIRE] elementen
Alleen de inhoud van de instanties van de [ISO 19139](#ISO19139) klasse met betrekking tot sequenties in de tijd kan worden omgezet in instanties van de klasse dct: PeriodOfTime. In een dergelijk geval bepalen die specificaties dat elk attribuut van de klasse dct: PeriodOfTime aangereikt wordt vanaf het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 11.
#### Instantiëring zonder [INSPIRE] element
Als de instantie van de klasse dct: PeriodOfTime niet wordt gekoppeld aan een instantie van de [ISO 19139](#ISO19139) klasse betreffende een sequentie in de tijd, dan bepalen deze specificaties toch dat in de inhoud van de meertalige of eentalige domeinattributen wordt voorzien volgens de terminologische en syntactische regels van het [federaal metadataprofiel](#profildemétadonnéesfédéral) die van toepassing zijn op het element [ISO 19139](#ISO19139) dat eraan gekoppeld is in tabel 11.

### Klasse dqv: QualityMeasurement
De klasse dqv: QualityMeasurement komt overeen met de ruimtelijke resolutie van de betrokken resource, d.w.z. met het detailniveau van de resource.
Conform deze specificaties kan de klasse zich instantiëren in het attribuut dqv:hasQualityMeasurement en dcat:spatialResolutionInMeters. In beide gevallen is de instantie aanbevolen en uniek.
#### Profiel van de klasse
Het huidige profiel voorziet in verschillende specificaties naar gelang van de plaats waar de klasse zich instantieert. Deze vloeien in hoofdzaak voort uit de noodzaak om de ruimtelijke resolutie te beschrijven aan de hand van begrippen die aan het resourcetype aangepast zijn.
De attributen eigen aan de instanties betreffende de vectoriële resources worden gespecificeerd in tabel 12 in bijlage. De attributen eigen aan alle instanties betreffende de vectoriële resources worden gespecificeerd in tabel 13 in bijlage.
#### Omzetting vanuit [INSPIRE] elementen
Alleen de inhoud van de instanties van de [ISO 19139](#ISO19139) klasse met betrekking tot de ruimtelijke resolutie kan worden omgezet in instanties van de klasse dqv: QualityMeasurement. In een dergelijk geval bepalen die specificaties dat elk attribuut aangereikt wordt vanaf het [ISO 19139](#ISO19139) element dat eraan gekoppeld is de tabel in bijlage.
#### Instantiëring zonder [INSPIRE] element
Als de instantie van de klasse dqv: QualityMeasurement niet wordt gekoppeld aan een instantie van het [ISO 19139](#ISO19139) element betreffende de ruimtelijke resolutie, dan bepalen deze specificaties toch dat in de inhoud van de meertalige of eentalige domeinattributen wordt voorzien volgens de terminologische en syntactische regels van het[federaal metadataprofiel](#profildemétadonnéesfédéral) die van toepassing zijn op het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in de tabel in bijlage.

### Klasse dct: Location
De klasse dct: Location komt overeen met de beschrijving van een geografische zone, d.w.z. een begrensd gedeelte van het aardoppervlak.
Conform deze specificaties kan de klasse zich instantiëren in het attribuut dct:location.
####  Profiel van de klasse
Het huidige profiel voorziet in specificaties die onafhankelijk zijn van het attribuut waarbinnen de klasse zich instantieert. De attributen eigen aan alle instanties van de klasse dct:location worden gespecificeerd in tabel 14 in bijlage.
Bij ontstentenis van werkelijk gemeenschappelijke standaarden omvatten de op de klasse toepasselijke specificaties de attributen locn:geometry en dcat:bbox. De inhoud van deze twee attributen moet strikt identiek zijn en verwijzen naar de beschrijving van de grondoppervlakte die de resource inneemt in een specifiek formaat. Beide attributen moeten vier keer worden genoteerd, zodat de ingenomen grondoppervlakte volgens de volgende formaten wordt gespecificeerd:

- [Well Know Text ](http://www.opengis.net/ont/geosparql#wktLiteral);
- [Geographic Markup Language ](http://www.opengis.net/ont/geosparql#gmlLiteral);
- GeoJSON aan de hand van:
  - De [identifier IANA](https://www.iana.org/assignments/media-types/application/vnd.geo+json) ;
  - De [identifier opengis](http://www.opengis.net/ont/geosparql#geoJSONLiteral).

####  Omzetting vanuit [INSPIRE] elementen
Alleen de inhoud van de instanties van de [ISO 19139](#ISO19139) klasse met betrekking tot de ruimtelijke resolutie kan worden omgezet in instanties van de klasse dct:Location. In een dergelijk geval bepalen die specificaties dat elk attribuut aangereikt wordt vanaf het [ISO 19139](#ISO19139) element dat eraan gekoppeld is de tabel in bijlage.
####  Instantiëring zonder [INSPIRE] element
Als de instantie van de klasse dct:Location niet wordt gekoppeld aan een instantie van de [ISO 19139](#ISO19139) klasse betreffende een organisatie, dan bepalen deze specificaties toch dat in de inhoud van de meertalige of eentalige domeinattributen wordt voorzien volgens de terminologische en syntactische regels van het [federaal metadataprofiel](#profildemétadonnéesfédéral) die van toepassing zijn op het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 14.

### Klasse ConceptScheme
De klasse skos:ConceptScheme komt overeen met de beschrijving van een thesaurus, d.w.z. een gestructureerd geheel van gekoppelde concepten.
Conform deze specificaties kan de klasse zich instantiëren in het attribuut dcat:themeTaxonomy.
#### Profiel van de klasse
Het huidige profiel voorziet in specificaties die onafhankelijk zijn van het attribuut waarbinnen de klasse zich instantieert. De attributen eigen aan alle instanties van de klasse skos:ConceptScheme worden gespecificeerd in tabel 15 in bijlage.
#### Omzetting vanuit [INSPIRE] elementen
Geen enkele [ISO 19115](#ISO19115) klasse kan worden omgezet in een instantie van de klasse skos:ConceptScheme.
#### Instantiëring zonder [INSPIRE] element
Deze specificaties bepalen dat de klasse skos: ConceptScheme a posteriori wordt geïnstantieerd, wanneer alle andere klassen naar behoren geïnstantieerd zijn. Deze specificaties bepalen dat de klasse skos:ConceptScheme geïnstantieerd wordt op basis van de URL's die aanwezig zijn in de attributen skos:inScheme van de instanties van de klasse skos:Concept.

### Klasse vcard Organization
De klasse vcard:Organization komt overeen met de beschrijving van een organisatie, d.w.z. een gestructureerd geheel van personen met een of meer welbepaalde doelen
Conform deze specificaties kan de klasse zich instantiëren in de attributen dcat:contactPoint.
Profiel van de klasse
Het huidige profiel voorziet in specificaties die onafhankelijk zijn van het attribuut waarbinnen de klasse zich instantieert. De attributen eigen aan alle instanties van de klasse vcard: Organization, worden gespecificeerd in tabel 16 in bijlage.
#### Omzetting vanuit [INSPIRE] elementen
Alleen de inhoud van de instanties van de [ISO 19139](#ISO19139) klasse met betrekking tot organisaties kan worden omgezet in instanties van de klasse vcard:Organization. In een dergelijk geval bepalen die specificaties dat elk attribuut van de klasse vcard: Organization aangereikt wordt vanaf het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 16.
Deze specificaties bepalen eveneens dat de attributen waarvan het domein overeenkomt met een klasse, worden aangereikt door middel van een of meer instantiëringen van die klasse, conform de specificaties van het huidige profiel.
#### Instantiëring zonder [INSPIRE] element
Als de instantie van de klasse vcard: Organization niet wordt gekoppeld aan een instantie van de [ISO 19139](#ISO19139) klasse betreffende een organisatie, dan bepalen deze specificaties toch dat in de inhoud van de meertalige of eentalige domeinattributen wordt voorzien volgens de terminologische en syntactische regels van het [federaal metadataprofiel](#profildemétadonnéesfédéral) die van toepassing zijn op het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in de tabel in bijlage.

Deze specificaties bepalen eveneens dat de inhoud van de attributen waarvan het domein overeenkomt met een klasse, wordt aangereikt door middel van een of meer instantiëringen van die klasse, conform de specificaties van het huidige profiel.

### Klasse vcard:Address
De klasse vcard:Address komt overeen met de beschrijving van een postadres van een vcard-agent.
Conform deze specificaties kan de klasse zich instantiëren in de klasse vcard:Organization.
#### Profiel van de klasse
Het huidige profiel voorziet in specificaties die onafhankelijk zijn van het attribuut waarbinnen de klasse zich instantieert. De attributen eigen aan alle instanties van de klasse vcard:Address worden gespecificeerd in tabel 17 in bijlage.
#### Omzetting vanuit [INSPIRE] elementen
Alleen de inhoud van de instanties van de [ISO 19139](#ISO19139) klasse met betrekking tot postadressen kan worden omgezet in instanties van de klasse vcard:Address. In een dergelijk geval bepalen die specificaties dat elk attribuut van de klasse vcard:Address aangereikt wordt vanaf het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 17.
#### Instantiëring zonder [INSPIRE] element
Als de instantie van de klasse vcard: Address niet wordt gekoppeld aan een instantie van de [ISO 19139](#ISO19139) klasse betreffende een organisatie, dan bepalen deze specificaties toch dat in de inhoud van de meertalige of eentalige domeinattributen wordt voorzien volgens de terminologische en syntactische regels van het [federaal metadataprofiel](#profildemétadonnéesfédéral) die van toepassing zijn op het [ISO 19139](#ISO19139) element dat eraan gekoppeld is in tabel 17.

## Normen waarnaar verwezen wordt

<a id="ISO19115"></a>
[ISO 19115](https://www.iso.org/standard/26020.html) : 

ISO norm over de metadata van datasets en services van geografische aard, gebruikt voor de implementatie van de [INSPIRE richtlijn](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32007L0002&from=FR)

<a id="ISO19139"></a>
[ISO 19139](https://www.iso.org/fr/standard/32557.htm) : 

ISO norm over de XML implementatie van de [ISO 19115](#ISO19115) norm die wordt gebruikt voor de implementatie van de [INSPIRE richtlijn](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32007L0002&from=FR)

<a id="TG2"></a>
[TG 2.0](https://inspire.ec.europa.eu/id/document/tg/metadata-iso19139) : 

norm voor de implementatie van de INSPIRE metadata, gebaseerd op de normen [ISO 19115](#ISO19115) en [ISO 19139](#ISO19139)

<a id="profildemétadonnéesfédéral"></a>
profil de métadonnées fédéral :

niet-officiële federale norm conform de [TG 2.0](#TG2)

<a id="CSW"></a>
[CSW](https://portal.ogc.org/files/?artifact_id=20555) : 

OGC-norm betreffende de publicatie van metadata

<a id="TGrelativesauxservicesdedécouverte"></a>
TG relatives aux services de découverte : 

norm voor het implementeren van de INSPIRE-ontdekkingsdiensten

<a id="DCAT"></a>
[DCAT](https://www.w3.org/TR/vocab-dcat-1/) : 

W3C norm voor het standaardiseren van de catalogi van de datasets op het web

<a id="DCAT2"></a>
[DCAT 2](https://www.w3.org/TR/vocab-dcat-1/) : 

W3C voor het standaardiseren van de catalogi van de datasets op het web

<a id="DCATAP1"></a>
[DCAT AP 1](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/11) : 

ISA norm die de [DCAT](#DCAT) standaard implementeert en er conform mee is om de openbare datasets te beschrijven die worden verdeeld binnen de Unie

<a id="DCATAP2"></a>
[DCAT AP 2](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/200) : 

ISA norm die de [DCAT 2](#DCAT2) standaard implementeert en er conform mee is om de openbare datasets te beschrijven die worden verdeeld binnen de Unie

<a id="GeoDCATAP2"></a>
[Geo DCAT AP 2](https://semiceu.github.io/GeoDCAT-AP/drafts/latest/#properties-for-distribution) : 

ISA norm die de [DCAT AP 2](#DCATAP2) standaard implementeert en er conform mee is om de openbare geografische datasets te beschrijven die worden verdeeld binnen de Unie

<a id="StatDCATAP1"></a>
[Stat DCAT AP 1](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/statdcat-application-profile-data-portals-europe/release/100) :

ISA norm die de [DCAT AP 1](#DCATAP1) standaard implementeert en er conform mee is om de openbare statistische datasets te beschrijven die worden verdeeld binnen de Unie

<a id="DCATAP2fédéral"></a>
DCAT AP 2 fédéral : 

informele federale norm, opgenomen in dit document, conform [DCAT AP 2](#DCATAP2)

<a id="ATOM"></a>
[ATOM](https://tools.ietf.org/html/rfc4287) : 

IETF norm over de syndicatie van content

<a id="TGrelativesauxservicesdetéléchargement"></a>
[TG relatives aux services de téléchargement](https://inspire.ec.europa.eu/documents/technical-guidance-implementation-inspire-download-services) : 

norm voor de implementatie van de INSPIRE downloaddiensten, gebaseerd op de [WFS] en de [ATOM](#ATOM) normen

# Annexe I

## A. dcat:Catalog

### Instantiëring van dcat:Catalog
| URI                 | Naam                                                       | Omschrijving                                                                                | Vereiste voor eerste instantie | Vereiste voor andere instantie | Kardinaliteit | Type               | Bron                                                                                                                                                                                                                                                                    |
| ------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dct:title           | titel                                                      | Naam van de catalogus                                                            | M                         | M                         | 1             | meertalig           | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:title                                                                                                                                                                                                   |
| dct:description     | beschrijving                                               | Bondige tekstuele omschrijving van de catalogus                                                     | M                         | O                         | 1             | meertalig           | //\*/gmd:identificationInfo/\*/gmd:abstract                                                                                                                                                                                                                             |
| dct:publisher       | uitgever                                                   | Entiteit die verantwoordelijk is voor het beschikbaar stellen, van de catalogus           | M                         | O                         | 1             | foaf:Organization   | //\*/gmd:contact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue=’publisher’]]                                                                                                                                                                          |
| dcat:dataset        | dataset                                                    | Dataset die deel uitmaakt van de catalogus            | R                         | W                         | 1-n           | dcat:Dataset        | [indien catalogus gegenereerd vanuit een CSW --> getrecords met type = dataset <> indien catalogus gegenereerd door wizard: aanmaak a posteriori op basis van de vermelde datasets](https://github.com/celinevil/inspire-dcat/edit/main/DCATAPprofil.nl.md#CSW)         |
| dcat:service        | service                                                    | Informatie over de service(s) waarnaar verwezen wordt in de betrokken catalogus             | R                         | W                         | 0-n           | dcat:DataService    | [indien catalogus gegenereerd vanuit een CSW --> getrecords met type = service/applicatie indien catalogus gegenereerd door wizard: aanmaak a posteriori op basis van de vermelde services](https://github.com/celinevil/inspire-dcat/edit/main/DCATAPprofil.nl.md#CSW) |
| foaf:homepage       | onthaalpagina                                              | Human readable versie van de betrokken catalogus                                            | R                         | R                         | 0-1           | rdf:Description     | [Geen XPATH: https://www.geo.be/home (of homepage van de catalogus eigen aan de instelling als die geharvest is)](https://www.geo.be/home)                                                                                                                              |
| dct:language        | taal                                                       | Taal/talen van de betrokken catalogus                                                       | M                         | O                         | 4             | skos:Concept        | //\*/gmd:locale/gmd:PT_Locale/gmd:languageCode/gmd:LanguageCode/@codeListValue                                                                                                                                                                                          |
| dct:issued          | datum van eerste publicatie                                | Het tijdsmoment waarop de datum werd gepubliceerd door de uitgever                            | R                         | O                         | 0-1           | datum (YYYY-MM-DD)  | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='publication']]/gmd:date                                                                                                               |
| dct:spatial         | geografische dekking                                 | Beschrijving van het geografische gebied waarover de dataset informatie heeft  | R                         | O                         | 1-n           | dct:Location        | //\*/gmd :identificationInfo/\*/gmd :extent/gmd :EX_Extent/gmd :geographicElement                                                                                                                                                                                       |
| dcat :themeTaxonomy | gecontroleerde woordenschat                                | Informatie over de thesaurussen waaruit de sleutelwoorden die de datasets beschrijven komen | O                         | W                         | 0-n           | skos :ConceptScheme | generatie a posteriori door opsomming van alle thesaurussen waarnaar verwezen wordt in de klassen Dataset en DataService                                                                                                                                                |
| dct :hasPart        | ingesloten catalogus                                       | Informatie over de catalogus/catalogi die inbegrepen is/zijn in de betrokken catalogus      | O                         | W                         | 0-n           | dcat:Catalog        | [indien catalogus gegenereerd vanuit een CSW --> nihil <> indien catalogus gegenereerd door wizard: voorzien in veld champ](https://github.com/celinevil/inspire-dcat/edit/main/DCATAPprofil.nl.md#CSW)                                                                 |
| dct:isPartOf        | bevattende catalogus                                       | Informatie over de bevattende catalogus/catalogi in de betrokken catalogus                  | O                         | W                         | 0-n           | dcat:Catalog        | [indien catalogus gegenereerd vanuit een CSW --> ID van de catalogus van BOSA+ ID van de DCAT hoofdcatalogus van het NGI <> indien catalogus gegenereerd door wizard voorzien in veld](https://github.com/celinevil/inspire-dcat/edit/main/DCATAPprofil.nl.md#CSW)      |
| dcat:record         | record                                                | Beschrijving van een registratie van één resource in de catalogus                                     | R                         | W                         | 0-n           | dcat:CatalogRecord  | a posteriori generatie door alle CatalogRecord instanties te identificeren                                                                                                                                                                                              |
| dcat:distribution   | distributie                                                | Beschrijving van de beschikbare distributie van een resource in de catalogus                        | R                         | R                         | 0-n           | dcat:Distribution   | \--> genereren met de link naar de XML serialisatie (en eventueel JSON)                                                                                                                                                                                                 |
| dcat:catalog        | catalogus                                                  | Beschrijving van een catalogus waarvan de inhoud interessant is in de context van de beschreven catalogus        | O                         | W                         | 0-n           | dcat:Catalog        | [indien catalogus gegenereerd vanuit een CSW --> nihil indien catalogus gegenereerd door wizard: voorzien in veld](https://github.com/celinevil/inspire-dcat/edit/main/DCATAPprofil.nl.md#CSW)                                                                          |
| dcat:contactPoint   | contactinformatie van de betrokken catalogus                     | Relevante contactinformatie waarmee een eindgebruiker in contact kan treden met  verantwoordelijke van de catalogus            | R                         | R                         | 0-1           | vcard:Organization  | //\*/ gmd:contact/ gmd:CI_ResponsibleParty[ gôleole/ gmd:CI_RoleCode[@codeListValue=’publisher’]]                                                                                                                                                                       |
| dct:identifier      | identifier                                                 | Unieke alfanumerieke identifier van de catalogus                                            | M                         | M                         | 1             | eentalig            | Geen XPATH: XML serialisatie?                                                                                                                                                                                                                                           |
| dcat:theme          | trefwoord afkomstig uit een gecontroleerde woordenschat | Trefwoord afkomstig van een thesaurus die de dataset beschrijft                          | O                         | W                         | 0-n           | skos:Concept        | //\*/ gmd:identificationInfo/\*/ gmd:descriptiveKeywords/ gmd:MD_Keywords[ gmd:thesaurusName/ gmd:CI_Citation/ gmd:title/\*={}]/ gmd:keyword/\*                                                                                                                         |

**Tabel 1 : klasse dcat:Catalog klasse**

## B. dcat:Dataset

### Instantiëring van dcat:Dataset
| URI                           | Naam                                                       | Omschrijving                                                                                                                                       | Vereiste eerste instantie | Vereiste andere instantie | Kardinaliteit | Range                   | Bron                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dct:title                     | titel                                                      | Naam van de dataset                                                                                                                     | M                         | M                         | 1             | meertalig               | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:title/\* (titel genomen overeenkomstig de specificaties van het federaal profiel)                                                                                                                                                                                                                                                             |
| dct:description               | beschrijving                                               | Beschrijving van de betrokken dataset                                                                                                              | M                         | O                         | 1             | meertalig               | //\*/gmd:identificationInfo/\*/gmd:abstract/\*                                                                                                                                                                                                                                                                                                                                                                |
| dcat:contactPoint             | contactinformatie                                                | Relevante contactinformatie waarmee een eindgebruiker in contact kan treden met de verantwoordelijke van de dataset                                                                            | O                         | O                         | 0-n           | vcard:Organization      | //\*/gmd:contact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='pointOfContact']]                                                                                                                                                                                                                                                                                                           |
| dcat:distribution             | distributie                                                | Beschikbare distributie van de dataset                                                                       | R                         | W                         | 0-n           | dcat:Distribution       | [Indien dataset gegenereerd vanuit een ISO 19139 fiche --> de inhoud van de ATOM FEED gebruiken waarnaar verwezen wordt in deze fiche indien dataset gegenereerd door wizard: genereren door manueel invullen in een ad-hocveld](https://github.com/celinevil/inspire-dcat/edit/main/DCATAPprofil.nl.md#ISO19139)                                                                                             |
| dcat:keyword                  | trefwoord                                               | Trefwoord of tag afkomstig van een thesaurus die de dataset beschrijft                                                                                 | O                         | W                         | 0-n           | meertalig               | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD_Keywords[not(./gmd:thesaurusName)]/gmd:keyword/\*                                                                                                                                                                                                                                                                                               |
| dcat:theme                    | trefwoord afkomstig uit een gecontroleerde woordenschat | Trefwoord afkomstig van een thesaurus die de dataset beschrijft                                                                                          | M                         | W                         | 1-n           | skos:Concept            | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD_Keywords[gmd:thesaurusName/gmd:CI_Citation/gmd:title/\*={}]/gmd:keyword/\*                                                                                                                                                                                                                                                                      |
| dct:subject                   | ISO categorie                                              | [de rubriek waartoe de dataset behoort volgens de afspraken in de ISO-standaard voor de geografische metadata](https://github.com/celinevil/inspire-dcat/edit/main/DCATAPprofil.nl.md#ISO19115) | O                         | W                         | 0-n           | skos:Concept            | //\*/gmd:identificationInfo/\*/gmd:topicCategory/\*                                                                                                                                                                                                                                                                                                                                                           |
| dct:spatial                   | geografische dekking                                    | Geografische gebied waarover de dataset informatie heeft                                                             | R                         | W                         | 0-n           | dct:Location            | //\*/gmd:identificationInfo/\*/gmd:extent/gmd:EX_Extent/gmd:geographicElement                                                                                                                                                                                                                                                                                                                                 |
| dct:temporal                  | bestreken periode                                          | Informatie over de periode(s) die bestreken wordt/worden door de betrokken dataset                                                                 | R                         | W                         | 0-n           | dct:PeriodOfTime        | //\*/gmd:identificationInfo/\*/gmd:extent/gmd:EX_Extent/gmd:temporalElement                                                                                                                                                                                                                                                                                                                                   |
| dct:created                   | aanmaakdatum                                         | Datum van aanmaak van de betrokken dataset                                                                                                         | R                         | W                         | 0-1           | datum (YYYY-MM-DD)      | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='creation']]/gmd:date                                                                                                                                                                                                                                                        |
| dct:modified                  | wijzigingsdatum                                           | Meest recente datum waarop de dataset is gewijzigd, bijgewerkt of aangepast                                                                                                      | R                         | W                         | 0-1           | datum (YYYY-MM-DD)      | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='revision']]/gmd:date                                                                                                                                                                                                                                                        |
| dct:issued                    | publicatiedatum van eerste publicatie                                | Tijdsmoment waarop de dataset werd voor het eerst werd gepubliceerd door de uitgever                                                                                                      | O                         | W                         | 0-1           | datum (YYYY-MM-DD)      | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='publication']]/gmd:date                                                                                                                                                                                                                                                     |
| foaf:page                     | metadata pagina                                            | Informatie over de link(s) met details over de inhoud van de dataset                                                                               | R                         | R                         | 0-1           | URL meertalig           | //\*/gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource[gmd:protocol/\*={WWW:LINK-1.0-http--link} and gmd:function/\*/@codeListValue={'information'}]/gmd:linkage/gmd:name                                                                                                                                                           |
| dct:accrualPeriodicity        | updatefrequentie                                           | Informatie over de frequentie van de updates van de betrokken dataset                                                                              | R                         | W                         | 0-1           | skos:Concept            | //\*/gmd:identificationInfo/\*/gmd:resourceMaintenance/gmd:MD_MaintenanceInformation/gmd:maintenanceAndUpdateFrequency/gmd:MD_MaintenanceFrequencyCode/@codeListValue                                                                                                                                                                                                                                         |
| dct:identifier                | identifier                                                 | Unieke alfanumerieke identifier van de betrokken dataset                                                                                           | M                         | M                         | 1             | multilingue             | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:identifier/\*/gmd:code/\*                                                                                                                                                                                                                                                                                                                     |
| dcat:landingPage              | landingspagina                                              | Webpagina in een menselijk leesbare vorm (HTML) van de bron metadata record                                                                                                              | R                         | R                         | 0-4           | rdf:Description         | [https://www.geo.be/catalog/details/ + //\*/gmd:fileIdentifier](https://www.geo.be/catalog/details/)                                                                                                                                                                                                                                                                                                          |
| dct:language                  | taal                                                       | Informatie over de taal/talen van de betrokken dataset                                                                                             | R                         | W                         | 0-4           | skos:Concept            | //\*/gmd:identificationInfo/\*/gmd:language/gmd:LanguageCode/@codeListValue                                                                                                                                                                                                                                                                                                                                   |
| dct:provenance                | oorsprong                                                  | Informatie over de oorsprong van de betrokken dataset                                                                                              | O                         | W                         | 0-1           | dct:ProvenanceStatement | //\*/gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:lineage/gmd:LI_Lineage/gmd:statement                                                                                                                                                                                                                                                                                                                          |
| dct:conformsTo                | specificatie of structureringsregel                        | Informatie over de kwaliteitsnormen van de dataset                                                                                                 | O                         | W                         | 0-n           | dct:Standard            | //\*/gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:report/gmd:DQ_DomainConsistency/gmd:result/gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation ET //\*/gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource[gmd:protocol/\*={WWW:LINK-1.0-http--link} and gmd:function/\*/@codeListValue={'information'}]/gmd:linkage/gmd:name  |
| dct:source                    | brondataset                                                | Informatie over een brondataset                                                                                                                    | O                         | W                         | 0-1           | dcat:Dataset            | [indien dataset gegenereerd vanuit een ISO 19139 fiche --> gebruik de XPATH //\*/gmd:identificationInfo/\*/gmd:aggregationInfo indien dataset gegenereerd door wizard: genereren door manuele selectie in een ad-hocveld](https://github.com/celinevil/inspire-dcat/edit/main/DCATAPprofil.nl.md#ISO19139)                                                                                                    |
| dqv:hasQualityMeasurement     | ruimtelijke resolutie                                      | Informatie over de ruimtelijke resolutie van de betrokken dataset                                                                                  | R                         | W                         | 0-1           | dqv:QualityMeasurement  | //\*/gmd:identificationInfo/\*/gmd:spatialResolution/gmd:MD_Resolution                                                                                                                                                                                                                                                                                                                                        |
| dct:accessRights              | toegankelijkheid                                           | Informatie over de beperkingen met betrekking tot het gebruik van de dataset                                                                       | M                         | W                         | 1             | dct:RightsStatement     | [//\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD_LegalConstraints[\*/gmd:MD_RestrictionCode[@codeListValue='otherRestrictions']]/gmd:otherConstraints[gco:CharacterString or gmx:Anchor[not(starts-with(@xlink:href, 'http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))\\]\\]](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))%5C%5D%5C%5D) |
| adms:sample                   | voorbeeld van verspreiding                                 | Verwijzing naar een voorbeeld van verspreiding van de dataset                                                                                      | O                         | W                         | 0-1           | dcat:Distribution       | geen XPATH gespecificeerd                                                                                                                                                                                                                                                                                                                                                                                     |
| dct:publisher                 | uitgever                                                   | Informatie over de organisatie die verantwoordelijk is voor de beschikbaarheid van de dataset                                                      | O                         | W                         | 0-n           | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='publisher']]                                                                                                                                                                                                                                                                               |
| geodcat:custodian             | onderhouder                                                | Informatie over de organisatie die verantwoordelijk is voor het onderhoud van de dataset                                                           | O                         | W                         | 0-n           | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='custodian']]                                                                                                                                                                                                                                                                               |
| dct:creator                   | producent                                                  | Informatie over de organisatie die verantwoordelijk is voor de productie van de betrokken dataset                                                  | O                         | W                         | 0-n           | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='author']]                                                                                                                                                                                                                                                                                  |
| geodcat:distributor           | verspreider                                                | Informatie over de organisatie die verantwoordelijk is voor de verspreiding van de dataset                                                         | O                         | W                         | 0-n           | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='distributor']]                                                                                                                                                                                                                                                                             |
| geodcat:originator            | auteur                                                     | Informatie over de organisatie die verantwoordelijk is voor de aanmaak van de dataset                                                              | O                         | W                         | 0-n           | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='originator']]                                                                                                                                                                                                                                                                              |
| geodcat:principalInvestigator | inzamelaar                                                 | Informatie over de organisatie die verantwoordelijk is voor de inzameling van de opzoekinformatie                                                  | O                         | W                         | 0-n           | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='principalInvestigator']]                                                                                                                                                                                                                                                                   |
| geodcat:processor             | verwerker                                                  | Informatie over de organisatie die de dataset gewijzigd heeft na de verwerking van de gegevens                                                     | O                         | W                         | 0-n           | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='processor']]                                                                                                                                                                                                                                                                               |
| geodcat:resourceProvider      | leverancier                                                | Informatie over de organisatie die de dataset aanlevert                                                                                            | O                         | W                         | 0-n           | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='resourceProvider']]                                                                                                                                                                                                                                                                        |
| geodcat:user                  | gebruiker                                                  | Informatie over de organisatie die de dataset gebruikt                                                                                             | O                         | W                         | 0-n           | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='user']]                                                                                                                                                                                                                                                                                    |
| dct:rightsHolder              | rechthebbende                                              | Organisatie die de rechten op de dataset bezit                                                                                                     | O                         | W                         | 0-1           | foaf:Organization       | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='user']]/gmd:organisationName                                                                                                                                                                                                                                                               |
| dct:license                   | gebruiksvoorwaarden                                        | Informatie over de bijzondere gebruiksvoorwaarden van deze distributie                                                                             | M                         | W                         | 1             | dct:LicenseDocument     | [//\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD_LegalConstraints[\*/gmd:MD_RestrictionCode[@codeListValue='otherRestrictions']]/gmd:otherConstraints[gco:CharacterString or gmx:Anchor[not(starts-with(@xlink:href, 'http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))\\]\\]](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))%5C%5D%5C%5D) |
| adms:representationTechnique  | type dataset                                               | Informatie over de ruimtelijke weergave van de dataset                                                                                             | R                         | W                         | 1             | skos:Concept            | //\*/gmd:identificationInfo/\*/gmd:spatialRepresentationType                                                                                                                                                                                                                                                                                                                                                  |

**Tabel 3 : dcat:Dataset klasse **

## C. dcat:DataService

### Instantiëring van dcat:DataService
| URI                           | Naam                                                       | Omschrijving                                                                                      | Vereiste voor instantiëring in attribuut dcat:dataService | Vereiste voor instanciëring in een andere attribuut | Kardinaliteit | Type              | Bron                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dct:title                     | titel                                                      | Titel van de betrokken service                                                                    | M                         | M                         | 1             | meertalig           | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:title/\*                                                                                                                                                                                                                                                                                                                                      |
| dct:description               | beschrijving                                               | Beschrijving van de betrokken service                                                             | M                         | M                         | 1             | meertalig           | //\*/gmd:identificationInfo/\*/gmd:abstract/\*                                                                                                                                                                                                                                                                                                                                                                |
| dcat:endpointURL              | URL van de service                                         | URL van de betrokken service                                                                      | M                         | M                         | 0-n           | URL                 | Te bekijken                                                                                                                                                                                                                                                                                                                                                                                                   |
| dcat:servesDataset            | toegankelijke dataset                                      | Identificatie van de dataset(s) die toegankelijk is/zijn via de betrokken service                 | R                         | R                         | 0-n           | dcat:Dataset        | [indien dataservice gegenereerd vanuit een ISO 19139 fiche --> de lijst gebruiken van de identifiers van de datasets die aanwezig zijn in de getcapabilities <> indien dataservice gegenereerd door wizard: genereren door manuele selectie in een ad-hocveld van de al gedocumenteerde datasets](https://github.com/belgif/inspire-dcat/blob/main/DCATAPprofil.nl.md#ISO19139)                               |
| dct:accessRights              | toegangsbeperking                                          | Informatie over de beperkingen met betrekking tot het gebruik van de betrokken service            | M                         | M                         | 1             | dct:RightsStatement | [//\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD_LegalConstraints[gmd:accessConstraints/gmd:MD_RestrictionCode[@codeListValue='otherRestrictions']]/gmd:otherConstraints[gmx:Anchor[starts-with(@xlink:href,'http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess')\\]\\]](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess')%5C%5D%5C%5D)            |
| dcat:keyword                  | sleutelwoord                                               | Vrij sleutelwoord dat de betrokken service beschrijft                                             | R                         | R                         | 0-n           | meertalig           | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD_Keywords[not(./gmd:thesaurusName)]/gmd:keyword/\*                                                                                                                                                                                                                                                                                               |
| dcat:theme                    | sleutelwoord afkomstig uit een gecontroleerde woordenschat | Sleutelwoord afkomstig van een thesaurus die de service beschrijft                                | R                         | R                         | 0-n           | skos:Concept        | //\*/gmd:identificationInfo/\*/gmd:descriptiveKeywords/gmd:MD_Keywords[gmd:thesaurusName/gmd:CI_Citation/gmd:title/\*={}]/gmd:keyword/\*                                                                                                                                                                                                                                                                      |
| dct:created                   | datum van aanmaak                                          | Datum van aanmaak van de betrokken service                                                        | R                         | R                         | 0-1           | datum (YYYY-MM-DD)  | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='creation']]/gmd:date                                                                                                                                                                                                                                                        |
| dct:modified                  | datum van update                                           | Datum van de laatste wijziging van de service                                                     | R                         | R                         | 0-1           | datum(YYYY-MM-DD)   | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='revision']]/gmd:date                                                                                                                                                                                                                                                        |
| dct:issued                    | datum van eerste publicatie                                | Datum van de eerste publicatie van de service                                                     | O                         | O                         | 0-1           | datum (YYYY-MM-DD)  | //\*/gmd:identificationInfo/\*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date[gmd:dateType/gmd:CI_DateTypeCode[@codeListValue='publication']]/gmd:date                                                                                                                                                                                                                                                     |
| dct:conformsTo                | specificatie of structureringsregel                        | Informatie over de kwaliteitsnormen van de service                                                | O                         | O                         | 0-n           | dct:Standard        | //\*/gmd:dataQualityInfo/gmd:DQ_DataQuality/gmd:report/gmd:DQ_DomainConsistency/gmd:result/gmd:DQ_ConformanceResult/gmd:specification/gmd:CI_Citation                                                                                                                                                                                                                                                         |
| dct:type                      | type service                                               | Informatie over het type service                                                                  | R                         | R                         | 1             | skos:Concept        | //\*/gmd:identificationInfo/\*/srv:serviceType                                                                                                                                                                                                                                                                                                                                                                |
| geodcat:distributor           | verspreider                                                | Informatie over de organisatie die verantwoordelijk is voor de verspreiding van de service        | O                         | O                         | 0-1           | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='publisher']]                                                                                                                                                                                                                                                                               |
| geodcat:originator            | auteur                                                     | Informatie over de organisatie die verantwoordelijk is voor de aanmaak van de service             | O                         | O                         | 0-1           | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='custodian']]                                                                                                                                                                                                                                                                               |
| geodcat:principalInvestigator | inzamelaar                                                 | Informatie over de organisatie die verantwoordelijk is voor de inzameling van de opzoekinformatie | O                         | O                         | 0-1           | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='author']]                                                                                                                                                                                                                                                                                  |
| geodcat:processor             | verwerker                                                  | Informatie over de organisatie die de dataset gewijzigd heeft na de verwerking van de gegevens    | O                         | O                         | 0-1           | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='distributor']]                                                                                                                                                                                                                                                                             |
| geodcat:resourceProvider      | leverancier                                                | Informatie over de organisatie die de service aanlevert                                           | O                         | O                         | 0-1           | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='originator']]                                                                                                                                                                                                                                                                              |
| geodcat:user                  | gebruiker                                                  | Informatie over de organisatie die de service gebruikt                                            | O                         | O                         | 0-1           | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='principalInvestigator']]                                                                                                                                                                                                                                                                   |
| dct:creator                   | producent                                                  | Informatie over de organisatie die verantwoordelijk is voor de productie van de betrokken service | O                         | O                         | 0-1           | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='processor']]                                                                                                                                                                                                                                                                               |
| geodcat:custodian             | onderhouder                                                | Informatie over de organisatie die verantwoordelijk is voor het onderhoud van de service          | O                         | O                         | 0-1           | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='resourceProvider']]                                                                                                                                                                                                                                                                        |
| dct:rightsHolder              | rechthebbende                                              | Organisatie die de rechten op de service bezit                                                    | O                         | O                         | 0-1           | foaf:Organization   | //\*/gmd:identificationInfo/\*/gmd:pointOfContact/gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode[@codeListValue='user']]                                                                                                                                                                                                                                                                                    |
| dct:license                   | gebruiksvoorwaarden                                        | Informatie over de bijzondere gebruiksvoorwaarden van deze distributie                            | M                         | M                         | 1             | dct:LicenseDocument | [//\*/gmd:identificationInfo/\*/gmd:resourceConstraints/gmd:MD_LegalConstraints[\*/gmd:MD_RestrictionCode[@codeListValue='otherRestrictions']]/gmd:otherConstraints[gco:CharacterString or gmx:Anchor[not(starts-with(@xlink:href, 'http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))\\]\\]](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess'))%5C%5D%5C%5D) |
| dct:conformsTo                | systeem van geografische projectie                         | Informatie over de ruimtelijke en tijdelijke referentiesystemen                                   | R                         | R                         | 0-n           | codedValue          | //\*gmd:referenceSystemInfo/gmd:MD_ReferenceSystem/gmd:referenceSystemIdentifier/gmd:RS_Identifier/gmd:code                                                                                                                                                                                                                                                                                                   |

**Tabel 5 : dcat:DataService klasse**


## D. dcat:Distribution

### Elke instantiëring van dcat:Distribution
| URI                 | Naam                               | Omschrijving                                                                           | Vereiste | Kardinaliteit | Type                | Bron                                      |
| ------------------- | ---------------------------------- | -------------------------------------------------------------------------------------- | -------- | ------------- | --------------------- | ----------------------------------------- |
| dct:title           | titel                              | Titel van de betrokken verspreiding                                                    | O        | 0-1           | meertalig             | //atom:feed/atom :title                   |
| dcat:accessURL      | toegangs-URL                       | Webadres van de betrokken verspreiding van de dataset                                  | M        | 1             | URL                   | //atom:feed/atom:entry/atom:link          |
| dct:description     | beschrijving                       | Beschrijving van de bijzonderheden van deze verspreiding                               | O        | 0-1           | meertalig             | //atom:feed/atom:entry/atom:subtitle      |
| dct:format          | formaat                            | Informatie over het bijzondere formaat van deze verspreiding                           | M        | 1             | dct:MediaTypeOrExtent | //atom:feed/atom:entry/atom:link/@type    |
| dcat:mediaType      | type formaat                       | Type formaat/drager voor de verspreiding (IANA)                                        | O        | 0-1           | dct:MediaType         | //atom:feed/atom:entry/atom:link/@type    |
| dcat:downloadURL    | download-URL                       | Webadres om de betrokken verspreiding rechtstreeks te downloaden                       | O        | 0-1           | URL                   | //atom:feed/atom:entry/atom:link          |
| dcat:compressFormat | gecomprimeerd formaat              | Informatie over het bijzondere gecomprimeerd formaat van deze verspreiding (IANA)      | O        | 0-1           | dct:MediaType         | //atom :feed/atom :entry/atom :link/@type |
| dct:conformsTo      | systeem van geografische projectie | Informatie over de bijzondere projectie van deze verspreiding                          | O        | 0-1           | dct:Standard          | //atom:feed/atom:entry/atom:category      |
| dcat:byteSize       | grootte                            | Grootte van de verspreiding in bytes                                                   | O        | 0-1           | xsd:decimal           | geen XPATH gespecificeerd                 |
| adms:status         | statuut                            | Informatie over de maturiteit van de verspreiding                                      | O        | 1             | skos:Concept          | geen XPATH gespecificeerd spécifié        |
| dct:spatial         | ruimtelijke overdekking            | Informatie over de geografische zone die overdekt wordt door de betrokken verspreiding | O        | 0-1           | dct:Location          | //atom:feed/atom:entry/georss:box         |
| dct:temporal        | bestreken periode                  | Informatie over de tijdspanne die wordt bestreken door de betrokken verspreiding       | R        | 0-1           | dct:PeriodOfTime      | //atom:feed/atom:entry/atom:link/@time    |
| dct:type            | type verspreiding                  | Link naar een type verspreiding                                                        | O        | 0-n           | skos:Concept          | geen XPATH gespecificeerd                 |
| dct:language        | taal                               | Informatie over de taal/talen die gebruikt wordt/worden in de distributie              | R        | 0-4           | skos:Concept          | geen XPATH gespecificeerd                 |

**Tabel 7 : klasse dcat:Distribution geïnstantieerd in eender welke instantie**


## E. foaf:Organization

### Elke instantiëring van foaf:Organization in een instantie
| URI                    | Naam      | Omschrijving                                               | Vereiste | Kardinaliteit | Type          | Bron                                                                                    |
| ---------------------- | --------- | ---------------------------------------------------------- | -------- | ------------- | --------------- | --------------------------------------------------------------------------------------- |
| foaf:name              | naam      | Naam van de organisatie                                    | M        | 1-n           | Meertalig       | ./gmd:organisationName                                                                  |
| dct:type               | type      | Duidt het organisatietype aan                              | O        | 0-1           | skos:Concept    | geen XPATH gespecificeerd                                                               |
| foaf:mbox              | mailadres | mailadres van de organisatie (met gebruik van URI mailto:) | R        | 0-1           | Eentalig        | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address/gmd:electronicMailAddress |
| foaf:workplaceHomepage | Website   | Website van de organisatie                                 | R        | 1-4           | rdf:Description | ./gmd:contactInfo/gmd:CI\_Contact/gmd:onlineResource/gmd:CI\_OnlineResource/gmd:linkage |
| locn:address           | Postadres | Postadres van de organisatie                               | O        | 0-1           | locn:Address    | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address                           |

**Tabel 8 : klasse foaf:Organization geïnstantieerd in een instantie van om het even welke klasse**

## F. dcat:CatalogRecord

### Instantiëring van dcat:CatalogRecord
| URI               | Naam                                 | Omschrijving                                                                                     | Vereiste | Kardinaliteit | Type              | Bron                                                                                                                                                                    |
| ----------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------ | -------- | ------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| foaf:primaryTopic | instantie waarnaar de fiche verwijst | Informatie over de dataset, service of catalogus                                                 | M        | 1             | dcat:Dataset       | dcat:Dataservice                                                                                                                                                        | dcat:Catalog | generatie a posteriori met integratie van alle ID’s van alle primaire instantiëringen (d.w.z. de instanties die niet overeenkomen met de waarde van een attribuut van dezelfde klasse)
| dct:modified      | datum van update                     | Datum van de laatste update van de Catalog Record                                                | M        | 1             | datum (YYYY-MM-DD) | //\* /gmd:dateStamp/\*                                                                                                                                                  |
| dct:language      | taal                                 | Informatie over de taal/talen die gebruikt wordt/worden in de metadata van de dataset of service | M        | 1-n           | skos :Concept      | //\*/gmd:locale/gmd:PT\_Locale/gmd:languageCode/gmd:LanguageCode\[@codeListValue={}\]                                                                                   |
| dcat:contactPoint | Contactpunt                          | Informatie over de modaliteiten om contact op te nemen over de dataset of service                | M        | 1             | vcard:Organization | //\*/gmd:contact/gmd:CI\_ResponsibleParty                                                                                                                               |
| dct:identifier    | identifier                           | Unieke alfanumerieke identifier van de betrokken catalogrecord                                   | M        | 1             | eentalig           | //\*/gmd:fileIdentifier                                                                                                                                                 |
| dct:source        | Catalogrecord source                 | Informatie over de originele metadatafiche van de dataset of service                             | O        | 0-1           | eentalig           | http://csw.geo.be/eng/csw?request=GetRecordById&service=CSW&version=2.0.2&elementSetName=full&outputSchema=http://www.isotc211.org/2005/gmd&id=+//\*/gmd:fileIdentifier |
| dcat:landingPage  | onthaalpagina                        | Human readable versie van de originele metadatafiche van de dataset of service                   | O        | 0-4           | rdf:Description    | https://www.geo.be/catalog/details/ + //*/gmd:fileIdentifier                                                                                                            |

**Tabel 9 : klasse dcat:CatalogRecord klasse geïnstantieerd in een instantie van de klasse dcat:Catalog**

## G. locn:Address

### Instantiëring van locn:Address
| URI               | Naam      | Omschrijving           | Vereiste | Kardinaliteit | Type| Bron                  |
| ----------------- | --------- | ---------------------- | -------- | ------------- | --------- | --------------------- |
| locn:thoroughfare | postadres | Straat en huisnummer   | M        | 1             | meertalig | .  /gmd:deliveryPoint |
| locn:postName     | gemeente  | Naam van de gemeente   | M        | 1             | meertalig | .  /gmd:city          |
| locn:postCode     | postcode  | Postcode van het adres | M        | 1             | eentalig  | ./gmd:postalCode      |
| locn:adminUnitL1  | land      | Land                   | M        | 1             | meertalig | ./gmd:country         |

**Tabel 10 : klasse locn:Address geïnstantieerd in een instantie van om het even welke klasse**

## H. skos:Concept

### Instantiëring van skos:Concept
| URI           | Naam                    | Omschrijving                               | Vereiste | Kardinaliteit | Type   | Bron                                             |
| ------------- | ----------------------- | ------------------------------------------ | -------- | ------------- | -------- | ------------------------------------------------ |
| rdf:type      | type concept            | Type concept                               | O        | 0-1           | eentalig | geen                                             |
| skos:inScheme | thesaurus van oorsprong | Thesaurus waaruit het concept afkomstig is | R        | 0-1           | URL      | .  /gmd:thesaurusName/gmd:CI\_Citation/gmd:title |

**Tabel 11 : klasse skos:Concept geïnstantieerd in een instantie van om het even welke klasse**

## I. dct:PeriodOfTime

### Instantiëring van skos:PeriodOfTime
| URI            | Naam          | Omschrijving                 | Vereiste | Kardinaliteit | Type    | Bron                                                                    |
| -------------- | ------------- | ---------------------------- | -------- | ------------- | -------- | ----------------------------------------------------------------------- |
| dcat:startDate | aanvangsdatum | Begindatum van de tijdspanne | M        | 1             | eentalig | /gmd:EX_TemporalExtent/gmd :extent/gml32:TimePeriod/gml32:beginPosition |
| dcat:endDate   | einddatum     | Einddatum van de tijdspanne  | M        | 1             | eentalig | ./gmd:EX_TemporalExtent/gmd :extent/gml32:TimePeriod/gml32:endPosition  |

**Tabel 12 : klasse dct:PeriodOfTime geïnstantieerd in een instantie van om het even welke klasse**

## J. dqv:QualityMeasurement

### Instantiëring van dqv: QualityMeasurement – vectoriële dataset
| URI                              | Naam                                      | Omschrijving                              | Vereiste | Kardinaliteit | Type        | Bron                                                                                                   |
| -------------------------------- | ----------------------------------------- | ----------------------------------------- | -------- | ------------- | ------------ | ------------------------------------------------------------------------------------------------------ |
| dqv:isMeasurementOf              | gemeten schaalgrootte                     | Gemeten schaalgrootte                     | O        | 0-1           | meertalig    | Gehardcoded waarde naargelang van het type dataset                                                     |
| sdmx-attribut:unitMeasure        | meeteenheid van de schaalgroottes         | Meeteenheid van de schaalgroottes         | W        | 1             | skos:Concept | ./gmd :MD\_Resolution/gmd:distance/gco:Distance/@uom                                                   |
| dqv:value                        | waarde van de meting van de schaalgrootte | Waarde van de meting van de schaalgrootte | W        | 1             | eentalig     | ./gmd :MD\_Resolution /gmd:distance/gco:Distance                                                       |
| geodcat:spatialResolutionAsScale | conceptuele schaal van de dataset         | Conceptuele schaal van de dataset         | M        | 1             | eentalig     | ./gmd :MD\_Resolution/gmd:equivalentScale/ gmd:MD\_RepresentativeFraction/ gmd:denominator/gco:Integer |

**Tabel 13 : klasse dqv:QualityMeasurement die betrekking heeft op de beschrijving van een vectoriële dataset**

### Instantiëring van dqv:QualityMeasurement – matriciële dataset
| URI                              | Naam                                      | Omschrijving                              | Vereiste | Kardinaliteit | Type        | Bron                                                                                                   |
| -------------------------------- | ----------------------------------------- | ----------------------------------------- | -------- | ------------- | ------------ | ------------------------------------------------------------------------------------------------------ |
| dqv:isMeasurementOf              | gemeten schaalgrootte                     | Gemeten schaalgrootte                     | O        | 0-1           | meertalig    | Gehardcoded waarde naargelang van het type dataset                                                     |
| sdmx-attribut:unitMeasure        | meeteenheid van de schaalgroottes         | Meeteenheid van de schaalgroottes         | R        | 1             | skos:Concept | ./gmd :MD\_Resolution/gmd:distance/gco:Distance/@uom                                                   |
| dqv:value                        | waarde van de meting van de schaalgrootte | Waarde van de meting van de schaalgrootte | M        | 1             | eentalig     | ./gmd :MD\_Resolution /gmd:distance/gco:Distance                                                       |
| geodcat:spatialResolutionAsScale | conceptuele schaal van de dataset         | Conceptuele schaal van de dataset         | W        | 1             | eentalig     | ./gmd :MD\_Resolution/gmd:equivalentScale/ gmd:MD\_RepresentativeFraction/ gmd:denominator/gco:Integer |

**Tabel 14 : klasse dqv:QualityMeasurement die betrekking heeft op de beschrijving van een matriciële dataset**

## K. dct:Location

### Instantiëring van dct:Location in een instantie van om het even welke klasse
| URI             | Nom                                     | Description                                 | Exigence | Cardinalité | Domaine    | Source |
| --------------- | --------------------------------------- | ------------------------------------------- | -------- | ----------- | ---------- | ------ |
| locn:geometry   | geometrie                               | Coördinaten van de geometrie van de dataset | M        | 1           | Eentalig   |        |
| dcat:bbox       | geograpfisch afbakeningsrechthoek       | Coördinaten van de geometrie van de dataset | M        | 1           | Eentalig   |        |
| Skos :prefLabel | naam van de geografische entiteit       | Naam van de geografische entiteit           | R        | 0-1         | meertalig  |        |
| dct:identifier  | identifier van de geografische entiteit | Identifier van de geografische entiteit     | R        | 0-1         | codedValue |        |

**Tabel 15 : klasse dct:Location geïnstantieerd in een instantie van om het even welke klasse**

## L. skos:ConceptScheme

### Instantiëring van skos:ConceptScheme in een instantie van dcat:Catalog
| URI            | Nom                         | Description                 | Exigence | Cardinalité | Domaine   | Source                                                                                                                                                                                                        |
| -------------- | --------------------------- | --------------------------- | -------- | ----------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dct:title      | Titel van de thesaurus      | Titel van de thesaurus      | M        | 1           | meertalig | Generatie op basis van de aangeleverde URL's in de skos:inScheme eigenschappen van de instanties van de klasse skos:Concept (de inScheme is dus nodig en dient voorzien te zijn van een machine-readable URL) |
| dct:issued     | Datum van eerste publicatie | Datum van eerste publicatie | O        | 0-1         | datum     | Generatie op basis van de aangeleverde URL's in de skos:inScheme eigenschappen van de instanties van de klasse skos:Concept (de inScheme is dus nodig en dient voorzien te zijn van een machine-readable URL) |
| Dct:identifier | Identifier van de thesaurus | Identifier van de thesaurus | M        | 1           | URL       | Generatie op basis van de aangeleverde URL's in de skos:inScheme eigenschappen van de instanties van de klasse skos:Concept (de inScheme is dus nodig en dient voorzien te zijn van een machine-readable URL) |

**Tabel 16 : klasse skos:ConceptScheme geïnstantieerd in een instantie van dcat:Catalog**

## M. vcard:Organization

### Instantiëring van vcard:Organization in een instantie van om het even welke attribuut

| URI                     | Naam      | Omschrijving                                               | Vereiste | Kardinaliteit | Type           | Bron                                                                                    |
| ----------------------- | --------- | ---------------------------------------------------------- | -------- | ------------- | --------------- | --------------------------------------------------------------------------------------- |
| vcard:organization-name | naam      | Naam van de organisatie                                    | M        | 1-n           | Meertalig       | ./gmd:organisationName                                                                  |
| vcard:hasEmail          | mailadres | Mailadres van de organisatie (met gebruik van URI mailto:) | R        | 0-1           | Eentalig        | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address/gmd:electronicMailAddress |
| vcard:hasURL            | website   | Website van de organisatie                                 | R        | 1-4           | rdf:Description | ./gmd:contactInfo/gmd:CI\_Contact/gmd:onlineResource/gmd:CI\_OnlineResource/gmd:linkage |
| vcard:hasAddress        | postadres | Postadres van de organisatie                               | O        | 0-1           | vcard:Address   | ./gmd:contactInfo/gmd:CI\_Contact/gmd:address/gmd:CI\_Address                           |

**Tabel 18 : klasse vcard:Organization geïnstantieerd in een instantie van om het even welke attribuut**

## N. vcard:Address

### Instantiëring van vcard:Address in eender welke attribuut

| URI                  | Naam      | Omschrijving           | Vereiste | Kardinaliteit | Type     | Bron                  |
| -------------------- | --------- | ---------------------- | -------- | ------------- | --------- | --------------------- |
| vcard:street-address | postadres | Straat en huisnummer   | M        | 1             | meertalig | .  /gmd:deliveryPoint |
| Vcard :locality      | gemeente  | Naam van de gemeente   | M        | 1             | meertalig | .  /gmd:city          |
| vcard:postal-code    | postcode  | Postcode van het adres | M        | 1             | eentalig  | ./gmd:postalCode      |
| vcard:country-name   | land      | Land                   | M        | 1             | meertalig | ./gmd:country         |

**Tabel 19 : klasse vcard:Address geïnstantieerd in eender welke attribuut**

## O. dct:LicenseDocument

### Instantiëring van dct:LicenseDocument in eender welke attribuut

| URI             | Naam                          | Omschrijving                  | Vereiste | Kardinaliteit | Type     | Bron |
| --------------- | ----------------------------- | ----------------------------- | -------- | ------------- | --------- | ---- |
| dct:type        | type document                 | Type document                 | M        | 1             | URI       |      |
| dct:title       | titel van het document        | Titel van het document        | M        | 1             | meertalig |      |
| dct:description | beschrijving van het document | Beschrijving van het document | O        | 0-1           | meertalig |      |

**Tabel 20 : klasse dct:LicenseDocument geïnstantieerd in een eender welk attribuut**

## P. rdf:Description

### Instantiëring van rdf:Description in eender welke attribuut

| URI          | Nom                   | Description           | Exigence | Cardinalité | Domaine    | Source                               |
| ------------ | --------------------- | --------------------- | -------- | ----------- | ---------- | ------------------------------------ |
| dct:language | taal van het document | Taal van het document | M        | 1           | codedValue | /gmd:LocaliseCharacterString/@locale |

**Tableau 21 : klasse rdf:Description geïnstantieerd in een eender welk attribuut**

# Annexe II

| Betrokken klasse | Betrokken attribuut | Voorgestelde thesaurussen | Vereiste |
| ---------------- | ------------------- | ------------------------- | -------- |
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

**Lijst 1: thesaurussen**

