from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OrderForm, AddSend
from .models import Order


# Create your views here.
@login_required
def dashboard(req):
    totalsummary = req.user.totalsummary
    money = totalsummary.totalMoney
    income = totalsummary.totalIncome
    orders = totalsummary.totalOrder
    sent = totalsummary.sentOrder
    failorder = orders - sent
    failmoney = money - income
    if orders != 0:
        percent = f'{round((sent * 100) / orders, 2)}% / {round((failorder * 100) / orders, 2)}%'
    else:
        percent = f'0% / 0%'

    context = {
        'income': f'{round(income, 2):,}',
        'orders': orders,
        'sent': sent,
        'failorder': failorder,
        'percent': percent,
        'failmoney': f'{round(failmoney, 2):,}'
    }
    return render(req, 'OrderManagement/Dashboard.html', context)


@login_required
def profile(req):
    return render(req, 'OrderManagement/Profile.html')


@login_required
def addorder(req):
    if req.method == 'POST':
        form = OrderForm(req.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.seller = req.user
            order.save()
            totalsummary = req.user.totalsummary
            totalsummary.totalMoney += order.price
            totalsummary.totalOrder += 1
            totalsummary.save()
            return redirect('OrderDetail', id=order.id)
    else:
        form = OrderForm()
        return render(req, 'OrderManagement/AddOrder.html', {'form': form})


@login_required
def searchorder(req):
    if req.GET != {}:
        searchBy = req.GET['searchBy']
        keyword = req.GET['keyword']
        if keyword == '':
            return render(req, 'OrderManagement/SearchOrder.html')
        if searchBy == '1':
            try:
                searchBy = int(searchBy)
                orders = Order.objects.filter(seller=req.user, id=int(keyword)).order_by('-id')
            except:
                return render(req, 'OrderManagement/SearchOrder.html')
        else:
            orders = Order.objects.filter(seller=req.user, buyerName__contains=keyword).order_by('-id')
        return render(req, 'OrderManagement/SearchOrder.html', {'searchBy': searchBy, 'keyword': keyword, 'orders': orders})

    else:
        return render(req, 'OrderManagement/SearchOrder.html')


@login_required
def waitsendorder(req):
    orders = Order.objects.filter(seller=req.user, status=2).order_by('-id')
    paginator = Paginator(orders, 20)
    page_number = req.GET.get('page')
    orders = paginator.get_page(page_number)
    return render(req, 'OrderManagement/WaitSendOrder.html', {'orders': orders})


@login_required
def allorder(req):
    orders = Order.objects.filter(seller=req.user).order_by('-id')
    paginator = Paginator(orders, 20)
    page_number = req.GET.get('page')
    orders = paginator.get_page(page_number)
    return render(req, 'OrderManagement/AllOrder.html', {'orders': orders})


@login_required
def orderdetail(req, id):
    order = Order.objects.get(pk=id)
    if req.method == 'POST':
        form = AddSend(req.POST)
        if form.is_valid():
            order.status = 3
            order.logistic = form.cleaned_data['logistic']
            order.trackingId = form.cleaned_data['trackingId']
            order.save()
            totalsummary = req.user.totalsummary
            totalsummary.sentOrder += 1
            totalsummary.save()
            return render(req, 'OrderManagement/OrderDetail.html', {'order': order})
    else:
        order.price = f'{round(order.price, 2):,}'
        form = AddSend()
        return render(req, 'OrderManagement/OrderDetail.html', {'order': order, 'form': form})
