from django.db import models

class Lab(models.Model):
    lab_number = models.IntegerField()
    lab_name = models.TextField()

    def __str__(self):
        return str(self.lab_number) + " - " + self.lab_name