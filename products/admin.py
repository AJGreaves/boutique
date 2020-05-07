from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Adds extra fields in admin panel so you can see product
    data all in one table.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    # Adds fields to view in admin panel.
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
