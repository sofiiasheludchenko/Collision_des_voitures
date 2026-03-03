import pandas as pd

#==============================Voiture1==============================

#------------------------------masse 1------------------------------
while True:
    masse_voiture1 = float(input("Entrer la masse (kg) du premier vehicule:"))
    if masse_voiture1 == 0:
        print("Erreur: La masse du véhicule 1 ne peut pas être 0 kg!")
    else:
        break

#------------------------------vitesses 1------------------------------
vitesse_initiale1 = float(input("Entrer la vitesse (m/s) initiale du premier véhicule:"))
vitesse_finale = float(input("Entrer la vitesse finale (m/s) souhaité du vehicule 1:"))

#------------------------------positions 1 en x------------------------------
while True:  # le loop fait en sorte que si l'utilisateur met une valeur hors de -20 et 20, ca affiche un message d'erreur tant qu'il met une valeur valide
    position_x_1 = float(input("Indiquer la position de la voiture 1 en x entre -20m et 20m:"))  # Attention lorsque la position ne rentre pas dans les restrictions: Afficher erreur.
    if -20 <= position_x_1 <= 20:
        break
    else:
        print("Erreur: La position de la voiture 1 en x doit être entre -20m et 20m")

while True:  # le loop fait en sorte que si l'utilisateur met une valeur hors de -20 et 20, ca affiche un message d'erreur tant qu'il met une valeur valide
    positionfinale_x_1 = float(input("Indiquer la position finale de la voiture 1 en x entre -20m et 20m:"))  # Attention lorsque la position ne rentre pas dans les restrictions: Afficher erreur.
    if -20 <= positionfinale_x_1 <= 20:
        break
    else:
        print("Erreur: La position finale de la voiture 1 en x doit être entre -20m et 20m")  

#------------------------------positions 1 en y------------------------------
while True:
    position_y_1 = float(input("Indiquer la position de la voiture 1 en y entre -20m et 20m:"))
    if -20 <= position_y_1 <= 20:
        break
    else:
        print("Erreur: La position de la voiture 1 en y doit être entre -20m et 20m")

while True:
    positionfinale_y_1 = float(input("Indiquer la position de la voiture 1 en y entre -20m et 20m:"))
    if -20 <= position_y_1 <= 20:
        break
    else:
        print("Erreur: La position de la voiture 1 en y doit être entre -20m et 20m")





#==============================Voiture2==============================

#------------------------------masse 2------------------------------
while True:
    masse_voiture2 = float(input("Entrer la masse (kg) du deuxième vehicule:"))
    if masse_voiture2 == 0:
        print("Erreur: La masse du véhicule 2 ne peut pas être 0 kg!")
    else:
        break

#------------------------------vitesses 2------------------------------
vitesse_initiale2 = float(input("Entrer la vitesse (m/s) intiale du deuxième véhicule:"))
vitesse_finale = float(input("Entrer la vitesse finale souhaité du vehicule 2:"))


#------------------------------positions 2 en x------------------------------
while True:
    position_x_2 = float(input("Indiquer la position de la voiture 2 en x entre -20m et 20m:"))
    if -20 <= position_x_2 <= 20:
        break
    else:
        print("Erreur: La position de la voiture 2 en x doit être entre -20m et 20m")



#------------------------------positions 2 en y------------------------------
while True:
    position_y_2 = float(input("Indiquer la position de la voiture 2 en y entre -20m et 20m du deuxième vehicule:"))
    if -20 <= position_y_2 <= 20:
        break
    else:
        print("Erreur: La position de la voiture 2 en y doit être entre -20m et 20m")

        while True:
    positionfinale_x_2 = int(input("Indiquer la position finale de la voiture 2 en x entre -20m et 20m:"))
    if -20 <= positionfinale_x_2 <= 20:
        break
    else:
        print("Erreur: La position finale de la voiture 2 en x doit être entre -20m et 20m")

while True:
    positionfinale_y_2 = int(input("Indiquer la position finale de la voiture 2 en y entre -20m et 20m du deuxième vehicule:"))
    if -20 <= positionfinale_y_2 <= 20:
        break
    else:
        print("Erreur: La position finale de la voiture 2 en y doit être entre -20m et 20m")
        
#Creation du tableau comparatif
donnes_dict = {
    'Vitesse initiale (m)': vitesse_initiale1, 
    'Vitesse finale (m)': 
    'Masse (kg)': []
}
df_donnes_collision_voitures = pd.DataFrame(donnes_dict, index=['Vehicule 1','Vehicule 2'])
print(df_donnes_collision_voitures)
