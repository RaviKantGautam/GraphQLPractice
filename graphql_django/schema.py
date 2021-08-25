from authentication.schema import Query as auth
from authentication.schema import Mutation as authmute
from inventory.schema import Query as inventory
from inventory.schemarelay import Query as inventory1
from inventory.schema import Mutation as inventorymute
import graphene

# This is the method to register all queries at the project level
class Query(auth, inventory,inventory1, graphene.ObjectType):
    pass

# This is the method to register all mutation at the project level
class Mutation(authmute, inventorymute, graphene.ObjectType):
    pass

# __call__ this schema variable in settings file.
schema = graphene.Schema(query=Query, mutation=Mutation)