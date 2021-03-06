# Generated by Django 2.2.4 on 2019-12-02 00:22

import contas.models.usuario
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=120, unique=True, verbose_name='Nome de Usuário')),
                ('data_expiracao', models.DateField(null=True, verbose_name='Data Expiração')),
                ('tipo', models.CharField(choices=[('R', 'Requisitor'), ('T', 'Tester'), ('S', 'Supervisor'), ('A', 'Administrador')], max_length=1, verbose_name='Tipo de Usuário')),
            ],
            options={
                'db_table': 'USUARIO',
            },
            managers=[
                ('objects', contas.models.usuario.UsuarioManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=155, verbose_name='Nome Completo')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('celular', models.CharField(max_length=11, verbose_name='Celular')),
                ('apelido', models.CharField(max_length=120, verbose_name='Apelido')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TESTER',
            },
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=155, verbose_name='Nome Completo')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('celular', models.CharField(max_length=11, verbose_name='Celular')),
                ('apelido', models.CharField(max_length=120, verbose_name='Apelido')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'SUPERVISOR',
            },
        ),
        migrations.CreateModel(
            name='Requisitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=155, verbose_name='Nome Completo')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('celular', models.CharField(max_length=11, verbose_name='Celular')),
                ('apelido', models.CharField(max_length=120, verbose_name='Apelido')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'REQUISITOR',
            },
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=155, verbose_name='Nome Completo')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('celular', models.CharField(max_length=11, verbose_name='Celular')),
                ('apelido', models.CharField(max_length=120, verbose_name='Apelido')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ADMINISTRADOR',
            },
        ),
        migrations.CreateModel(
            name='AdministradorUsuario',
            fields=[
            ],
            options={
                'verbose_name': 'administrador',
                'verbose_name_plural': 'administradores',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('contas.usuario',),
            managers=[
                ('objects', contas.models.usuario.UsuarioManager()),
            ],
        ),
        migrations.CreateModel(
            name='RequisitorUsuario',
            fields=[
            ],
            options={
                'verbose_name': 'requisitor',
                'verbose_name_plural': 'requisitores',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('contas.usuario',),
            managers=[
                ('objects', contas.models.usuario.UsuarioManager()),
            ],
        ),
        migrations.CreateModel(
            name='SupervisorUsuario',
            fields=[
            ],
            options={
                'verbose_name': 'supervisor',
                'verbose_name_plural': 'supervisores',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('contas.usuario',),
            managers=[
                ('objects', contas.models.usuario.UsuarioManager()),
            ],
        ),
        migrations.CreateModel(
            name='TesterUsuario',
            fields=[
            ],
            options={
                'verbose_name': 'tester',
                'verbose_name_plural': 'testers',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('contas.usuario',),
            managers=[
                ('objects', contas.models.usuario.UsuarioManager()),
            ],
        ),
    ]
