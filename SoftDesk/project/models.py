from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

def valeur_annee_actuelle():
    pass

class User(AbstractUser):
    age = models.PositiveIntegerField(validators=[MinValueValidator(16)])
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    contributor = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    

class Project(models.Model):
    BACKEND = "Back-end"
    FRONTEND = "Front-end"
    IOS = "iOS"
    ANDROID = "Android"

    TYPE_PROJET = [(BACKEND,"Back-end"),
                   (FRONTEND,"Front-end"),
                   (IOS,"iOS"),
                   (ANDROID,"Android")]
    
    nom = models.CharField(max_length=128,
                           verbose_name="Titre du Projet")
    author = models.ForeignKey(User,
                               on_delete=models.PROTECT,
                               related_name="Project_Auteur")
    description = models.TextField(max_length=2048)
    type = models.CharField(max_length=30,
                            choices=TYPE_PROJET)
    contributeur = models.ManyToManyField(User,
                                          related_name="Project_Contributeur")
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

class Issue(models.Model):
    # Nature de l'Issue
    BUG = "Bug"
    TACHE = "Tâche"
    AMELIORATION = "Amélioration"

    NATURE_ISSUE = [(BUG, "Bug"),
                    (TACHE, "Tâche"),
                    (AMELIORATION, "Amélioration")]

    # Priorité de l'Issue
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

    PRIORITE_ISSUE = [(LOW, "Low"),
                      (MEDIUM, "Medium"),
                      (HIGH, "High")]
    
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
    author = models.ForeignKey(User,
                               on_delete=models.PROTECT,
                               related_name="Issue_Auteur")
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE)
    attribution = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name="Utilisateur_attribue")
    balise = models.CharField(max_length=20,
                              choices=NATURE_ISSUE)
    progression = models.CharField(max_length=20,
                                   choices=STATUT_ISSUE,
                                   default="To Do")
    contributeur = models.ManyToManyField(User,
                                          through="IssueComment",
                                          related_name="Contributions")
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

class IssueComment(models.Model):
    issue = models.ForeignKey(Issue,
                              on_delete=models.CASCADE,
                              related_name="issue")
    author = models.ForeignKey(User,
                               on_delete=models.SET_DEFAULT,
                               default="contributeur inconnu")
    description = models.TextField(max_length=2048)
    created_time = models.DateTimeField(auto_now_add=True)
