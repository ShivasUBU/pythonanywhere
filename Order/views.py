from django.shortcuts import render
from OrderManagement.models import Order


# Create your views here.
def orderpublic(req, id):
    order = Order.objects.get(pk=id)
    order.price = f'{round(order.price, 2):,}'
    return render(req, 'OrderManagement/OrderDetail.html', {'order': order})
