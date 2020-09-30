from django.forms import ModelForm
from .models import Order


# Create the form class.
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['productName', 'price', 'productDetail']
