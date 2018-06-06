# Generated by Django 2.0.4 on 2018-06-02 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('edu', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=8, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('applied_time', models.DateTimeField(auto_now_add=True)),
                ('credit', models.DecimalField(decimal_places=1, max_digits=2)),
                ('status', models.NullBooleanField(default='null')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.College')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedCourse_Pos_Ti',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.BooleanField()),
                ('card_id', models.CharField(max_length=18)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=11)),
                ('birth', models.CharField(max_length=10)),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edu.College')),
                ('no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edu.Position')),
            ],
        ),
        migrations.CreateModel(
            name='Times',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Weeks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='appliedcourse_pos_ti',
            name='a_classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Classroom'),
        ),
        migrations.AddField(
            model_name='appliedcourse_pos_ti',
            name='a_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Times'),
        ),
        migrations.AddField(
            model_name='appliedcourse_pos_ti',
            name='a_week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Weeks'),
        ),
        migrations.AddField(
            model_name='appliedcourse_pos_ti',
            name='applied_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.AppliedCourse'),
        ),
        migrations.AddField(
            model_name='appliedcourse',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.Teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='appliedcourse_pos_ti',
            unique_together={('a_classroom', 'a_time', 'a_week', 'applied_course')},
        ),
    ]