# Generated by Django 2.2.4 on 2019-11-23 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testes', '0001_initial'),
        ('requisicao', '0001_initial'),
        ('placas', '0002_remove_cadastro_lote_qtd_placa'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='item_requisicao',
            name='Teste',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='testes.Teste', verbose_name='Teste'),
        ),
        migrations.AddField(
            model_name='item_requisicao',
            name='username',
            field=models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='contas_usuario_username_item', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cadastro_requisicao',
            name='Modelo',
            field=models.ForeignKey(limit_choices_to={'Ativo': True}, on_delete=django.db.models.deletion.PROTECT, related_name='Modelo_placas_modelo', to='placas.Modelo_placas'),
        ),
        migrations.AddField(
            model_name='cadastro_requisicao',
            name='username',
            field=models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='contas_usuario_username_requisicao', to=settings.AUTH_USER_MODEL),
        ),
    ]