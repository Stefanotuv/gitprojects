# Generated by Django 2.1.1 on 2018-10-27 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_auto_20181027_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='ActivityType',
        ),
        migrations.AddField(
            model_name='useractivities',
            name='webstVisited',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='exercise.Website'),
        ),
    ]
