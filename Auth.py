import requests
import json


def update_headers_new(url):
    url_keycloak = url + "/auth/realms/genrestest/protocol/openid-connect/token"

    keycloak_data = {
        'grant_type': 'client_credentials',
        'scope': 'roles',
        'client_id': 'ltds',
        'client_secret': '30a0c9fb-95d1-4fc9-b22a-ccddd7904869',
    }

    # print(cls.keycloack_address, cls.client_id, cls.client_secret)
    # print("http://genrestest.nntc.pro/auth/realms/genrestest/protocol/openid-connect/token", 'ltds', '30a0c9fb-95d1-4fc9-b22a-ccddd7904869')

    headers_keycloak = {
        'Content-Length': '105',
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    r_keycloak = requests.post(url_keycloak, headers=headers_keycloak, data=keycloak_data)

    bearer_token = json.loads(r_keycloak.text)['access_token']

    headers_data = {
        'Authorization': 'Bearer ' + str(bearer_token),
        'Content-type': 'application/json',
        'Accept': 'text/plain'
    }

    return headers_data
