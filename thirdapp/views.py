from django.shortcuts import render
from .models import Jeju, Shop

def shop(request):
    shop_list = Shop.objects.all()
    return render(
        request,
        'thirdapp/shop.html',
        {'shop_list': shop_list}
    )

def jeju(request):
    jeju = Jeju.objects.all()
    return render(
        request,
        'thirdapp/jeju.html',
        {'jeju':jeju}
    )