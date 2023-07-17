from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Mail
from django.conf import settings


@require_POST
@csrf_exempt
def send(request):
    try:
        mail_settings = Mail.objects.first()
        if mail_settings:
            ...

        subject = 'GRTAK'
        html_message = render_to_string('mail/index.html')
        plain_message = strip_tags(html_message)
        mail = send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            ['pizza.grtak@gmail.com'],
            html_message=html_message,
            fail_silently=False
        )
        if mail:
            return JsonResponse({'status': 'success', 'message': 'Thank you...'})
    except Exception as e:

        return JsonResponse({'status': 'error', 'message': str(e)})
