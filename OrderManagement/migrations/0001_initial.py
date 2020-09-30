# Generated by Django 3.1.1 on 2020-09-29 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalSummary',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('totalMoney', models.FloatField(default=0.0)),
                ('totalIncome', models.FloatField(default=0.0)),
                ('totalOrder', models.IntegerField(default=0)),
                ('sentOrder', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('productDetail', models.TextField(max_length=255)),
                ('buyerName', models.CharField(blank=True, max_length=50)),
                ('buyerPhone', models.CharField(blank=True, max_length=10)),
                ('sendAddress', models.TextField(blank=True, max_length=255)),
                ('logistic', models.CharField(blank=True, max_length=50)),
                ('trackingId', models.CharField(blank=True, max_length=50)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'รอผู้ซื้อทำรายการ'), (2, 'รอจัดส่ง'), (3, 'จัดส่งแล้ว')], default=1)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
