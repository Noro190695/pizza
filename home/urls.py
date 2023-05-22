from django.urls import path
from .views import *
urlpatterns = [
    path('', HomeView.as_view()),
    path('terms-conditions', TermsConditions.as_view(), name='terms_conditions'),
    path('privacy-policy', PrivacyPolicy.as_view(), name='privacy_policy'),
    path('refund-policy', RefundPolicy.as_view(), name='refund_policy'),
    path('delivery-terms', DeliveryTerms.as_view(), name='delivery_terms'),
    path('payment', Payment.as_view(), name='payment'),
]
