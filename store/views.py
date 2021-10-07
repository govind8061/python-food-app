from django.shortcuts import render
from .models import Food
from .models import Category

# Create your views here.
def home_page(request):
    food=None
    category=Category.objects.all()
    categoryId=request.GET.get('category')
    if categoryId:
        food=Food.get_all_foods_by_category_id(categoryId)
    else:
        food=Food.objects.all()

    discounted_price=[]
    for f in Food.objects.all():
        discounted_price.append(f.price*(100-f.discount)/100)

        
    context={'foods':food, 'category':category, 'd_price':discounted_price}
    template='index.html'
    return render(request,template,context)

