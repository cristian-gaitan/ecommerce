from django.shortcuts import render 
from store.models import Product 
#funcion render sirve para mostrar mi vista
def home(reguest):
    products = Product.objects.all().filter(is_available= True)

    context= {
        'products': products,
    }


    return render(reguest, 'home.html', context)
