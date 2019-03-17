from django.shortcuts import render

def product_list(request):
    return render(request, 'products/index.html')

def product_detail(request):
    return render(request, 'products/detail.html')