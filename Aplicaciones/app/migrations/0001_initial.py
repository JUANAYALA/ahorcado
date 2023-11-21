# Generated by Django 4.2.7 on 2023-11-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palabra', models.CharField(max_length=50)),
                ('letras_adivinadas', models.CharField(default='', max_length=50)),
                ('intentos_restantes', models.IntegerField(default=6)),
            ],
        ),
    ]