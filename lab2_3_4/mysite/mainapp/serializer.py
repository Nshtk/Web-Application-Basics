from mainapp import models
from rest_framework import serializers


class HeadquarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Headquarter
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    headquarter = HeadquarterSerializer(read_only=True)

    class Meta:
        model = models.Manufacturer
        fields = ['name', 'description', "headquarter"]


class FurnitureTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FurnitureType
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    furniture_type = FurnitureTypeSerializer(many=True, read_only=True)
    manufacturer = ManufacturerSerializer(read_only=True)

    class Meta:
        model = models.Product
        fields = ['name', 'description', "furniture_type", "manufacturer", "price"]


class ProductInstanceSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = models.ProductInstance
        fields = ['id', 'product', "status"]
