from rest_framework import serializers, exceptions
from .models import User, Product, Buyer, LoginUser
#from django.db.models import Q
from django.contrib.auth import get_user_model

class SellerInfoSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = User
        fields = [ 'id', 'first_name', 'last_name', 'state_of_residence', 'email', 'password' ]

    def create(self, validated_data):
    	email = validated_data.get('email', None)
    	password = validated_data.get('password', None)
    	last_name = validated_data.get('last_name', None)
    	first_name = validated_data.get('first_name', None)
    	state_of_residence = validated_data.get('state_of_residence', None)
    	return User.objects.create_user(email = email, password = password, first_name = first_name, last_name = last_name, state_of_residence = state_of_residence, is_staff = True)

class SellerCheckSerializer(serializers.ModelSerializer):

	class Meta:
		model = LoginUser
		fields = [ 'email', 'password']

		extra_kwargs = {'password' : {'write_only' : True}, 'email' : {'write_only' : True}} #password can be written but will not be seen when the response is returned



class ProductSerializer(serializers.ModelSerializer):

	seller_name = serializers.ReadOnlyField(source='seller.first_name')
	seller_location = serializers.ReadOnlyField(source='seller.state_of_residence')

	class Meta:
		model = Product
		fields = [ 'id', 'seller', 'seller_name', 'seller_location', 'name', 'price', 'image', 'sold' ]

class BuyerSerializer(serializers.ModelSerializer):

	product_seller_name = serializers.ReadOnlyField(source='product.seller.first_name')

	class Meta:
		model = Buyer 
		fields = [ 'id', 'product', 'product_seller_name',  'name', 'email', 'location' ]