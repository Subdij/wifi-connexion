# Wifi Connexion Automation

## Description

Ce projet automatise la connexion à un réseau WiFi en utilisant Selenium pour interagir avec une page de connexion web. Le script se reconnecte automatiquement toutes les 3 heures et 30 minutes pour maintenir la connexion active.

## Fonctionnalités

- Connexion automatique au réseau WiFi en utilisant les informations d'identification fournies.
- Vérification continue de l'URL pour détecter les redirections vers une page spécifique.
- Minimisation de la fenêtre de commande dans la zone de notification.
- Utilisation d'un fichier `.env` pour stocker les informations sensibles (URL, nom d'utilisateur et mot de passe).

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances Python :
    ```sh
    pip install selenium python-dotenv
    ```
3. Téléchargez et extrayez [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) et assurez-vous qu'il est dans votre PATH.
