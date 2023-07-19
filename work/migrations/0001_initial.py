# Generated by Django 4.0.3 on 2023-07-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='work')),
            ],
        ),
    ]