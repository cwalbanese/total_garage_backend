from django.db import models

# First search parameter
class Year(models.Model):
    year_make = models.CharField(max_length=100)

    def __str__(self):
        return self.year_make

# Second search parameter
class Repair(models.Model):
    year = models.ForeignKey(Year,
                               on_delete=models.CASCADE,
                               related_name='repairs')
    model = models.CharField(max_length=100)
    miles = models.CharField(max_length=100)
    repair = models.CharField(max_length=500)

    def __str__(self):
        return self.model