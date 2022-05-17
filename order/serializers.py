from rest_framework import serializers
from .models import Order, OrderStatus, ShippingAddress


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ('id', 'name')


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ('id', 'city', 'address', 'postal_code')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'owner', 'ordered', 'shipped', 'paid', 'order_status', 'shipping_address',
                  'product')

    # def create(self, validated_data):
    #     order = Order(
    #         name=validate_data['name'],
    #         description=validate_data['description'],
    #         price=validate_data['price'],
    #         weight=validate_data['weight'],
    #         fat=validate_data['fat'],
    #         average_rate=validate_data['average_rate']
    #     )
    #     order.pop("email")
    #     # Now you have a clean valid email string
    #     # You might want to call an external API or modify another table
    #     # (eg. keep track of number of accounts registered.) or even
    #     # make changes to the email format.
    #
    #     # Once you are done, create the instance with the validated data
    #     return Order.objects.create(email=email, **validated_data)
