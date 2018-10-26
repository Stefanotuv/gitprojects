# Generated by Django 2.1.1 on 2018-10-26 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('surname', models.CharField(max_length=264, unique=True)),
                ('email', models.EmailField(blank=True, max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='UserActivities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('appUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.AppUser')),
            ],
        ),
    ]