# Projet Bras Robotique — Robot Ramasseur de Déchets

## 🎯 Contexte et Objectif

L'objectif du projet est de développer un **prototype de robot ramasseur de déchets** afin d'automatiser l'assainissement urbain. Le robot est conçu autour de deux grandes parties :

- **Un bras articulé** chargé de ramasser les déchets et de les déposer dans une corbeille embarquée.
- **Un châssis mobile** chargé de transporter le système et de naviguer dans l'environnement en évitant les obstacles.

## 👥 Organisation de l'équipe

Le projet a été structuré autour de trois pôles :

| Pôle | Rôle |
|------|------|
| **Mécanique** | Conception et fabrication de la structure mécanique du bras |
| **Électronique** | Conception du système électronique (capteurs, actionneurs) |
| **Informatique** | Développement des programmes (navigation, détection d'objets) |

---

## 🔧 1. Pôle Mécanique

### Cahier des charges du bras robotique
- Longueur totale ≥ 700 mm
- Charge maximale : 500 g
- Nombre de degrés de liberté : 6 (5 si non atteignable)
- Précision du mouvement : ± 5 mm

---

## ⚡ 2. Pôle Électronique

### Composants du système
- **Capteur  ultrasons (HC-SR04)** — détection d'obstacles
- **Kit de voiture 4 roues** — base mobile du châssis
- **Servomoteurs** — actionnement des articulations du bras
- **Caméra** — perception visuelle pour la détection de déchets
- **Microcontrôleur ESP32** — contrôle du système
- **Carte electronique devant relier les différents composants**

## 💻 3. Pôle Informatique

### Objectif
Entraîner un modèle de détection d'objets capable de reconnaître différents types de déchets : bouteilles de 50 cl, canettes, papiers froissés, etc.


---

## 📌 État global du projet

| Pôle | Statut |
|------|--------|
| Mécanique | 🟡 Modèle 3D identifié, impression et assemblage en cours |
| Électronique | 🟡 Composants étudiés, intégration non réalisée |
| Informatique | 🔴 Recherches préliminaires uniquement |



---



