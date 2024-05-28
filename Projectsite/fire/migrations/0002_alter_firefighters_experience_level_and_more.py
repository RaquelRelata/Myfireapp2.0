# Generated by Django 5.0.4 on 2024-05-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firefighters',
            name='experience_level',
            field=models.CharField(blank=True, choices=[('Entry-Level Firefighters', 'Entry-Level Firefighters'), ('Junior Firefighters', 'Junior Firefighters'), ('Senior Firefighters', 'Senior Firefighters'), ('Company Officers', 'Company Officers'), ('Chief Officers', 'Chief Officers')], max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='firefighters',
            name='rank',
            field=models.CharField(blank=True, choices=[('Veteran', 'Probationary Firefighter'), ('Firefighter I', 'Firefighter I'), ('Firefighter II', 'Firefighter II'), ('Firefighter III', 'Firefighter III'), ('Driver', 'Driver'), ('Captain', 'Captain'), ('Battalion Chief', 'Battalion Chief')], max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='firefighters',
            name='station',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
