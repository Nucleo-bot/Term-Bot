# Generated by Django 3.1 on 2020-10-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0050_auto_20201010_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='docfiles',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
