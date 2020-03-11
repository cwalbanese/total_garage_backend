from django.db import models

class Repair(models.Model):
    year = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    miles = models.CharField(max_length=100)
    repair = models.TextField(max_length=255)

    def __str__(self):
        return self.repair