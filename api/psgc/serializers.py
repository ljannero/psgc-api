from rest_framework import serializers
from api.psgc.models import Region, Province, City, Barangay


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ['url', 'code', 'name']


class ProvinceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Province
        fields = ['url', 'region', 'name', 'code']


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ['url', 'region', 'province', 'name', 'code']


class BarangaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Barangay
        fields = ['url', 'region', 'province', 'city', 'name', 'code']
