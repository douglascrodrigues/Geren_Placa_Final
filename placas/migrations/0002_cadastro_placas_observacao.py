# Generated by Django 2.2.4 on 2019-09-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro_placas',
            name='Observacao',
            field=models.TextField(blank=True, verbose_name='Observação'),
        ),
    ]
