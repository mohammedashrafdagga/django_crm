from django.shortcuts import render


def index_page(request):
    return render(request, 'core/index.html')


def about_page(request):
    return render(request, 'core/about.html')
