# -*- coding: utf-8 -*-

# Programma-naam: Dronkenmans wandeling
 
import math as mth
import random as rnd
import matplotlib.pyplot as plt

# Hoofdstuk 8
# 8.4 Opdracht 3: Dronkenmans wandeling


# opdracht 3.1: 
    
# beginpositie deeltje:
x = 0
y = 0

# Stapgrootte:
r = 1
# Aantal stappen
N = 20


L_x = []
L_y = []

# Dronkenmans wandeling:
for i in range(0,N):
    alpha = rnd.random() * 2 * mth.pi
    #r = rnd.random() # Verwijder '#' om ook stapgrootte random 
    # te variëren tussen 0 en 1.
    dx = r * mth.cos(alpha)
    dy = r * mth.sin(alpha)
    L_x.append(x)
    L_y.append(y)
    x += dx
    y += dy
    
#plot dronkenmans wandeling:
plt.subplot(221)
plt.plot(L_x,L_y,'b')
plt.xlabel('x')
plt.ylabel('y')
#plt.show()


# Opdracht 3.2

# Dronkenmans wandeling:
def Dronk(n,m,stap):
    L_dO = []
    som_dO = 0 # som van afstanden van de deeltjes tot de oorsprong
    for j in range(0,n): # Ieder deeltje mag een wandeling maken
        
        # Beginpositie deeltje
        x = 0
        y = 0
        
        # Dronkenmans wandeling per deeltje:
        for k in range(0,m): # Ieder deeltje doet m aantal stappen
            alpha = rnd.random() * 2 * mth.pi
            # stap is een Boolean code om de stapgrootte constant te houden op 1 of random te varieren.
            if stap == 1:
                r = rnd.random()
            if stap == 0:
                r = 1     
            dx = r * mth.cos(alpha)
            dy = r * mth.sin(alpha)
            x += dx
            y += dy
        dO = mth.sqrt(x**2 + y**2) # Afstand d van het deeltje tot de oorsprong O
        som_dO += dO
        L_dO.append(dO)
        
    # Bereken gemiddelde afstand van de deeltjes tot de oorsprong:
    gem_dO = float(som_dO) / n
    
    # Standaarddeviatie uitrekenen:
    som_afw_sq = 0
    for dO_i in L_dO:
        afw_sq = (dO_i - gem_dO)**2
        som_afw_sq += afw_sq
    Sd_dO = (1./(n-1)) * som_afw_sq
    return gem_dO, Sd_dO

print 'Vrij deeltje:'
print 'n = aantal deeltjes, m = aantal stappen'
print # witregel
print 'Voor n = 100 en m = 10, en stapgrootte 1, is de gemiddelde afstand van deeltjes tot de oorsprong %f' % Dronk(100,10,0)[0]
print 'en de standaarddeviatie is %f' % Dronk(100,10,0)[1]
print # witregel
print 'Voor n = 100 en m = 1000, en stapgrootte 1, is de gemiddelde afstand van deeltjes tot de oorsprong %f' % Dronk(100,1000,0)[0]
print 'en de standaarddeviatie is %f' % Dronk(100,1000,0)[1]
print # witregel
print 'Voor n = 100 en m = 10, en random stapgrootte, is de gemiddelde afstand van deeltjes tot de oorsprong %f' % Dronk(100,10,1)[0]
print 'en de standaarddeviatie is %f' % Dronk(100,10,1)[1]
print # witregel
print 'Voor n = 100 en m = 1000, en random stapgrootte, is de gemiddelde afstand van deeltjes tot de oorsprong %f' % Dronk(100,1000,1)[0]
print 'en de standaarddeviatie is %f' % Dronk(100,1000,1)[1]
    

# Opdracht 3.3

# Dronkenmans wandeling in een doos:


# n = aantal deeltjes
# m = aantal stappen
# stapgrootte: stap = 1 betekent random stapgrootte, stap = 0 betekent een stapgrootte van 1

