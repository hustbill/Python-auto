## Introduction

[Graphene](http://graphene-python.org) is an opinionated Python library for building GraphQL schemas/types fast and easily.

- **Easy to use:** Graphene helps you use GraphQL in Python without effort.
- **Relay:** Graphene has builtin support for Relay.
- **Data agnostic:** Graphene supports any kind of data source: SQL (Django, SQLAlchemy), NoSQL, custom Python objects, etc.
  We believe that by providing a complete API you could plug Graphene anywhere your data lives and make your data available
  through GraphQL.

## Integrations

Graphene has multiple integrations with different frameworks:

| integration       | Package                                                                                 |
| ----------------- | --------------------------------------------------------------------------------------- |
| Django            | [graphene-django](https://github.com/graphql-python/graphene-django/)                   |
| SQLAlchemy        | [graphene-sqlalchemy](https://github.com/graphql-python/graphene-sqlalchemy/)           |
| Google App Engine | [graphene-gae](https://github.com/graphql-python/graphene-gae/)                         |

Also, Graphene is fully compatible with the GraphQL spec, working seamlessly with all GraphQL clients, such as [Relay](https://github.com/facebook/relay), [Apollo](https://github.com/apollographql/apollo-client) and [gql](https://github.com/graphql-python/gql).

## Installation

For instaling graphene, just run this command in your shell

```bash
pip install "graphene>=2.0"
```

## Examples

Here is one example for you to get started:

```python
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(description='A typical hello world')

    def resolve_hello(self, info):
        return 'World'

schema = graphene.Schema(query=Query)
```

Then Querying `graphene.Schema` is as simple as:

```python
query = '''
    query SayHello {
      hello
    }
'''
result = schema.execute(query)
```

If you want to learn even more, you can also check the following [examples](examples/):

- **Basic Schema**: [Starwars example](examples/starwars)
- **Relay Schema**: [Starwars Relay example](examples/starwars_relay)

## Documentation

Documentation and links to additional resources are available at
https://docs.graphene-python.org/en/latest/
