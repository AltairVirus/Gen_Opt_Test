class ModelRequest:
    def __init__(self, model, group):
        self.query = """mutation AddModel($input: ModelInput!) {
          addModel(input: $input) {
            name
            id
            tags {
              id
              __typename
            }
            __typename
          }
        }"""

        self.variables = {
            "input": {
                "groupId": f"{group.ID}",
                "id": f"{model.id}",
                "name": f"{group.NAME}",
                "nameShortRu": f"{group.NAME}",
                "tagIds": model.Tag
            }
        }
