def sn(prompt):
    return input(prompt).lower()[0] == 's'

def quit():
    input("Premi invio per uscire.")
    raise SystemExit

def scelta(prompt, *answers):
    print(prompt)
    for i in range(len(answers)):
        print(f"{i}. {answers[i]}")
    print()
    return int(input("scelta: "))

def sta_vedendo_qualcuno():
    x = scelta("La tua crush si vede con qualcuno in modo amoroso o erotico per caso?", 'si', 'no')
    if x == 0:
        definisci_vedersi()
    elif x == 1:
        come_la_conosci()
    quit()

def definisci_vedersi():
    x = scelta("Definisci vedersi.", "Hanno degli appuntamenti, ma abbastanza casual. niente di ufficiale", "Sono proprio fidanzati.")
    if x == 0:
        if not sn("è davvero così casual? dimmi la verità. "):
            print("Non glielo dire se non vuoi dei gran casini.")
            quit()
        multi_o_singolo()
    print("Non glielo dire se non vuoi dei gran casini.")
    quit()

def multi_o_singolo():
    if sn("Si vede con una sola persona? "):
        situationship()
    print("Diglielo, ma anche tu potresti finire per essere 'uno dei tanti'.")
    quit()

def situationship():
    print("Bene bene bene. Sono in una situationship. Cioè una relazione semi-amorosa ma non ufficiale in nessun modo.")
    if sn("In quella 'relazione', si fanno trascinare dall'altro? "):
        print("Puoi dirglielo, ma è probabile che non accetteranno per via della persona con cui sono in 'relazione' ora.")
        quit()
    print("Non glielo dire a meno che tu non voglia farti trascinare in una situationship come l'altro tizio.")
    quit()

def come_la_conosci():
    if sn("La conosci nella vita reale, vero? Non è che l'hai conosciuta online, vero? Sì o no: "):
        irl()
    else:
        online_person()

def online_person():
    if sn("La tua crush è una celebrità? "):
        print("Voglio dire, puoi anche dirglielo, tanto non lo sapranno mai e ci sono 10000 persone come te.")
        quit()
    if sn("Li conosci da un'app di incontri? "):
        print("Diglielo, ma tecnicamente dovrebbero saperlo già se l'app vi ha matchati.")
        quit()
    if sn("L'hai mai vista nella vita reale? "):
        print("Diglielo.")
        quit()
    print("Puoi dirglielo, ma forse lei non ti piacerà davvero quando TU la vedrai e sarai nei guai.")
    quit()

def irl():
    x = scelta("Ma quindi come la conosci? Scegli la prima risposta corretta.", "attraverso amicizie", "è solo a scuola con me", "è al lavoro con me", "è sconosciuta, la vedo in posti pubblici qualche volta.")
    if x == 0:
        amici()
    if x == 1:
        scuola()
    if x == 2:
        lavoro()
    print("Bruh diglielo, tanto che hai da perdere? (Al massimo cambi negozio.)")
    quit()

def lavoro():
    do_you_fear_being_fired()
    a_che_livello()

def a_che_livello():
    x = scelta("La tua crush a che livello è nella gerarchia dell'azienda? ", "Al mio livello", "è mia superiore", "è una mia sottoposta")
    if x == 0:
        stesso_livello()
    if x == 1:
        superiore()
    sottoposta()

def sottoposta():
    if sn("Sul serio, c'è DAVVERO una possiilità che tu le piaccia?"):
        print("SE glielo dici, Risorse Umane lo verrà a sapere. Quindi no.")
        quit()
    print("no bruh")
    quit()

def superiore():
    print("C'è una possibilità dell'1%% che sarai promosso e una possibilità del 99%% che sarai licenziato subito.")
    quit()

def stesso_livello():
    if sn("Ti piace veramente? Quindi non è che ti piace solo perchè le sei sempre vicino? "):
        if sn("Mi stai dicendo che ti piacerebbe anche se non la vedessi sempre? DAVVERO SUL SERIO? "):
            print("Decidi tu. O sarà la migliore relazione della tua vita, o non potrai più guardarla in faccia.")
            quit()
        no_scuola()
    no_scuola()

def do_you_fear_being_fired():
    if sn("Hai paura di essere licenziato? "):
        print("Non glielo dire. Probabilmente è contro le regole.")
        quit()

def scuola():
    if sn("vedi la tua crush spesso, tipo siete nella stessa classe o qualcosa? "):
        scuola_vedi_Spesso()
    print("E diglielo, non perdi niente.")
    quit()

