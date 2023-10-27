text="chersétudiantsdelaclasseran1aujourdhuinousvoulonsvousrappeleràquelpointvousêtesexceptionnelsvousavezentreprisunvoyagepassionnantverslemondedelaprogrammationetvousavezdéjàparcouruunegrandepartieducheminlesdéfisquiseprésententàvouspeuventsemblerintimidantsmaisnoubliezjamaisquevousavezlepouvoirdelessurmonterlaprogrammationnestpasseulementunensembledecompétencestechniquescestuneformedartchaquelignedecodequevousécrivezestuneœuvredartensoiuneexpressiondevotrecréativitéetdevotreingéniositévousavezlepotentieldecréerdesapplicationsdessiteswebetdeslogicielsquichangerontlemondenayezpaspeurdeserreurscarcesontleserreursquivousfontgrandirchaquebugquevouscorrigezchaqueproblèmequevousrésolvezvousrapprochedelamaîtrisedecettedisciplinecomplexelesdifficultésnesontquedesopportunitésdéguiséespourapprendreetgrandirnoubliezpasnonplusquevousnêtespasseulsdanscetteaventurevotreclasseestuneéquipeunecommunautédepersonnespartageantlamêmepassionetlesmêmesdéfisentravaillantensembleenpartageantvosconnaissancesetenvoussoutenantmutuellementvouspouvezaccomplirdeschosesincroyablesvousavezchoisiuncheminexigeantmaisaussiincroyablementgratifiantvousêteslescréateursdedemainlesconstructeursdufuturneperdezjamaisdevuevosrêvesetvosaspirationscontinuezàtravaillerduràrestercurieuxetàrepousservoslimitesnouscroyonsenvousetnoussommesimpatientsdevoirlesmerveillesquevouscréerezalorsenavantdéveloppeursran1!lemondeabesoindevotretalentdevotrepassionetdevotredéterminationvousêtescapablesdetoutetnoussommesfiersdevousaccompagnerdanscetteaventureextraordinaireboncourageetquelecodesoitavecvous!avectoutnotresoutienléquipemns".lower()






cpt_max = 0 
letter_max = ''

for letter in text : 
    cpt = 0
    for letter_to_compare in text : 
        if letter == letter_to_compare and letter != "":
            cpt = cpt + 1
            if letter == "e" and letter_to_compare == "ê" or letter_to_compare == "é" or letter_to_compare == "è" or letter_to_compare == "ë" :
                cpt = cpt + 1
            if letter == ["ç"] and letter_to_compare == "c" :
                cpt = cpt + 1
            if letter == ["î","ï"] and letter_to_compare == "i" :
                cpt = cpt + 1
            if letter == ["ô","ö"] and letter_to_compare == "o" :
                cpt = cpt + 1
            if letter == ["û","ü"] and letter_to_compare == "u" :
                cpt = cpt + 1
        if cpt > cpt_max :
            cpt_max = cpt
            letter_max = letter

print(f"La lettre la plus présente est {letter_max} avec {cpt_max} occurences.")