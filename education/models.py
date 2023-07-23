from django.db import models

class Education(models.Model):
    image = models.ImageField(upload_to='education',  null=True, blank=True)
    title = models.CharField(max_length=250)
    center = models.CharField(max_length=250)
    year = models.CharField(max_length=25)
    description = models.TextField()
    certificate = models.URLField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)



    class Meta:
        db_table='education'
        verbose_name='education'
        verbose_name_plural='educations'
        ordering=['year']

    def __str__(self):
        return self.title
