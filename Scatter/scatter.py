

# Programma-naam: Opdracht 9 Rutherford scattering
import numpy as np
import math as mth
import random as rnd
import matplotlib.pyplot as plt


dt = 0.00001 # tijdstapgrootte
t_max = 1 # maximale hoeveelheid stappen

e_0 = 8.85 * 10**(-12) # geleidbaarheid van vaccuum in Farad per meter    

# Deeltje 1:

m1 = 9.109534 * 10**(-31) # massa in atomaire massa-eenheden
q =  - 1.6022 * 10**(-19)     # elektrische lading in Coulomb van deeltje 1
x1 = - 6     # x-coordinaat deeltje 1
y1 = 0.2     # y-coordinaat deeltje 1
vx1 = 50     # beginsnelheid in x-richting van deeltje 1
vy1 = 0     # beginsnelheid in y-richting van deeltje 1
v1_abs0 = mth.sqrt(vx1**2 + vy1**2) # absolute beginsnelheid deeltje 1

# Potentiaalveld (deeltje 2):

Q = - 1.6022 * 10**(-19) # lading van het potentiaalveld (of deeltje 2)
x2 = 0 # x-coordinaat deeltje 2 
y2 = 0 # y-coordinaat deeltje 2


def C_law(q,Q,r): # Coulomb's wet
    richting =  - np.sign(q/Q) # bepaalt teken van de kracht
    # Als q en Q hetzelfde teken hebben is F negatief (afstoting) en andersom
    E = float(Q) / (4 * mth.pi * e_0 * r**2)
    F = richting * q * E # in de orde van 10**-26
    return F

# Analystische oplossing (Werkt alleen met een potentiaal veld in de oorsprong!)
# om scatterhoek te berekenen

dx = x2 - x1
dy = y2 - y1
b =  abs(dy)
l = b * v1_abs0
r_A = mth.sqrt(dx**2 + dy**2) # beginwaarde r
v1_abs_A = v1_abs0
E_A = 0.5 * m1 * v1_abs_A**2 + float(Q*q)/r_A
#teta_0 = mth.atan(2 * E_A * m1 * l**2 * Q**(-1) * q**(-1))
teta_s = 2 * mth.atan(float(q**2)/(4 * mth.pi * e_0 * m1 * v1_abs0**2 * b))
teta_0 = 0.5 * (teta_s + mth.pi)


# Numerieke oplossing:

LN_t = [0, dt] # Numerieke lijst voor t-waarden
LN_x1y1 = [] # numerieke lijst voor coordinaten van deeltje 1
LN_vx1vy1 = [] # numerieke lijst voor snelheden van deeltje 1
LN_r = [] # lijst voor r-waarden

LN_Ek = [] # numerieke lijst van kinetische energie waarden
LN_Ep = [] # numerieke lijst voor potentiele energie waarden
LN_Et = [] # numerieke lijst voor totale energie waarden

# Euler methode(alleen voor de eerste stap):

# afstanden berekenen:
dx = x2 - x1 
dy = y2 - y1
r = mth.sqrt(dx**2 + dy**2) # afstand tussen deeltje 1 en 2
LN_r.append(r)

# Eerste waarden in lijst plaatsen:
LN_x1y1.append([x1,y1])
LN_vx1vy1.append([vx1,vy1])
Ek = 0.5 * m1 * v1_abs0**2 # kinetische energie
Ep = (float(q * Q)) / (4 * mth.pi * e_0 * r) # potentiele energie
Et = Ep + Ek # totale energie
#LN_Ek.append(Ek) 
LN_Ep.append(Ep)
#LN_Et.append(Et)    
            
# kracht componenten berekenen:
F_abs = C_law(q,Q,r) 
F_x = (float(dx) / r) * F_abs
F_y = (float(dy) / r) * F_abs

# versnelling berekenen:        
ax1_1 = float(F_x) / m1
ay1_1 = float(F_y) / m1

# nieuwe snelheid berekenen:
vx1 = vx1 + ax1_1
vy1 = vy1 + ay1_1
v1_abs = mth.sqrt(vx1**2 + vy1**2)
    
# nieuwe posities berekenen:
x1 = x1 + vx1 * dt
y1 = y1 + vy1 * dt

# afstanden berekenen:
dx = x2 - x1 
dy = y2 - y1
r = mth.sqrt(dx**2 + dy**2) # afstand tussen deeltje 1 en 2
LN_r.append(r)

# tweede waarden in de lijst plaatsen:
LN_x1y1.append([x1,y1])
LN_vx1vy1.append([vx1,vy1])
Ek = 0.5 * m1 * v1_abs**2 
Ep = (float(q * Q)) / (4 * mth.pi * e_0 * r)
Et = Ep + Ek
LN_Ek.append(Ek) 
LN_Ek.append(Ek)
LN_Ep.append(Ep)
LN_Et.append(Et)
LN_Et.append(Et)
      
# kracht componenten berekenen:
F_abs = C_law(q,Q,r) 
F_x = (float(dx) / r) * F_abs
F_y = (float(dy) / r) * F_abs

# versnelling berekenen:        
ax1_2 = float(F_x) / m1
ay1_2 = float(F_y) / m1

     
               
