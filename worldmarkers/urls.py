from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as auth_views
from .api import router
from world.views import main_page

urlpatterns = [
    path('', main_page),
    path('api/v1/auth/', auth_views.obtain_auth_token),
    path('api/v1/accounts/', include('rest_registration.api.urls')),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
