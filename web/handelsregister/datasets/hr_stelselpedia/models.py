from django.contrib.gis.db import models
# Create your models here.


class Persoon(models.Model):
    """
    """
    rechtsvorm = models.CharField(max_length=50, blank=True, null=True)
    uitgebreiderechtsvorm = models.CharField(
        max_length=240, blank=True, null=True)

    volledigenaam = models.CharField(max_length=240, blank=True, null=True)

    # locatie

    # bezoekadres
    # postadres
    # bezoekadres

    # BeperkingRechtsHandeling (BIR)

    # BijzondereRechtstoestand(BRT)

    # Schuldsanering SSN

    # SurseanceVanBetaling SUR

    # Faillisement (FAL)


class NatuurlijkPersoon(models.Model):
    """
    NPS
    """

    # /Locatie-NatuurlijkPersoon (LOC)LOC-LOCj - woonadres.

    # NatuurlijkPersoonid -  identificatie {NatuurlijkPersoon}

    # Burgerservicenummer.

    # geboortedatum
    geboortedatum = models.DecimalField(
        max_digits=8, decimal_places=0, blank=True, null=True)

    # Geboorteplaats
    geboorteplaats = models.CharField(max_length=240, blank=True, null=True)

    # geboorteland
    geboorteland = models.CharField(max_length=50, blank=True, null=True)

    # geslachtsnaam

    geslachtsnaam = models.CharField(max_length=240, blank=True, null=True)
    # voornamen

    naam = models.CharField(max_length=600, blank=True, null=True)
    # voorvoegsel Geslachtsnaam
    geslachtsaanduiding = models.CharField(
        max_length=20, blank=True, null=True)
    # Geslachtsnaam

    # Voorvoegsel Geslachtsnaam

    # Voornamen

    # Geslachtsaanduiding ? man / vrouw / unknown
    geslachtsaanduiding = models.CharField(
        max_length=20, blank=True, null=True)

    # Overlijdensdatum

    # adellijkeTitel

    # aanduidingNaamgebruik

    # GeslachtsnaamPartner

    # VoorvoegselGeslachtsnaamPartner

    # handelingsbekwaam


class NietNatuurlijkPersoon(models.Model):
    """
    NNP

    Een NietNatuurlijkPersoon is een Persoon met rechten
    en plichten die geen {NatuurlijkPersoon} is.

    De definitie sluit aan bij de definitie in de stelselcatalogus.
    In het handelsregister wordt de {EenmanszaakMetMeerdereEigenaren}
    en {RechtspersoonInOprichting} niet als {Samenwerkingsverband}
    geregistreerd. Voor het handelsregister worden deze beschouwd
    als niet-natuurlijke personen.
    """

    # Objecttype NietNatuurlijkPersoon (NNP)

    # kenmerkrelatieauthentiekdefinitie
    # RSIN-RSINjaHet door een kamer toegekend uniek nummer voor
    # de {NietNatuurlijkPersoon}. Dit geldt sinds 06-12-2011, en geldt
    # mogelijk niet voor oudere niet-natuurlijke personen.
    # naam-naamjaDe naam van de {NietNatuurlijkPersoon}.
    # DatumAanvang
    # DatumEinde
    # ookGenoemd- andere naam
    # verkorteNaam
    # datumUitschrijving -
    # Ontbinding (ONT) OntbindingdatumAanvang - datum ontbonden.
    # datumEinde - Datum waarop de bijzondere buitenlandse rechtstoestand
    # is beëindigd
    # aanleiding -
    # Liquidatie (LIQ)LiquidatieDatumAanvang - LiquidatieDatumAanvangneeDe
    # datum waarop de ontbinding ingaat.

    # DatumEindejaDe -
    # DatumEindejaDeneeDe datum waarop de liquidatie is
    # beëindigd (einde vereffening).

    # BuitenlandseRechtstoestand (BUR)
    # Aanvang -
    # Einde
    # beschrijving- De beschrijving van de buitenlandse uitspraak.

    # RechtelijkeUitspraak (UIT)RechtelijkeUitspraakAansprakelijkheid (ASH)
    # ASH-moeder
    # ASH-dochter

    # Deponering (DEP)Deponering


