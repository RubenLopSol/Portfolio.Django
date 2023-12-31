# Generated by Django 4.0.3 on 2023-07-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='description_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='title_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='title_es',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
