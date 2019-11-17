from rest_framework import serializers

from .models import CarNameModel, CarModel


class CarNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarNameModel
        fields = ['id', 'lang', 'name']


class CarSerializer(serializers.ModelSerializer):
    name = CarNameSerializer(many=True)

    class Meta:
        model = CarModel
        fields = ['id', 'name', 'year', 'created_at']
