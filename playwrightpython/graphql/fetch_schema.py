# import requests
# from sgqlc.introspection import introspect
#
# GRAPHQL_URL = "https://your-graphql-endpoint.com/graphql"  # Replace with your actual endpoint
#
#
# # Fetch the schema via introspection query
# def fetch_graphql_schema():
#     response = requests.post(
#         GRAPHQL_URL,
#         json={"query": introspect},
#         headers={"Content-Type": "application/json"}
#     )
#
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception(f"Failed to fetch schema: {response.status_code}\n{response.text}")
#
#
# # Save schema to a file
# def save_schema(schema_data, filename="schema.json"):
#     with open(filename, "w", encoding="utf-8") as f:
#         import json
#         json.dump(schema_data, f, indent=2)
#     print(f"Schema saved to {filename}")
#
#
# # Run script
# if __name__ == "__main__":
#     schema_data = fetch_graphql_schema()
#     save_schema(schema_data)

# python fetch_schema.py
# This will fetch and save the schema as schema.json


# sgqlc-codegen schema schema.json schema.py


# from sgqlc.endpoint.http import HTTPEndpoint
# from schema import mutation, ReviewInput, Episode  # Import generated classes
#
# # Define GraphQL endpoint
# GRAPHQL_URL = "https://your-graphql-endpoint.com/graphql"
#
# # Set up the endpoint
# endpoint = HTTPEndpoint(GRAPHQL_URL)
#
# # Define mutation input
# variables = {
#     "ep": Episode.JEDI,
#     "review": ReviewInput(stars=5, commentary="This is a great movie!")
# }
#
# # Execute mutation
# data = endpoint(mutation.create_review_for_episode, variables=variables)
#
# # Print the response
# print("Response:", data)