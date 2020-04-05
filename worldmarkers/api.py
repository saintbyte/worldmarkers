
from rest_framework import routers
from world import api_views as world_views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'country', world_views.CountryViewSet)
router.register(r'town', world_views.TownViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
