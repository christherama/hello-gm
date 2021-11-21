from ariadne import make_executable_schema
from ariadne.asgi import GraphQL
from schema import type_defs
from controller import resolvers

schema = make_executable_schema(type_defs, *resolvers)
application = GraphQL(schema)
