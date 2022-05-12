import os
from dotenv import load_dotenv

import SpotifyAPI
from common import APIQueryType

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


def main():
    client = SpotifyAPI.SpotifyAPI(CLIENT_ID, CLIENT_SECRET)
    print(client.search('Time', APIQueryType.TRACK))


if __name__ == '__main__':
    main()
