# Generated by Django 4.2 on 2023-07-08 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.CharField(max_length=100, verbose_name='From E-mail')),
                ('server_email', models.CharField(max_length=100, verbose_name='Server Email')),
                ('email_use_tls', models.BooleanField(default=True)),
                ('email_use_ssl', models.BooleanField(default=False)),
                ('email_port', models.IntegerField(verbose_name='Mail PORT')),
                ('email_user', models.CharField(max_length=100, verbose_name='Mail user')),
                ('email_password', models.CharField(max_length=255, verbose_name='Mail password')),
            ],
        ),
    ]