class BuitenlandseVennootschap(models.Model):
    """
    BRV

    Een BuitenlandseVennootschap is opgericht naar buitenlands recht.

    In het handelsregister wordt van een {BuitenlandseVennootschap}
    opgenomen: het registratienummer uit het buitenlands register,
    de naam van het register en de plaats en land waar het register
    gehouden wordt.

    """
    # buitenlandsRegister - De naam van het buitenlandsregister

    # plaatsBuitenlandsRegister - plaatsBuitenlandsRegisterneeDe naam van
    # het register in het buitenland wordt ingevoerd en de plaats daarbij
    # is vrij invulbare tekst.

    # inschrijfnummer - nummer waaronder BuitenlandseRechtspersoon Of
    # Vennootschap} is ingeschreven in het buitenlandse register.

    # landVanOprichting

    # land- # Het land waar de {BuitenlandseVennootschap} is ingeschreven.
    # geplaatstKapitaal (KAP)KAP-KAPneeHet geplaatste aandelenkapitaal is het

    # (recht op) kapitaal dat door de onderneming is uitgegeven en dat door
    # aandeelhouders aan de onderneming is verschaft.

    # BuitenlandseVennootschapGegevens (BVG)
    # BuitenlandseVennootschapGegevenshoofdvestiging Buiten Nederland -
    # of de hoofdvestiging van de onderneming buiten Nederland is gevestigd.

    # omschrijvingRechtsvorm- De omschrijving van de rechtsvorm
    # zoals deze in het land van inschrijving bekend is.
    # datumEersteInschrijvingBuitenland
    # zetel- De zetel is de plaats waar een {Rechtspersoon} volgens
    # de statuten gevestigd is, dit kan een andere zijn dan de plaats
    # waar de werkzaamheden daadwerkelijk worden uitgevoerd.

    # datumFormeelBuitenlandsSinds - De datum waarop de vennootschap als
    # formeel buitenlandse vennootschap is aangemerkt.

    # rechtsvormcategorie - De Nederlandse rechtsvormcategorie
    # van de {BuitenlandseVennootschap}.

    # datumAkteOprichting - De datum waarop de akte van oprichting is gemaakt.

    # Locatie-BuitenlandseNNP (LOC) postadres
    # Locatie-BuitenlandseNNP (LOC) postadresbezoekadres


