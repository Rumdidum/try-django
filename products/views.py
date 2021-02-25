from django.shortcuts import render, get_object_or_404
from .forms import ProductForm, RawProductForm
from .models import Product

# def render_initial_data(request):
#     initial_data = {
#         'title': "My awesome title"
#     }
#     obj = Prodct.objects.get(id=1)
#     my_form = RawProductForm(request.POST or None, instance=obj)
#     context = {
#         'form': my_form
#     }
#     return render(request, "products/product_create.html", context)
def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id=my_id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST) 
#         if my_form.is_valid():
#             # now the data is good
#             print("Aufgeräumte daten -", my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print("Alle fehler auflisten -",my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     # context = {
#     #     'title': obj.title,
#     #     'description': obj.description,
#     # }
#     context = {
#         'object': obj
#     }
#     return render(request, "products/product_detail.html", context)
#     