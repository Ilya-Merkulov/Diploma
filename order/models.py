from django.db import models
from user.models import User
from product.models import Product

DEFAULT_ORDER_STATUS_ID = 1


# def get_total_cost(self):
#     return sum(item.get_cost() for item in self.items.all())

class ShippingAddress(models.Model):
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=20)


class OrderStatus(models.Model):
    name = models.CharField(max_length=30)


# Product models
# owner  # заказяик
# order_status  # статус заказа
# ordered = models.DateTimeField(auto_now_add=True)  # дата создания заказа
# shipped = models.DateTimeField(null=True)  # дата отправи
# paid = models.BooleanField(default=False)  # оплачено ли
# shipping_address  # таблица адресов
# product  # таблица с продуктами и ордерами

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='owner')
    ordered = models.DateTimeField(auto_now_add=True)  # дата создания заказа
    shipped = models.DateTimeField(null=True)  # дата отправи
    paid = models.BooleanField(default=False)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, blank=True, null=True,
                                     related_name='order_status', default=DEFAULT_ORDER_STATUS_ID)

    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='shipping_address')
    product = models.ManyToManyField(Product, through='OrderProduct')

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderProduct(models.Model):
    order = models.ForeignKey(Product, on_delete=models.CASCADE)
    product = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)  # verbose_name='Кількісь',

    def get_cost(self):
        return self.quantity * self.price