class BinnenlandseNietNatuurlijkPersoon(models.Model):
    """
    BNP
    """

    # EenmanszaakMetMeerdereEigenaren - Een eenmanszaak met onverdeelde boedel

    # RechtspersoonInOprichting (RPO) - {Rechtspersoon} die in oprichting is.

    # rechtsvormcategorie - De rechtsvorm die de Rechtspersoon na
    # oprichting zal krijgen.

    # Samenwerkingsverband (SWV) Een Samenwerkingsverband is een
    # groep van natuurlijke personen, rechtspersonen, samenwerkingsverbanden
    # (of een combinatie hiervan) aan wie een {Onderneming} toebehoort
    # zoals bedoeld in artikel 10 lid 3 van de Handelsregisterwet 2007.

    # rechtsvorm - De rechtsvorm van het {Samenwerkingsverband}.

    # aantalCommanditaireVennoten - aantalCommanditaireVennotenneeHet
    # aantal commanditaire (of stille) vennoten van de C.V.

    # CommanditairKapitaal (CKP)CommanditairKapitaalbedrag -
    # CommanditairKapitaalbedragneeDe waarde van het commanditair kapitaal.

    # soort-soortneeDe soort commanditair kapitaal.

    # Duur (DUU)DuureindeDuur-DuureindeDuurnee
    # De datum waarop is afgesproken dat het {Samenwerkingsverband} eindigt.

    # onbepaald-onbepaaldneeIndicatie of de duur niet beperkt is.
    # Rechtspersoon (RP) - Een {Rechtspersoon} is een door de wet mogelijk
    # gemaakt rechtssubject, welke drager van rechten en plichten is.

    # /activiteitenGestaaktPer - Datum waarop de activiteiten van
    # de onderneming zijn gestaakt.

    # buitenlandsRegister - De naam van het buitenlands register.
    # rechtsvorm-rechtsvormjaDeDe rechtsvorm van de {Rechtspersoon}.

    # plaatsBuitenlandsRegisterneeDe - De plaatsnaam van het register
    # in het buitenland.

    # statutaireZetel - statutaireZeteljaDe zetel is de plaats waar
    # een {Rechtspersoon}volgens de statuten gevestigd is.

    # datumAkteOprichting - De datum waarop de akte van oprichting is verleden

    # inschrijfnummerBuitenland - Het nummer waaronder de rechtspersoon
    # is ingeschreven in het buitenlandse register.

    # datumOprichting - De datum waarop de {Rechtspersoon}is opgericht.
    # bedragKostenOprichting - De oprichtingskosten van de Rechtspersoon,
    # en dit geldt alleen bij een N.V., S.E. en S.C.E.

    # land- Het land waar de zetel van de rechtspersoon naar is verplaatst.

    # datumAkteStatutenWijziging - datumAkteStatutenWijzigingnee De datum
    # waarop de akte, waarin de statutenwijziging is opgenomen, is verleden.

    # datumLaatsteStatutenWijziging - De datum waarop de statutenwijziging
    # is ingegaan.

    # publiekrechtelijkeRechtsvorm - Een nadere aanduiding van de
    # publiekrechtelijke {Rechtspersoon}.

    # overigePrivaatrechtelijkeRechtsvorm - De rechtsvorm van de overige
    # privaatrechtelijke {Rechtspersoon}. Bevat de waarden van
    # RechtsvormOverigePrivaatrechtelijke als een mogelijke nieuw gemelde
    # rechtsvorm (in vrije tekst)

    # bevoegdheidVereninging - De rechtsbevoegdheid van de vereniging.
    # ingangStatuten - Ingangsdatum van de gewijzigde statuten.
    # beleggingsMijMetVeranderlijkKapitaal -Indicatie bij een
    # Naamloze Vennootschap die aangeeft of het een beleggingsmaatschappij
    # met veranderlijk kapitaal betreft.

    # stelselInrichting - Het monistische of dualistische stelsel van
    # een Besloten Vennootschap (BV), Naamloze Vennootschap (NV),
    # Société Européenne (SE) of Societas Cooperativa Europaea (SCE) ofwel
    # Europese Coöperatieve Vennootschap.

    # bijzondereStructuur - structuur die aangenomen kan worden door een BV,
    # NV, SE, OWM of Coöp

    # maatschappelijkKapitaal (KAP)KAP- Het {Maatschappelijk kapitaal} is het
    # in de statuten vermelde maximumbedrag, van de N.V., S.E. of S.C.E.,
    # waartegen aandelen mogen worden uitgegeven. Van de B.V. wordt het
    # maatschappelijk kapitaal sinds 1-10-2012 niet meer geregistreerd.

    # geplaatstKapitaal (KAP) - Het geplaatste aandelenkapitaal,
    # van de B.V., N.V., S.E. of S.C.E., is het (recht op) kapitaal dat door
    # de onderneming is uitgegeven en dat door aandeelhouders aan de
    # onderneming is verschaft.

    # gestortKapitaal (KAP) HetdatumEersteInschrijvingHandelsregister
    # KAPneeHetHetHetdatumEersteInschrijvingHandelsregisterneeDe datum waarop
    # de rechtspersoon als eerste is ingeschreven in het handelsregister.

    # VoornemenTotOntbinding (VTO) VoornemenTotOntbindingdatumAanvang-
    # VoornemenTotOntbindingdatumAanvangneeDatum aanvang van het
    # {VoornemenTotOntbinding}.

    # datumEinde - datumEindeneeDatum einde van het {VoornemenTotOntbinding}.
    # Activiteiten - (ACT) Activiteiten die bij een {Rechtspersoon} horen.
    # Communicatiegegeven - (COM)C Locatie-Rechtspersoon
    # Locatie-postadres
    # Locatie-rechtspersoon (LOC) postadresbezoekadres


