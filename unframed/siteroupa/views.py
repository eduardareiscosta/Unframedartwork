from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, ItemForm
from .models import Item, Order, Category, Subcategory, ItemImage
from django.views import generic




def index(request):
    return render(request, 'siteroupa/index.html')

def login(request):
    return render(request, "siteroupa/login.html")

def mulher(request):
    return render(request, "siteroupa/mulher.html")

def acessorios(request):
    return render(request, "siteroupa/acessorios.html")

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = '/account/login'
    template_name = 'registration/signup.html'

def items_list(request, pk=1):
    start = int(1*pk) - 1
    end = start + 15
    items = Item.objects.all()[start:end]
    context = {
        'items': items
    }
    return render(request, 'siteroupa/store.html', context)

def items_get(request, pk=1):
    items = Item.objects.get(pk=pk)
    context = {
        'item': items
    }
    return render(request, 'siteroupa/item.html', context)


def item_create(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST, request.FILES)
        if item_form.is_valid():
            item = item_form.save()  # Save the item

            # Handle uploaded images and create Image objects
            for image_file in request.FILES.getlist('images'):
                ItemImage.objects.create(item=item, image=image_file)

            return redirect('/store/page/1')  # Redirect to a success page
    else:
        item_form = ItemForm()

    return render(request, 'siteroupa/create_item.html', {'item_form': item_form})

