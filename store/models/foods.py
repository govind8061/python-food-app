from django.db import models
from .category import Category

# Create your models here.

class Food(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="uploads/menu", height_field=None, width_field=None, max_length=None)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=2)
    price=models.IntegerField(default=20)
    discount=models.IntegerField(default=0)
    
    @staticmethod
    @staticmethod
    def get_all_foods():
        return Food.objects.all()
    @staticmethod
    def get_all_foods_by_category_id(category_id):
        if category_id:
            return Food.objects.filter(category=category_id)
        else:
            return Food.objects.all()