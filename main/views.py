from django.shortcuts import render
from products.models import Product, Category
from django.views.generic import View

class IndexView(View):
    def get(self,request):
        products = Product.objects.all()
        
        context = {
            'products':products,
        }
        return render(request, 'index.html', context)
    
