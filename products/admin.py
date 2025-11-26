from django.contrib import admin
from .models import (Product, Category, Quantity, ProductQuantity, NutritionMetric, NutritionLabel,)


class ProductQuantityInline(admin.TabularInline):
    model = ProductQuantity
    extra = 1
    fields = ('quantity', 'price', 'stock')  # include price here, it's valid


class NutritionLabelInline(admin.TabularInline):
    model = NutritionLabel
    extra = 1
    fields = ('metric', 'amount_per_100g')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Quantity)
class QuantityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(NutritionMetric)
class NutritionMetricAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'from_price', 'category')
    readonly_fields = ('sku',)
    inlines = [ProductQuantityInline, NutritionLabelInline]
