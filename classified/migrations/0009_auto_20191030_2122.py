# Generated by Django 2.2.5 on 2019-10-30 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classified', '0008_auto_20191028_2135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classifiedad',
            options={'ordering': ('-date_updated',), 'verbose_name': 'advert', 'verbose_name_plural': 'adverts'},
        ),
    ]
