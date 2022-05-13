import json
import os
from dotenv import load_dotenv

import SpotifyAPI

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


def main():
    client = SpotifyAPI.SpotifyAPI(CLIENT_ID, CLIENT_SECRET)
    data = client.get_artist_info('Jess Glynne')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
