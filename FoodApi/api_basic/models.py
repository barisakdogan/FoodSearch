from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
