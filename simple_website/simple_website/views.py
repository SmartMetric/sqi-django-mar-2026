from django.shortcuts import render

def home(request):
    return render(request, 'simple_website/home.html')

def profile(request):
    return render(request, 'simple_website/profile.html')

def services(request):
    return render(request, 'simple_website/services.html')

def help_page(request):
    return render(request, 'simple_website/help.html')