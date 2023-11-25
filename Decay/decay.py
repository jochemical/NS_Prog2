# programmanaam: Decay
# Hoofdstuk 4:

from math import * # importeert alle functies van de math-bilbiotheek
from numpy import * # importeert alle functies van de numpy-bilbiotheek
import matplotlib.pyplot as plt # importeert de matplotlib.pyplot bilbiotheek onder de verwijzing plt

# Opdracht 4

N0 = 10 # begin-hoeveelheid Bromine
T_half = 16.1 # halveringstijd
dt = 0.01*T_half # tijdstapgrootte
t_max = 750 # aantal tijdstippen
t = 0 # klok
L = - math.log(2)/T_half # vervalconstante Bromine

# Euler Methode

Lijst_t = [0] # reeks voor de x-as
ELijst_NB = [N0] # Bromide reeks voor de y-as
ELijst_NS = [0] # Selenium reeks voor de y-as
ENB_t1 = N0 # dit is de beginwaarde voor Bromide in de onderstaande loop
ENS_t1 = 0 # dit is de beginwaarde voor Selenium in onderstaande loop

for tijdstap in range(0,t_max):
    ENB_t2 = ENB_t1 + (L*ENB_t1*dt) # rekent nieuwe waarde uit voor Bromide
    ENS_t2 = ENS_t1 + ((-L)*ENB_t1*dt) # rekent nieuwe waarde uit voor Selenium
    t = t + dt # klok
    Lijst_t.append(t)
    ELijst_NS.append(ENS_t2)
    ELijst_NB.append(ENB_t2)
    ENB_t1 = ENB_t2 # zorgt dat de loep doorrekend met de nieuwe waarde van Bromide
    ENS_t1 = ENS_t2 # zorgt dat de loep doorrekend met de nieuwe waarde van Selenium


# Analytische oplossing

t = 0 # reset klok
ALijst_NB = [N0]
ALijst_NS = [0]

for tijdstap in range(0,t_max):
    t = t + dt
    ANB = N0 * math.exp(L * t)
    ANS = N0 - ANB
    ALijst_NB.append(ANB)
    ALijst_NS.append(ANS)


# Runga-Kutta methode (4e orde)
t = 0 # reset klok
RKLijst_NB = [N0] # Lijst voor Bromide-waarden
RKLijst_NS = [0] # Lijst voor Selenium-waarden
RKNB_t1 = 10 # Beginwaarde Bromide
RKNS_t1 = 0 # Beginwaarde Selenium

for tijdstap in range(0,t_max):
    # Voor de Runga-Kutta methode worden eerst de 4 k-waarden uitgerekend:
    k1 = dt * L * RKNB_t1
    RKNB_t2 = (RKNB_t1 + k1 * 0.5)
    k2 = dt * L * RKNB_t2
    RKNB_t3 = RKNB_t1 + k2 * 0.5
    k3 = dt * L * RKNB_t3
    RKNB_t4 = RKNB_t1 + k3 
    k4 = dt * L * RKNB_t4
    
    dN = (float(1)/6) * (k1 + 2 * k2 + 2 * k3 + k4)
    RKNB_T2 = RKNB_t1 + dN # rekent de nieuwe waarde uit voor Bromide
    RKNS_T2 = RKNS_t1 - dN # rekent de nieuwe waarde uit voor Selenium
    RKLijst_NB.append(RKNB_T2)
    RKLijst_NS.append(RKNS_T2)

    RKNB_t1 = RKNB_T2 # zorgt ervoor dat je doorrekend op nieuwe waarde van RKNB_t1
    RKNS_t1 = RKNS_T2 # zorgt ervoor dat je doorrekend op nieuwe waarde van RKNS_t1


# precisie test

PLijst_E = [] # Lijst van de afwijkingen van de Euler methode
PLijst_RK = [] # Lijst van de afwijkingen van de Runga-Kutta methode

# precisie van de Euler methode:

somE = 0 # variabele voor cumulatieve afwijking van de Euler methode
for afw in range(0,t_max+1):
    testE = abs(float((ELijst_NB[afw] - ALijst_NB[afw]))/ALijst_NB[afw])
    somE = somE + testE # hoe groter de afwijking, hoe groter deze som    
    PLijst_E.append(testE)
# precisie van de Runga-Kutta methode:

somRK = 0 # variabele voor cumulatieve afwijking van de Runge-Kutta methode
for afw in range(0,t_max+1):
    testRK = abs(float((RKLijst_NB[afw] - ALijst_NB[afw]))/ALijst_NB[afw])
    somRK = somRK + testRK # hoe groter de afwijking, hoe groter deze som    
    PLijst_RK.append(testRK)


# Uitvoer printen en plotten:        
print 'Opdracht Hoofdtstuk 4:'

# uitvoer precisie:

print
print 'Cumulatieve afwijking van de Euler methode:'
print somE
print 'Cumulatieve afwijking van de Runga-Kutta methode:'
print somRK
print '(De laagste waarde heeft de hoogste precisie.)'

# Euler grafiek
plt.subplot(211)
plt.xlabel('Tijd')
plt.ylabel('N')
#plt.plot(Lijst_t,ELijst_NB,'g') # Euler grafiek voor Bromide: groen
#plt.plot(Lijst_t,ELijst_NS,'y') # Euler grafiek voor Selenium: geel

# Analytische grafiek
#plt.plot(Lijst_t,ALijst_NB,'k') # Analytische grafiek voor Bromide: zwart
#plt.plot(Lijst_t,ALijst_NS,'k') # Analytische grafiek voor Selenium: zwart

# Runga-Kutta grafiek
plt.plot(Lijst_t,RKLijst_NB,'b') # Runga-Kutta grafiek voor Bromide: blauw
plt.plot(Lijst_t,RKLijst_NS,'r') # Runga-Kutta grafiek voor Selenium: rood 

# precisies plotten
plt.subplot(212)
plt.xlabel('Tijd')
plt.ylabel('Afwijking')
plt.plot(Lijst_t,PLijst_E,'y') # afwijking Euler: geel 
plt.plot(Lijst_t,PLijst_RK,'b') # afwijking Runga-Kutta: blauw

# instellingen grafiek
plt.xlim(0,dt * t_max + 5)
#plt.ylim(0,N0 + 0.25 * N0)
plt.show()

# Einde programma:
# einde programma
print
print 'end programme' # print 'end programme'
