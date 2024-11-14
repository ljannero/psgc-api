from django.urls import path, include
from rest_framework import routers
from api.psgc import views

router = routers.DefaultRouter()

router.register(r'region', views.RegionViewSet)
router.register(r'province', views.ProvinceViewSet)
router.register(r'city', views.CityViewSet)
router.register(r'barangay', views.BarangayViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
