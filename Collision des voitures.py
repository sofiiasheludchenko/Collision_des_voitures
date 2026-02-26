#Voiture1
vitesse_initiale1 = int(input("Entrer la vitesse (m/s) initiale du premier véhicule:"))
masse_voiture1 = int(input("Entrer la masse (kg) du premier vehicule:"))

while True: #le loop fait en sorte que si l'utilisateur met une valeur hors de -20 et 20, ca affiche un message d'erreur tant qu'il met une valeur valide
  position_x_1 = int(input("Indiquer la position de la voiture 1 en x entre -20m et 20m:")) #Attention lorsque la position ne rentre pas dans les restrictions: Afficher erreur.
  if -20 <= position_x_1 <= 20:
    break
  else:
    print("Erreur: La position de la voiture 1 en x doit être entre -20m et 20m")

while True:
  position_y_1 = int(input("Indiquer la position de la voiture 1 en y entre -20m et 20m:"))
  if -20 <= position_y_1 <= 20:
    break
  else:
    print("Erreur: La position de la voiture 1 en y doit être entre -20m et 20m")
  


#Voiture2
vitesse_initiale2 = int(input("Entrer la vitesse (m/s) intiale du deuxième véhicule:"))
masse_voiture2 = int(input("Entrer la masse (kg) du deuxième vehicule:"))

while True:
  position_x_2 = int(input("Indiquer la position de la voiture 2 en x entre -20m et 20m:"))
  if -20 <= position_x_2 <= 20:
    break
  else:
    print("Erreur: La position de la voiture 2 en x doit être entre -20m et 20m")

while True:
  position_y_2 = int(input("Indiquer la position de la voiture 2 en y entre -20m et 20m du deuxième vehicule:"))
  if -20 <= position_y_2 <= 20:
    break
  else:
    print("Erreur: La position de la voiture 2 en y doit être entre -20m et 20m")
