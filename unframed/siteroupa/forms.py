from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Item

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email',
                  'telephone', 'address', 'postal_code')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email',
                  'telephone', 'address', 'postal_code')


class ItemForm(forms.ModelForm):
    #images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Item
        fields = ['name', 'price', 'subcategory', 'description',
                  'color', 'stock', 'onsale', 'main_image']
