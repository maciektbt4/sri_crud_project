from django.db import models

# Create your models here.
class Person(models.Model):
    sex = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return self.name