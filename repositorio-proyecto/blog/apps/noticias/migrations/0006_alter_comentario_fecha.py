# Generated by Django 3.2 on 2022-12-16 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0005_alter_noticia_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
