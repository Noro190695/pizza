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
