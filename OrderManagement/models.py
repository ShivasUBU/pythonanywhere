from django.db import models
from django.conf import settings


# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        swappable=True,
    )
    productName = models.CharField(max_length=50)
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    productDetail = models.TextField(max_length=255)
    buyerName = models.CharField(max_length=50, blank=True)
    buyerPhone = models.CharField(max_length=10, blank=True)
    sendAddress = models.TextField(max_length=255, blank=True)
    Sent = models.BooleanField(default=False)  # สถานะจัดส่ง

    def __str__(self):
        return f'{self.id} - {self.buyerName}'


class SentOrder(models.Model):
    Order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    logistic = models.CharField(max_length=50)
    trackingId = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Order}'
