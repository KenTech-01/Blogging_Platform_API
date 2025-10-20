from django.contrib import admin
from django.urls import path, include 
from rest_framework import routers 
from Platform_API_V2.views import PostViewSet 

router = routers.DefaultRouter()
router.register('Posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
]