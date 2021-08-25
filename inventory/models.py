from enum import unique
from django.db import models
from django.db.models import constraints
from graphql_django.db import *

# Create your models here.

class Category(ModelAbstractBase):
    '''
    Model: Category.
    Description: This models is use to manage the categories in inventory.
    '''
    name = models.CharField(
        max_length=50, 
        help_text='Enter the category name.',
        error_messages={
            "blank": "Please enter the valid name."
            },
        verbose_name="Name"
        )

    def __str__(self):
        # @return  __str__()
        return self.name

    class Meta:
        db_table = "cateory"
        # unique_together = [
        #     'name'
        # ]
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
        ordering = ['-created']


class Product(ModelAbstractBase):
    '''
    Model: Product.
    Description: This model is use to manage products in inventory.
    '''
    name = models.CharField(
        max_length=50,
        help_text="Enter the product name.",
        error_messages={
            'blank':'Please enter the valid product name.'
            },
        verbose_name="Name"
    )

    notes = models.TextField(
        help_text='Enter the description.',
        verbose_name='Description',
        error_messages={
            "blank":'Enter the valid description.'
            }
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        help_text="Choose the category.",
        related_name='product',
        verbose_name='Category'
        )
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['category']),
        ]
        ordering = ['-created']
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
        