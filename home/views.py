from django.views.generic import TemplateView
from .models import *


class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        products = Product.objects.all()
        context['sizes'] = ProductSize.objects.all().order_by('size')
        context['home'] = Home.objects.first()
        context['products'] = products
        return context


class TermsConditions(TemplateView):
    template_name = "home/terms-conditions.html"

    def get_context_data(self, **kwargs):
        context = super(TermsConditions, self).get_context_data(**kwargs)
        products = Product.objects.all()
        context['sizes'] = ProductSize.objects.all().order_by('size')
        context['home'] = Home.objects.first()
        context['products'] = products
        return context


class PrivacyPolicy(TemplateView):
    template_name = "home/privacy_policy.html"

    def get_context_data(self, **kwargs):
        context = super(PrivacyPolicy, self).get_context_data(**kwargs)
        products = Product.objects.all()
        context['sizes'] = ProductSize.objects.all().order_by('size')
        context['home'] = Home.objects.first()
        context['products'] = products
        return context


class RefundPolicy(TemplateView):
    template_name = "home/refund_policy.html"

    def get_context_data(self, **kwargs):
        context = super(RefundPolicy, self).get_context_data(**kwargs)
        products = Product.objects.all()
        context['sizes'] = ProductSize.objects.all().order_by('size')
        context['home'] = Home.objects.first()
        context['products'] = products
        return context


class Payment(TemplateView):
    template_name = "home/payment.html"

    def get_context_data(self, **kwargs):
        context = super(Payment, self).get_context_data(**kwargs)
        products = Product.objects.all()
        context['sizes'] = ProductSize.objects.all().order_by('size')
        context['home'] = Home.objects.first()
        context['products'] = products
        return context


class DeliveryTerms(TemplateView):
    template_name = "home/delivery_terms.html"

    def get_context_data(self, **kwargs):
        context = super(DeliveryTerms, self).get_context_data(**kwargs)
        products = Product.objects.all()
        context['sizes'] = ProductSize.objects.all().order_by('size')
        context['home'] = Home.objects.first()
        context['products'] = products
        return context
