# Generated by Django 3.1 on 2020-09-09 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0026_auto_20200905_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]