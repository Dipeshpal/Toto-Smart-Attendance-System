# Generated by Django 2.1.7 on 2019-03-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20190318_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='slug',
            field=models.SlugField(default=389),
        ),
    ]
