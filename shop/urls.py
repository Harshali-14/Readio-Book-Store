from django.urls import path, include
from .views import chatbot_view
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'books', BookViewSet)
router.register(r'cart', CartViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'wishlist', WishlistViewSet)
router.register(r'ratings', RatingViewSet)


urlpatterns = [
    path("chatbot/", chatbot_view, name="chatbot"),
    path('api/', include(router.urls)),
]