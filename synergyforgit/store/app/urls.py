"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import product_view, view, product_category_image, products_by_categories_view, json_product_view, category_image_view, json_show, index
from django.conf.urls.static import static
from .settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls), #+
    path('',index, name="index"), # не работает на момент 29го марта 
    path('products/', product_view), #+      (GET - работает, POST - нет) 
    path('products/<int:id>', view), #+ (GET - работает)
    path('<int:id>/category',product_category_image, name='product_category_image'),  #+
    path('by_categories/', products_by_categories_view, name='products_by_categories'), #+
    path('list/<int:id>', json_product_view, name='json_product_view'),  #+    
    path("categories/<str:name>", category_image_view), #+
    path('json', json_show, name= 'jsom_show') #+
    ]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
