# Generated by Django 4.1.1 on 2022-10-19 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medapp', '0003_remove_elder_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elder',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
