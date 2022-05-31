import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 
import pandas as pd 
import time 

#connect to Spotify's API 
client_id = ' ' 
client_secret = ' '

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret) 
sp = spotipy.spotify(client_crednetials_manager = client_credentials_manager) 

#get track ids from 
def get_track_ids(user, playlist_id): 
    id = []
    play_list = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']: 
        track = item['track']
        id.append(track['id'])

    return id 

#create a function to grab all track information from track ids
def get_features(id): 
    meta = sp.track(id)
    features = sp.audio_features(id) 

    #meta data 
    name = meta['name'] 
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity'] 

    #features from the data 
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness'] 
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, release_date, length, popularity, acousticness, danceability,
            energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    return track    

#loop over track ids 
tracks = [] 
for i in range(len(ids)): 
    time.sleep(1)
    track = getTrackFeatures(ids[i])
    tracks.append(track)

#create a pandas df 
#save to a csv file- optional 
df = pd.DataFram(tracks, colums = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'acousticness', 'danceability',
    'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df.to_csv("spotify.csv", sep =',')

#convert release_date to a DateTime format 
df['release_date'] = 
pd.to_datetime(df['release_date'], format ='%Y-%m-%d') 

