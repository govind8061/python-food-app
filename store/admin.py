from django.contrib import admin
from .models import Food
from .models import Category

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display=['name','img','category','price','discount']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']


admin.site.register(Food,FoodAdmin)
admin.site.register(Category,CategoryAdmin)