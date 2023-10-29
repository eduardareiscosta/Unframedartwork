from django.urls import include, path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib import admin

app_name = 'siteroupa'
urlpatterns = [
    path('', views.index, name='index'),
    path('account/', include('django.contrib.auth.urls')),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('store/page/<pk>', views.items_list, name='store'),
    path('store/item/<pk>', views.items_get, name='item'),
    path('store/create_item', views.item_create, name='create_item'),
    path('mulher/',views.mulher, name='mulher'),
    path('acessorios/' , views.acessorios, name='acessorios'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)