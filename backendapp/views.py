from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers

# Create your views here.
class CustomerList(APIView):

    def get(self, request):
        customer = models.Customer.objects.all()
        serializer = serializers.customerSerializers(customer, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass

class WasherList(APIView):

    def get(self, request):
        washer = models.Washer.objects.all()
        serializer = serializers.washerSerializers(washer, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass

class ServiceList(APIView):

    def get(self, request):
        service = models.Service.objects.all()
        serializer = serializers.serviceSerializers(service, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass

class PackageList(APIView):

    def get(self, request):
        package = models.Package.objects.all()
        serializer = serializers.packageSerializers(package, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass

class OrderList(APIView):

    def get(self, request):
        order = models.Order.objects.all()
        serializer = serializers.orderSerializers(order, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass

class RatingList(APIView):

    def get(self, request):
        rating = models.Rating.objects.all()
        serializer = serializers.ratingSerializers(rating, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass

class bukuList(APIView):

    def get(self, request):
        rating = models.buku.objects.all()
        serializer = serializers.bukuSerializers(rating, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass

class beritaList(APIView):

    def get(self, request):
        rating = models.berita.objects.all()
        serializer = serializers.beritaSerializers(rating, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass


class bantuanList(APIView):

    def get(self, request):
        rating = models.bantuan.objects.all()
        serializer = serializers.bantuanSerializers(rating, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass

class nilaiList(APIView):

    def get(self, request):
        rating = models.nilai.objects.all()
        serializer = serializers.nilaiSerializers(rating, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass