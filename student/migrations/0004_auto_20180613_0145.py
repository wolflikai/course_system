# Generated by Django 2.0.4 on 2018-06-13 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_finalselect_ctime'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stuselected',
            unique_together=set(),
        ),
    ]
