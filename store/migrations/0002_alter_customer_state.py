# Generated by Django 3.2.8 on 2022-11-30 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa ', 'Goa '), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh ', 'Himachal Pradesh '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka')], max_length=50),
        ),
    ]
