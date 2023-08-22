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

    def upload_file(self, file, params: dict, data):

        url = self.baseurl + self.parser_endpoint
        response = request("POST", url=url,
                           headers={**self.auth, **{'Content-Type': 'multipart/form-data; boundary=----123456789',
                                                    'Content-Length': '255',
                                                    'Accept': '*/*',
                                                    'Accept-Encoding': 'gzip, deflate',
                                                    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                                                    'Connection': 'keep-alive',
                                                    'Cookie': '__ddg1_=InDiKq0JWbCKJLnozBS5',
                                                    'Host': 'genrestest.nntc.pro',
                                                    'Origin': 'http://genrestest.nntc.pro'
                                                    }},
                           json=data,
                           params=params,
                           files={'file': ("filename", file)})
        return Response(response)
