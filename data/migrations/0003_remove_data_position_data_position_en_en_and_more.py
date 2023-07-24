# Generated by Django 4.0.3 on 2023-07-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_data_position_en_data_position_es'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='position',
        ),
        migrations.AddField(
            model_name='data',
            name='position_en_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='position_en_es',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='position_es_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='position_es_es',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='position_en',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='data',
            name='position_es',
            field=models.CharField(max_length=250),
        ),
    ]