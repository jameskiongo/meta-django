from decimal import Decimal

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Category, MenuItem, Rating


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Rating
        fields = ["user", "menuitem_id", "rating"]
        validators = [
            UniqueTogetherValidator(
                queryset=Rating.objects.all(), fields=["user", "menuitem_id", "rating"]
            )
        ]
        extra_kwargs = {"rating": {"min_value": 0, "max_value": 5}}


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "slug", "title"]


class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source="inventory")
    price_after_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MenuItem
        fields = [
            "id",
            "title",
            "price",
            "stock",
            "price_after_tax",
            "category",
            "category_id",
        ]

        extra_kwargs = {"price": {"min_value": 2}, "stock": {"min_value": 0}}

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)
