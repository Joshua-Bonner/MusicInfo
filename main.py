import os
from dotenv import load_dotenv
import SpotifyAPI

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


def main():
    client = SpotifyAPI.SpotifyAPI(CLIENT_ID, CLIENT_SECRET)


if __name__ == '__main__':
    main()