class FunctieVervulling(models.Model):
    """
    BRV

    Een {Functievervulling} is een vervulling door een {Persoon}
    van een functie voor een {Persoon}.

    Een {FunctieVervulling} geeft de relatie weer van de {Persoon}
    als functionaris en de {Persoon} als eigenaar van de {Onderneming} of
    """

    # datumAanvang- De datum van aanvang van de functievervulling.

    # datumEindeneeDatum - De datum van beëindiging van de functievervulling.

    # FunctieTitel (FNT)FunctieTitelfunctietitel-FunctieTitelfunctietitelNeeDe
    # titel als die afwijkt van de functie titel
    # bestuurder, commissaris, gevolmachtigde, beheerder,
    # lid van het toezichthoudend,
    # besturend of leidinggevend orgaan en functionaris volgens het
    # buitenlands recht.

    # indicatieStatutair - Indicatie of titel in de statuten is opgenomen.

    # Schorsing (SOR) - De datum waarop de schorsing is ingegaan.

    # datumEindeneeDatum - De datum waarop de schorsing is opgeheven.

    # Een Persoon (PRS) heeft een Functievervulling (FVV)FVVHR:

    # Persoon (PRS) - Een Functievervulling (FVV) door Persoon

    # (PRS)PRSHR: PRS Persoon is een Functievervulling

    # (FVV)FVVHR: PRS EenFunctievervulling (FVV)
    # voor een Persoon (PRS)PRSHR: Persoon (PRS) PRS

    # FunctievervullingAansprakelijke - De {Aansprakelijke} is de {Persoon}
    # die aansprakelijk is voor de rechtshandelingen van het {Samenwerkingsverband}.

    # functie- Een nadere aanduiding van de {Aansprakelijke}.
    # handelingsbekwaam - Geeft aan of de Aansprakelijke, die NatuurlijkPersoon
    # is, handelingsbekwaam is of niet. Het attribuut is voor
    # de {NietNatuurlijkPersoon} niet aanwezig.

    # BevoegdheidAansprakelijke (BHA) - Het soort bevoegdheid die een
    # aansprakelijke van een {Samenwerkingsverband} kan hebben.

    # beperkingInEuros - beperkingInEuros De bevoegdheid is beperkt
    # tot het genoemde bedrag.

    # overigeBeperking - overige Beperking Indicatie of er een
    # andere beperking voor de aansprakelijke geldt.

    # Bestuursfunctie (BSF) De functionaris die als bestuurder werkzaam
    # is bij een privaatrechtelijke {Rechtspersoon}.
    # functieJaEen-functieJaEenJaDe nadere aanduiding van de {Bestuurder}.

    # BevoegdheidBestuurder (BHB)BevoegdheidBestuurdersoortBevoegdheid-
    # BevoegdheidBestuurdersoortBevoegdheidNeeDe soort bevoegdheid
    # die een bestuurder kan hebben.

    # bevoegdMetAnderePersonen-bevoegdMetAnderePersone Indicatie die aangeeft
    # dat er een gezamenlijke bevoegdheid is met andere personen (Ja) of
    # met de andere bestuurders (Nee).

    # VertegenwoordigerBestuurderRechtspersoon VBR- De NatuurlijkPersoon als
    # vertegenwoordiger van de {Rechtspersoon} die bestuurder is bij een EESV.

    # Gemachtigde GMA - Een Gemachtigde wordt gekenmerkt door een volmacht
    # verleend door de {Persoon} bij wie de {Gemachtigde} is toegetreden.

    # functie - De- Een nadere aanduiding van de {Gemachtigde}.

    # Volmacht (VOL) Volmachtstatutair - Volmachtstatutair De indicatie
    # die aangeeft of de {Volmacht} in de en is opgenomen.
    # heeft betrekking op een vestigingHR: Vestiging (VES) BeperkteVolmacht

    # beperkingInGeld- Indien de Gemachtigde tot een bepaald
    # bedrag is gemachtigd.

    # doenVanOpgaveAanHandelsregister - doenVanOpgaveAanHandelsregister
    # Indien de {Gemachtigde} opgave mag doen van aan het handelsregister.

    # overigeVolmacht - Indicatie die aangeeft dat de Gemachtigde een
    # Volmacht heeft die niet gestructureerd als soort handeling opgenomen
    # kan worden.

    # omschrijvingOverigeBeperkingen - De inhoud van de niet gestructureerd
    # op te nemen beperking in de volmacht.

    # BeperkingInHandeling

    # beperkingInGeldNeeIndien - Indien de gemachtigde een (gestructureerde)
    # beperking in handelen heeft kan daarvoor een beperking tot een bepaald
    # bedrag in geld worden opgegeven.

    # soortHandeling- Indien de gemachtigde een gestructureerde beperking
    # in handelen heeft kan gekozen worden uit een standaardlijst
    # met beperkingen.

    # VolledigeVolmacht

    # OverigeFunctionaris (OFV) De functionaris die niet in een van de
    # andere groepen is genoemd.

    # functie - Een nadere aanduiding van de {OverigeFunctionaris}.

    # geplaatst_kapitaal : (KAP) KAPNeeHet geplaatste aandelenkapitaal
    # is het (recht op) kapitaal dat door de onderneming is uitgegeven en
    # dat door de aandeelhouders aan de onderneming is verschaft.

    # gestort kapitaalHR: Kapitaal (KAPNeeHetNeeHet gestorte aandelenkapitaal
    # is het deel van het geplaatste kapitaal waarvan de onderneming
    # daadwerkelijk de gelden heeft ontvangen.

    # afwijkendAansprakelijkheidsbeding - Hier wordt de aanwezigheid van
    # een afwijkendaansprakelijkheidsbeding van leden geregistreerd,
    # in het geval van een EESV.

    # BevoegdheidFunctionarisVolgensBuitenlandsRecht (BBR)
    # De soort bevoegdheid die een functionaris naar buitenlands recht
    # kan hebben.

    # PubliekrechtelijkeFunctionaris (PRF) De functionaris die werkzaam is
    # bij een publiekrechtelijke {Rechtspersoon}.

    # functieJaEenJaDeJaEenNeeEen-functieJaEenJaDeJaEenNeeEenJaEen nadere
    # aanduiding van de {PubliekrechtelijkeFunctionaris}.

    # BevoegdheidPubliekRechtelijkeFunctionaris (BPF)
    # BevoegdheidPubliekRechtelijkeFunctionarissoortBevoegdheid-
    # BevoegdheidPubliekRechtelijkeFunctionarissoortBevoegdheidNeede
    # soort bevoegdheid die een functionaris naar buitenlands recht kan hebben.

    # FunctionarisBijzondereRechtstoestand (FBR) - De door de rechter
    # aangewezen functionaris bij schuldsanering, surseance van betaling,
    # faillissement, onderbewindstelling, of ondercuratelestelling of
    # provisioneel bewind van de {Persoon}.

    # Curator (CUR) Een curator is een {NatuurlijkPersoon}
    # die door de rechter is aangewezen om het beheer te voeren over
    # de bezittingen van een {NatuurlijkPersoon} of een {Rechtspersoon}.

    # RechterCommissaris (RCO) - De rechter-commissaris houdt,
    # bij een faillissement, in de eerste plaats toezicht op de {Curator}.

    # Bewindvoerder (BWV) Een bewindvoerder behartigt de financiële
    # belangen van een {NatuurlijkPersoon} die dat zelf
    # (tijdelijk) niet kan of mag.


