from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Home(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=200),
        subtitle=models.TextField(_("Subtitle")),
        description=models.TextField(_("Description")),
        delivery_text=models.CharField(_("Delivery Text"), max_length=200),
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'

    def __str__(self):
        return self.title


class ProductComponents(TranslatableModel):
    icon = models.FileField(upload_to='svg/', validators=[FileExtensionValidator(['svg'])], verbose_name='Icon')
    translations = TranslatedFields(
        name=models.CharField(_("Name"), max_length=200),
    )

    class Meta:
        verbose_name = 'Product component'
        verbose_name_plural = 'Product components'

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.IntegerField(_('size'))

    def __str__(self):
        return str(self.size)


class ProductSize(models.Model):
    price = models.IntegerField(verbose_name='price')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_size_foreign')
    size = models.ForeignKey('Size', on_delete=models.CASCADE, related_name='size_foreign')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name


class Product(TranslatableModel):
    img = models.ImageField(_('img'), upload_to='images/products')
    mobile_img = models.ImageField(verbose_name='Mobile image', upload_to='images/mobile/products')
    component = models.ManyToManyField('ProductComponents')
    translations = TranslatedFields(
        name=models.CharField(_('name'), max_length=55),
    )
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
