# Generated by Django 3.1.7 on 2021-03-31 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_usuario_segmento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competencia',
            old_name='id_segmento',
            new_name='segmento',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Segmento',
        ),
        migrations.AddField(
            model_name='usuario',
            name='segmento',
            field=models.ManyToManyField(to='cadastro.Segmento'),
        ),
    ]
