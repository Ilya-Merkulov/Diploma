from rest_framework import serializers
from .models import Product, Category, Label, Brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('id', 'name')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    # brand = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # category = serializers.PrimaryKey(many=False, read_only=True)
    # PrimaryKeyRelatedField(many=False, read_only=True)
    # product_filter = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'available',
                  'brand', 'category', 'label', 'created', 'updated')

    # def create(self, validated_data):
    #     brands = validated_data.pop("brand", [])
    #     print("brands")
    #     print(brands)
    #     product = Category.Product.create(**validated_data)
    #     for brand in brands:
    #         product.brand.create(**brand)
    #     return product
