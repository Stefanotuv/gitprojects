# Generated by Django 2.1.1 on 2018-10-28 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0014_auto_20181027_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='sitetype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.SiteType'),
        ),
    ]
