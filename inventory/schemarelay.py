from graphene import relay, ObjectType
import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Category, Product

# Here i have make the use of relay

'''
Relay: It a way to extent the functionality of graphene like filter, pagination, hidden IDs, .etc
For applying filters, I have make the use of `pip install django-filter`.

Example: 
{
  allCategories(first:2){
    edges{
      node{
        id
        name
        status
        product{
          edges{
            node{
              name
              category{
                status
              }
            }
          }
        }
      }
    }
  }
}


'''

class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'product']
        interfaces = (relay.Node, )

class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = ['name', ]
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    product = relay.Node.Field(ProductNode)
    all_products = DjangoFilterConnectionField(ProductNode)


schema = graphene.Schema(query=Query)
