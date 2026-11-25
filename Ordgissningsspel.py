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

hemligt_ord = rand.choice(ord_)
antal_bokstäver = len(hemligt_ord)
dolt_ord = ["*"] * antal_bokstäver
försök = 7
fel_gissningar = []

print(f"Du ska gissa ett ord bokstav för bokstav på {antal_bokstäver} täcken\nAnge din Gissning")
print(len(hemligt_ord))

while försök > 0 and "*" in dolt_ord:
    print("".join(dolt_ord))
    print(f"Försök kvar: {försök}")
    print(f"Felgissningar: {fel_gissningar}")
   
    gissning = input("Gissa en bokstav: ").lower()