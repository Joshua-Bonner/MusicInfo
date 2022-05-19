import base64
import requests
from urllib.parse import urlencode

from Common.common import APIQueryType


class SpotifyAPI(object):
    """Retrieves music information from the SpotifyAPI

    """

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

        # set up request
        headers = {'Authorization': f'Bearer {self.authorization_token}'}
        endpoint = self.spotify_api_url+'/search?'
        data = urlencode({'q': query, 'type': query_type.value})
        search_url = f'{endpoint}{data}'

        # initiate request and return its output in a json dictionary
        request = requests.get(search_url, headers=headers)
        if request.status_code not in range(200, 299):
            raise Exception(f'Request failed with error code: {request.status_code}')

        return request.json()

    def get_artist_info(self, artist_name: str) -> dict:
        """Using the SpotifyAPI search function retrieve artist information
           based on the artists name

        :param artist_name: The name of the artist to query
        :return: A dictionary of dictionaries that contain information regarding each
                 individual track with the same name:
                    Key = unique Spotify id
                    Values = artist, followers, genre
        """

        # validity check on artist_name
        if artist_name is None or artist_name == '':
            raise Exception(f'Must provide valid artist name')

        # return dictionary
        artist_data = {}

        # call to SpotifyAPI search
        data = self.search(artist_name, APIQueryType.ARTIST)

        # drill into dictionary object returned by search and grab necessary info
        for artists in data['artists']['items']:
            name = str(artists['name']).lower()
            if name == artist_name.lower():
                artist_info = {
                    'Artist': artists['name'],
                    'Followers': artists['followers']['total'],
                    'Genre': artists['genres']
                }
                artist_data[artists['id']] = artist_info

        # in the event that no data is found return status indicating as such
        if len(artist_data) == 0:
            print(f'Artist data cannot be found on Spotify')
            return {}

        return artist_data

    def get_album_info(self, album_name: str):
        """Using the SpotifyAPI search function retrieve album information
           based on the track name

        :param album_name: The name of the album to query
        :return: A dictionary of dictionaries that contain information regarding each
                 individual album with the same name:
                     Key = unique Spotify id
                     Values = album, artist, release date
        """

        # validity check on track_name
        if album_name is None or album_name == '':
            raise Exception(f'Must provide valid track name')

        # return dictionary
        album_data = {}

        # call to SpotifyAPI search
        data = self.search(album_name, APIQueryType.ALBUM)

        # drill into dictionary object returned by search and grab necessary info
        for albums in data['albums']['items']:
            name = str(albums['name']).lower()
            if name == album_name.lower():
                album_info = {
                    'Album': albums['name'],
                    'Artist': albums['artists'][0]['name'],
                    'Release Date': albums['release_date']
                }
                album_data[albums['id']] = album_info

        # in the event that no data is found return status indicating as such
        if len(album_data) == 0:
            print(f'Track data cannot be found on Spotify')
            return {}

        return album_data

    def get_track_info(self, track_name: str) -> dict:
        """Using the SpotifyAPI search function retrieve track information
           based on the track name

        :param track_name: The name of the track to query
        :return: A dictionary of dictionaries that contain information regarding each
                 individual track with the same name:
                     Key = unique Spotify id
                     Values = track, artist, album
        """

        # validity check on track_name
        if track_name is None or track_name == '':
            raise Exception(f'Must provide valid track name')

        # return dictionary
        track_data = {}

        # call to SpotifyAPI search
        data = self.search(track_name, APIQueryType.TRACK)

        # drill into dictionary object returned by search and grab necessary info
        for tracks in data['tracks']['items']:
            name = str(tracks['name']).lower()
            if name == track_name.lower():
                track_info = {
                    'Track': tracks['name'],
                    'Artist': tracks['artists'][0]['name'],
                    'Album': tracks['album']['name']
                }
                track_data[tracks['id']] = track_info

        # in the event that no data is found return status indicating as such
        if len(track_data) == 0:
            print(f'Track data cannot be found on Spotify')
            return {}

        return track_data
