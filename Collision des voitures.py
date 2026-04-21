
import pandas as pd
import numpy as np

# ==============================Voiture1==============================

while True:
    try:
        masse_voiture1 = float(input("Entrer la masse (kg) du premier vehicule:"))
        if masse_voiture1 == 0:
            print("ERREUR: La masse ne peut pas être 0!")
        else:
            break
    except ValueError:
        print("ERREUR: nombre invalide!")

while True:
    try:
        vitesse_initiale1 = float(input("Entrer la vitesse initiale (m/s) du premier véhicule:"))
        break
    except ValueError:
        print("ERREUR!")

while True:
    try:
        position_x_1 = float(input("Position x voiture 1 (-20 à 20):"))
        if -20 <= position_x_1 <= 20:
            break
    except:
        print("ERREUR!")

while True:
    try:
        position_y_1 = float(input("Position y voiture 1 (-20 à 20):"))
        if -20 <= position_y_1 <= 20:
            break
    except:
        print("ERREUR!")

while True:
    try:
        angle_1 = float(input("Angle voiture 1 (0 à 360):"))
        if 0 <= angle_1 <= 360:
            break
    except:
        print("ERREUR!")

masse_passager1 = float(input("Masse du passager 1 (kg):"))
ceinture1 = input("Passager 1 a une ceinture? (o/n):").strip().lower() == 'o'

# ==============================Voiture2==============================

while True:
    try:
        masse_voiture2 = float(input("Entrer la masse (kg) du deuxième vehicule:"))
        if masse_voiture2 == 0:
            print("ERREUR!")
        else:
            break
    except:
        print("ERREUR!")

while True:
    try:
        vitesse_initiale2 = float(input("Entrer la vitesse initiale (m/s) du deuxième véhicule:"))
        break
    except:
        print("ERREUR!")

while True:
    try:
        position_x_2 = float(input("Position x voiture 2 (-20 à 20):"))
        if -20 <= position_x_2 <= 20:
            break
    except:
        print("ERREUR!")

while True:
    try:
        position_y_2 = float(input("Position y voiture 2 (-20 à 20):"))
        if -20 <= position_y_2 <= 20:
            break
    except:
        print("ERREUR!")

while True:
    try:
        angle_2 = float(input("Angle voiture 2 (0 à 360):"))
        if 0 <= angle_2 <= 360:
            break
    except:
        print("ERREUR!")

masse_passager2 = float(input("Masse du passager 2 (kg):"))
ceinture2 = input("Passager 2 a une ceinture? (o/n):").strip().lower() == 'o'

# ==============================MOUVEMENT==============================

angle1_rad = np.radians(angle_1)
angle2_rad = np.radians(angle_2)

vx1 = vitesse_initiale1 * np.cos(angle1_rad)
vy1 = vitesse_initiale1 * np.sin(angle1_rad)

vx2 = vitesse_initiale2 * np.cos(angle2_rad)
vy2 = vitesse_initiale2 * np.sin(angle2_rad)

# ==============================DETECTION COLLISION==============================

dt = 0.01
temps = 0
temps_max = 10

collision = False

while temps < temps_max:
    x1 = position_x_1 + vx1 * temps
    y1 = position_y_1 + vy1 * temps

    x2 = position_x_2 + vx2 * temps
    y2 = position_y_2 + vy2 * temps

    distance = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    if distance < 1:
        collision = True
        temps_collision = temps
        positionfinale_x_1 = x1
        positionfinale_x_2 = x2
        break

    temps += dt

# ==============================PHYSIQUE==============================

if collision:
    # Quantité de mouvement
    q1 = masse_voiture1 * vx1
    q2 = masse_voiture2 * vx2

    q_total = q1 + q2

    # Vitesse finale (inelastique)
    vitesse_finale = (q1 + q2) / (masse_voiture1 + masse_voiture2)

    # variation de vitesse
    delta_v1 = vitesse_finale - vx1
    delta_v2 = vitesse_finale - vx2

    # temps collision physique
    temps_collision_physique = 0.1

    # décélération
    a1 = delta_v1 / temps_collision_physique
    a2 = delta_v2 / temps_collision_physique

    # forces
    F1 = masse_voiture1 * a1
    F2 = masse_voiture2 * a2

    # énergie
    E_initiale = 0.5 * masse_voiture1 * vitesse_initiale1**2 + 0.5 * masse_voiture2 * vitesse_initiale2**2
    E_finale = 0.5 * (masse_voiture1 + masse_voiture2) * vitesse_finale**2
    E_dissipee = E_initiale - E_finale

    # Affichage des résultats avec deux chiffres après la virgule
    print("\n===== COLLISION DETECTEE =====")
    print(f"Temps de collision: {temps_collision:.2f} s")
    print(f"Vitesse résiduelle: {vitesse_finale:.2f} m/s")
    print(f"Force subie par chacun des deux véhicules: {abs(F1):.2f} N")
    print(f"Energie dissipée dans la collision: {E_dissipee:.2f} J")

    # ==============================IMPACT PASSAGERS==============================

    # Force du passager = même force que le vehicule (proportionnelle a sa masse)
    F_passager1 = abs(F1) * (masse_passager1 / masse_voiture1)
    F_passager2 = abs(F2) * (masse_passager2 / masse_voiture2)

    # Sans ceinture la force est plus grande 
    if not ceinture1:
        F_passager1 = F_passager1 * 2
    if not ceinture2:
        F_passager2 = F_passager2 * 2

    print("\n===== IMPACT SUR LES PASSAGERS =====")
    print(f"--- Passager 1 ---")
    print(f"Ceinture: {'OUI' if ceinture1 else 'NON'}")
    print(f"Force ressentie: {F_passager1:.2f} N")
    print(f"--- Passager 2 ---")
    print(f"Ceinture: {'OUI' if ceinture2 else 'NON'}")
    print(f"Force ressentie: {F_passager2:.2f} N")

else:
    print("\nAucune collision détectée")

# ==============================TRAJECTOIRES==============================

n_steps = 50

x_traj_1 = np.linspace(position_x_1, position_x_1 + vx1*2, n_steps)
y_traj_1 = np.linspace(position_y_1, position_y_1 + vy1*2, n_steps)

# ==============================TABLEAU==============================

positionfinale_x_1 = position_x_1 if not collision else positionfinale_x_1
positionfinale_x_2 = position_x_2 if not collision else positionfinale_x_2

donnes_dict = {
    'Vitesse initiale (m/s)': [vitesse_initiale1, vitesse_initiale2],
    'Position initiale X': [position_x_1, position_x_2],
    'Position finale X': [positionfinale_x_1, positionfinale_x_2],
    'Masse (kg)': [masse_voiture1, masse_voiture2],
}

df = pd.DataFrame(donnes_dict, index=['Vehicule 1', 'Vehicule 2'])
print("\nTableau récapitulatif:")
print(df.round(2).to_string())
