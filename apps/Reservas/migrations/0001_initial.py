# Generated by Django 2.1.7 on 2019-03-03 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Parrillero', models.DateField()),
                ('Comunal', models.DateField()),
            ],
        ),
    ]