class Activiteit(models.Model):
    """
    ACT

    Van deze entiteit zijn de entiteiten Activiteiten-CommercieleVestiging},
    {ActiviteitenNietCommerciele Vestiging en ActiviteitenRechtpersoon
    afgeleid.

    Zie ook de toelichting van Activiteiten bij de uitleg van het semantisch
    gegevensmodel in de officiële catalogus, paragraaf 1.5
    """
    # activiteitsomschrijving - De omschrijving van de activiteiten die
    # de {Vestiging} of {Rechtspersoon} uitoefent.

    # SBI-code-codeneeDe codering van de activiteit conform de SBI2008.
    # omschrijving-omschrijvingneeOmschrijving van de activiteit
    # hoofdactiviteit-hoofdactiviteitneeIndicatie die aangeeft welke van
    # de activiteiten de hoofdactiviteit is.


class MaatschappelijkeActiviteit(models.Model):
    """
    MAC

    Een {Maatschappelijke Activiteit} is de activiteit van een
    {Natuurlijk persoon} of {Niet-natuurlijk persoon}.

    De {Maatschappelijke Activiteit} is het totaal van alle activiteiten
    uitgeoefend door een {Natuurlijk Persoon} of een {Niet-natuurlijk Persoon}.
    Een {Maatschappelijke Activiteit} kan ook als {Onderneming} voorkomen.
    """

    # naam - De (statutaire) naam of eerste handelsnaam van de inschrijving.
    naam = models.CharField(max_length=600, blank=True, null=True)

    # kvkNummer - Betreft het identificerende gegeven voor de
    kvknummer = models.CharField(
        unique=True, max_length=8, blank=True, null=True)

    # MaatschappelijkeActiviteit id
    macid = models.DecimalField(
        primary_key=True, max_digits=18, decimal_places=0)

    # datumAanvang - De datum van aanvang van de {MaatschappelijkeActiviteit}.
    datumaanvang = models.DecimalField(
        max_digits=8, decimal_places=0, blank=True, null=True)

    # datumEindeneeDatum - De datum van beëindiging van de
    datumeinde = models.DecimalField(
        max_digits=8, decimal_places=0, blank=True, null=True)

    # {MaatschappelijkeActiviteit}.

    # incidenteelUitlenenArbeidskrachten - die aangeeft of de ondernemer
    # tijdelijk arbeidskrachten ter beschikking stelt en dit niet onderdeel
    # is van zijn 'reguliere' activiteiten.

    # nonMailing- Indicator die aangeeft of de inschrijving haar
    # adresgegevens beschikbaar stelt voor mailing-doeleinden.

    # Communicatiegegeven - MaatschappelijkeActiviteit COM ageleid van
    # communicatiegegevens van inschrijving

    # foreign key naar COM.
    communicatiegegevens = models.ForeignKey(
        'CommunicatieGegevens', null=True, blank=True)

    # Activiteiten - MaatschappelijkeActiviteit ACT De SBI-activiteit(en) van
    # de {MaatschappelijkeActiviteit} is het totaal van alle {SBI-activiteit}
    # en die voorkomen bij de {MaatschappelijkeActiviteit} behorende
    # {NietCommercieleVestigingen} en bij de {Rechtspersoon}.


    # /Locatie-MaatschappelijkeActiviteit
    # LOC postadres/
    # Locatie-MaatschappelijkeActiviteit (LOC)LOC-LOC-LOC
    # bezoekadreshoofdvestiging
    # HR: Vestiging (VES)

    vestiging = models.ForeignKey('Vestiging', blank=True, null=True)

    # activiteiten = models.JSON

    # -MaatschappelijkeActiviteit-VestigingdatumAanvang-

    # VestigingdatumAanvangneeDe datum van aanvang van de relatie tussen
    # de {MaatschappelijkeActiviteit} en de {NietCommercieleVestiging}.

    # datumEindeneeDatumjaDe - De einddatum van de relatie tussen de
    # {MaatschappelijkeActiviteit} en de {NietCommercieleVestiging}.

    # wordt uitgeoefend inHR: NietCommercieleVestiging (NCV)

    # -heeft als eigenaarHR: Persoon (PRS)PRS-

    # Onderneming (OND) - Van een {Onderneming} is sprake indien een
    # voldoende zelfstandig optredende organisatorische eenheid van één
    # of meer personen bestaat waarin door voldoende inbreng van arbeid of
    # middelen, ten behoeve van derden diensten of goederen worden geleverd of
    # werken tot stand worden gebracht met het oogmerk daarmee materieel
    # voordeel te behalen.

    # /kvkNummerjaBetreft- Betreft het identificerende gegeven voor
    # de {Onderneming}, is gelijk aan het KvKNummer van de
    # bijbehorende {MaatschappelijkeActiviteit}

    # totaalWerkzamePersonen - totaal aantal werkzame personen bij de
    # onderneming. Som van fulltime en parttime.

    # fulltimeWerkzamePersonen - aantal fulltime (>15 uur per week)
    # werkzame personen bij de onderneming

    # parttimeWerkzamePersonen - Het aantal parttime (<=15 uur per week)
    # werkzame personen bij de onderneming

    # datumAanvang - De datum van aanvang van de {Onderneming}.

    # datumEindeneeDatum - De datum van beëindiging van de {Onderneming}.

    # wordt uitgeoefend doorHR: Activiteiten-Onderneming (ACT)
    # Overdrachtis overgedragen als / afgesloten

    # datumOverdracht-datumOverdrachtjaDe datum van overdracht
    # van de {Onderneming}.

    # Voortzetting

    # datumVoortzetting- De datum van voortzetting van de {Onderneming}.

    # Onderneming - VestigingdatumAanvangHiermee wordt vastgelegd in welke
    # periode (datumAanvang-datumEinde) de {CommercieleVestiging} bij
    # een {Onderneming} behoort.

    # datumAanvang-De datum van aanvang van de relatie tussen de
    # {Onderneming} en de {CommercieleVestiging}.

    # datumEinde - De einddatum van de relatie tussen de Onderneming en
    # de {CommercieleVestiging}.

    # wordt uitgeoefend inHR: CommercieleVestiging (CVS)


