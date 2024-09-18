from rest_framework import serializers

from drinks.models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = 'id name description'.split()
