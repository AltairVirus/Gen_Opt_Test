import Auth
from requests import request
from Response import Response


class GenResClient:
    graphql_endpoint = "/generated-resources/graphql"
    parser_endpoint = "/taskmanager/api/parser/TechRegimeAndSendOblects"

    def __init__(self, url: str):
        self.baseurl = url
        self.auth = Auth.update_headers_new(self.baseurl)

    def post_gql_request(self, query: str, variables: dict):
        url = self.baseurl + self.graphql_endpoint
        response = request("POST", url=url, headers=self.auth, json={"query": query, "variables": variables})
        return Response(response)

    def upload_file(self, file, params: dict):
        url = self.baseurl + self.parser_endpoint
        response = request("POST", url=url, headers={**self.auth, **{
            'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}},
                           params=params,
                           data=file)
        return Response(response)
