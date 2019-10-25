# Generated by Django 2.2.6 on 2019-10-24 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
            },
        ),
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id_paciente', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Cedula')),
                ('Primer_Nombre', models.CharField(max_length=30, verbose_name='Primer Nombre')),
                ('Segundo_Nombre', models.CharField(max_length=30, verbose_name='Segundo Nombre')),
                ('Primer_Apellido', models.CharField(max_length=30, verbose_name='Primer Apellido')),
                ('Segundo_Apellido', models.CharField(max_length=30, verbose_name='Segundo Apellido')),
                ('Nacimiento', models.DateField(verbose_name='Fecha Nacimiento')),
                ('Telefono', models.BigIntegerField(verbose_name='Telefono')),
                ('Genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Citas.Genero')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
    ]