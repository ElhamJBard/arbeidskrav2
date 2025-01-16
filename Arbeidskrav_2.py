""" Arbeidskrav 2 """


# Oppgave 1
# beregning av alder til brukeren i 2024

alder = int(input('Hvilket år er du født?'))
alder_i_2024 = 2024 - alder
print = (f' Du vil være {alder_i_2024} i 2024.')



# Oppgave 2
# antall pizza som skal kjøpes inn til klassefesten

import math

antall_elever = int(input('Skriv inn antall elever:' ))
antall_pizza_som_trengs = antall_elever / 4 
antall_pizzaer = math.ceil(antall_pizza_som_trengs) # for å runde opp antall pizza slik at det ikke blir for lite
print(f'Det må kjøpes {antall_pizzaer} pizza til festen.')



# oppgave 3 
# beregning av grader til radianer


import numpy as np

v_grad = float(input('Skriv inn gradtallet:' ))

def beregning_radianer(grader):
    radianer = grader* (np.pi/180)
    return radianer

radianer = beregning_radianer(v_grad)
print(f'{v_grad} grader er {radianer} radianer')


# oppgave 4a
# dictionary med ulike tall

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike":["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }
 
# oppgave 4b
land_input = input("Hvilket land ønsker du å sjekke? \n")
print(f"Hovedstaden i landet er {data[land_input][0]} og det er {data[land_input][1]} millioner innbyggere i hovedstaden.")
 
# oppgave 4c
nytt_land = input("Ønsker du å legge til et nytt land? Skriv inn ja eller nei for å gå videre.")
 
if nytt_land == "ja":
    nytt_land_valg = input("hvilket land? ")
    hovedstad = input("hva er hovedstaden? ")
    innbyggere = input("hvor mange innbyggere er det? ")
    data[nytt_land_valg] = [hovedstad, innbyggere]
else:
    print("Du har valgt å ikke legge til flere land i dictionary dataen.")
print(data)



# oppgave 5
# arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant og en halv sirkel

import math

def beregning_av_areal_og_omkrets(a, b):
    
    # beregning av areal av halvsirkel
    radius = a / 2
    areal_halvsirkel = (math.pi * radius**2) / 2
    
    # begrening av areal av trekant
    areal_trekant = (a * b) / 2
    
    # beregning av areal samlet
    areal_samlet = areal_halvsirkel + areal_trekant
    
    # beregning av omkrets: buelengde av halvsirkel + skrålinje + b
    buelengde_halvsirkel = math.pi * radius
    skrålinje = math.sqrt(a**2 + b**2)
    ytre_omkrets = buelengde_halvsirkel + skrålinje + b 
    
    return areal_samlet, ytre_omkrets

a = 10 # lengden av a
b = 7 # lengden av b

# hent ut resultatene fra funksjonen
areal_samlet, ytre_omkrets = beregning_av_areal_og_omkrets(a, b)

# utskrift av resultatene
print(f'Arealet av figuren er {areal_samlet:.2f} kvm')
print(f'Den ytre omkretsen er {ytre_omkrets:.2f} meter')



# oppgave 6 
# kode som plotter funksjonen 𝑓(𝑥) = −𝑥2 − 5, for x på intervallet [-10,10]

import numpy as np

import matplotlib.pyplot as plt
 
x = np.linspace(-10, 10, 200)

y = -x**2 -5

plt.plot(x, y , color="pink")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plotting av funkasjon f(x)")
plt.grid()
plt.show()
