from django.db import models

# Create your models here.


class Film (models.Model):

    name = models.CharField(max_length=20)
    year = models.IntegerField()
    rate = models.IntegerField()


    def __str__(self):
        return F"{self.name}-{self.year}"





