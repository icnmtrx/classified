# Generated by Django 2.2.5 on 2019-10-28 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191028_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='registered_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_registered'),
        ),
    ]
