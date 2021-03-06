# Generated by Django 3.2.6 on 2021-10-19 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compte', '0007_client_commentaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=60)),
                ('pour', models.CharField(choices=[('Courts', 'Courts'), ('Longs', 'Longs'), ('/', '/')], default='', max_length=6)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=6)),
                ('duree', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_heure', models.DateTimeField(blank=True, null=True, verbose_name='Date-heure: JJ.MM.AAAA HH:MM (H+1)')),
                ('commentaire', models.TextField(blank=True, default='')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compte.client')),
            ],
        ),
        migrations.CreateModel(
            name='ResPres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duree_effective', models.TimeField(blank=True, default='00:00', null=True)),
                ('prix', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('prestation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservations.prestation')),
                ('reservation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservations.reservation')),
            ],
            options={
                'unique_together': {('reservation', 'prestation')},
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='prestations',
            field=models.ManyToManyField(through='reservations.ResPres', to='reservations.Prestation'),
        ),
    ]
