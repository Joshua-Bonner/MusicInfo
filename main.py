import os
from dotenv import load_dotenv
import SpotifyAPI

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


def main():
    spotify_api = SpotifyAPI.SpotifyAPI()
    access_token = spotify_api.get_authorization_token(CLIENT_ID, CLIENT_SECRET)
    print(access_token)


if __name__ == '__main__':
    main()
