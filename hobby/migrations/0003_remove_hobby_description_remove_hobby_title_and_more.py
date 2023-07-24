# Generated by Django 4.0.3 on 2023-07-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0002_hobby_description_en_hobby_description_es_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hobby',
            name='description',
        ),
        migrations.RemoveField(
            model_name='hobby',
            name='title',
        ),
        migrations.AddField(
            model_name='hobby',
            name='description_en_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hobby',
            name='description_en_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hobby',
            name='description_es_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hobby',
            name='description_es_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hobby',
            name='title_en_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hobby',
            name='title_en_es',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hobby',
            name='title_es_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hobby',
            name='title_es_es',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='description_en',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='description_es',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='title_en',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='title_es',
            field=models.CharField(max_length=100),
        ),
    ]
