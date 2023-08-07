# Projet10_OpenClassRoom
Projet10 d'OpenClassRoom dans le cadre de la formation OpenClassRoom developpeur d'application Python

# Descriptif
Création d'une API sécurisée RESTful en utilisant Django REST
L'API permet de créer et modifier des Projets qui peuvent contenir des Issues et des Commentaires 

## Table des Matières
1. [Installation](#Installation)
2. [Sécurité](#Sécurité)
3. [Modèle](#Modèle)
4. [Requete](#Requete)
5. [Contribution](#Contribution)

# Installation
## Pré-requis
Créer un environnement dédié
```
$ python -m venv env
```
A l'intérieur de l'environnement installer les packages
```
$ pip install -r requirements.txt
```

## La base de donnée
La base de donnée doit être initialisé avant de commencer :
La base de donnée est au format db.sqlite3
```
python manage.py migrate
```

## Lancement du programme
Le serveur s'active via la commande
```
python manage.py runserver
```

# Sécurité
L'application necessite une inscription et la génération de jeton token
```
http://127.0.0.1:8000/inscription/
http://127.0.0.1:8000/api/token/
```

# Modèle
L'API travaille avec 4 ressources
## User
Basé sur AbstractUser de Django auquel sont rajouté
- age : Doit être au minimum de 16 ans
- can_be_contacted : Booléen
- can_data_be_shared : Booléen

## Project
- nom : Texte
- author : Lié à User
- description : Texte
- type : Back-end / Front-end / iOS / Android
- contributeur : Lié à User

## Issue
- nom : Texte
- author : Lié à User
- statut : Texte
- priorite : Low / Medium / High
- project : Lié à Project
- attribution : Lié à User
- balise : Bug / Tache / Amelioration
- progression : To Do / In Progress / Finished
- contributeur : Lié à User

## IssueComment
- issue : Lié à Issue
- author : Lié à User
- description : Texte
  
# Requete
Voici quelques exemples de requete:
Permet de voir la liste des projets
```
http://127.0.0.1:8000/api/project/
```
Permet de voir le projet 3
```
http://127.0.0.1:8000/api/project/3/
```
Permet de voir la liste des issues
```
http://127.0.0.1:8000/api/issue/
```
Permet de voir l'issue 1
```
http://127.0.0.1:8000/api/issue/1/
```

# Contribution
Commençant en programmation Python, et notamment Django REST, je suis preneur :
1. des détections de bug
2. des suggestions d'amélioration du code
3. des suggestions d'amélioration de la documentation
