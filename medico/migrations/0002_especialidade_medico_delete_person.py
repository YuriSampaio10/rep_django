# Generated by Django 5.0.4 on 2024-04-12 00:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id_especialidade', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id_medico', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.TextField()),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('data_nascimento', models.DateField()),
                ('crm', models.CharField(max_length=20)),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medico.especialidade')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
