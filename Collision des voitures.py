import pandas as pd
import tkinter as tk

# ==============================Voiture1==============================

# ------------------------------masse 1------------------------------
while True:
    masse_voiture1 = float(input("Entrer la masse (kg) du premier vehicule:"))
    if masse_voiture1 == 0:
        print("Erreur: La masse (kg) du véhicule 1 ne peut pas être 0 kg!")
    else:
        break

# ------------------------------vitesses 1------------------------------
vitesse_initiale1 = float(input("Entrer la vitesse initiale (m/s) du premier véhicule:"))
position_finale1 = float(input("Entrer la position finale (m) souhaité du vehicule 1:"))

# ------------------------------positions 1 en x------------------------------
while True:  # le loop fait en sorte que si l'utilisateur met une valeur hors de -20 et 20, ca affiche un message d'erreur tant qu'il met une valeur valide
    position_x_1 = float(input("Indiquer la position initiale (m) de la voiture 1 en x entre -20m et 20m:"))  # Attention lorsque la position ne rentre pas dans les restrictions: Afficher erreur.
    if -20 <= position_x_1 <= 20:
        break
    else:
        print("Erreur: La position initiale (m) de la voiture 1 en x doit être entre -20m et 20m")

while True:  # le loop fait en sorte que si l'utilisateur met une valeur hors de -20 et 20, ca affiche un message d'erreur tant qu'il met une valeur valide
    positionfinale_x_1 = float(input("Indiquer la position finale (m) de la voiture 1 en x entre -20m et 20m:"))  # Attention lorsque la position ne rentre pas dans les restrictions: Afficher erreur.
    if -20 <= positionfinale_x_1 <= 20:
        break
    else:
        print("Erreur: La position finale (m) de la voiture 1 en x doit être entre -20m et 20m")

    # ------------------------------positions 1 en y------------------------------
while True:
    position_y_1 = float(input("Indiquer la position initiale (m) de la voiture 1 en y entre -20m et 20m:"))
    if -20 <= position_y_1 <= 20:
        break
    else:
        print("Erreur: La position initiale (m) de la voiture 1 en y doit être entre -20m et 20m")

while True:
    positionfinale_y_1 = float(input("Indiquer la position finale (m) de la voiture 1 en y entre -20m et 20m:"))
    if -20 <= position_y_1 <= 20:
        break
    else:
        print("Erreur: La position finale (m) de la voiture 1 en y doit être entre -20m et 20m")

# ==============================Voiture2==============================

# ------------------------------masse 2------------------------------
while True:
    masse_voiture2 = float(input("Entrer la masse (kg) du deuxième vehicule:"))
    if masse_voiture2 == 0:
        print("Erreur: La masse (kg) du véhicule 2 ne peut pas être 0 kg!")
    else:
        break

# ------------------------------vitesses 2------------------------------
vitesse_initiale2 = float(input("Entrer la vitesse intiale (m/s) du deuxième véhicule:"))
position_finale2 = float(input("Entrer la position finale (m) souhaité du vehicule 2:"))

# ------------------------------positions 2 en x------------------------------
while True:
    position_x_2 = float(input("Indiquer la position initiale (m) de la voiture 2 en x entre -20m et 20m:"))
    if -20 <= position_x_2 <= 20:
        break
    else:
        print("Erreur: La position initiale (m) de la voiture 2 en x doit être entre -20m et 20m")

while True:
    positionfinale_x_2 = float(input("Indiquer la position finale (m) de la voiture 2 en x entre -20m et 20m:"))
    if -20 <= positionfinale_x_2 <= 20:
        break
    else:
        print("Erreur: La position finale (m) de la voiture 2 en x doit être entre -20m et 20m")

# ------------------------------positions 2 en y------------------------------
while True:
    position_y_2 = float(input("Indiquer la position initiale (m) de la voiture 2 en y entre -20m et 20m du deuxième vehicule:"))
    if -20 <= position_y_2 <= 20:
        break
    else:
        print("Erreur: La position initiale (m) de la voiture 2 en y doit être entre -20m et 20m")

while True:
    positionfinale_y_2 = float(
        input("Indiquer la position finale (m) de la voiture 2 en y entre -20m et 20m du deuxième vehicule:"))
    if -20 <= positionfinale_y_2 <= 20:
        break
    else:
        print("Erreur: La position finale (m) de la voiture 2 en y doit être entre -20m et 20m")

#------------------------------creation du tableau comparatif------------------------------

donnes_dict = {
    'Vitesse initiale (m)': [vitesse_initiale1, vitesse_initiale2],
    'Position vers la quelle la voiture se dirigeait (m)': [position_finale1, position_finale2],
    'Position finale des vehicules apres la collision(m)'
    'Vitesse finale des vehicules apres la collision (m)': [0,0], #parfaitement inelastique (pour le sprint 1)
    'Masse (kg)': [masse_voiture1, masse_voiture2],
}
df_donnes_collision_voitures = pd.DataFrame(donnes_dict, index=['Vehicule 1', 'Vehicule 2'])
print(df_donnes_collision_voitures)
# vérification de collisions
#==============================Collision sur trajectoire==============================

import numpy as np

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
        print(f"\n Collision détectée ! Les voitures se rencontrent à environ x={x_traj_1[i]:.2f} m, y={y_traj_1[i]:.2f} m")
        break

if not collision_detectee:
    print("\n Aucune collision détectée sur la trajectoire.")

