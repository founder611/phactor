from django.shortcuts import render

# Create your views here.

def phactor_homepage(request):
    return render(request, 'homepage.html')