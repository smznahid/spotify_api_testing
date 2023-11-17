import json
from spotipy.oauth2 import SpotifyClientCredentials


class CredentialsLoader:

    @staticmethod
    def get_creds():
        with open('credentials.json', 'r') as file:
            creds = json.load(file)
    
        cid = creds['client_id']
        secret = creds['client_secret']
        redirect_URI = creds['redirect_URI']

        return cid, secret, redirect_URI