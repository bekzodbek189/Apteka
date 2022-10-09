from rest_framework import serializers
from .models import *

class TabletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablet
        fields = "__all__"

class InSerializer(serializers.ModelSerializer):
    class Meta:
        model = In
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class Order_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Item
        fields = "__all__"