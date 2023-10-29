from django.contrib import admin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
from .models import Category, Subcategory, Item, Order

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email']

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Item)
admin.site.register(Order)