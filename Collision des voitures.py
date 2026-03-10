import pandas as pd
import tkinter as tk
import numpy as np

# ==============================Voiture1==============================

# ------------------------------masse 1------------------------------
while True:
    try:
        masse_voiture1 = float(input("Entrer la masse (kg) du premier vehicule:"))
        if masse_voiture1 == 0:
            print("ERREUR: La masse (kg) du véhicule 1 ne peut pas être 0 kg!")
        else:
            break
    except ValueError:
        print("ERREUR: Veuillez entrer un nombre valide!")

# ------------------------------vitesses 1------------------------------
while True:
    try:
        vitesse_initiale1 = float(input("Entrer la vitesse initiale (m/s) du premier véhicule:"))
        break
    except ValueError:
        print("ERREUR: Veuillez entrer un nombre valide!")


# ------------------------------positions 1 en x------------------------------
while True:
    try:
        position_x_1 = float(input("Indiquer la position initiale (m) de la voiture 1 en x entre -20m et 20m:"))
        if -20 <= position_x_1 <= 20:
            break
        else:
            print("ERREUR: La position initiale (m) de la voiture 1 en x doit être entre -20m et 20m")
    except ValueError:
        print("ERREUR: Veuillez entrer un nombre valide!")

while True:
    try:
        positionfinale_x_1 = float(input("Indiquer la position finale (m) de la voiture 1 en x entre -20m et 20m:"))
        if -20 <= positionfinale_x_1 <= 20:
            break
        else:
            print("ERREUR: La position finale (m) de la voiture 1 en x doit être entre -20m et 20m")
    except ValueError:
        print("ERREUR: Veuillez entrer un nombre valide!")

    # ------------------------------positions 1 en y------------------------------
while True:
    try:
        position_y_1 = float(input("Indiquer la position initiale (m) de la voiture 1 en y entre -20m et 20m:"))
        if -20 <= position_y_1 <= 20:
            break
        else:
            print("ERREUR: La position initiale (m) de la voiture 1 en y doit être entre -20m et 20m")
    except ValueError:
        print("ERREUR: Veuillez entrer un nombre valide!")

while True:
    try:
        positionfinale_y_1 = float(input("Indiquer la position finale (m) de la voiture 1 en y entre -20m et 20m:"))
        if -20 <= positionfinale_y_1 <= 20:
            break
        else:
            print("ERREUR: La position finale (m) de la voiture 1 en y doit être entre -20m et 20m")
    except ValueError:
        print("ERREUR: Veuillez entrer un nombre valide!")

# ==============================Voiture2==============================

# ------------------------------masse 2------------------------------
while True:
    try:
        masse_voiture2 = float(input("Entrer la masse (kg) du deuxième vehicule:"))
        if masse_voiture2 == 0:
            print("ERREUR: La masse (kg) du véhicule 2 ne peut pas être 0 kg!")
        else:
            break
    except ValueError:
        print("ERREUR: Veuillez entrer un nombre valide!")

# ------------------------------vitesses 2------------------------------
while True:
    try:
        vitesse_initiale2 = float(input("Entrer la vitesse initiale (m/s) du deuxième véhicule:"))
        break
    except ValueError:
        print("ERREUR: Veuillez entrer un nombre valide!")
# ------------------------------positions 2 en x------------------------------
while True:
    try:
        position_x_2 = float(input("Indiquer la position initiale (m) de la voiture 2 en x entre -20m et 20m:"))
        if -20 <= position_x_2 <= 20:
            break
        else:
            print("ERREUR: La position initiale (m) de la voiture 2 en x doit être entre -20m et 20m")
    except ValueError:
        print("ERREUR: Veuillez entrer un nombre valide!")

while True:
    try:
        positionfinale_x_2 = float(input("Indiquer la position finale (m) de la voiture 2 en x entre -20m et 20m:"))
        if -20 <= positionfinale_x_2 <= 20:
            break
        else:
            print("ERREUR: La position finale (m) de la voiture 2 en x doit être entre -20m et 20m")
    except ValueError:
        print("ERREUR: Veuillez entrer un nombre valide!")

# ------------------------------positions 2 en y------------------------------
while True:
    try:
        position_y_2 = float(input("Indiquer la position initiale (m) de la voiture 2 en y entre -20m et 20m:"))
        if -20 <= position_y_2 <= 20:
            break
        else:
            print("ERREUR: La position initiale (m) de la voiture 2 en y doit être entre -20m et 20m")
    except ValueError:
        print("ERREUR: Veuillez entrer un nombre valide!")

while True:
    try:
        positionfinale_y_2 = float(input("Indiquer la position finale (m) de la voiture 2 en y entre -20m et 20m:"))
        if -20 <= positionfinale_y_2 <= 20:
            break
        else:
            print("ERREUR: La position finale (m) de la voiture 2 en y doit être entre -20m et 20m")
    except ValueError:
        print("ERREUR: Veuillez entrer un nombre valide!")


# vérification de collisions
#==============================Collision sur trajectoire==============================

# Nombre de pas pour simuler le déplacement
n_steps = 1000

# Création des trajectoires linéaires
x_traj_1 = np.linspace(position_x_1, positionfinale_x_1, n_steps)
y_traj_1 = np.linspace(position_y_1, positionfinale_y_1, n_steps)

x_traj_2 = np.linspace(position_x_2, positionfinale_x_2, n_steps)
y_traj_2 = np.linspace(position_y_2, positionfinale_y_2, n_steps)

collision_detectee = False
tolerance = 0.1  # tolérance de 0.1 m pour considérer une collision

for i in range(n_steps):
    distance = np.sqrt((x_traj_1[i] - x_traj_2[i])**2 + (y_traj_1[i] - y_traj_2[i])**2)
    if distance <= tolerance:
        collision_detectee = True
        print("\n Collision détectée !")
        break

if not collision_detectee:
    print("\n Aucune collision détectée sur la trajectoire.")

#------------------------------creation du tableau comparatif------------------------------

donnes_dict = {
    'Vitesse initiale (m/s)': [vitesse_initiale1, vitesse_initiale2],
    "Position initiale (m)": [position_x_1, position_x_2],
    'Position finale (m)': [positionfinale_x_1, positionfinale_x_2],
    'Trajectoire (m)' : [x_traj_1[i],y_traj_1[i]],
    'Vitesse finale des vehicules apres la collision (m/s)': [0,0], #parfaitement inelastique (pour le sprint 1)
    'Masse (kg)': [masse_voiture1, masse_voiture2],
}
df_donnes_collision_voitures = pd.DataFrame(donnes_dict, index=['Vehicule 1', 'Vehicule 2'])
print(df_donnes_collision_voitures.round(2).to_string())
