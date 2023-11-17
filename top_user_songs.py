import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_creds import CredentialsLoader


scope = "user-top-read"
cid, secret, redirect_url = CredentialsLoader.get_creds()

client_creds_manager = SpotifyClientCredentials(cid, secret)

sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(client_id=cid,
                                                              client_secret=secret,
                                                              redirect_uri=redirect_url,
                                                              scope=scope))


top_songs_dict = sp.current_user_top_tracks(limit=5)
       
# ['items'][i]['album']['external_urls']['spotify'] -> gets song URL

# ['items'][i]['album']['artists'][0]['name'] -> gets name
# ['items'][i]['name'] -> gets song name (album name)
for i in range(5):
    curr_artist = top_songs_dict['items'][i]['album']['artists'][0]['name']
    curr_url = top_songs_dict['items'][i]['album']['external_urls']['spotify']
    curr_song = top_songs_dict['items'][i]['name']
    print(f"Number {i+1}. Artist: {curr_artist}, \n Number {i+1} Song: {curr_song}, \n Number {i+1}. song url: {curr_url} \n\n")