def Dronk_doos(n,m,stap):
    L_eindx = [] # lijst voor x-coordinaat van het deeltje ten einde van de wandeling
    L_eindy = [] # lijst voor y-coordinaat van het deeltje ten einde van de wandeling
    
    N_rechts = 0 # houdt aantal deeltjes bij dat zich aan de rechterkant van de doos bevindt.
    L_dO = [] # Lijst voor afstand van het deeltje tot de oorsprong
    som_dO = 0 # som van afstanden van de deeltjes tot de oorsprong
    
    for j in range(0,n): # Ieder deeltje mag een wandeling maken
        
        # defenieer doos:
        x_min = -10
        x_max = 10
        y_min = -10
        y_max = 10
        
        delta_x = x_max - x_min
        delta_y = y_max - y_min
        
        # Beginpositie deeltje
        x = x_min + rnd.random() * delta_x
        y = y_min + rnd.random() * delta_y
        
        # Dronkenmans wandeling per deeltje:
        for k in range(0,m): # Ieder deeltje doet m aantal stappen
            alpha = rnd.random() * 2 * mth.pi
            # stap is een Boolean code om de stapgrootte constant te houden op 1 of random te varieren.
            if stap == 1:
                r = rnd.random()
            if stap == 0:
                r = 1     
            dx = r * mth.cos(alpha)
            dy = r * mth.sin(alpha)
            x += dx
            y += dy
            
            # Reflectie aan de randen:
            if x > x_max:
                dx_max = x - x_max
                x = x - dx_max
            if x < x_min:
                dx_min = x - x_min
                x = x - dx_min
            if y > y_max:
                dy_max = y - y_max
                y = y - dy_max
            if y < y_min:
                dy_min = y - y_min
                y = y - dy_min
        if x > 0.5*delta_x:
            N_rechts += 1                    
        dO = mth.sqrt(x**2 + y**2) # Afstand d van het deeltje tot de oorsprong O
        som_dO += dO
        L_dO.append(dO)
        
    # Bereken gemiddelde afstand van de deeltjes tot de oorsprong:
    gem_dO = float(som_dO) / n
    
    # Standaarddeviatie uitrekenen:
    som_afw_sq = 0
    for dO_i in L_dO:
        afw_sq = (dO_i - gem_dO)**2
        som_afw_sq += afw_sq
    Sd_dO = (1./(n-1)) * som_afw_sq
    return gem_dO, Sd_dO, N_rechts

print # witregel
print # witregel
print 'Deeltje in een doos:'
print 'n = aantal deeltjes, m = aantal stappen'
print # witregel
print 'Voor n = 100 en m = 10, en stapgrootte 1, is de gemiddelde afstand van deeltjes tot de oorsprong %f' % Dronk_doos(100,10,0)[0]
print 'en de standaarddeviatie is %f' % Dronk_doos(100,10,0)[1]
print # witregel
print 'Voor n = 100 en m = 1000, en stapgrootte 1, is de gemiddelde afstand van deeltjes tot de oorsprong %f' % Dronk_doos(100,1000,0)[0]
print 'en de standaarddeviatie is %f' % Dronk_doos(100,1000,0)[1]
print # witregel
print 'Voor n = 100 en m = 10, en random stapgrootte, is de gemiddelde afstand van deeltjes tot de oorsprong %f' % Dronk_doos(100,10,1)[0]
print 'en de standaarddeviatie is %f' % Dronk_doos(100,10,1)[1]
print # witregel
print 'Voor n = 100 en m = 1000, en random stapgrootte, is de gemiddelde afstand van deeltjes tot de oorsprong %f' % Dronk_doos(100,1000,1)[0]
print 'en de standaarddeviatie is %f' % Dronk_doos(100,1000,1)[1]


