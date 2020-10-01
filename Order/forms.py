from django.forms import ModelForm
from OrderManagement.models import Order


# Create the form class.
class AddBuyerInfo(ModelForm):
    class Meta:
        model = Order
        fields = ['buyerName', 'buyerPhone', 'sendAddress']
