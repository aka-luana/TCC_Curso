# Generated by Django 3.1.5 on 2021-02-03 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroDePessoa', '0009_remove_usuario_sangue'),
        ('Sangue', '0002_auto_20210203_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiposanguineo',
            name='fk_usuario_tipo_sanguineo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CadastroDePessoa.usuario'),
        ),
    ]