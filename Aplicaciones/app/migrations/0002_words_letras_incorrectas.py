# Generated by Django 4.2.7 on 2023-11-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='words',
            name='letras_incorrectas',
            field=models.CharField(default='', max_length=50),
        ),
    ]
