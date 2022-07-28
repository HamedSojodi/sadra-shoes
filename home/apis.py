from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer
from .models import Product


class ProductListApiView(APIView):

    def get(self, request):
        product = Product.objects.all()
        ser_data = ProductSerializer(instance=product, many=True).data
        return Response(ser_data, status=status.HTTP_200_OK)
