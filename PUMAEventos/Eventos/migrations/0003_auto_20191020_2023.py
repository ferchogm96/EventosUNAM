# Generated by Django 2.2.5 on 2019-10-20 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eventos', '0002_auto_20191020_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='correo',
            field=models.EmailField(default='null@c.com', max_length=150),
        ),
        migrations.AlterField(
            model_name='evento',
            name='entidad',
            field=models.CharField(max_length=150),
        ),
    ]
