# Generated by Django 3.1 on 2020-09-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0034_projeto_margem'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='unidade',
            field=models.CharField(blank=True, default='UND', max_length=15),
        ),
    ]