# Generated by Django 3.2.8 on 2022-11-30 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Lp', 'Leptop'), ('Dtp', 'Desktop'), ('Tw', 'Topviewer'), ('Sh', 'SecondHand')], max_length=3)),
                ('product_image', models.ImageField(upload_to='product_img')),
            ],
        ),
    ]
