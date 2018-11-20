from django.db import models


class Lab(models.Model):
    number = models.IntegerField()
    name = models.TextField()

    def __str__(self):
        return str(self.number) + " - " + self.name


class LabPart(models.Model):
    lab = models.ForeignKey('myqueue.Lab', on_delete=models.CASCADE, related_name='parts')
    name = models.TextField()

    def __str__(self):
        return "Lab " + str(self.lab.number) + " - " + self.name


class Group(models.Model):
    bench = models.IntegerField()
    names = models.TextField()

    def __str__(self):
        return "Bench " + str(self.bench)
