from django.shortcuts import render
from products.models import Product, Category
from django.views.generic import View
from django.shortcuts import get_object_or_404



def for_all_category(request):
    categories = Category.objects.all()
    context = {
        'categories':categories,
    }
    return context




class IndexView(View):
    """ All products """

    def get(self,request):
        products = Product.objects.all()
        
        context = {
            'products':products,
        }
        return render(request, 'index.html', context)
    

class CategoyrView(View):
    def get(self, request, category_name):
        category = get_object_or_404(Category,name = category_name)
        products = Product.objects.filter(category = category)

        context = {
            'category':category,
            'products':products
        }
        return render(request,'category.html',context)

