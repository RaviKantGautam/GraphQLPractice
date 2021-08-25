import graphene
import graphql_jwt

# This is the basic implementation of JWT token based authentication.
class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

# This is pre app registration of schema
'''
Note: You can register only one schema in graphql.
'''
# scheme = graphene.Scheme(query=Query, mutation=Mutation)