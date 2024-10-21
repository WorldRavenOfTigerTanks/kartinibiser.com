from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
import urllib.request
import requests

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            t='1596711219:AAGk7xqokACxi4IhrlpAQsKxpzRSKDwiPWs'
            c='-494970882'
            a=request.POST['first_name']
            b=request.POST['last_name']
            d=request.POST['postal_code2']
            f=request.POST['postal_code']
            e=request.POST['year_in_school2']
            g=request.POST['city']


            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                
            # очистка корзины
            cart.clear()

            requests.get(f'https://api.telegram.org/bot{t}/sendMessage?chat_id={c}&text=Новый заказ ')
            requests.get(f'https://api.telegram.org/bot{t}/sendMessage?chat_id={c}&text=Имя: {a}')
            requests.get(f'https://api.telegram.org/bot{t}/sendMessage?chat_id={c}&text=Фамилия: {b}')
            requests.get(f'https://api.telegram.org/bot{t}/sendMessage?chat_id={c}&text=Телефон: {d}')
            requests.get(f'https://api.telegram.org/bot{t}/sendMessage?chat_id={c}&text=Город: {g}')
            requests.get(f'https://api.telegram.org/bot{t}/sendMessage?chat_id={c}&text={e}')
            requests.get(f'https://api.telegram.org/bot{t}/sendMessage?chat_id={c}&text=Номер отделения: {f}')
            requests.get(f'https://api.telegram.org/bot{t}/sendMessage?chat_id={c}&text=-------------------------------------------------------')




            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})