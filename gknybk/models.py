from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    def __str__(self):
        return "%s (%s)" % (self.name, self.email)

class Betetkonyv(models.Model):
    sorszam = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return "%s" % (self.sorszam)

class Betetkonyv_User(models.Model):
    betetkonyv = models.ForeignKey(Betetkonyv,on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    ertek = models.PositiveIntegerField()
    def __str__(self):
        return "%s %s" % (self.owner.name, self.betetkonyv.sorszam)



class Sorsolas(models.Model):
    betetkonyv = models.ForeignKey(Betetkonyv,on_delete=models.CASCADE)
    nyeremeny = models.CharField(max_length=50)
    datum = models.DateField()
    def __str__(self):
        return "%s %s" % (self.betetkonyv.sorszam, self.datum)
