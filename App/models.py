from django.db import models

# Create your models here.
class Record(models.Model):
    date = models.DateField()
    amount = models.IntegerField()
    purpose = models.CharField(max_length=100)
    closing = models.IntegerField()


