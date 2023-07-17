from django.db import models


class Payment(models.Model):
    payment_status = (
        (0, 'PENDING'),
        (1, 'SUCCESS'),
        (2, 'ERROR'),
    )

    readonly_fields = ('*',)

    full_name = models.CharField(max_length=255, verbose_name='Full Name')
    phone = models.CharField(max_length=255, verbose_name='Phone')
    email = models.CharField(max_length=255, verbose_name='E-mail')
    address = models.CharField(max_length=255, verbose_name='Address')
    payment_id = models.CharField(max_length=255)
    products = models.JSONField(verbose_name='Product')
    status = models.CharField(default='Pending', verbose_name='status')

    def __str__(self):
        return self.payment_id
