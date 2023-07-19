from django.db import models



class Work(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    year = models.CharField(max_length=25)
    description = models.TextField()
    logo = models.ImageField(upload_to='work',  null=True, blank=True)

