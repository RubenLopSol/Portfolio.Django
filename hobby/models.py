from django.db import models

class Hobby(models.Model):
    title_en = models.CharField(max_length=100)
    title_es = models.CharField(max_length=100)
    description_en = models.TextField()
    description_es = models.TextField()
    image = models.ImageField(upload_to='hobby',  null=True, blank=True)


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    

    class Meta:
        db_table='hobby'
        verbose_name= 'hobby'
        verbose_name_plural='hobbies'
        ordering=['id']

    def __str__(self):
        return f"Hobby {self.title_en}"
