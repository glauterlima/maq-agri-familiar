# Generated by Django 5.2 on 2025-04-08 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maqdisponivel', '0003_alter_maquina_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquina',
            name='foto',
            field=models.CharField(max_length=500),
        ),
    ]
