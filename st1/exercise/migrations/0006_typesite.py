# Generated by Django 2.1.1 on 2018-10-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_auto_20181027_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=264, unique=True)),
            ],
        ),
    ]