# Adams-Bashforth methode:

# start waarden:
x1_1 = LN_x1y1[0][0]# de eerste 1 is alleen maar om aan te geven dat het om deeltje 1 gaat
x1_2 = LN_x1y1[1][0]
vx1_1 = LN_vx1vy1[0][0] 
vx1_2 = LN_vx1vy1[1][0]
ax1_1 = ax1_1
ax1_2 = ax1_2

y1_1 = LN_x1y1[0][1]
y1_2 = LN_x1y1[1][1]
vy1_1 = LN_vx1vy1[0][1]
vy1_2 = LN_vx1vy1[1][1]
ay1_1 = ay1_1
ay1_2 = ay1_2

for t in np.arange(dt*2,t_max,dt): # eerste twee componenten uit de lijst zijn al uitgerekend

    #dt = dt * (float(v1_abs0) / v1_abs) # nieuwe dt om nauwkeurigheid te vergroten
    LN_t.append(t) # tijd vastleggen
    
    # nieuwe positie
    x1_3 = x1_2 + dt * (1.5 * vx1_2 - 0.5 * vx1_1)
    y1_3 = y1_2 + dt * (1.5 * vy1_2 - 0.5 * vy1_1)
    LN_x1y1.append([x1_3,y1_3])

    # afstanden berekenen:
    dx = x2 - x1_3 
    dy = y2 - y1_3
    r = mth.sqrt(dx**2 + dy**2) # afstand tussen deeltje 1 en 2    
    LN_r.append(r)
    
    # potentiele energie:
    Ep = (float(q * Q)) / (4 * mth.pi * e_0 * r)
    LN_Ep.append(Ep)

    # nieuwe snelheid berekenen:
    vx1_3 = vx1_2 + (1.5 * ax1_2 - 0.5 * ax1_1) * dt
    vy1_3 = vy1_2 + (1.5 * ay1_2 - 0.5 * ay1_1) * dt    
    v1_abs = mth.sqrt(vx1_3**2 + vy1_3**2)
    LN_vx1vy1.append([vx1_3, vy1_3])
    
    # kinetische energie
    Ek = 0.5 * m1 * v1_abs ** 2
    LN_Ek.append(Ek)

    # totale energie:
    Et = Ep + Ek
    LN_Et.append(Et)
    
    # kracht componenten berekenen:
    F_abs = C_law(q,Q,r) 
    F_x = (float(dx) / r) * F_abs
    F_y = (float(dy) / r) * F_abs

    # versnelling berekenen:        
    ax1_3 = float(F_x) / m1
    ay1_3 = float(F_y) / m1
    
    # vernieuwing parameters
    x1_2 = x1_3
    x1_1 = x1_2
    y1_2 = y1_3
    y1_1 = y1_2
    
    vx1_2 = vx1_3
    vx1_1 = vx1_2
    vy1_2 = vy1_3
    vy1_1 = vy1_2    
        
    ax1_2 = ax1_3
    ax1_1 = ax1_2
    ay1_2 = ay1_3
    ay1_1 = ay1_2


# numerieke scatterhoek testen aan analytische scatterhoek:
x1y1l = LN_x1y1[len(LN_x1y1)-1]
teta_s_test = float(x1y1l[1]) / x1y1l[0]
# print 'Deze numerieke teta_s: %f zou gelijk moeten zijn aan de analytische teta_s: %f.' % (teta_s_test,teta_s)


# Kleinste r-waarde bepalen
R_min = 10**99
for i in range(0,len(LN_r)):
    if LN_r[i] < R_min:
        R_min = LN_r[i] 
        coord = LN_x1y1[i]         
teta_0_test = mth.atan2(coord[1],coord[0])
print 'Deze numerieke teta_0: %f zou gelijk moeten zijn aan de analytische teta_0: %f' % (teta_0_test,teta_0)
#print coord
#print ((mth.pi)*0.5-teta_0_test)



# plotten van de baan van deeltje 1 en stilstaand deeltje 2:
L_x = [coordinaat[0] for coordinaat in LN_x1y1] # lijst samenstellen bestaande uit alleen x-waarden
L_y = [coordinaat[1] for coordinaat in LN_x1y1] # lijst samenstellen bestaande uit alleen y-waarden
plt.subplot(121)
plt.plot(L_x, L_y, label='baan van bewegend deeltje 1') # deeltje 1
plt.plot(x2,y2,'or',label='stilstaand deeltje 2') # deeltje 2
plt.legend()
plt.xlim(-10,15)
plt.ylim(-1,5)
plt.xlabel('x-coordinaat')
plt.ylabel('y-coordinaat')
plt.title('Afgelegde weg van deeltje 1')
plt.show()            

# energie grafieken plotten:
plt.subplot(122)
plt.plot(LN_t,LN_Ek,'r', label='Kinetische energie')
plt.plot(LN_t,LN_Ep,'b', label='Potentiele energie')
plt.plot(LN_t,LN_Et,'k', label='Totale energie')
#plt.xlim(0,1.1*t_max)
#plt.ylim(0,10**-24)
plt.title('Verschillende energieen van deeltje 1')
plt.legend()
plt.xlabel('Tijd')
plt.ylabel('Energie')
plt.show()


