# Generated by Django 4.2 on 2023-06-28 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone')),
                ('email', models.CharField(max_length=255, verbose_name='E-mail')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('payment_id', models.CharField(max_length=255)),
                ('products', models.JSONField(verbose_name='Product')),
                ('status', models.SmallIntegerField(choices=[(0, 'PENDING'), (1, 'SUCCESS'), (2, 'ERROR')], default=(0, 'PENDING'))),
            ],
        ),
    ]
