# Generated by Django 2.2.5 on 2019-10-26 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classified', '0002_classifiedad_активный'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classifiedad',
            old_name='активный',
            new_name='active',
        ),
    ]