def dronkenwandeling(m,stap):
    L_x = []
    L_y = []
    
        
    # defenieer doos:
    x_min = -10
    x_max = 10
    y_min = -10
    y_max = 10
    
    delta_x = x_max - x_min
    delta_y = y_max - y_min
    
    # Beginpositie deeltje
    x = x_min + rnd.random() * delta_x
    y = y_min + rnd.random() * delta_y
    
    # Dronkenmans wandeling van het deeltje:
    for k in range(0,m): # Het deeltje doet m aantal stappen
        alpha = rnd.random() * 2 * mth.pi
        
        # stap is een Boolean code om de stapgrootte constant te houden op 1 of random te varieren.
        if stap == 1:
            r = rnd.random()
        if stap == 0:
            r = 1     
            
        dx = r * mth.cos(alpha)
        dy = r * mth.sin(alpha)
        x += dx
        y += dy
        
        # Reflectie aan de randen:
        if x > x_max:
            dx_max = x - x_max
            x = x - dx_max
        if x < x_min:
            dx_min = x - x_min
            x = x - dx_min
        if y > y_max:
            dy_max = y - y_max
            y = y - dy_max
        if y < y_min:
            dy_min = y - y_min
            y = y - dy_min
        L_x.append(x)
        L_y.append(y)                        
    return L_x, L_y

wandeling = dronkenwandeling(3000,0)

# Plotten van de wandeling:
plt.subplot(222)
plt.plot(wandeling[0],wandeling[1],'b')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-14,14)
plt.ylim(-14,14)
plt.show()

# Opdracht 3.4:

N4 = 400    # totaal aantal deeltjes
herh = 1 # aantal keer herhalen van het experiment
L_deeltjes = [] # Lijst met alle coordinaten van alle deeltjes
L_m = [] # Lijst met waarden hoeveel stappen er zijn gebruikt
        
# defenieer doos:
x_min = -10
x_max = 10
y_min = -10
y_max = 10
    
delta_x = x_max - x_min
delta_y = y_max - y_min
grens = x_min + 0.5 * delta_x # grenswaarde tussen linker en rechter deel van de doos 



for herhaling_simulatie in range(0,herh):

    # Deeltjes plaatsen in de linkerzijde van de doos:
    for u in range(0,N4):
        # Beginpositie deeltje
        x = x_min + rnd.random() * 0.5 * delta_x
        y = y_min + rnd.random() * delta_y
        coord_Di = [x,y] # begincoordinaat van deeltje i
        L_deeltjes.append(coord_Di)
    
    # deeltjes dronken wandelingen laten maken:
    m_teller = 0 # variabele dat het aantal stappen bijhoudt.
    N_l = N4 # Aantal deeltjes in linkerhelft van de doos
    N_r = 0 # Aantal deeltjes in de rechterhelft van de doos
    while N_r < N_l:    
        for v in range(0,N4):
            m_teller += 1
            xi = L_deeltjes[v][0] # variabele die de x-coord vastlegt nog voor het zetten van een stap

            alpha = rnd.random() * 2 * mth.pi
            r = 1 # vaste stapgrootte     
            
            dx = r * mth.cos(alpha)
            dy = r * mth.sin(alpha)
            x += dx
            y += dy
        
            # Reflectie aan de randen:
            if x > x_max:
                dx_max = x - x_max
                x = x - dx_max
            if x < x_min:
                dx_min = x - x_min
                x = x - dx_min
            if y > y_max:
                dy_max = y - y_max
                y = y - dy_max
            if y < y_min:
                dy_min = y - y_min
                y = y - dy_min
            coord_Di_nieuw = [x,y]
            L_deeltjes[v] = coord_Di_nieuw 
            if xi < grens and x > grens:
                N_r += 1
                N_l -= 1  
            if xi > grens and x < grens:
                N_r -= 1
                N_l += 1
            #print N_l
            if N_r >= N_l:
                break
    L_m.append(m_teller)

# opsplitsen van de coordinaten lijst
L_deeltjesx = []
L_deeltjesy = []
for w in range(0,N4):
    L_deeltjesx.append(L_deeltjes[w][0])
    L_deeltjesy.append(L_deeltjes[w][1])
 
print # witregel
print 'Opdracht 4.3:'
print 'Evenwicht wordt bereikt na het doorlopen van %d stappen.' % m_teller
# print 'Het gemiddelde aantal stappen dat nodig is om tot evenwichtstoestand te komen is %f.' %m_teller_gem

# plotten van eindsituatie; deeltjes in evenwichtstoestand:
plt.subplot(223)
plt.xlim(grens,x_max+0.5*delta_x)
plt.ylim(y_min-0.5*delta_y,y_max+0.5*delta_y)
plt.plot(L_deeltjesx,L_deeltjesy,'b.')
plt.show()










