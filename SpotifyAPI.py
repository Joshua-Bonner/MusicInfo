import base64
import requests


class SpotifyAPI(object):

    def __init__(self):
        pass

    @staticmethod
    def get_authorization_token(client_id: str, client_secret: str) -> str:
        """Retrieves the authorization token for use with the Spotify API

        :param: client_id and api_key retrieved from Spotify API
        :return: access token as a string object
        """
        url = 'https://accounts.spotify.com/api/token'
        client_credentials = f'{client_id}:{client_secret}'
        client_credentials_b64 = base64.b64encode(client_credentials.encode())
        token_data = {'grant_type': 'client_credentials'}
        token_headers = {'Authorization': f'Basic {client_credentials_b64.decode()}'}
        request = requests.post(url=url, data=token_data, headers=token_headers)
        token_response_data = request.json()
        return token_response_data['access_token']
