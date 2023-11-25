# -*- coding: utf-8 -*-
# Programma-naam: Het file-probleem
 
import math as mth
import random as rnd
import matplotlib.pyplot as plt

# Hoofdstuk 8
# 8.4 Opdracht 4: Het file-probleem


M = 1200     # Aantal zones
R = 1       # Straal van de ronde baan
v_max = 10  # Maximum snelheid
t_max = 20 # Aantal tijdstappen
N_max = 200 # maximaal aantal auto's
L_v_gem = []    # Lijst met gemiddelde snelheden
L_N = [] # Lijst met N-waarden


# beginposities auto's (in zones):
rad_zone = float(2 * mth.pi) / M # Aantal radialen per zone

for N in range(1,N_max): # N bepaald de dichtheid
    L_v = []    # Lijst met snelheden
    L_A = []    # Lijst met posities en snelheden van auto's    
    begin_afst = M/N # begin afstand tussen de auto's in aantal zones.
    # !!! Deze mag niet groter worden dan M / N, anders staan de auto's niet 
    # meer juist in volgorde !!!
    
    for auto_i in range (0,N):
        pos_i = begin_afst * auto_i
        L_pv = [pos_i, 0.0]# Lijst met positie en snelheid 
        L_A.append(L_pv)
    
    # Beginsnelheden auto's (in aantal zones per tijdseenheid):
    for auto_j in range(0,N):
        v_j = rnd.random() * v_max # Beginsnelheden worden random bepaald. 
        L_A[auto_j][1] = int(v_j) 
    
    
    # Rijden auto's:
    p = 0.1 # De kans dat een auto vertraagt
    
    for t in range(0,t_max):
        # Plotten van de auto's:
    
        L_x = []
        L_y = []
            
        for j in range(0,N):
            rad_j = rad_zone * L_A[j][0]
            x = R * mth.cos(rad_j)
            y = R * mth.sin(rad_j)
            L_x.append(x)
            L_y.append(y)
        if N == 15: # plot alleen de situatie met 15 auto's
            plt.figure(1)
            plt.plot(L_x,L_y,'bo', markersize = 10)
            plt.xlim(-1.5*R, 1.5*R)
            plt.ylim(-1.5*R, 1.5*R)
            plt.draw() # update grafiek
            plt.pause(0.001) 
            plt.clf() # clear grafiek
        
        for i in range(0,N):
                
        # Snelheden:
            
            # Voorkomen van botsen:
            if i == N - 1:
                p_voorligger = L_A[0][0] + M # positie 'voorligger'; M wordt er 
                # toegevoegd omdat de L_A[0][0] een rondje achterloopt
                d = p_voorligger - L_A[i][0]
            else: 
                p_voorligger = L_A[i+1][0] # positie voorligger; auto's moeten in 
                # volgorde blijven!   
                d = p_voorligger - L_A[i][0] # afstand tussen auto i en voorligger
            if d > M: # als de voorligger een of meerdere rondjes voorloopt op auto i
                d = d % M # dan is de afstand de resthoeveelheid bij een deling door M 
            if L_A[i][1] >= d:
                L_A[i][1] = d - 1 # verlagen van de snelheid  
            else:
                
            # auto's versnellen tot maximum snelheid:
                if L_A[i][1] < v_max:
                    L_A[i][1] += 1 # auto versnelt            
            
            # auto's random vertragen:
            p_test = rnd.random()
            if p_test < p and L_A[i][1] > 0:
                L_A[i][1] -= 1 # Auto vertraagd op basis van toevalsvariabele
            
            # auto's mogen niet achteruit rijden:
            if L_A[i][1] < 0:
                L_A[i][1] = 0 
            
            L_v.append(L_A[i][1]) # eindsnelheid wordt opgeslagen in lijst L_v
                    
        # nieuwe positie auto            
            L_A[i][0] = L_A[i][0] + L_A[i][1]
        
    som_v = 0
    for v in L_v:
        som_v = som_v + v
    v_gem = float(som_v) / len(L_v) 
    L_v_gem.append(v_gem)
    L_N.append(float(N)/M)

# plotten van de grafiek: gemiddelde snelheid vs. auto-dichtheid
plt.figure(2)
plt.plot(L_N,L_v_gem)
plt.xlabel('Auto-dichtheid N/M')
plt.ylabel('gemiddelde snelheid zones/t')
plt.show()












