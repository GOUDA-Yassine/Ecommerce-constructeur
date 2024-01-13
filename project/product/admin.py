from django.contrib import admin
from .models import Product , Categories

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["name", "price", "category" ]


admin.site.register(Product, ProductAdmin )
admin.site.register(Categories)