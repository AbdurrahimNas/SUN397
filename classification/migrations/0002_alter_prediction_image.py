# Generated by Django 5.0.3 on 2024-04-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='image',
            field=models.ImageField(upload_to='predictedImages/', verbose_name='Image'),
        ),
    ]
