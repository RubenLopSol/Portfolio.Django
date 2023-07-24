from django.db import models

class Work(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    year = models.CharField(max_length=25)
    description_en = models.TextField()
    description_es = models.TextField()
    logo = models.ImageField(upload_to='work',  null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'Work'
        verbose_name = 'Work'
        verbose_name_plural = 'Work'    
        ordering = ['year']

    def __str__(self):
        return f"Work {self.company}"