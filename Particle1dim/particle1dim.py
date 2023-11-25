# programmanaam: Particle1dim

# Hoofdstuk 5:

import math
import matplotlib.pyplot as plt

# Opdracht 5

# parameters:

V_max = 1 # maximale potentiaal
x_pot = 0 # positie van de maximale potentiaal
dt    = 0.001 # tijdstapgrootte


def V(x): # Gaussische functie voor de potentiaal
    V = V_max * math.exp(-0.5*(x-x_pot)**2)
    return V

def V_d(x): # afgeleide functie voor de potentiaal
    V_d = V_max * (x - x_pot) * math.exp(-0.5 * (x - x_pot) ** 2)
    return V_d


# Lijsten

L_t = [0, dt] # lijst voor t-waarden
L_x = [] # lijst voor x-waarden
L_p = [] # lijst voor p-waarden

L_Ek = [] # lijst voor kinetische energieen
L_Ep = [] # lijst voor potentiele energieen
L_Et = [] # lijst voor totale energieen


# beginwaarden:

t_max = 20000
x_1 = -10 # beginpositie van het deeltje
p_1 = 1 # beginimpuls (= beginsnelheid) van het deeltje

# Euler methode alleen voor de eerste stap:

x_2 = x_1 + dt * V_d(x_1)
p_2 = p_1 + V_d(x_2) * dt
L_p.append(p_1)
L_p.append(p_2)
L_x.append(x_1)
L_x.append(x_2)

# Eerste twee energie-waarden

E_k = 0.5 * p_1 ** 2 # kinetische energie
E_p = V(x_1)  # potentiele energie
E_t = E_p + E_k # totale energie
L_Ep.append(E_p)
L_Ek.append(E_k)
L_Et.append(E_t)
E_k = 0.5 * p_2 ** 2
E_p = V(x_2) 
E_t = E_p + E_k
L_Ep.append(E_p)
L_Ek.append(E_k)
L_Et.append(E_t)


# Methode van Adams-Bashforth:

for t in range(2,t_max): # eerste 2 componenten worden overgeslagen
    # want deze zijn door bovenstaande code al gevuld.
    
    # tijd
    L_t.append(t * dt)
    
    # positie
    x_3 = x_2 + dt * (1.5 * p_2 - 0.5 * p_1)
    L_x.append(x_3)
    
    # potentiele energie
    E_p = V(x_3) 
    L_Ep.append(E_p)
    
    # impuls
    p_3 = p_2 + (1.5 * V_d(x_2) - 0.5 * V_d(x_1)) * dt
    L_p.append(p_3)
    
    # kinetische energie
    E_k = 0.5 * p_3 ** 2
    L_Ek.append(E_k)
    
    # totale energie
    E_t = E_p + E_k 
    L_Et.append(E_t)
    
    # vernieuwing parameters
    x_2 = x_3
    x_1 = x_2
    p_2 = p_3
    p_1 = p_2
    

# Plotten van de grafieken:
plt.figure(1)
# grafiek voor positie:
plt.subplot(221)
plt.xlabel('Tijd')
plt.ylabel('Positie')
plt.plot(L_t,L_x)

# grafiek voor impuls:
plt.subplot(222)
plt.xlabel('Tijd')
plt.ylabel('Impuls')
plt.plot(L_t,L_p)

# energie grafieken:
plt.subplot(223)
plt.xlabel('Tijd')
plt.ylabel('Energie')
plt.plot(L_t,L_Ek,'r') # plot kinetische energie: rood
plt.plot(L_t,L_Ep,'b') # plot potentiele energie: blauw
plt.plot(L_t,L_Et,'y') # plot totale energie: geel

# grafiek instellingen:
#plt.xlim(0,t_max * dt)
#plt.ylim(0,0.7)
plt.show()

# einde programma
print 'end programme' # print 'end programme'

