from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from parler.utils.i18n import get_active_language_choices

from home.models import Product, ProductSize, Size
import json
from cart.cart import Cart


@require_GET
def get(request):
    cart = Cart(request)
    return JsonResponse({
        'cart': cart.session['cart'],
        'total_price': cart.get_total_price()
    })


@require_POST
@csrf_exempt
def add(request, product_id):
    try:
        cart = Cart(request)
        data = json.loads(request.body.decode('utf-8'))
        product = Product.objects.language(data.get('lang')).get(pk=product_id)
        try:
            size = Size.objects.get(size=data.get('size'))
        except Size.DoesNotExist as e:
            return JsonResponse({'status': False, 'message': str(e)})
        try:
            product_size = ProductSize.objects.filter(product_id=product_id, size=size.id)
        except Size.DoesNotExist as e:
            return JsonResponse({'status': False, 'message': str(e)})

        cart.add(
            product=product,
            quantity=data.get('quantity'),
            notes=data.get('notes'),
            size=size.size,
            price=product_size[0].price,
            update_quantity=data.get('update')
        )

        return JsonResponse({'status': True, 'data': cart.get_product(f'{product_id}-{size}')})
    except Product.DoesNotExist as e:
        return JsonResponse({'status': False, 'message': str(e)})


@require_GET
@csrf_exempt
def remove(request, product_id, product_size):
    try:
        cart = Cart(request)
        product = Product.objects.get(pk=product_id)
        return JsonResponse({'status': True, 'data': cart.remove(product, product_size)})
    except Product.DoesNotExist as e:
        return JsonResponse({'status': False, 'message': str(e)})


@require_GET
def clean(request):
    cart = Cart(request)
    return JsonResponse({'status': True, 'cart': cart.clean()})
