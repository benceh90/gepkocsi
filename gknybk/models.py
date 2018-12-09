from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    def __str__(self):
        return "%s (%s)" % (self.name, self.email)

class Betetkonyv_User(models.Model):
    betetkonyv = models.CharField(max_length=20, unique=True,blank=False)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    ertek = models.PositiveIntegerField()
    def __str__(self):
        return "%s %s" % (self.owner.name, self.betetkonyv)

class Sorsolas(models.Model):
    betetkonyv = models.CharField(max_length=20,blank=False)
    nyeremeny = models.CharField(max_length=50)
    datum = models.DateField()
    def __str__(self):
        return "%s %s" % (self.betetkonyv, self.datum)
