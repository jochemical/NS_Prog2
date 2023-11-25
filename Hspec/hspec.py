# programmanaam: hspec

# Hoofdstuk 6:

import math
import matplotlib.pyplot as plt
import numpy as np

# Opdracht 6

# variabelen:

m     = 1 # massa 
V0    = 1 # minimum waarde van de potentiaal, V0 = 1 want V0 wordt gebruikt als de eenheid van energie
a     = 1 # afstand waarvoor potentiaal = 0, a = 1 want a wordt gebruikt als de eenheid van lengte
h_bar = float(6.626070040*10**(-34))/ (2*math.pi)
gamma = a * (h_bar**(-1)) * (2*m*V0)**0.5

# functie voor de potentiaal:

def vpot(x):
    V = 4 * V0 * ((float(a)/x)**12 - (float(a)/x)**6)
    return V # Lennard-Jones potentiaal

# Test functie vpot:

print 'Test functie vpot:'
print 'vpot(2^(1/6))='
print vpot(2**(float(1)/6))
print 'vpot(1)='
print vpot(1)
print '---> functie "vpot" is correct'

# mbv een grafiek
L_x = []
L_vpot = []
for x in np.arange(0.96,5.96,0.1):
    L_x.append(x)
    vpot_test = vpot(x)
    L_vpot.append(vpot_test)

plt.subplot(211)
plt.xlabel('positie')
plt.ylabel('potentiaal')
plt.plot(L_x,L_vpot)
plt.show()


# functie action

def action(e):
    gamma = 21.7
    dx = 0.001 # stapgrootte integratie
    dA = 0 # intergratie-stroken
    A = 0 # totale oppervlak onder de grafiek
    x_in = ( 0.125 * (4 + (16 + 16 * e)**0.5))**(-1./6)
    x_out = ( 0.125 * (4 - (16 + 16 * e)**0.5))**(-1./6)
    for x in np.arange(x_in+dx,x_out,dx): # integreren
        dA = (math.fabs(e - vpot(x)))**0.5 * dx 
        A = A + dA 
    s = gamma * A # s-waarde uitrekenen
    return [x_in, x_out, s]


# testen van de functie Action:

L_e = [] # lijst met energiewaarden
L_x_in = [] # lijst met x_in-waarden
L_x_out = [] # lijst met x_out-waarden 
L_s = [] # lijst met s-waarden
for e in np.arange(-0.9,-0.09,0.1):
    s_test = action(e)[2] # de testwaarde van s
    x_in_test = action(e)[0] # de testwaarde van x_in
    x_out_test = action(e)[1] # de testwaarde van x_out
    L_e.append(e)
    L_s.append(s_test)
    L_x_in.append(x_in_test)
    L_x_out.append(x_out_test)    

plt.subplot(212)
plt.xlabel('energie')
plt.ylabel('s(rood), x_in(blauw), x_out(geel)')
plt.plot(L_e,L_s,'r') # s-waarden vs. energiewaarden: rood
plt.plot(L_e,L_x_in,'b') # x_in-waarden vs. energiewaarden: blauw
plt.plot(L_e,L_x_out,'y') #  # x_out-waarden vs. energiewaarden: geel
plt.show()

# functie Eigen:

def eigen(estart,value): # bisectie methode
    x_l = estart # minimum testwaarde
    x_r = -0.01 # maximum testwaarde
    precisie = x_r - x_l # initiele precisie
    while precisie > 0.001: # while loop stopt bij deze precisie
        x_m = 0.5 * (x_l + x_r) # middelste waarde tussen de twee testwaarden
        if np.sign(action(x_m)[2]-value) == np.sign(action(x_l)[2]-value): # het derde element van de uitvoer van action is de s-waarde
            x_l = x_m # de minimum testwaarde wordt vervangen door de x_m
        if np.sign(action(x_m)[2]-value) == np.sign(action(x_r)[2]-value):
            x_r = x_m # de maximum testwaarde wordt vervangen door de x_m
        precisie = x_r - x_l # de nieuw bereikte positie wordt vastgesteld
    return x_m # x_m is de benaderde e-waarde waarvoor s(e) -value = 0    

  
# Testen van de functie Eigen:
      
e0 = eigen(-0.9,math.pi*0.5)
e1 = eigen(e0,math.pi*1.5)    
print
print 'eigen-functie testen:'
print 'e0 ='
print e0
print 'e1 ='
print e1
print '------> functie "eigen" is correct'


# Lijst opstellen van eigenwaarden

E_vorig = 666 # voorgaande eigenwaarde van de energie wordt gebruikt om de loop af te breken    
L_E = [] # lijst voor energie eigenwaarden
for n in range(0,10): # n zijn altijd integers
    value = (n + 0.5) * math.pi
    E = eigen(-0.9,value)
    if E == E_vorig:
        break # loop stopt als dezelfde eigenwaarde wordt berekend
    L_E.append(E)
    if E >= -0.01:
        break # loop stopt als een eigenwaarde wordt berekend die hoger is dan -0.1 
    E_vorig = E
print
print 'Alle mogelijke energie-eigenwaarden zijn:'
print L_E # print alle eigenwaarden
print

# einde programma
print 'end programme'

