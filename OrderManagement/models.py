from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .genqr import genQR


# Create your models here.
class Order(models.Model):
    waitBuyer = 1
    waitSend = 2
    sent = 3
    statusChoices = (
        (waitBuyer, 'รอผู้ซื้อทำรายการ'),
        (waitSend, 'รอจัดส่ง'),
        (sent, 'จัดส่งแล้ว'),
    )
    id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    productName = models.CharField(max_length=50)
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    productDetail = models.TextField(max_length=255)
    buyerName = models.CharField(max_length=50, blank=True)
    buyerPhone = models.CharField(max_length=10, blank=True)
    sendAddress = models.TextField(max_length=255, blank=True)
    logistic = models.CharField(max_length=50, blank=True)
    trackingId = models.CharField(max_length=50, blank=True)
    status = models.PositiveSmallIntegerField(choices=statusChoices, default=waitBuyer)

    def __str__(self):
        if self.buyerName == '':
            return f'{self.id} - รอผู้ซื้อกรอกข้อมูล'
        else:
            return f'{self.id} - {self.buyerName}'


@receiver(post_save, sender=Order)
def gen_qr_code(sender, instance, created, **kwargs):
    if created:
        order = instance
        genQR(order.id, order.seller.profile.phone, order.price)


class TotalSummary(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    totalMoney = models.FloatField(default=0.0)
    totalIncome = models.FloatField(default=0.0)
    totalOrder = models.IntegerField(default=0)
    sentOrder = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} TotalSummary'


@receiver(post_save, sender=User)
def update_total_summary(sender, instance, created, **kwargs):
    if created:
        TotalSummary.objects.create(user=instance)
    instance.totalsummary.save()
