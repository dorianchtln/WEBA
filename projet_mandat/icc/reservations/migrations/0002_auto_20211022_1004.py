# Generated by Django 3.2.5 on 2021-10-22 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='date_heure',
        ),
        migrations.AddField(
            model_name='reservation',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date: JJ.MM.AAAA '),
        ),
        migrations.AddField(
            model_name='reservation',
            name='heure',
            field=models.TimeField(blank=True, choices=[('08:00', '08:00'), ('08:30', '08:30'), ('09:00', '09:00'), ('09:30', '09:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30')], null=True, verbose_name='Heure: JJ.MM.AAAA HH:MM (H+1)'),
        ),
    ]