import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Tocht(models.Model):
    naam = models.CharField(
        unique=True,
        max_length=64,
    )
    datum = models.DateField(
    )
    pub_datum = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return(self.naam)


class Wandelaar(models.Model):
    email = models.EmailField(
        unique= True,
    )
    tocht = models.ForeignKey(
        Tocht,
        on_delete=models.CASCADE,
    )
    pub_datum = models.DateTimeField(
        auto_now=True,
    )
    def __str__(self):
        return self.email


class DeelnemersAantal(models.Model):
    tocht = models.ForeignKey(
        Tocht,
        unique=True,
        on_delete=models.CASCADE,
    )
    lid5km = models.IntegerField()
    lid10km = models.IntegerField()
    lid15km = models.IntegerField()
    lid20km = models.IntegerField()
    lid25km = models.IntegerField()
    nietlid5km = models.IntegerField()
    nietlid10km = models.IntegerField()
    nietlid15km = models.IntegerField()
    nietlid20km = models.IntegerField()
    nietlid25km = models.IntegerField()

    def aantallid(self):
        return (self.lid5km +
        self.lid10km +
        self.lid15km +
        self.lid20km +
        self.lid25km)

    def aantalnietlid(self):
        return (self.nietlid5km +
        self.nietlid10km +
        self.nietlid15km +
        self.nietlid20km +
        self.nietlid25km)

    def aantal(self):
        return (self.aantallid +
        self.aantalnietlid)

    def __str__(self):
        return (self.tocht, self.aantal)