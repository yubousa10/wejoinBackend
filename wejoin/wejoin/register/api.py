from .models import Register
from .models import UserBase
from .serializers import RegisterSerializer
from .serializers import UserBaseSerializer
from rest_framework.authtoken.models import Token
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserList(APIView):
    def get(self, request, format=None):
        customers = UserBase.objects.all()
        alluserbase = UserBaseSerializer(customers,many=True)
        return Response(alluserbase.data)
    def post(self, request, format=None):
        serializer = UserBaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class getUserbyEmail(APIView): 
     def get(self, request, format=None):
        try:
            email = request.GET.get('email','default')
            customers = UserBase.objects.get(email=email)
        except customers.DoesNotExist:
            return HttpResponse(status=404)
        if request.method == 'GET':
            serializer = UserBaseSerializer(customers)
            return Response(serializer.data)
        
    
class getRegisterInfoByemail(APIView):
     def get(self, request, format=None):
        try:
            email = request.GET.get('email','default')
            user = UserBase.objects.get(email=email)
            registerinfo = Register.objects.get(userbase=user)
        except registerinfo.DoesNotExist:
            return HttpResponse(status=404)
        if request.method == 'GET':
            serializer = RegisterSerializer(registerinfo)
            return Response(serializer.data)
        
class RegisterList(APIView):
    def get(self, request, format=None):
        registerinfoList = Register.objects.all()
        serialized_registerinfoList = RegisterSerializer(registerinfoList,many=True)
        return Response(serialized_registerinfoList.data)
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
                    

                
        
           
      

