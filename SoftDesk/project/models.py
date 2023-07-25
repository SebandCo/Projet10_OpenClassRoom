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
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    contributor = models.BooleanField(default=False)

class Project(models.Model):
    BACKEND = "back-end"
    FRONTEND = "front-end"
    IOS = "iOS"
    ANDROID = "Android"

    TYPE_PROJET = [(BACKEND,"back-end"),
                   (FRONTEND,"front-end"),
                   (IOS,"iOS"),
                   (ANDROID,"Android")]
    
    nom = models.CharField(max_length=128,
                           verbose_name="Titre du Projet")
    description = models.TextField(max_length=2048)
    type = models.CharField(max_length=30,
                            choices=TYPE_PROJET)

class Issue(models.Model):
    # Nature de l'Issue
    BUG = "bug"
    TACHE = "tâche"
    AMELIORATION = "amélioration"

    NATURE_ISSUE = [(BUG, "bug"),
                    (TACHE, "tâche"),
                    (AMELIORATION, "amélioration")]

    # Priorité de l'Issue
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    PRIORITE_ISSUE = [(LOW, "low"),
                      (MEDIUM, "medium"),
                      (HIGH, "high")]
    
    # Statut de progression de l'Issue
    TO_DO = "To Do"
    IN_PROGRESS = "In Progress"
    FINISHED = "Finished"

    STATUT_ISSUE = [(TO_DO, "To Do"),
                    (IN_PROGRESS, "In Progress"),
                    (FINISHED, "Finished")]

    nom = models.CharField(max_length=128,
                           verbose_name="Titre du problème")
    statut = models.CharField(max_length=128,
                              verbose_name="Statut du problème")
    priorite = models.CharField(max_length=10,
                                choices=PRIORITE_ISSUE)
    attribution = models.ForeignKey(User,
                                    default="Problème non affecté",
                                    on_delete=models.SET_DEFAULT)
    balise = models.CharField(max_length=20,
                              choices=NATURE_ISSUE)

class Comment(models.Model):
    commentaire = models.TextField(max_length=2048)




'''class Issue(models.Model):
    # Nature de l'Issue
    NATURE_ISSUE = (
        ("bug", "bug"),
        ("tâche", "tâche"),
        ("amélioration", "amélioration"),
    )

    balise = models.CharField(max_length=20, choices=NATURE_ISSUE)
    
    
    class Student(models.Model):
    FRESHMAN = "FR"
    SOPHOMORE = "SO"
    JUNIOR = "JR"
    SENIOR = "SR"
    GRADUATE = "GR"
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, "Freshman"),
        (SOPHOMORE, "Sophomore"),
        (JUNIOR, "Junior"),
        (SENIOR, "Senior"),
        (GRADUATE, "Graduate"),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )'''