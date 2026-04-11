from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('books', BookViewSet)   # ✅ THIS CREATES /api/books/
router.register('cart', CartViewSet)
router.register('orders', OrderViewSet)
router.register('wishlist', WishlistViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = router.urls