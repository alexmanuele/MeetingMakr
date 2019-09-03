from django.db import models

class LabGroup(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Person(models.Model):
    lab = models.ForeignKey('LabGroup', on_delete=models.CASCADE,)
    name = models.CharField(max_length=200)
    presented = models.BooleanField(default=False)
    def __str__(self):
        return self.name
