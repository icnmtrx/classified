# Generated by Django 2.2.5 on 2019-11-14 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classified', '0012_classifiedad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='region',
            name='title',
            field=models.CharField(max_length=100, verbose_name='region'),
        ),
    ]