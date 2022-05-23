from django.db import models

# Create your models here.

class Person(models.Model):
    # ...
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    birth_date = models.DateField()
    creation_date = models.DateField()
    score_average = models.FloatField()
