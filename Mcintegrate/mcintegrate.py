
# Programma-naam: Numerieke intergratie

import math as mth
import random as rnd
import matplotlib.pyplot as plt

# Hoofdstuk 8

# 8.3 Opdracht 2: Numerieke integratie

# Aantal hit-miss-punten:
it = 1000 

# Defenieer cirkel:
R = 1 # straal cirkel
opp_cirkel = mth.pi * R**2

# Defenieer vierkant:
x_min = - 1
x_max = 1
y_min = -1
y_max = 1
delta_x = x_max - x_min
delta_y = y_max - y_min
opp_4kant = delta_x * delta_y

# Numerieke Integratie:
hits = 0 # telt hoeveel punten de cirkel raken
miss = 0 # telt hoeveel punten de cirkel niet raken

for i in range(1,it):
    x = x_min + rnd.random() * delta_x
    y = y_min + rnd.random() * delta_y
    r = mth.sqrt(x**2 + y **2)
    if r < 1:
        hits += 1
    else:
        miss += 1

ratio_ht = float(hits) / (miss + hits) # ratio tussen het aantal hits 
# en het totaal aantal punten

opp_cir_num = ratio_ht * opp_4kant # benadering van het oppervlak van de cirkel

# pi kan numeriek worden berekend op basis 
# van het oppervlak en de straal van de cirkel:
Pi = float(opp_cir_num) / (R**2) 

# ratio_ht is gelijk aan de ratio van het oppervlak van de cirkel en het vierkant:
ratio_circ_4kant = float(opp_cir_num) / opp_4kant

# Uitvoer printen
print 'De numeriek berekende waarde van pi is %f.' % Pi 
print 'De ratio_ht (%f) is gelijk aan ratio_circ_4kant (%f)' % (ratio_ht,ratio_circ_4kant)
print # witregel


# Integraal normaalverdeling:

it2 = 100 # maximaal aantal hits+miss punten

def normal(x,s,m): # functie voor normale verdeling 
    # (m = gemiddelde, s = standaardafwijking)
    f = (1/(s * mth.sqrt(2 * mth.pi))) * mth.exp(-0.5 * ((x - m)/s)**2)
    return f

# Defenieer normaalverdeling:
m = 0
s = 1

# Defenieer vierkant:
x2_min = - 1
x2_max = 1
y2_min = 0
y2_max = normal(m,s,m)
delta_x2 = x2_max - x2_min
delta_y2 = y2_max - y2_min
opp_4kant2 = delta_x2 * delta_y2


L_opp_norm = [] # lijst voor oppervlakten onder de Gauss-curve
L_N = [] # lijst voor aantal iteraties
L_afw = [] # lijst voor afwijkingen van het oppervlakte
L_afw_hy = [] # lijst met hypothetische afwijkingen om berekende afwijkingen 
# mee te vergelijken


for N in range(1,it2):
    
    # numerieke integratie
    hits2 = 0
    miss2 = 0
    
    # Hits-Miss methode:
    for j in range(1,N):
        x2 = x2_min + rnd.random() * delta_x2
        y2 = y2_min + rnd.random() * delta_y2
        f2 = normal(x2,s,m)
        if y2 < f2:
            hits2 += 1     
        else:
            miss2 += 1
    if hits2 + miss2 > 0: # voorkomt delen door 0
        # benadering van de integraal:
        opp_norm = (float(hits2)/(hits2 + miss2)) * opp_4kant2 
    if hits2 + miss2 == 0:
        opp_norm = 0
    L_N.append(N)
    L_opp_norm.append(opp_norm)
    
    # Afwijking berekenen:
    afw = abs(opp_norm - 0.68)
    L_afw.append(afw)

    # Hypothetische afwijking berekenen:
    afw_hy = 1./mth.sqrt(N) # hypothetische afwijking
    L_afw_hy.append(afw_hy)
      

print 'De benadering van het oppervlak onder de Gauss-curve met %f aantal iteraties is %f.' % (it2,opp_norm)
print 'Dit was te verwachten, omdat het oppervlak onder de Gauss-curve tussen de waarden van de standaarddeviatie gelijk is aan 68 procent.'

# Plotten van de waarden van de integraal als functie van het aantal punten it2:
plt.subplot(211)
plt.plot(L_N,L_opp_norm,'b')
plt.xlabel('aantal iteraties')
plt.ylabel('oppervlakte onder Gauss-curve')

# Plotten van de afwijkingen
plt.subplot(212)
plt.plot(L_N,L_afw,'y')
plt.plot(L_N,L_afw_hy,'b')
plt.xlabel('Aantal iteraties')
plt.ylabel('Relatieve afwijking')
plt.show()

