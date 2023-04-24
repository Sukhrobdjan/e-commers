from django.contrib import admin
from .models import Product,ProductImg,Comment,Category


class ProductImgInline(admin.TabularInline):
    model = ProductImg


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','id','date','category','author']
    inlines = [ProductImgInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImg)
admin.site.register(Comment)
admin.site.register(Category)