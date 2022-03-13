from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Location(models.Model):
    spot = models.CharField(max_length=120)

    def __str__(self):
        return self.spot


class Transport(models.Model):
    vehicle = models.CharField(max_length=120)

    def __str__(self):
        return self.vehicle


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=220)
    date = models.DateTimeField()
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE)
    location = models.ManyToManyField(Location, blank=False)
    duration = models.DurationField()
    description = models.TextField(blank=True)
    transport = models.ManyToManyField(Transport)
    event_img = models.ImageField(upload_to='events/static/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    enrollment_no = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    traveller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=11)
    adult = models.IntegerField(default=1)
    child = models.IntegerField(default=0)

    def __str__(self):
        return self.enrollment_no
