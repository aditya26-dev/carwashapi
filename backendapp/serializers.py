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


class nilaiSerializers(serializers.ModelSerializer):

    class Meta:
        model = nilai
        fields = '__all__'

class bukuSerializers(serializers.ModelSerializer):

    class Meta:
        model = buku
        fields = '__all__'

class beritaSerializers(serializers.ModelSerializer):

    class Meta:
        model = berita
        fields = '__all__'

class bantuanSerializers(serializers.ModelSerializer):

    class Meta:
        model = bantuan
        fields = '__all__'