# Generated by Django 3.2.6 on 2021-10-12 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametres', '0002_auto_20211012_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametres',
            name='codePostal',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]
