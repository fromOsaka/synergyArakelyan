import json

import collections.abc
import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404, FileResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from .models import Product, Category

class Product:
    __MAX_ID = 0
    
    def __init__(self, name: str,
                category: str,
                color: str,
                release_year: int,
                engine_capacity: bool):
        self.id = Product.__MAX_ID
        Product.__MAX_ID += 1
        #pol9 in class
        self.name = name
        self.category = category
        self.color = color
        self.release_year = release_year
        self.engine_capacity = engine_capacity
    
    def __str__(self):
        return (
            f'id:{self.id}\n'
            + f'Name: {self.name}\n'
            + f'Category: {self.category}\n'
            + f'Color: {self.color}\n'
            + f'Release Year: {self.release_year}\n'
            + f'Engine Capacity: {self.engine_capacity}\n'
        )
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'color': self.color,
            'release_year': self.release_year,
            'engine_capacity': self.engine_capacity
            }
    
    def  save_as_json(self):
        with open(f'core/dumps/{self.id}.json', 'w+') as file:
            json.dump(self.to_dict(),file)


products = [Product("Mazda", "car", "blue", 2019, 1.6),
    Product("BMW", "moto", "white", 2020, 2),
    Product("Toyota", "car","cyan", 2022, 3.5),
    Product("Mercedes", "car", "red", 2018, 2.6),
    Product("Ducati", "moto", "black", 2015, 1.6)] 

categories_files = {
    'car' : 'media/car.jpg',
    'moto' : 'media/moto.jpg'
}

@csrf_exempt
def product_view(request: HttpRequest):                                 
    
    if request.method == 'GET':
        category = request.GET.get('category')
        return HttpResponse('\n'.join([
            str(product) for product in products
            if category is None
            or product.category==category
        ]))

    if request.method == 'POST':
        body = json.loads(request.body.decode('UTF-8'))
        product = Product(
            name = body['name'],
            category = body['category'],
            author = body['author'],
            release_year=datetime.date(*map(int))
        )

def view(request: HttpResponse, id : int):              
    
    if request.method == 'GET':
        filtered = [product for product in products 
                    if product.id == id]
        if len(filtered) == 0:
            return HttpResponse(status = 404)
        
        return HttpResponse(str(filtered[0]))
    

def get_product(id: int):
    products_with_id = [product for product in products 
                    if product.id == id]
    if len(products_with_id) == 0:
        return HttpResponse(status = 404)
    
    return products_with_id[0]
    
def category_image_view(request: HttpRequest, name: str):
    if name not in categories_files.keys():
        raise Http404
    
    return FileResponse(open(categories_files[name],'rb'),as_attachment=True)


def product_category_image(request: HttpRequest, id : int):
    product = get_product(id)

    return FileResponse(open(f'media/{product.category}.jpg','rb'),
                        as_attachment=True) 

    
def products_by_categories_view(request: HttpRequest):
    products_list = (product.to_dict() for product in products)
    response = {}
    
    for product in products_list:
        category = response.get(product['category'])
        
        if category is None:
            response[product['category']] = [product]
        else:
            category.append(product)
    
    return JsonResponse(response)

def json_product_view(request: HttpRequest, id: int):
    product = get_product(id)
    product.save_as_json()

    return FileResponse(open(f'core/dumps/{id}.json', 'rb'))

def json_show(request):
    data = {'cost' : 14,
            'title' : 'book'
            }
    return JsonResponse(data)


def index(request):
    return render(request, 'core/template/index.html')

