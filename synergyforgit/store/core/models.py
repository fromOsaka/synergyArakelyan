import json

from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=128, default ='Имя не присвоено')
    category_picture = models.ImageField(upload_to='image/')
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = 'Категоря'
        verbose_name_plural = 'Категории'




class Product(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.product_name
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'





class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15,null=True,unique=True, verbose_name='Наименование')
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
        )
    color = models.CharField(max_length=15, verbose_name='Цвет')
    release_year = models.DateField(auto_now=True, verbose_name='Дата выпуска',null=False)
    engine_capacity = models.CharField(max_length=4, verbose_name='Объем двигателя')
    count = models.PositiveSmallIntegerField(default=0,null=False)
    
    def __str__(self):
        return (
             f'Name: {self.name}\n'
            + f'Category: {self.category}\n'
        )