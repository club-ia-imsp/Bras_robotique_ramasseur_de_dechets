# Documentation Projet bras robotique

## Contexte et Objectif

L'objectif du projet était de développer un prototype de robot ramasseur de déchets afin d'automatiser l'assainissement de nos villes. Le robot devrait disposer de deux grandes parties : un bras articulé chargé de ramasser les déchets et de les déposer dans une corbeille embarquée, puis un châssis chargé de transporter le système et de le faire naviguer dans l'environnement tout en évitant les obstacles.

## Méthode adoptée et travail effectué

Afin de mieux structurer et d'optimiser l'efficacité, l'équipe a été divisée en trois pôles : le pôle mécanique chargé de la structure mécanique du système, le pôle électronique chargé de concevoir le système électronique, et le pôle informatique dont l'objectif est d'implémenter les différents programmes devant permettre au robot de fonctionner et d'accomplir sa tâche.

### 1. Travail effectué par la partie mécanique

Pour rappel, le bras robotique à construire devait répondre aux exigences suivantes :

- Longueur totale ≥ 700 mm
- Charge maximale : 500 g
- Nombre de degrés de liberté : 6 (5 si possible)
- Précision du mouvement : ± 5 mm

L'objectif dans un premier temps était d'initier les membres de ce pôle à la conception assistée par ordinateur en utilisant le logiciel SolidWorks à travers la modélisation d'un bras robotique déjà existant (voir le tutoriel de modélisation en annexe), puis dans un second temps de designer la structure mécanique complète du robot.

Cependant, ce bras présentait quelques inconvénients, notamment l'absence de place pour les moteurs, ce qui a compliqué sa mise en place réelle. De plus, le design complet d'un bras robotique demandait des compétences plus avancées en conception mécanique. Ainsi, la solution finalement envisagée consiste à imprimer un modèle déjà existant de bras robotique afin d'accélérer les travaux (voir le lien de téléchargement des fichiers 3D en annexe).

La suite consiste donc à imprimer les pièces du bras et à assembler toutes les pièces.

### 2. Travail effectué par la partie électronique

Le rôle de la partie électronique consistait à faire fonctionner les capteurs et actionneurs dont le système devrait être équipé. Voici une liste de ces équipements :

- **Capteur Ultrason** (Tutoriel de fonctionnement : https://www.moussasoft.com/hc-sr04-capteur-ultrason-avec-arduino/)
- **Kit de voiture à 4 roues** (Tutoriel : https://www.instructables.com/4WD-SMART-ROBOT-CAR/)
- **Servomoteurs** (Tutoriel : https://arduino.developpez.com/tutoriels/arduino-a-l-ecole/?page=projet-12-utiliser-un-servomoteur)
- **Caméra**
- **Microcontrôleur ESP32** (compréhension et utilisation : https://www.upesy.fr/blogs/tutorials/esp32-quickstart-installation-programming-guide)

Il s'agissait dans un premier temps d'étudier le fonctionnement de ces différents composants afin de pouvoir les intégrer de façon efficace au système. Cette étude fut à peu près réalisée, mais sans réel impact sur le projet général, le robot physique n'étant pas présent.

### 3. Partie informatique

L'objectif ici était d'entraîner un modèle de détection d'objets capable de reconnaître un certain nombre de déchets (bouteilles de 50 cl, canettes, papiers froissés, etc.). Des recherches ont donc été effectuées, mais rien n'a pu être fait compte tenu du manque d'expertise technique dans le domaine et de la disponibilité des membres.

## Annexe

### Mécanique

- [Fichiers 3D du bras à imprimer](https://drive.google.com/drive/folders/1QIcgumQFBaZ3t6ZXj4NdoFknqQUg_Gtr?usp=sharing)

### Électronique

- [Tutoriel capteur ultrason HC-SR04 avec Arduino](https://www.moussasoft.com/hc-sr04-capteur-ultrason-avec-arduino/)
- [Tutoriel kit voiture 4 roues (Instructables)](https://www.instructables.com/4WD-SMART-ROBOT-CAR/)
- [Tutoriel utilisation d'un servomoteur avec Arduino](https://arduino.developpez.com/tutoriels/arduino-a-l-ecole/?page=projet-12-utiliser-un-servomoteur)
- [Guide de démarrage ESP32 (UPESY)](https://www.upesy.fr/blogs/tutorials/esp32-quickstart-installation-programming-guide)

### Informatique

- [Initiation à la détection d'objets — YOLO (DataCamp)](https://www.datacamp.com/fr/blog/yolo-object-detection-explained)
- [Documentation Ultralytics — détection](https://docs.ultralytics.com/fr/tasks/detect)

### Autre lien utile

- [SO-ARM100 — GitHub (TheRobotStudio)](https://github.com/TheRobotStudio/SO-ARM100)
