# Generated by Django 2.0.4 on 2018-06-13 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_auto_20180612_1615'),
        ('student', '0004_auto_20180613_0145'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='finalselect',
            unique_together={('time', 'week')},
        ),
    ]
