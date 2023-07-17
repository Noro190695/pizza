from django.contrib import admin
from .models import Mail


class PaymentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Mail, PaymentAdmin)
