from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from .views import SellerInfoViewSet, ProductViewSet, BuyerViewSet, SellerLoginView, SellerLogoutView

router = routers.DefaultRouter()
router.register('SellerInfo', SellerInfoViewSet)
router.register('Products', ProductViewSet)
router.register('Buyers', BuyerViewSet)

urlpatterns = [

	path('', include(router.urls)),
	path('login/', SellerLoginView.as_view()),
	path('logout/', SellerLogoutView.as_view())
	
]