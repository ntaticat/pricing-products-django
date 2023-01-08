from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
def index(request):
    return render(request, 'index.html')

def catalog(request):
    
    products = list(models.Product.objects.all())
    
    catalog_type = request.GET.get('type', 'Todos los muebles')
    print(catalog_type)
    return render(request, 'catalog.html', {
        "product_type": f'{catalog_type}',
        "products": products
    })
