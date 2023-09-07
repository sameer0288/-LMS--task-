# books/urls.py

from rest_framework import routers
from .views import BookViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'profiles', UserProfileViewSet)

urlpatterns = [
    # Your other URLs go here
]

urlpatterns += router.urls
