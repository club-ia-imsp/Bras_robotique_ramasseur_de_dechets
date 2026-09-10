# Cahier des charges

## Contexte et Objectif

Ce projet vise à automatiser l’assainissement des villes afin  permettre aux êtres humains de se concentrer sur des tâches beaucoup plus valorisantes . Il consistera à créer un robot mobile munie d’un bras lui permettant de saisir les déchets et de les placer dans des corbeilles embarquées. Le choix de la corbeille dépendra de la nature du déchet détecté et ainsi le robot facilitera dans le même temps le recyclage des déchets pour une utilisation ultérieure. 

## Fonction attendues

- Détecter et ramasser des déchets précis dans un environnement bien déterminé
- Eviter les obstacles
- Préciser le nombre de déchets triés pour chaque catégorie

## Contraintes du système

### Pour le bras robotique

- Longueur totale ≥700mm
- Charge maximale : 500 g
- Nombre de degrés de libertés : 5
- Précision du mouvement: +-5mm
- Espace de travail minimum de 9 m2

### Pour la voiture

- Supporter la charge du bras robotique en plus de la charge maximale autorisée .
- Avoir une autonomie de 10 minutes au minimum
- Précision de la détection des déchets : +-5mm

## Quelques spécifications techniques

- Le robot utilisera principalement des servo moteurs MG vu que les charges à soulever ( les déchets ) ne pèsent pas trop
- Utilisation de Roboflow pour l’annotation des données
- Utilisation de YOLO pour l’entraînement (fine tunning)
- Composants électroniques à utiliser :
    - mini ordinateur embarqué pour faire tourner le modèle : Raspberry pi
    - Servo moteurs MG
    - Kit de voiture : roues+ moteur+driver
    - Capteurs ultrasons pour l’évitement d’obstacles
    - Carte électronique permettant de relier différents composants ( à  conçevoir)
    - Caméra pour la détection des déchets
    - ESP 32/ Arduino : recevoir des commandes du mini ordinateur et contrôler les moteurs et capteurs
    

## Travail à faire et Méthodologie

### Partie mécanique

- Prise en main du logiciel de modélisation SolidWorks
- Conception du modèle 3D du bras robotique et du châssis
- Impression des pièces
- Test et corrections

### Partie Electronique

- Prise en main du principe de fonctionnement et  du câblage des différents composants électronique intervenant dans le système
- Conception des  cartes électronique  reliant les composants électronique du bras robotique et ceux de la voiture
- Tests et validations

### Partie informatique

- Prise en main des outils nécessaire à la détection : Roboflow pour l’annotation d’images , YOLO pour l’entraînement
- Collecte des données : Prise d’images de différents types de déchets
- Annotation des images
- Entraînement d’un modèle YOLO chargé de reconnaître les déchets
- Déploiements tests et corrections

##