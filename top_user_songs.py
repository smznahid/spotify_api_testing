import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_creds import CredentialsLoader

cid, secret, redirect_url = CredentialsLoader.get_creds()