import random as rand
ord_ = ["yxa", "kameleont", "jazzmusik", "yoghurt", "lyx", "fotboll"
    "vederkvickelse", "oförvitlig", "obskyr", "förnumstig", "vederstygglig",
    "kontradiktion", "ambivalent", "prokrastinera", "perplex", "prekär",
    "excentrisk", "obsolet", "retorik", "förbehållsam", "lakonisk",
    "förklenande", "idiosynkratisk", "kontemplera", "subtil", "perifer",
    "antites", "paradox", "inkonsekvent", "desillusionerad", "melankolisk",
    "försåtlig", "besynnerlig", "vedertagen", "överhängande", "förhärskande",
    "tillkortakommande", "förvillelse", "förnimmelse", "misshaglig", "oförsonlig",
    "efemär", "prekognition", "förkovran", "tillintetgöra", "försumbar",
    "oumbärlig", "förevändning", "förbehåll", "förvanskning", "godtycklig",
    "hänsynslös", "förtrytelse", "förargelse", "vidlyftig", "omständlig",
    "tvetydig", "förtegen", "högtravande", "mångfacetterad", "genomgripande",
    "föreställningsförmåga", "vedermöda", "förskansning", "obestridlig", "förgänglig",
    "förkroppsliga", "åskådliggöra", "försumlighet", "inskränkt", "självförhärligande",
    "förnäm", "oförklarlig", "till synes", "konsekvent", "diskrepans",
    "fragmentarisk", "perception", "intrikat", "komplexitet", "resonemang",
    "förförståelse", "eftertänksam", "självbespegling", "omdömesgill", "förhastad",
    "vidskeplig", "obarmhärtig", "förbehållslös", "oförtruten", "oupphörlig",
    "tillförlitlighet", "genmäle", "förvillelse", "illavarslande", "anspråkslös",
    "beskaffenhet", "tillmötesgående", "förutsättningslös", "motsägelsefull", "omvälvande",
    "ofrånkomlig", "förkovra", "eftertanke", "svårbegriplig"]

spela_igen = "ja"
alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

while spela_igen == "ja":
    hemligt_ord = rand.choice(ord_)
    dolt_ord = ["*"] * len(hemligt_ord)
    försök = 7
    fel_gissningar = []
    print(f"Du ska gisse ett ord på {len(hemligt_ord)} bokstäver\n------------------------------------\n")

    while försök > 0 and "*" in dolt_ord:
        print("".join(dolt_ord))
        print(f"Antal försök: {försök}")
        print(f"Felgissningar: {fel_gissningar}")
       
        gissning = input("Gissa en bokstav: ").lower()
        print("--------------------\n")
       
        if len(gissning) != 1 or gissning not in alfabet:
            print("Felmeddelande! Försök vänligen igen: ")
        elif gissning in fel_gissningar or gissning in dolt_ord:
            print("Du har redan gissat på den bokstaven!\n")
        elif gissning in hemligt_ord:
            for i in range(len(hemligt_ord)):
                if hemligt_ord[i] == gissning:
                    dolt_ord[i] = gissning
        else:
            fel_gissningar.append(gissning)
            försök = försök - 1

    if "*" not in dolt_ord:
        print(f"Grattis, du vann! Ordet var: {hemligt_ord}\n")
    else:
        print(f"Du förlorade! Ordet var: {hemligt_ord}\n")

    spela_igen = input("Vill du spela igen? (ja/nej): ").lower()
