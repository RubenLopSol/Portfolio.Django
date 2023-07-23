from django.db import models

class Hobby(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='hobby',  null=True, blank=True)


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    

    class Meta:
        db_table='hobby'
        verbose_name= 'hobby'
        verbose_name_plural='hobbies'
        ordering=['id']

    def __str__(self):
        return self.title
