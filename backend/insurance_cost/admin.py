from django.contrib import admin

from .models import CargoType, InsuranceCost, Rate


@admin.register(CargoType)
class CargoTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    empty_value_display = '-пусто-'


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    empty_value_display = '-пусто-'


@admin.register(InsuranceCost)
class CInsuranceCostAdmin(admin.ModelAdmin):
    list_display = ('id', 'cargo_type', 'rate', 'date', 'cost')
    empty_value_display = '-пусто-'