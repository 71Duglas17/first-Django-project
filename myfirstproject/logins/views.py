from django.shortcuts import render, redirect

# Create your views here.

def logins_page(request):
    return render(request, 'logins/logins_page.html')