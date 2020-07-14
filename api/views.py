from django.shortcuts import render
from .models import User, Product, Buyer, LoginUser
from .serializers import SellerInfoSerializer, ProductSerializer, BuyerSerializer, SellerCheckSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
#----------------------------------#

class SellerInfoViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() #Queries all objects in this model
    serializer_class = SellerInfoSerializer
    permission_classes=(AllowAny,)

class SellerLoginView(APIView):
    serializer_class = SellerCheckSerializer
    permission_classes=(AllowAny,)
    def post(self, request, format=None):

    	serializer = SellerCheckSerializer(data = request.data)

    	if serializer.is_valid(raise_exception = True):
    		email = serializer.validated_data.get('email', None)
    		password = serializer.validated_data.get('password', None)

    		try:
	    		user = authenticate(request, username = email, password = password)
	    		login(request, user)
	    		userObj = get_user_model().objects.get(email = email)

                if userObj.first_name:
                    user_get = userObj.first_name #get users firstname if theres none returns an empty string
                else:
                    user_get = ''

	    		token, created = Token.objects.get_or_create(user = userObj)

	    	except Exception as e: 
	    		return Response('user does not exist', status = 400)
	    	
    		return Response({'token' : token.key, 'first_name' : user_get}, status = 201) 
    	return Response(serializer.errors, status = 400)

class SellerLogoutView(APIView):
	#logout user
	permission_classes=(AllowAny,)
	def post(self, request):
		logout(request)
		return Response(status = 200)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all() #Queries all objects in this model
    serializer_class = ProductSerializer
    permission_classes=(AllowAny,)


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all() #Queries all objects in this model
    serializer_class = BuyerSerializer
    permission_classes=(AllowAny,)