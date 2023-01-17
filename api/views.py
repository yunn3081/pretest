from django.shortcuts import render
from django.http import HttpResponseBadRequest
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework import serializers
from api.models import Order
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.core.exceptions import PermissionDenied

ACCEPTED_TOKEN = ('omni_pretest_token')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        # fields = ('order_num', 'total_price', 'created')

# class IsAuthenticate(permissions.BasePermission):
    
#     def __init__(self, f):
#         self.f = f

#     def has_permission(self, request, view, func):
#         headers = request.headers

#         if headers['Mykey'] == ACCEPTED_TOKEN:
#             return True
#         return False

def is_authenticated(func):
    def wrap(*args, **kwargs):

        headers = args[1].headers

        if headers.get('X-Mykey') == ACCEPTED_TOKEN:
            result = func(*args, **kwargs)
            return result

        print('------this is my headers', headers)
        raise PermissionDenied

    return wrap

class ImportOrder(APIView):
    
    @is_authenticated
    def post(self, request):
        # Add your code here
        verify_data = OrderSerializer(data=request.data)

        if verify_data.is_valid():
            verify_data.save()
            return Response({"message": "create some data!", "data": verify_data.data})
        else:
            return HttpResponseBadRequest()

    @is_authenticated
    def get(self, request):

        order = get_object_or_404(Order, pk=1)
        serializer = OrderSerializer(order)
        return Response(serializer.data)