class GroupOfModelRequest:
    def __init__(self, group):
        self.query = """mutation AddModelGroup($input: ModelGroupInput!) {
          addModelGroup(input: $input) {
            id
            name
            nameShortRu
            __typename
          }
        }"""

        self.variables = {
            "input": {
                "id": f"{group.ID}",
                "nameShortRu": f"{group.NAME}"
            }
        }
