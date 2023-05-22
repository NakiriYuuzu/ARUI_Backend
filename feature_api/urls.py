from django.urls import path
from .views import *

urlpatterns = [
    path('sku', SkuView.as_view()),
    path('button', ButtonView.as_view()),
    path('sku_button', SKUBtnView.as_view()),
]
