
# Programma-naam: Opdracht 10 Van Allen gordels

import numpy as np
import math as mth
import random as rnd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 


def inprod(A,B): # functie voor inproduct tussen twee 3 dimensionale vectoren
    C = A[0]*B[0] + A[1]*B[1] + A[2]*B[2]
    return C

def uitprod(A,B):
    C = np.array([ A[1]*B[2]-A[2]*B[1] , A[2]*B[0]-A[0]*B[2] , A[0]*B[1]-A[1]*B[0] ])    
    return C
                
def abslt(A):
    C = mth.sqrt(A[0]**2. + A[1]**2. + A[2]**2.)
    return C
    
def B_veld(R): # invoer R is een lijst van een x, y, en z-coordinaat
    m_dak = np.array([0.,0.,1.]) # richtingsvector dipool
    R_dak = R * (abslt(R))**(-1.) # richtingsvector voor R 
    R_e = 6.4 * 10**6 # Straal Aarde
    B_0 = 3.5 * 10**(-5) # Tesla
    
    B = B_0 * ( -1. * m_dak + 3. * inprod(m_dak,R_dak) * R_dak) / (abslt(R)/R_e)**3. # positieafhankelijk magneetveld
    return B

def a(v,B,q,m):
    c = 299792458. # lichtsnelheid    
    if (float(abslt(v)**2.)) / (c**2.) > 1:
        print 'error in a'
        print float(abslt(v))/c
    gamma = mth.sqrt( 1. - ((float(abslt(v)**2.)) / (c**2.)))
    a = (q * uitprod(v,B)*(m ** -1.)) * gamma
    return a    

# start 3Dgrafiek:
fig = plt.figure(1)
ax = Axes3D(fig)

# constanten:
c = 299792458. # lichtsnelheid
R_e = 6.4 * 10**6 # Straal Aarde

# Oppervlak van de aarde:   
LA_x = []
LA_y = [] 
LA_z = []  
for alpha in np.arange(0, 2 * mth.pi, 0.01 * mth.pi):    
    for teta in np.arange(0, 1*mth.pi, 0.01*mth.pi):
        Ax = R_e * mth.sin(teta) * mth.cos(alpha)
        LA_x.append(Ax) 
        Ay = R_e * mth.sin(teta) * mth.sin(alpha)
        LA_y.append(Ay)
        Az = R_e * mth.cos(teta)
        LA_z.append(Az)

# Lijsten om Aard-as te plotten:
LA_asx = [0.,0.]
LA_asy = [0.,0.]
LA_asz = [-1.5 * R_e, 1.5 * R_e]

plt.plot(LA_x,LA_y,LA_z,'b') # plot Aarde
plt.plot(LA_asx,LA_asy,LA_asz,'k') # plot Aard-as


# Dubbele lijst met begin waardes:

# protonen:
L_Rp = [np.array([4.*R_e,4.0*R_e,0*R_e]),np.array([3.*R_e,3.0*R_e,-2.0*R_e]),np.array([3.0*R_e,0.*R_e,0.*R_e]),np.array([0.*R_e,3.*R_e,3.*R_e])]
# Dubbelde lijst met begin snelheden:
L_vp = [np.array([0.,0.4*c,0.]),np.array([0.,0.4*c,0.]),np.array([0.4*c,0.,0.]),np.array([0.,-0.2*c,-0.2*c])]

# elektronen:
L_Re = [np.array([-2.*R_e,-2.0*R_e,0*R_e]),np.array([-5.*R_e,-5.0*R_e,-5.0*R_e]),np.array([-5.0*R_e,0.*R_e,0.*R_e]),np.array([0.*R_e,-5.*R_e,-5.*R_e])]
# Dubbelde lijst met begin snelheden:
L_ve = [np.array([0.,-0.4*c,0.]),np.array([0.,0.4*c,0.4 *c]),np.array([0,0.,0.4*c]),np.array([0.,0.4*c,0.4*c])]




# deeltje 1, proton:
m_p = 1.67262 * 10.**-27. # massa deeltje in kg
q_p = 1.6022 * 10.**(-19.) # lading deeltje in Coulomb


# deeltje 2, elektron:
m_e = 9.109534 * 10.**(-31.) # massa deeltje
q_e = - 1.6022 * 10.**(-19.) # lading deeltje

