
# Programma-naam: Werpen van toevalsgetallen

import math as mth
import random as rnd
import matplotlib.pyplot as plt

# Hoofdstuk 8

# 8.2 Opdracht 1: Werpen van toevalsgetallen

OG1 = - 5 # Ondergrens
BG1 = 5 # Bovengrens
delta1 = BG1 - OG1

N1 = 20 # Aantal toevalsgetallen
L_T = [] # Lijst met toevalsgetallen

for i in range(0,N1):
    T = OG1 + rnd.random() * delta1 # Toevalsgetal tussen -5 en 5
    L_T.append(T)

# Gemiddelde berekenen van de toevalsgetallen:
somL_T = 0 # variabele voor de som van de toevalsvariabelen
for j in range(0,N1):
    somL_T += L_T[j]

M = somL_T / N1 # gemiddelde van de lijst toevalsgetallen

# Standaarddeviatie berekenen van de toevalsvariabelen:
som_afwL_T = 0 # variabele voor de som van de afwijking
for k in range(0,N1):
    som_afwL_T += (L_T[k] - M)**2

S = mth.sqrt((1./(N1 - 1)) * som_afwL_T) # standaard afwijking

print 'Het gemiddelde van de randomgetallen is:'
print M
print 'De standaardafwijking van de randomgetallen is:'
print S


# Werpen van toevalsvariabelen volgens een normaalverdeling:

N2 = 2000 # aantal keer werpen van de toevalsvariabele volgens normaalverdeling
m = 0 # gemiddelde van de normaalverdeling
s = 1 # standaarddeviatie van de normaalverdeling

a = - 5 # Ondergrens
b = 5 # Bovengrens
delta_ab = b - a

def normal(x,s,m): # functie voor normale verdeling 
    # (m = gemiddelde, s = standaardafwijking)
    f = (1/(s * mth.sqrt(2 * mth.pi))) * mth.exp(-0.5 * ((x - m)/s)**2)
    return f

# rnd.random.seed() # zorgt voor reproduceerbaarheid van het randomgetal

# Randomgetallen werpen die de normale verdeling volgen - Hit or Miss methode
f_max = normal(m,s,m)
L_TN = [] # Lijst met toevalsgetallen volgens een normaalverdeling
for l in range(0,N2):
    x = a + rnd.random() * delta_ab # Toevalsgetal tussen a en b
    f = normal(x,s,m)
    r = 0 + rnd.random() * f_max
    if r < f:
        L_TN.append(x)

# Controleren van het gemiddelde en de standaarddeviatie:

# Gemiddelde testen van de toevalsgetallen:

somL_TN = 0 # variabele voor de som van de toevalsvariabelen
for q in range(0,len(L_TN)):
    somL_TN += L_TN[q]

MN = somL_TN / N2 # gemiddelde van de lijst toevalsgetallen

# Standaarddeviatie testen van de toevalsvariabelen:

som_afwL_TN = 0 # variabele voor de som van de afwijking
for t in range(0,len(L_TN)):
    som_afwL_TN += (L_TN[t] - MN)**2

SN = mth.sqrt((1./(N2 - 1)) * som_afwL_TN) # standaard afwijking

print # witregel
print 'test gemiddelde:'
print MN
print 'test standaardafwijking:'
print SN
print '------> correct'
print # witregel
print 'end programme'

# Plotten van histogrammen:

plt.subplot(211)
n, bins, patches = plt.hist(L_T,50, facecolor = 'blue') # plot vlakke verdeling

plt.subplot(212)
n, bins, patches = plt.hist(L_TN,80, facecolor = 'green') # plot normale verdeling
plt.show()


