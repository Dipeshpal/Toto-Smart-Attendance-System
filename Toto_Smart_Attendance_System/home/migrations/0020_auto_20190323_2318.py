# Generated by Django 2.1.7 on 2019-03-23 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20190323_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='slug',
            field=models.SlugField(default=449),
        ),
    ]
