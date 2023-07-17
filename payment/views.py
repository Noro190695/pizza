from django.http import JsonResponse
from django.views.generic import TemplateView
from home.models import Home
import requests
from django.http import HttpResponseRedirect
from home.models import Product, ProductSize


_API_URL = 'https://servicestest.ameriabank.am/VPOS'



def pay(request):
    try:
        fetchData = {
            "ClientID": "a7159a8d-d3fe-4986-8c75-a45900a394ef",
            "Username": "3d19541048",
            "Password": "lazY2k",
            "Description": "Test Payment 3",
            "OrderID": "3136112",
            "Amount": 10,
            "BackURL": 'http://127.0.0.1:8000/payment/checkout/'
        }
        r = requests.post(f'{_API_URL}/api/VPOS/InitPayment', data=fetchData)
        data = r.json()
        if r.status_code == 200:
            paymentID = data['PaymentID']
            # cart = Cart(request)
            # post = request.POST
            # paymet = Payment()
            # paymet.full_name = post['name']
            # paymet.email = post['email']
            # paymet.phone = post['phone']
            # paymet.address = post['address']
            # paymet.payment_id = paymentID
            # paymet.address = post['address']
            # paymet.products = {
            #     'cart': cart.session['cart'],
            #     'totalprice': cart.get_total_price()
            # }
            # paymet.status = data['ResponseMessage']
            # paymet.save()
            url = f'{_API_URL}/Payments/Pay?id={paymentID}'
            return HttpResponseRedirect(url)
        else:
            return JsonResponse({'status': False, 'message': r.json()})
    except Product.DoesNotExist as e:
        return JsonResponse({'status': False, 'message': str(e)})


class Checkout(TemplateView):
    template_name = "payment/index.html"

    def get_context_data(self, **kwargs):
        context = super(Checkout, self).get_context_data(**kwargs)
        products = Product.objects.all()
        context['sizes'] = ProductSize.objects.all().order_by('size')
        context['home'] = Home.objects.first()
        context['products'] = products
        return context
