from django.shortcuts import render

from .forms import ProductCreateForm

from .models import Product



def product_create_view(request):
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "product/create.html", context)

def home(request, *args, **kwargs ):
    print(args, kwargs) 
    print(request.user)
    products = Product.objects.all()
    return render(request, "home.html", {'products': products})


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'name': obj.name,
        'description': obj.description,
        'price': obj.price, 
        'summary': obj.summary 
    }
    return render(request, "product/detail.html", context)
