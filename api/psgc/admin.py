from django.contrib import admin
from api.psgc.models import Region, Province, City, Barangay


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'region')
    search_fields = ('code', 'name', 'region__name')
    autocomplete_fields = ['region']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'province', 'region')
    search_fields = ('code', 'name', 'province__name', 'region__name')

    # Enabling autocomplete_fields disables `smart_selects` function
    # autocomplete_fields = ['province', 'region']


@admin.register(Barangay)
class BarangayAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'city', 'province', 'region')
    search_fields = ('code', 'name', 'city__name', 'province__name', 'region__name')

    # Enabling autocomplete_fields disables `smart_selects` function
    # autocomplete_fields = ['city', 'province', 'region']
