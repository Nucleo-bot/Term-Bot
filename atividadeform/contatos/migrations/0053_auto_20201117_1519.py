# Generated by Django 2.1.3 on 2020-11-17 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0052_auto_20201116_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='descricao',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]