class Vestiging(models.Model):
    """
    VES

    Een {Vestiging} is gebouw of een complex van gebouwen waar duurzame
    uitoefening van activiteiten van een {Onderneming} of
    {Rechtspersoon} plaatsvindt.

    De vestiging is een combinatie van {Activiteiten} en {Locatie}.
    """

    # kenmerkrelatieauthentiekdefinitierelatieauthentiekdefinitie
    # eersteHandelsnaam-
    # vestigingsnummer - Betreft het identificerende gegevens voor
    # de {Vestiging}.

    # datumAanvang-datumAanvangjaDe datum van aanvang van de {Vestiging}.

    # datumEinde-datumEindejaDe datum van beëindiging van de {Vestiging}.

    # datumVoortzetting-datumVoortzettingneeDatum voortzetting van de vestiging

    # Heeft als postadresHR: Locatie (LOC) postadres

    # Heeft als bezoekadresHR: Locatie (LOC)

    # bezoekadres
    # Communicatiegegeven-Vestiging (COM) Samenvoegingneeafgesloten

    # datumsamenvoeging-datumsamenvoegingneeSamenvoeging-datumsamenvoegingneeSamenvoegingneesamengevoegde

    # datumsamenvoeging Samenvoeging samengevoegde -

    # datumsamenvoeging NietCommercieleVestiging (NCV)
    # Een classificatie van de {Vestiging} van de {Maatschappelijke Activiteit}
    # niet zijnde de {Onderneming}.

    # naam - De naam van de {NietCommercieleVestiging}.

    # verkorteNaam- De administratieve naam in het handelsregister indien
    # de naam langer is dan 45 karakters.

    # ookGenoemd- Een andere naam waaronder de vereniging, stichtingen
    # en vereniging van eigenaars ook bekend is.

    # Heeft {Activiteiten} die bij een {NietCommercieleVestiging} horen.

    sbicodehoofdactiviteit = models.DecimalField(
        max_digits=6, decimal_places=0, blank=True, null=True)
    sbicodenevenactiviteit1 = models.DecimalField(
        max_digits=6, decimal_places=0, blank=True, null=True)
    sbicodenevenactiviteit2 = models.DecimalField(
        max_digits=6, decimal_places=0, blank=True, null=True)
    sbicodenevenactiviteit3 = models.DecimalField(
        max_digits=6, decimal_places=0, blank=True, null=True)

    sbiomschrijvinghoofdact = models.CharField(
        max_length=180, blank=True, null=True)
    sbiomschrijvingnevenact1 = models.CharField(
        max_length=180, blank=True, null=True)
    sbiomschrijvingnevenact2 = models.CharField(
        max_length=180, blank=True, null=True)
    sbiomschrijvingnevenact3 = models.CharField(
        max_length=180, blank=True, null=True)

    # HR: Locatie (LOC)

    # nee{Activiteiten} die bij een {NietCommercieleVestiging} horen.
    # CommercieleVestiging (CVS)CVS-CVSneeEen classificatie van de
    # Vestiging van de Onderneming.

    # /totaalWerkzamePersonen- Het totaal aantal werkzame personen bij de
    # vestiging. Som van fulltime en parttime.

    # fulltimeWerkzamePersonen- Het aantal fulltime (>15 uur per week)
    # werkzame personen bij de vestiging

    # parttimeWerkzamePersonen-parttimeWerkzamePersonenneeHet aantal
    # parttime (<=15 uur per week) werkzame personen bij de vestiging

    # Heeft {Activiteiten} die bij een {CommercieleVestiging} horen.HR:
    # Locatie (LOC) Activiteiten die bij een {CommercieleVestiging} horen.

    # export-exportneeIndicatie of de activiteit Export betreft.

    # import-importneeIndicatie of de activiteit Import betreft.

    # NietCommercieleVestiging (NCV) - heeft Handelsnaam

    # datumAanvang De-datumAanvang van de relatie van de {Handelsnaam}
    # met de {Vestiging}.

    # datumEinde De-datumEinde - Datum einde van de relatie van de
    # Handelsnaam met de Vestiging.

    # Handelsnaam (HN)


