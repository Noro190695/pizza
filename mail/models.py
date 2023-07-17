from django.db import models


class Mail(models.Model):
    from_email = models.CharField(verbose_name='From E-mail', max_length=100)
    server_email = models.CharField(verbose_name='Server Email', max_length=100)
    server_host = models.CharField(verbose_name='Server Host', max_length=100, default='smtp.sendgrid.net')
    email_use_tls = models.BooleanField(default=True)
    email_use_ssl = models.BooleanField(default=False)
    email_port = models.IntegerField(verbose_name='Mail PORT')
    email_user = models.CharField(verbose_name='Mail user', max_length=100)
    email_password = models.CharField(verbose_name='Mail password', max_length=255)

    def __str__(self):
        return self.server_host
