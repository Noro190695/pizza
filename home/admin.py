from django.contrib import admin
from .models import Home, ProductComponents, Product, Size, ProductSize


class HomeAdmin(admin.ModelAdmin):
    pass


class ProductComponentsAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass

class SizeAdmin(admin.ModelAdmin):
    pass
class ProductSizeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Home, HomeAdmin)
admin.site.register(ProductComponents, ProductComponentsAdmin)
admin.site.register(Product, ProductComponentsAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(ProductSize, ProductSizeAdmin)

