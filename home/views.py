from django.shortcuts import render
from django.contrib import messages
from home.forms import ContactForm
from django.views import generic
from home.models import Service

# Create your views here.
def index(request):
    return render(request, 'home/index.html')
def about(request):
    return render(request, 'home/about.html')  
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully! We will revert you back soon.')
    else:
        form = ContactForm()   
    form = ContactForm()   
    return render(request, 'home/contact.html', {'form':form})

#  add api views here