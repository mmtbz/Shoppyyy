from django.contrib import admin
from .models import Category, Product
from parler.admin import TranslatableAdmin


# Register your models here.
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

""""
use the prepopulated_fields attribute to specify fields where
the value is automatically set using the value of other fields
"""


class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_date', 'updated_date']
    list_filter = ['available', 'created_date', 'updated_date']
    list_editable = ['price', 'stock', 'available']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
