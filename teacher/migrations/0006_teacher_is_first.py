# Generated by Django 2.0.4 on 2018-06-15 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_auto_20180612_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='is_first',
            field=models.BooleanField(default=False),
        ),
    ]
