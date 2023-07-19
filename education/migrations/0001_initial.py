# Generated by Django 4.0.3 on 2023-07-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='education')),
                ('title', models.CharField(max_length=250)),
                ('center', models.CharField(max_length=250)),
                ('year', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('certificate', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'education',
                'verbose_name_plural': 'educations',
                'db_table': 'education',
                'ordering': ['year'],
            },
        ),
    ]
