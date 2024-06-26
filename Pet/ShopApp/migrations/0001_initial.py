# Generated by Django 5.0.3 on 2024-03-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('nome', models.CharField(max_length=100)),
                ('crmv', models.CharField(default='SP-0000', max_length=7)),
                ('telefone', models.CharField(default='00 00000-0000', max_length=13)),
                ('cep', models.CharField(default='00000-000', max_length=8)),
                ('numero', models.CharField(default='00000', max_length=5)),
                ('complemento', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(default='SP', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
