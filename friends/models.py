from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name
 
    class Meta:
        db_table = 'owners'




class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'dogs'