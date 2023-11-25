# programmanaam: Primes
# Hoofdstuk 3: Opdracht 1,2 en 3:

L_priem  = [2] # lijst met priemgetallen, start met eerste priemgetal 2
P_max = 1000 # maximaal aantal priemgetallen
P_new = 3 # initieel priemgetal en voorgaand priemgetal
L_nonP = [] # tijdelijke lijst met aaneengesloten niet-priemgetallen
L_nonP_max = [] # lijst met de langste aaneengesloten reeks niet-priemgetallen
nonP_max = 0 # houdt bij wat de maximale hoeveelheid
len_L_nonP_max = 0 # variabele dat bijhoudt wat de lengte is van de lijst van tijdelijk aaneengesloten niet priemgetallen

while len(L_priem) < P_max: # controleert of het aantal gevonden priemgetallen de maximale hoeveelheid priemgetallen niet overschreidt
    for deler in range(2,P_new):
        P_test = P_new % deler # test of P_new gedeeld kan worden door een lager getal
        if P_test == 0: # ieder getal dat door een lager getal te delen is (behalve 1), is geen priemgetal    
            L_nonP.append(P_new) # voegt het niet-priemgetal toe aan de tijdelijke lijst L_nonP
            break # stopt de for-loop indien P_new geen priemgetal blijkt te zijn                        
    else: # indien de for-loop helemaal kan worden doorlopen is P_new een priemgetal
        if len(L_nonP) > len_L_nonP_max:
            len_L_nonP_max = len(L_nonP) # stelt de lengte van de langste lijst niet priemgetallen (len_L_nonP_max) gelijk aan de lengte van de nieuw gevonden langere lijst 
            L_nonP_max = L_nonP # Stelt de langste lijst niet priemgetallen gelijk aan de nieuw gevonden langere lijst niet-priemgetallen
        L_nonP = [] # wist de lijst L_nonP
        L_priem.append(P_new) # voegt nieuw priemgetal toe aan de lijst L_priem            
    P_new = P_new + 1 # na de test of P_new een priemgetal is of niet, wordt een nieuwe potentieel priemgetal opgesteld
    # Voor opdracht 1 kan '+1' uit bovenstaande regel worden vervangen voor '+2' om berekening te versnellen.
    
print('Uitvoer opdracht 1:')
print('De lijst met de eerste 1000 priemgetallen bestaat uit:')
print L_priem # print de lijst met priemgetallen
print('Het 1000e priemgetal is:')
print L_priem[999] # print het 1000e priemgetal
print # print witregel

print('Uitvoer opdracht 2:')
print('De langste aaneengesloten reeks van niet priemgetallen bestaat uit:')
print L_nonP_max # print de lijst met de langste aaneengesloten niet-priemgetallen
print('De langste aaneengesloten reeks van niet priemgetallen heeft de volgende hoeveelheid getallen:')
print len_L_nonP_max # print hoeveelheid priemgetallen in L_nonP_max
        