# tijd variabele 
dt = 10**-3
t_max = 10

# Opties deeltjes

N_max = 10 # totaal aantal deeltjes, werkt alleen bij random startposities/snelheden
option_R0v0 = 1 # Bolean code voor start posities en snelheden: random = 0; lijst = 1


# Start afschieten deeltjes:

if option_R0v0 ==1:
    N_max = len(L_Rp)


# protonen:
for N in range(0,N_max):
        
    # Lijsten:
    L1_t = [] # Lijst voor tijdvariabele
    L1_R = [] # Lijst met positievectoren van deeltje 1
    L1_v = [] # Lijst met snelheidsvectoren van deeltje 1
    L1_a = [] # Lijst met versnellingsvectoren van deeltje 1

    # startwaarden voor deeltje instellen
    
    if option_R0v0 == 1:
        R1 = L_Rp[N]
        v1 = L_vp[N]                    
        v1_0abs = abslt(L_vp[N]) # variabele om de absolute snelheid constant te houden                        
    
    if option_R0v0 == 0: # random startwaarden:
        # random start coordinaten in een bolschil om de aarde (dus niet in de aarde)
        teta_start = rnd.random() * mth.pi
        alpha_start = rnd.random() * 2 * mth.pi
        R_start = 2* R_e + rnd.random() * R_e
        
        x_start = R_start * mth.sin(teta_start) * mth.cos(alpha_start) 
        y_start = R_start * mth.sin(teta_start) * mth.sin(alpha_start)
        z_start = R_start * mth.cos(teta_start)
        
        R1 = np.array([x_start,y_start,z_start])
        #R1 = R_e * np.array([2.*rnd.random(),2.*rnd.random(),2.*rnd.random()]) + R_e * np.array([-1.,-1.,-1.])
        
        # random startsnelheden
        vrand_abs = rnd.random() * c
        v1 = np.array([2.*rnd.random(),2.*rnd.random(),2.*rnd.random()]) + np.array([-1.,-1.,-1.])
        v1 = (abslt(v1)**-1) * v1
        v1 = vrand_abs * v1 
        
        v1_0abs = abslt(v1) # variabele om de absolute snelheid constant te houden
        
        
    # proton
    m1 = m_p
    q1 = q_p
    
    # Start met verplaatsen van het deeltje:
    for Ndt in np.arange(0.,t_max,dt):
        t = Ndt * dt
        L1_t.append(t)
        L1_R.append(R1)
        L1_v.append(v1)
        
        # magneetveld:
        B = B_veld(R1)
        
        # nieuwe versnelling:
        a1 = a(v1,B,q1,m1)  
        L1_a.append(a1)   
        
        # nieuwe snelheid:         
        v1 = v1 + a1 * dt
        
        #correctie voor absolute snelheid (deeltje mag alleen maar afbuigen)
        v1_abs = abslt(v1) # nieuwe absolute snelheid met afwijking
        v1_norm = v1 * (abslt(v1)**-1) # genormaliseerde nieuwe snelheid
        v1 = v1_norm * v1_0abs # gecorrigeerde absolute snelheid 
           
        # nieuwe positie:
        R1 = R1 + v1 * dt 
        
    # Plotten van de baan in 3D:
    L1_x = [r[0] for r in L1_R] # lijst samenstellen bestaande uit alleen x-waarden
    L1_y = [r[1] for r in L1_R] # lijst samenstellen bestaande uit alleen y-waarden
    L1_z = [r[2] for r in L1_R] # lijst samenstellen bestaande uit alleen z-waarden
        
    plt.plot(L1_x,L1_y,L1_z,'g') # plot baan proton
    if N == (N_max-1):
        plt.plot(L1_x,L1_y,L1_z,'g',label='Afgelegde weg protonen') # plot baan proton

   
dt = 10**-2
t_max = 100 
       
