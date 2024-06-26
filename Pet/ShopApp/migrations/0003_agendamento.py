# Generated by Django 5.0.3 on 2024-03-30 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0002_cliente_veterinario_bairro_veterinario_logradouro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopApp.animais')),
                ('procedimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopApp.servicos')),
            ],
        ),
    ]
