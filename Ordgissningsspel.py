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
dolt_ord = ["*"] * len(hemligt_ord)
forsok = 7
fel_gissningar = []
print(len(hemligt_ord))

while forsok > 0 and "*" in dolt_ord:
    print("".join(dolt_ord))
    print(f"Försök kvar: {forsok}")
    print(f"Felgissningar: {fel_gissningar}")
   
    gissning = input("Gissa en bokstav: ").lower()