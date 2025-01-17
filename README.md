# Wifi Connexion Automation

## Description

Ce projet automatise la connexion à un réseau WiFi en utilisant Selenium pour interagir avec une page de connexion web. Le script se reconnecte automatiquement toutes les 3 heures et 30 minutes pour maintenir la connexion active.

## Fonctionnalités

- Connexion automatique au réseau WiFi en utilisant les informations d'identification fournies.
- Vérification continue de l'URL pour détecter les redirections vers une page spécifique.
- Minimisation de la fenêtre de commande dans la zone de notification.
- Utilisation d'un fichier `.env` pour stocker les informations sensibles (URL et mot de passe).

## Prérequis

- [Python 3.10](https://www.python.org/downloads/)
- [Selenium](https://pypi.org/project/selenium/)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [RBTray](https://rbtray.github.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances Python :
    ```sh
    pip install selenium python-dotenv
    ```
3. Téléchargez et extrayez [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) et assurez-vous qu'il est dans votre PATH.
4. Téléchargez et extrayez [RBTray](https://rbtray.github.io/) dans un répertoire accessible (par exemple, `C:\RBTray`).