from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'home/index.html')
def about(request):
    return render(request, 'home/about.html')
def contact(request):
    return render(request, 'home/contact.html')

#  add api views here