# elektronen:     
for N in range(0,N_max):
         
    # Lijsten:
    L1_t = [] # Lijst voor tijdvariabele
    L1_R = [] # Lijst met positievectoren van deeltje 1
    L1_v = [] # Lijst met snelheidsvectoren van deeltje 1
    L1_a = [] # Lijst met versnellingsvectoren van deeltje 1

    # startwaarden voor deeltje instellen
    
    if option_R0v0 == 1:
        R1 = L_Re[N]
        v1 = L_ve[N]                    
        v1_0abs = abslt(L_ve[N]) # variabele om de absolute snelheid constant te houden                        
    
    if option_R0v0 == 0: # random startwaarden:
        # random start coordinaten in een bolschil om de aarde (dus niet in de aarde)
        teta_start = rnd.random() * mth.pi
        alpha_start = rnd.random() * 2 * mth.pi
        R_start = 2* R_e + rnd.random() * R_e
        
        x_start = R_start * mth.sin(teta_start) * mth.cos(alpha_start) 
        y_start = R_start * mth.sin(teta_start) * mth.sin(alpha_start)
        z_start = R_start * mth.cos(teta_start)
        
        R1 = np.array([x_start,y_start,z_start])
        #R1 = R_e * np.array([2.*rnd.random(),2.*rnd.random(),2.*rnd.random()]) + R_e * np.array([-1.,-1.,-1.])
        
        # random startsnelheden
        vrand_abs = rnd.random() * c
        v1 = np.array([2.*rnd.random(),2.*rnd.random(),2.*rnd.random()]) + np.array([-1.,-1.,-1.])
        v1 = (abslt(v1)**-1) * v1
        v1 = vrand_abs * v1 
        
        v1_0abs = abslt(v1) # variabele om de absolute snelheid constant te houden
    
    # elektron:    
    m1 = m_e
    q1 = q_e
        

    # Start met verplaatsen van het deeltje:
    for Ndt in np.arange(0.,t_max,dt):
        t = Ndt * dt
        L1_t.append(t)
        L1_R.append(R1)
        L1_v.append(v1)
        
        # magneetveld:
        B = B_veld(R1)
        
        # nieuwe versnelling:
        a1 = a(v1,B,q1,m1)  
        L1_a.append(a1)   
        
        # nieuwe snelheid:         
        v1 = v1 + a1 * dt
        
        #correctie voor absolute snelheid (deeltje mag alleen maar afbuigen)
        v1_abs = abslt(v1) # nieuwe absolute snelheid met afwijking
        v1_norm = v1 * (abslt(v1)**-1) # genormaliseerde nieuwe snelheid
        v1 = v1_norm * v1_0abs # gecorrigeerde absolute snelheid 
           
        # nieuwe positie:
        R1 = R1 + v1 * dt 
        
    # Plotten van de baan in 3D:
    L1_x = [r[0] for r in L1_R] # lijst samenstellen bestaande uit alleen x-waarden
    L1_y = [r[1] for r in L1_R] # lijst samenstellen bestaande uit alleen y-waarden
    L1_z = [r[2] for r in L1_R] # lijst samenstellen bestaande uit alleen z-waarden
        
    plt.plot(L1_x,L1_y,L1_z,'y') # plot baan elektron
    if N == (N_max-1):
        plt.plot(L1_x,L1_y,L1_z,'y',label='Afgelegde weg elektronen') # plot baan proton
   









# Plot 3D-grafiek:
#fig = plt.figure(1)
#ax = fig.add_subplot(111, projection='3d')
#ax = Axes3D(fig)


#plt.plot(L1_x,L1_y,L1_z,'g') # plot baan deeltje 1
#plt.plot(L2_x,L2_y,L2_z,'y') # plot baan deeltje 2

#plt.plot(0,0,0,'.b','markersize=0.1')

ax.set_zlim3d(-5*R_e, 5*R_e)
ax.set_ylim3d(-5*R_e, 5*R_e)
ax.set_xlim3d(-5*R_e, 5*R_e)

ax.set_xlabel('x(m)')
ax.set_ylabel('y(m)')
ax.set_zlabel('z(m)')
ax.set_title('Afgelegde weg van protonen en elektronen rond de Allen Gordel')
ax.text(0.5*R_e,0.5*R_e,0,'Aarde',color='k')

# plot 2D-grafiek:
#plt.subplot(222)
#plt.plot(LA_x,LA_y)
#plt.plot(L1_x,L1_y)
#plt.plot(0,0,'.k')
#plt.xlim(-5* R_e, 5*R_e)
#plt.ylim(-5*R_e, 5*R_e)
#plt.zlim(-2*R_e, 2*R_e)
#plt.legend(['Afgelegde weg proton','Afgelegde weg elektron'])


plt.legend() 
plt.show()











