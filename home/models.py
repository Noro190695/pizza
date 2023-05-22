from django.db import models
from django.core.validators import FileExtensionValidator


class Home(models.Model):
    logo = models.FileField(upload_to='svg/', validators=[FileExtensionValidator(['svg'])], verbose_name='Logo')
    desktop_image = models.ImageField(upload_to='images/', verbose_name='Desktop Image')
    mobile_image = models.ImageField(upload_to='images/', verbose_name='Mobile Image')
    title = models.CharField(max_length=255, verbose_name='Title')
    subtitle = models.CharField(max_length=255, verbose_name='Subtitle')
    desc = models.TextField(verbose_name='Description')
    delivery_text = models.CharField(max_length=255, verbose_name='Delivery text')

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'

    def __str__(self):
        return self.title


class ProductComponents(models.Model):
    icon = models.FileField(upload_to='svg/', validators=[FileExtensionValidator(['svg'])], verbose_name='Icon')
    name = models.CharField(max_length=55, verbose_name='Name')

    class Meta:
        verbose_name = 'Product component'
        verbose_name_plural = 'Product components'

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.IntegerField(verbose_name='Size')

    def __str__(self):
        return str(self.size)


class ProductSize(models.Model):
    price = models.IntegerField(verbose_name='Price')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_size_foreign')
    size = models.ForeignKey('Size', on_delete=models.CASCADE, related_name='size_foreign')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name


class Product(models.Model):
    img = models.ImageField(upload_to='images/products')
    mobile_img = models.ImageField(upload_to='images/mobile/products')
    name = models.CharField(max_length=55, verbose_name='Name')
    component = models.ManyToManyField('ProductComponents')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
