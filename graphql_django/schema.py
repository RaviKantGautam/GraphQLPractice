from authentication.schema import Query as auth
from authentication.schema import AuthMutation as authmute
from inventory.schema import Query as inventory
from inventory.schemarelay import Query as inventory1
from inventory.schema import Mutation as inventorymute
import graphene
from graphql_auth.schema import UserQuery, MeQuery

# This is the method to register all queries at the project level
class Query(UserQuery, MeQuery, auth, inventory, inventory1, graphene.ObjectType):
    '''
    This are query
    '''
    pass

# This is the method to register all mutation at the project level
class Mutation(authmute, inventorymute, graphene.ObjectType):
    '''
    This are mutations
    '''
    pass

# __call__ this schema variable in settings file.
schema = graphene.Schema(query=Query, mutation=Mutation)