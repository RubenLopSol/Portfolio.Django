from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='project',  null=True, blank=True)
    description = models.TextField()
    deployment = models.URLField(blank=True)
    code_front = models.URLField(blank=True)
    code_back = models.URLField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'project'
        verbose_name = 'project'
        verbose_name_plural = 'projects'    
        ordering = ['id']

    def __str__(self):
        return self.title