# Generated by Django 4.1.4 on 2022-12-08 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pymes', '0002_departamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='rubro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model_state', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('date_deleted', models.DateTimeField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre de Rubro')),
                ('sigla', models.CharField(max_length=200, verbose_name='Sigla del Rubro')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pymes.departamento')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
