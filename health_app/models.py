from django.db import models

# Create your models here.
class HealthData(models.Model):
    timestamp = models.DateTimeField()
    bim = models.FloatField(null=True)
    temperature = models.FloatField(null=True)
    spo2 = models.FloatField(null=True)
    strick = models.FloatField(null=True)
    bp = models.FloatField(null=True)

    def __str__(self):
      return f"Health Data - ID: {self.id}"
