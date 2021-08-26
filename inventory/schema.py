import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Category, Product
from graphql_jwt.decorators import login_required


class CategoryType(DjangoObjectType):
    '''
    Similar to serializers in DRF
    '''
    class Meta:
        model = Category
        fields = ("id", "name", "product", "created",)


class IngredientType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "notes", "category", "created")


class CategoryInput(graphene.InputObjectType):
    '''
    Similar to ModelForms to get input during mutations django
    '''
    name = graphene.String()


class CreateCategory(graphene.Mutation):
    '''
    Similar to custom serializers in DRF

    Example:
    mutation CreateCategory{
        createCategory(input:{name:"hellocat"}){
            ok
            category{
            id
            name
            }
        }
    }
    '''
    class Arguments:
        input = CategoryInput(required=True)
    
    #return Fields
    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    @staticmethod
    @login_required
    def mutate(root, info, input):
        '''
        Saves the valid data and return outputFields
        otherwise return None
        '''
        instance = Category(name=input.name)

        try:
            instance.save()
        except Exception as e:
            print(e)
            return CreateCategory(ok=False, category=input)
        return CreateCategory(ok=True, category=instance)
    

class UpdateCategory(graphene.Mutation):
    '''
    This method is use to update category
    
    Example:
    mutation UpdateCategory{
        updateCategory(id:2, input:{name:"wow"}){
            ok
            category{
            name
            status
            }
        }
    }

    '''
    class Arguments:
        id = graphene.ID(required=True)
        input = CategoryInput(required=True)
    
    #return Fields
    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, **kwargs):
        '''
        Saves the valid data and return outputFields
        otherwise return None
        '''
        id = kwargs.get('id')
        print(id)
        input = kwargs.get('input')

        try:
            instance = Category.objects.get(id=id)
            instance.name = input.name
            instance.save()
        except Category.DoesNotExist:
            return UpdateCategory(ok=False, category=input)
        return UpdateCategory(ok=True, category=instance)


class DeleteCategory(graphene.Mutation):
    '''
    This method is use to delete category
    
    Example:
    mutation DeleteCategory{
        deleteCategory(id:1){
            ok
            message
        }
    }
    '''
    class Arguments:
        id = graphene.ID(required=True)
    
    #return Fields
    ok = graphene.Boolean()
    message = graphene.String(default_value="get error in delete action")

    @staticmethod
    def mutate(root, info, **kwargs):
        '''
        Saves the valid data and return outputFields
        otherwise return None
        '''
        id = kwargs.get('id')

        try:
            Category.objects.get(id=id).delete()
        except Category.DoesNotExist:
            return DeleteCategory(ok=False, message="Doenst found category")
        return DeleteCategory(ok=True, message="Successfully Deleted.")



class Mutation(graphene.ObjectType):
    '''
    Better approach to keep Query and Mutation in different classes
    '''
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()


class Query(graphene.ObjectType):
    """
    This is the query schema.

    Here the below fields (all_ingredients, category_by_name, .etc)
    are the the fields which we are going to recieve

    Under these fields we have @methods which starts with 'resolve_field_name'
    These @methods extents the functionality of the fields and return the approppriate output
    Here the output strictly depends upon the fields types.
    """
    hello = graphene.String(default_value="Welcome to GraphQL.")
    
    all_ingredients = graphene.List(IngredientType)
    
    category_by_name = graphene.Field(
        CategoryType, 
        name=graphene.String(required=False), 
        id=graphene.String(required=False)
        )
    
    category_count = graphene.Float()


    # Here I have made some methods to fetch data
    
    # return all fields
    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Product.objects.select_related("category").all()

    # return basic filter at server side
    def resolve_category_by_name(root, info, **kwargs):
        print(kwargs)
        try:
            name = kwargs['name']
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            pass
        except KeyError:
            return Category.objects.get(id=kwargs['id'])
    
    # return Float
    def resolve_category_count(root, info):
        return Category.objects.all().count()
    
    # return string
    def resolve_hello(root, info):
        return "Hello sir"

# main methods to call the query(schema) and mutation  
schema = graphene.Schema(query=Query, mutation=Mutation)
