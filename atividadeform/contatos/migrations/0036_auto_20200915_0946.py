# Generated by Django 3.1 on 2020-09-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0035_produtos_unidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='modelo',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
