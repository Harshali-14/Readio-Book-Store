from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BookViewSet, CartViewSet, OrderViewSet, WishlistViewSet, RatingViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('books', BookViewSet)
router.register('cart', CartViewSet)
router.register('orders', OrderViewSet)
router.register('wishlist', WishlistViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = router.urls