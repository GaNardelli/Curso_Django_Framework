from django.shortcuts import render
from django.shortcuts import get_object_or_404
from core.models import Product

from django.http import HttpResponse

from django.template import loader

def index(request):
    products = Product.objects.all()

    if request.user.is_anonymous:
        status = "Usuário não logado"
    else:
        status = "Usuário logado"

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django Framework Chave',
        'status': status,
        'Produtos': products
    }
    return render(request, 'index.htm', context)


def contact(request):
    return render(request, 'contact.htm')

def product(request, pk):
    # product = Product.objects.get(id = pk)
    product = get_object_or_404(Product, id = pk)

    context = {
        'product' : product
    }
    return render(request, 'product.htm', context)

def error404(request, exception):
    return render(request,'404.htm')

def error500(request):
    return render(request,'500.htm')

