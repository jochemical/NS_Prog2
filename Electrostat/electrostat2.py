
# programmanaam: Numerieke methode in 2 dimensies

# Hoofdstuk 7.4

from math import * # importeert alle functies van de math-bilbiotheek
import numpy as np # importeert alle functies van de numpy-bilbiotheek
import matplotlib.pyplot as plt # importeert de matplotlib.pyplot bilbiotheek onder de verwijzing plt


# Opdracht 4

# ruimte V(x,y):
a = 1
b = 1

x_min = 0
x_max = a
y_min = 0
y_max = b

N = 101 # aantal subintervallen + 1

# De matrix potentiaal:
V_0 = 10 # startpotentiaal
n = N # aantal rijen van de matrix
m = N # aantal kollommen van de matrix
V = np.zeros((n,m)) # matrix bestaande uit 0-en met n rijen en m kolommen

# randvoorwaarden:
    # V = 0 voor x = 0
    # V = 0 voor x = a
    # V = 0 voor y = b
    # V = V_0 voor y = 0 (V_0 > 0):
for i in range(0,m):
    V[0][i] = V_0 # de hoekpunten (0,0) en (a,0) hebben eveneens de waarde V_0
# i = kollom-indicatie (maximaal m)
# j = rij-indicatie (maximaal n)

# Gauss-Seidel iteratie:

dE_break = 0.005 # E-waarde waaronder de iteratie moet stoppen (kan op hol slaan!)
dE = 10 ** 99 # startwaarde convergentie-monitor

E_vrg = 10000 # variabele die de voorgaande E bijhoudt 
L_E = [] # Lijst met E-waarden

it = 0 # test hoevaak de while loop wordt uitgevoerd
L_it = [] # Lijst met iteratie-waarden

omega = 1.9
while abs(dE) > dE_break: # convergentie-monitor
    #E = 0 # na iedere Gauss-Seidel iteratie wordt E weer gelijkgesteld aan 0
    it = it + 1 
    L_it.append(it)
    for i in range(1,m-1): # alle kollommen nalopen    
        for j in range(1,n-1): # alle rijen nalopen
            V[j][i] = (1 - omega) * V[j][i] + (0.25 * omega) * (V[j][i-1] + V[j][i+1] + V[j-1][i] + V[j+1][i])
            
# Convergion monitor:
    E = 0
    for i in range(1,m-1): # alle kollommen nalopen    
        for j in range(1,n-1): # alle rijen nalopen
            E += ((V[j][i] - V[j][i-1])**2 + (V[j][i] - V[j-1][i])**2)
    L_E.append(E)
    dE = E_vrg - E            
    E_vrg = E            
            
            
# Grafieken maken voor de potentiaal
dx = 1./m # stapgrootte in x-richting
dy = 1./n # stapgrootte in y-richting

x = 0
L_x = []
L_Vx = []
for i in range(0,m):
    L_Vx.append(V[50][i])
    L_x.append(x)
    x = x + dx
    
y = 0
L_y = []
L_Vy = []
for j in range(0,n):
    L_Vy.append(V[j][50])
    L_y.append(y)
    y = y + dy

   
# plot grafiek potentiaal in en x- en y-richting
plt.subplot(211)                   
plt.plot(L_x,L_Vx,'b') # blauw: potentiaal in x-richting
plt.plot(L_y,L_Vy,'g') # rood: potentiaal in y-richting
plt.xlabel('x-waarden')
plt.ylabel('y-waarden')
plt.show()

# grafiek E-waarden tov aantal iteraties
plt.subplot(212)
plt.plot(L_it,L_E)
plt.xlabel('Aantal iteraties')
plt.ylabel('E-waarde')
plt.show()




# De volgende code is geheel overgenomen van het python-document vana.py
# dat te vinden is op https://numnat.mprog.nl/ en bevat de analytische 
# oplossing waarmee bovenstaande code kan worden gecontrolleerd. 

import math
import matplotlib.pyplot as plt

class constants:
    def __init__(self,nstep, a,b,Vnul,nmax):
        self.nstep =nstep
        self.a = a
        self.b = b
        self.Vnul = Vnul
        self.nmax = nmax

        
myconstants =  constants(100,1.,1.,10.,101)

def F1(n):
    antw1 = (1./n)*(1-math.pow(-1.,n))
    return antw1

def F2(n,x):
    antw2 = math.sin((math.pi*n*x)/myconstants.a)
    return antw2

def F3(n,y):
    antw3 = ((math.exp(((math.pi*n)/myconstants.a)*(myconstants.b -y)) -
             math.exp (((-math.pi*n)/myconstants.a)*(myconstants.b-y)))/2.)
    return antw3

def F4(n):
    antw4=(math.exp((math.pi*n*myconstants.b)/myconstants.a)-
            math.exp((-math.pi*n*myconstants.b)/myconstants.a))/2.
    return antw4

def Va(x,y):
    V=0
    Vbijdrage =0
    for n in range(1,myconstants.nmax,2):
        Vbijdrage = (2.*myconstants.Vnul/math.pi)*F1(n)*F2(n,x)*F3(n,y)/F4(n)
        V = V+Vbijdrage
        if math.fabs(Vbijdrage/V)< math.pow(10.,-20):
            break
    return V

xmin = 0.
xmax = 1.
ymin = 0.
ymax = 1.

hx = (xmax-xmin)/myconstants.nstep
hy = (ymax-ymin)/myconstants.nstep

V = [[0]*myconstants.nstep for i in range (myconstants.nstep)]

x =[]
y =[]

for i in range(0,myconstants.nstep):
    x.append(i*hx)
    y.append(i*hy)

for i in range(1,myconstants.nstep):
    for j in range(1,myconstants.nstep):
        V[i][j]=Va(x[i],y[j])
    V[i][0]=myconstants.Vnul

Vxy1 = [0]*myconstants.nstep
xy1 = [0]*myconstants.nstep

for i in range(0,myconstants.nstep):
    Vxy1[i]=V[i][myconstants.nstep/2]
    xy1[i]=x[i]

Vxy2 = [0]*myconstants.nstep
xy2 = [0]*myconstants.nstep

for i in range(0,myconstants.nstep):
    Vxy2[i]=V[myconstants.nstep/2][i]
    xy2[i]=y[i]

plt.subplot(211)
plt.plot(xy1,Vxy1,'y')
plt.plot(xy2,Vxy2,'r')
plt.ylabel('Potential [a.u.]')
plt.xlabel('position [a.u.]')
plt.show()