class Locatie(models.Model):
    """
    LOC

    Een {Locatie} is een aanwijsbare plek op aarde.
    """

    adrid = models.DecimalField(max_digits=18, decimal_places=0)

    # volledigAdres - BAG - Samengesteld adres
    volledigadres = models.CharField(max_length=550, blank=True, null=True)

    # Vrije tekst om een Adres nader aan te kunnen duiden.

    # toevoegingAdres- toevoegingAdres -
    huisnummertoevoeging = models.CharField(
        max_length=5, blank=True, null=True)

    # Afgeschermd - Geeft aan of het adres afgeschermd is of niet.
    afgeschermd = models.BooleanField()

    # Adres(ADR)AdresBinnenlandsAdres
    # postbusnummer-postbusnummer

    # BAGidentificatie (BAG)postbusnummer

    # BAGidentificatieLocatie heeft betrekking op een adresseerbaar object
    # bag-id nummeraanduiding
    # Verblijfsobject ,Standplaats ,Ligplaats:
    # De unieke BAG identificatie van een verblijfsobject, standplaats
    # of ligplaats.

    # BRON = kvkadrm00 identificatieaoa
    bagid = models.CharField(max_length=16, blank=True, null=True)

    # Locatie heeft een adresseerbaarBAG: Nummeraanduidingnee
    # De unieke identificatie van de BAG Nummeraanduiding.

    # BuitenlandsAdres

    # straatHuisnummer- Het straat/huisnummer is een combinatie van de
    straathuisnummer = models.CharField(max_length=220, blank=True, null=True)
    # straat en huisnummer.

    # postcodeWoonplaats- De postcode/woonplaats is de combinatie van
    postcodewoonplaats = models.CharField(
        max_length=220, blank=True, null=True)

    # regio-regiojaRegio is een deel van het land (streek, provincie, etc.)
    regio = models.CharField(max_length=170, blank=True, null=True)

    land = models.CharField(max_length=50, blank=True, null=True)
    # land-landjaDe naam van het land waar het adres zich bevindt.

    # x, y ?
    xcoordinaat = models.DecimalField(
        max_digits=9, decimal_places=3, blank=True, null=True)
    ycoordinaat = models.DecimalField(
        max_digits=9, decimal_places=3, blank=True, null=True)

    geopunt = models.PointField(srid=28992, blank=True, null=True)


