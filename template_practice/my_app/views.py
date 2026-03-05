from django.shortcuts import render

def welcome(request):
    return render(request, 'my_app/welcome.html')