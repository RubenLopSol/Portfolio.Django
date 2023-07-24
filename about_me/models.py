from django.db import models

class About(models.Model):
    description_en = models.TextField()
    description_es = models.TextField()
    image = models.ImageField(upload_to='about',  null=True, blank=True)


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)    

    class Meta:
        db_table='about'
        verbose_name= 'about'
        verbose_name_plural='about'
        ordering=['id']

    def __str__(self):
        return f"About {self.id}"

