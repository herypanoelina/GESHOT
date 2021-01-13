from django.db import models


class employees(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=100)
    Fonction = models.CharField(max_length=300)
    mpp = models.CharField(max_length=100)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstname


class CHAMBREDEP(models.Model):
    res_id = models.IntegerField()
    Client_id = models.IntegerField()
    Num_chambre = models.IntegerField()
    nameChambre = models.CharField(max_length=200)
    date_arr = models.DateTimeField()
    date_dep = models.DateTimeField()


def __str__(self):
    return self.nameChambre


class CHAMBRE(models.Model):
    res_id = models.IntegerField()
    Client_id = models.IntegerField()
    Num_chambre = models.IntegerField()
    nameChambre = models.CharField(max_length=200)
    libre = models.CharField(max_length=1)


class CHAMBREARR(models.Model):
    res_id = models.IntegerField()
    Client_id = models.IntegerField()
    Num_chambre = models.IntegerField()
    nameChambre = models.CharField(max_length=200)
    date_arr = models.DateTimeField()
    date_dep = models.DateTimeField()


def __str__(self):
    return self.nameChambre


class CHAMBREHORS(models.Model):
    emp_id = models.IntegerField()
    Num_chambre = models.IntegerField()
    nameChambre = models.CharField(max_length=200)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    Motif = models.CharField(max_length=200)

    def __str__(self):
        return self.nameChambre


class CHAMBRERESERV(models.Model):
    res_id = models.IntegerField()
    Client_id = models.IntegerField()
    Num_chambre = models.IntegerField()
    nameChambre = models.CharField(max_length=200)
    date_arr = models.DateTimeField()
    date_dep = models.DateTimeField()


def __str__(self):
    return self.firstname


class reservation(models.Model):
    res_id = models.IntegerField()
    Client_id = models.IntegerField()
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=100)
    transport = models.CharField(max_length=50)
    Adresse = models.CharField(max_length=300)

    def __str__(self):
        return self.firstname