def scuola_vedi_Spesso():
    if sn("Ti piace veramente? Quindi non è che ti piace solo perchè le sei sempre vicino? "):
        if sn("Mi stai dicendo che ti piacerebbe anche se non la vedessi sempre? "):
            print("Diglielo. O sarà la migliore relazione della tua vita, o non potrai più guardarla in faccia per tutta la scuola. Però, la scuola non è tutta la vita.")
            quit()
        no_scuola()
    no_scuola()

def no_scuola():
    print("Non glielo dire perchè rovinerà la funzione che lei attualmente ha nella tua vita, cioè di pensare a lei quando ti annoi.")
    quit()

def amici():
    if sn("Sei amico personalmente della tua crush, quindi non attraverso un'altra persona? "):
        siete_in_un_gruppo()
    else:
        if scelta("Avete un amico in comune?", "si", "no, è la parente di un mio amico.") == 0:
            siete_in_un_gruppo()
        else:
            parente_amico()

def parente_amico():
    print("Oh Cielo.")
    if sn("è la sorella di un tuo amico? "):
        sorella()
    sn("La tua crush è un genitore di un tuo amico? ")
    print("Non voglio essere colpevole dello schifo che succederà. Non glielo dire, a meno che tu non sia certo che è un caso speciale e la passerai liscia.")
    quit()

def sorella():
    print("Oh Cielo.")
    if sn("Onestamente, pensi che ti piaccia solo perchè è la sorella del tuo amico? "):
        print("non glielo dire. non lo fare.")
        quit()
    if sn("La prospettiva di stare con lei è più importante del fatto che per un po' il tuo amico ti odierà? "):
        print("beeeh... diglielo ma sappi che sarà una telenovela.")
        quit()
    print("non glielo dire.")
    quit()

def siete_in_un_gruppo():
    if sn("Siete in un gruppo di amici insieme, cioè non è un'amicizia 1 a 1? "):
        gruppo_di_amici_si()
    else:
        print("\nDovresti dirglielo secondo me, ma ricorda che se tu non le piaci le vostre relazioni non saranno più come prima.")
        print("Tuttavia, visto che siete amici solo voi due, potrebbe essere l'idea migliore.")
        quit()

def gruppo_di_amici_si():
    if sn("La tua crush è mai uscita in modo amoroso con qualcun altro del gruppo di amici? "):
        definisci_vedersi_amici()
    else:
        mai_uscita_amici()

def mai_uscita_amici():
    if sn("la tua crush piace anche a qualcun altro del gruppo? "):
        if sn("è possibile che in effetti tu piaccia a lei? "):
            block()
        else:
            print("voglio dire... io non lo farei...")
            quit()
    else:
        block()

def definisci_vedersi_amici():
    if scelta("La tua crush...", "...usciva in modo casual ma amoroso con qualcun altro del gruppo o...", "...era in qualcosa di più serio tipo appuntamenti o una relazione?") == 0:
        yeah_amici()
    else:
        dating_nel_gruppo()

def dating_nel_gruppo():
    x = scelta("Quanto era seria la relazione?", "hanno fatto un solo appuntamento e non si piacevano davvero", "si sono visti per qualche settimana ma non troppo serio", "facevano sul serio, hanno conosciuto i genitori o altro")
    if x == 0:
        yeah_amici()
    else:
        controllo_bastardaggine_amici()

def controllo_bastardaggine_amici():
    d = int(input("Per quanti mesi la tua crush e questo tuo amico si sono incontrati? "))
    f = int(input("Da 1 a 10, quanto sei amico dell'ex della tua crush? "))
    g = int(input("Quanti mesi fa si sono lasciati esattamente? "))
    t = (d * f) / g
    if g < 2 or t > g:
        print("\nNOOO! NON GLIELO DIRE! ASPETTA FIDATI.")
        quit()
    print("\nProcedi al prossimo passo con estrema attenzione.")
    if sn("Almeno uno di loro due prova ancora qualcosa per l'altro? "):
        block()
    if not sn("sicuro? "):
        block()
    yeah_amici()

def block():
    if sn("Quello che provi per la tua crush è più importante del fatto che il tuo gruppo di amici POTREBBE cambiare per sempre e in peggio? "):
        print("Diglielo allora")
        quit()
    print("No, non glielo dire.")
    quit()

def yeah_amici():
    print("Si......... fallo...   MA solo se ne vale la pena considerando che una cosa del genere probabilmente cambierà il vostro gruppo di amici per sempre e forse in peggio.")
    quit()

def intro():
    print("Questo è un programma che, se tu hai una crush su qualcuno, ti fa diverse domande e poi ti dice se è il caso di dichiararti a lei oppure no.")

intro()
sta_vedendo_qualcuno()
