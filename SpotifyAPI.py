import base64
import json

import requests
from urllib.parse import urlencode

from common import APIQueryType


class SpotifyAPI(object):
    client_id = None
    client_secret = None
    authorization_token = None
    token_url = 'https://accounts.spotify.com/api/token'
    spotify_api_url = 'https://api.spotify.com/v1'

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret

        self.authorize_client()

    def authorize_client(self) -> bool:
        """Retrieves authorization token and authorizes client to use Spotify API

        :return: boolean value that indicates whether or not the client is authorized
        """

        # set up credentials to be used in the retrieval of the Spotify API Token
        client_credentials = f'{self.client_id}:{self.client_secret}'
        client_credentials_b64 = base64.b64encode(client_credentials.encode())
        token_data = {'grant_type': 'client_credentials'}
        token_headers = {'Authorization': f'Basic {client_credentials_b64.decode()}'}
        request = requests.post(url=self.token_url, data=token_data, headers=token_headers)

        # if the request is invalid handle failure
        if request.status_code not in range(200, 299):
            raise Exception(f'Failed to authenticate client with error code: {request.status_code}')
            return False

        # store access token into object variable
        token_response_data = request.json()
        self.authorization_token = token_response_data['access_token']
        print(f'Client authorized!')
        return True

    def search(self, query: str, query_type: APIQueryType) -> dict:
        """Searches for the query string by the APIQueryType using the Spotify API

        :param query: The search query
        :param query_type: Type of search {'artist', 'album', 'track'}
        :return: search results in json format
        """

        # type check query type
        if not isinstance(query_type, APIQueryType):
            raise Exception('Invalid query type!')
            return {}

        # set up request
        headers = {'Authorization': f'Bearer {self.authorization_token}'}
        endpoint = self.spotify_api_url+'/search?'
        data = urlencode({'q': query, 'type': query_type.value})
        search_url = f'{endpoint}{data}'

        # initiate request and return its output in a json dictionary
        request = requests.get(search_url, headers=headers)
        if request.status_code not in range(200, 299):
            raise Exception(f'Request failed with error code: {request.status_code}')
            return {}

        return request.json()

    def get_artist_info(self, artist_name: str):
        pass

    def get_album_info(self, album_name: str):
        pass

    def get_track_info(self, track_name: str) -> dict:
        """Using the SpotifyAPI search function retrieve track information
           based on the track name

        :param track_name: The name of the track to query the Spotify API for
        :return: A dictionary of dictionaries that contain information regarding each
                 individual track with the same name:
                     Key = unique Spotify id
                     Values = track, artist, album
        """

        # validity check on track_name
        if track_name is None or track_name == '':
            raise Exception(f'Must provide valid track name')
            return {}

        # return dictionary
        track_data = {}

        # call to SpotifyAPI search
        data = self.search(track_name, APIQueryType.TRACK)

        # drill into json object returned by search and grab necessary info
        for tracks in data['tracks']['items']:
            name = str(tracks['name']).lower()
            if name == track_name:
                track_info = {
                    'track': tracks['name'],
                    'artist': tracks['artists'][0]['name'],
                    'album': tracks['album']['name']
                }
                track_data[tracks['id']] = track_info

        # in the event that no data is found return status indicating as such
        if len(track_data) == 0:
            print(f'Track data cannot be found on Spotify')
            return {}

        return track_data
