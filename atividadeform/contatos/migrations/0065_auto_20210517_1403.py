# Generated by Django 2.1.3 on 2021-05-17 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contatos', '0064_subitem_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='data_alteracao',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='produtos',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='docfiles',
            name='docupload',
            field=models.FileField(max_length=500, upload_to=''),
        ),
    ]