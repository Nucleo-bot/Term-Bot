# Generated by Django 3.0.4 on 2021-03-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0060_auto_20210305_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='numero',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='telefone',
            field=models.CharField(default='4654654', max_length=15),
        ),
    ]