from django.db import models


class Logos(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='logos',  null=True, blank=True)


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)    

    class Meta:
        db_table='logos'
        verbose_name= 'logos'
        verbose_name_plural='logos'
        ordering=['name']

    def __str__(self):
        return self.name