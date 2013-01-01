from django.db import models



class Instrument(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=30, unique=True)

    class Meta:
        app_label = 'statcat'
