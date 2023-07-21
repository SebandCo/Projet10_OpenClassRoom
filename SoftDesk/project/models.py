from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime

def valeur_annee_actuelle(value):
    annee_actuelle = datetime.date.today().year
    return MaxValueValidator(annee_actuelle)(value)


class User(AbstractUser):
    age = models.PositiveIntegerField(validators=[MinValueValidator(1900),
                                                  valeur_annee_actuelle])
    consentement = models.BooleanField(default=False)
    contributor = models.BooleanField(default=False)

class Project(models.Model):
    nom = models.CharField(max_length=128,
                           verbose_name="Titre du Projet")

class Issue(models.Model):
    BUG = "bug"
    TACHE = "tâche"
    AMELIORATION = "amélioration"

    CHOIX_BALISES = ({BUG, "bug"},
                     {TACHE, "tâche"},
                     {AMELIORATION, "amélioration"})

    nom = models.CharField(max_length=128,
                           verbose_name="Titre du problème")
    statut = models.CharField(max_length=128,
                              verbose_name="Statut du problème")
    priorite = models.CharField(max_length=128)
    attribution = models.ForeignKey(User,
                                    default="Problème non affecté",
                                    on_delete=models.SET_DEFAULT)
    balise = models.CharField(max_length=30,
                              choices=CHOIX_BALISES)

class Comment(models.Model):
    commentaire = description = models.TextField(max_length=2048)
