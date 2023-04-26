from django.db import models

# Create your models here.
class Person(models.Model):
    sex = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="Email")
    birth_date = models.DateField(default="1990-01-01")

    #display the data with first_name
    def __str__(self):
        return self.first_name

class Car(models.Model):
    plate = models.CharField(max_length=50, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    owner = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='cars', null=True, blank=True)

    def __str__(self):
        return "%s (%s)" % (
            self.name,
            ", ".join(owner.first_name for owner in self.owner.all()),
        )