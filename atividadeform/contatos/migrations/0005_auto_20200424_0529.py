# Generated by Django 2.1.3 on 2020-04-24 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0004_auto_20200424_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatos',
            name='descricao',
            field=models.TextField(default='', max_length=1000, null=True),
        ),
    ]
