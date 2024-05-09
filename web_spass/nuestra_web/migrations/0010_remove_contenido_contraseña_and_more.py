# Generated by Django 5.0.3 on 2024-05-08 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuestra_web', '0009_alter_contenido_calidad_contraseña'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contenido',
            name='contraseña',
        ),
        migrations.AddField(
            model_name='contenido',
            name='contraseña_encriptada',
            field=models.BinaryField(null=True),
        ),
        migrations.AlterField(
            model_name='contenido',
            name='calidad_contraseña',
            field=models.CharField(choices=[('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta')], default='Baja', max_length=5),
        ),
        migrations.AlterField(
            model_name='contenido',
            name='link',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