class Handelsnaam(models.Model):
    """
    HN

    Een Handelsnaam is een naam waaronder een Onderneming of een
    Vestiging van een Onderneming handelt.

    Een Onderneming mag meerdere Handelsnamen hebben. De Vestiging heeft
    tenminste één, of meerdere, Handelsna(a)m(en) waarmee die naar
    buiten treedt.

    Bij privaatrechtelijke Rechtspersonen is de statutaire naam altijd ook
    een van de Handelsnamen van de bijbehorende Onderneming.

    De Handelsnamen van de Onderneming zijn een opsomming van alle
    Handelsnamen van alle Vestigingen.

    Indien een Handelsnaam dubbel voorkomt zal deze slechts éénmaal
    worden getoond.
    """

    # datumAanvang - Datum aanvang van de Handelsnaam

    # datumEinde - Datum einde van de Handelsnaam

    # handelsnaam - De Handelsnaam van de vestiging waaronder gehandeld wordt.

    # OndernemingHandelsnaamRelatie (OHR) - aanvang van de relatie
    # van de Handelsnaam met de Onderneming.

    # datumEinde - Datum einde van de relatie van de Handelsnaam
    # met de Onderneming.
    # Onderneming (OND) heeft handelsnaam


class CommunicatieGegevens(models.Model):
    """
    COM

    In het handelsregister worden over een Rechtspersoon waaraan geen
    Onderneming toebehoord en die geen Vestiging heeft of van een
    Vestiging, opgenomen:

    et telefoonnummer, het faxnummer, het e-mailadres en het internetadres
    """

    # BRON DATA KVKMACM00
    macid = models.DecimalField(
        primary_key=True, max_digits=18, decimal_places=0)

    # Domeinnaam -  Het internetadres (URL).
    domeinnaam1 = models.CharField(max_length=300, blank=True, null=True)
    domeinnaam2 = models.CharField(max_length=300, blank=True, null=True)
    domeinnaam3 = models.CharField(max_length=300, blank=True, null=True)

    # EmailAdres - waarop de ondernemen gemaild kan worden.
    emailadres1 = models.CharField(max_length=200, blank=True, null=True)
    emailadres2 = models.CharField(max_length=200, blank=True, null=True)
    emailadres3 = models.CharField(max_length=200, blank=True, null=True)

    # toegangscode - De internationale toeganscode waar
    # (telefoon of fax) betrekking heeft.
    toegangscode1 = models.DecimalField(
        max_digits=4, decimal_places=0, blank=True, null=True)
    toegangscode2 = models.DecimalField(
        max_digits=4, decimal_places=0, blank=True, null=True)
    toegangscode3 = models.DecimalField(
        max_digits=4, decimal_places=0, blank=True, null=True)

    # communicatieNummer - is het telefoon- of faxnummer zonder opmaak.
    communicatienummer1 = models.CharField(
        max_length=15, blank=True, null=True)
    communicatienummer2 = models.CharField(
        max_length=15, blank=True, null=True)
    communicatienummer3 = models.CharField(
        max_length=15, blank=True, null=True)

    soort1 = models.CharField(max_length=10, blank=True, null=True)
    soort2 = models.CharField(max_length=10, blank=True, null=True)
    soort3 = models.CharField(max_length=10, blank=True, null=True)
    # soortCommunicatieNummer- (Telefoonnummer en Faxnummer)


class RechterlijkeUitspraak(models.Model):
    """
    UIT

    Abstracte klasse Rechtelijke Uitspraak

    Een uitspraak van een rechter die invloed heeft op de
    registratie in het handelsregister. Het betreft hier een
    abstractie om andere klassen daadwerkelijk van een
    RechtelijkeUitspraak gegevens te kunnen voorzien.

    RechtelijkeUitspraak heeft de volgende relaties:


    """

    # Uitspraak (UIT) aanvang door

    # Uitspraak (UIT) einde door

    # datumUitspraak - Datum waarop de uitspraak door de rechter is gedaan
    # Gerecht (GER) - De naam van het gerecht
    # plaatsvindt - Plaats waar het gerecht is gevestigd


class Kapitaal(models.Model):
    """
    KAP

    """

    # bedrag- Het bedrag van het kapitaal uitgedrukt in de valuta en de waarde.

    # AantalAandelen - Het aantal aandelen van de genoemde
    # soort en waarde bij Aandeel.

    # Aandeelsoort - Beschrijving van het soort aandeel.

    # waarde - Waarde (nominaal) per aandeel.
