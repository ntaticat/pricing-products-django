from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def catalog(request):
    catalog_type = request.GET.get('type', 'Todos los muebles')
    print(catalog_type)
    return render(request, 'catalog.html', {
        "product_type": f'{catalog_type}'
    })
