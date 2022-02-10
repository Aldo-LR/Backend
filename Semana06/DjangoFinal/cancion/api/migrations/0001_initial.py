# Generated by Django 3.2 on 2022-02-06 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('cancion_id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(default='', max_length=200, verbose_name='TITULO')),
                ('url', models.CharField(default='', max_length=200, verbose_name='LINK')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='FECHA DE REGISTRO')),
            ],
        ),
    ]