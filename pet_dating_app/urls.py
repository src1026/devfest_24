from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PetProfileViewSet, MatchViewSet 

router = DefaultRouter()
router.register(r'petprofiles', PetProfileViewSet)
router.register(r'matches', MatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]