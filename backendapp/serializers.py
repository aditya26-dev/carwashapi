from rest_framework import serializers
from backendapp.models import Customer, Washer, Service, Package, Order, Rating

class customerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

class washerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Washer
        fields = '__all__'

class serviceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'

class packageSerializers(serializers.ModelSerializer):

    class Meta:
        model = Package
        fields = '__all__'

class orderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class ratingSerializers(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'