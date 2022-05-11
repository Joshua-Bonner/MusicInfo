import base64
import requests

from common import APIQueryType


class SpotifyAPI(object):
    client_id = None
    client_secret = None
    authorization_token = None
    token_url = 'https://accounts.spotify.com/api/token'
    spotify_api_url = 'https://api.spotify.com/v1/search'

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret

        self.authorize_client()

    def authorize_client(self):
        """Retrieves authorization token and authorizes client to use Spotify API

        """

        # set up credentials to be used in the retrieval of the Spotify API Token
        client_credentials = f'{self.client_id}:{self.client_secret}'
        client_credentials_b64 = base64.b64encode(client_credentials.encode())
        token_data = {'grant_type': 'client_credentials'}
        token_headers = {'Authorization': f'Basic {client_credentials_b64.decode()}'}
        request = requests.post(url=self.token_url, data=token_data, headers=token_headers)

        # if the request is invalid
        if request.status_code not in range(200, 299):
            print(f'Request failed with error code: {request.status_code}')
            return False

        # store access token into object variable
        token_response_data = request.json()
        self.authorization_token = token_response_data['access_token']
        print(f'Client authorized!')
        return True

    def search(self, query_type: APIQueryType):
        pass
