from django.db import models
from django.utils import timezone


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
    names = models.TextField(blank=True)
    part = models.ForeignKey('myqueue.LabPart', on_delete=models.CASCADE, related_name='groups', blank=True, null=True)
    status = models.ForeignKey('myqueue.Status', on_delete=models.CASCADE, related_name='groups', blank=True, null=True)
    help = models.BooleanField(default=False)
    time = models.DateTimeField(default=timezone.now)
    position = models.IntegerField(default=0)

    def list_add(self):
        # add to end of list
        self.position = Group.objects.filter(help=True).count()
        self.save()

    def list_remove(self):
        # remove from list
        groups = Group.objects.all()
        for group in groups:
            if group.position > self.position:
                group.position = group.position - 1
                group.save()
        self.position = 0
        self.save()

    def __str__(self):
        return "Bench " + str(self.bench)


class Status(models.Model):
    type = models.TextField()

    def __str__(self):
        return self.type
