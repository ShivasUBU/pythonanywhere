from django.shortcuts import render
from OrderManagement.models import Order
from .forms import AddBuyerInfo


# Create your views here.
def orderpublic(req, id):
    order = Order.objects.get(pk=id)
    if req.method == 'POST':
        form = AddBuyerInfo(req.POST)
        if form.is_valid():
            order.status = 2
            order.buyerName = form.cleaned_data['buyerName']
            order.buyerPhone = form.cleaned_data['buyerPhone']
            order.sendAddress = form.cleaned_data['sendAddress']
            order.save()
            totalsummary = req.user.totalsummary
            totalsummary.totalIncome += order.price
            totalsummary.save()
            return render(req, 'Order/Public.html', {'order': order})
    else:
        order.price = f'{round(order.price, 2):,}'
        form = AddBuyerInfo()
        return render(req, 'Order/Public.html', {'order': order, 'form': form})
