# Generated by Django 2.1.1 on 2018-10-27 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0013_remove_website_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TypeSite',
            new_name='SiteType',
        ),
        migrations.AddField(
            model_name='website',
            name='sitetype',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='exercise.SiteType'),
        ),
    ]
