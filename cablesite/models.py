from django.db import models

class User(models.Model):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.login

class Cable(models.Model):
    cable_mark = models.CharField(max_length=30)
    destination_to = models.CharField(max_length=50)
    destination_from = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    cross_section = models.FloatField()
    lenght = models.FloatField()

    def __str__(self):
        return self.cable_mark, self.destination_to, self.destination_from, self.status, self.cross_section, self.lenght


class Panel(models.Model):
    panel_name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.panel_name

class Device(models.Model):
    id_cable = models.ForeignKey(Cable, on_delete=models.CASCADE)
    id_panel = models.ForeignKey(Panel, on_delete=models.CASCADE)
    room = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    device_name = models.CharField(max_length=50)
    def __str__(self):
        return self.room

class Strand(models.Model):
    id_cable = models.ForeignKey(Cable, on_delete=models.CASCADE)
    strand_mark = models.CharField(max_length=50)
    resistance_on_earth = models.FloatField()
    resistance = models.FloatField()

class Report(models.Model):
    info = models.TextField()