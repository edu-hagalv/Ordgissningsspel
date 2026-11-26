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
    "beskaffenhet", "tillmötesgående", "förutsättningslös", "motsägelsefull",
    "omvälvande", "ofrånkomlig", "förkovra", "eftertanke", "svårbegriplig"]   #alla ord som kan dyka upp i en lista

spela_igen = "ja"      #variabel för att spela igen
alfabet = "abcdefghijklmnopqrstuvwxyzåäö"     # alla bokstäver som kan användas

while spela_igen == "ja":   # skapar en loop där man kan spela igen så länge variabeln spela_igen är True.
    hemligt_ord = rand.choice(ord_)    # Väljer ut ett slumpmäsigt ord från listan ovanför.
    dolt_ord = ["*"] * len(hemligt_ord)  # visar det dolda ordet som stjärnan.
    försök = 7               #antal bokstäver man kan gissa fel innan man förlorat.
    fel_gissningar = []          #alla bokstäver i en lista som fylls på medans man kör genom .append
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
