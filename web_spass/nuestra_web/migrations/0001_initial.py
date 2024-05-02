# Generated by Django 5.0.3 on 2024-04-25 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('contraseña_encriptada', models.BinaryField()),
                ('calidad', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
        ),
    ]