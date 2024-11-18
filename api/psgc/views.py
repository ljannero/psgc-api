from rest_framework import permissions, viewsets, filters
from api.psgc.models import Region, Province, City, Barangay
from api.psgc.serializers import RegionSerializer, ProvinceSerializer, CitySerializer, BarangaySerializer


class RegionViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows regions to be viewed or edited
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]


class ProvinceViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows provinces to be viewed or edited
    """
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['code', 'name', 'region__name']
    permission_classes = [permissions.IsAuthenticated]


class CityViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows cities to be viewed or edited
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['code', 'name', 'province__name', 'region__name']
    permission_classes = [permissions.IsAuthenticated]


class BarangayViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows barangays to be viewed or edited
    """
    queryset = Barangay.objects.all()
    serializer_class = BarangaySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['code', 'name', 'city__name', 'province__name', 'region__name']
    permission_classes = [permissions.IsAuthenticated]
