from django.contrib import admin
from .models import Home, ProductComponents, Product, Size, ProductSize
from parler.admin import TranslatableAdmin


class SizeAdmin(admin.ModelAdmin):
    pass


class ProductSizeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Home, TranslatableAdmin)
admin.site.register(ProductComponents, TranslatableAdmin)
admin.site.register(Product, TranslatableAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(ProductSize, ProductSizeAdmin)
