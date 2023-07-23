from django.db import models

class Data(models.Model):
    image = models.ImageField(upload_to='data',  null=True, blank=True)
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    gitHub = models.URLField()
    linkedin = models.URLField()
    cv = models.FileField(upload_to='data')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'data'
        verbose_name = 'data'
        verbose_name_plural = 'data'
        ordering = ['name']

    def __str__(self):
        return self.name