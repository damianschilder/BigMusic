import requests
import json

def uri_converter(spotify_artist_name, music_platform):
    
    if music_platform == "musicbrainz":
        artist_search = requests.get(f'https://musicbrainz.org/ws/2/artist?query={spotify_artist_name}&limit={5}&fmt=json')
        
        # retrieve text from JSON
        artist_json = json.loads(artist_search.text)

        # select first artist
        artist_data = artist_json["artists"][0]
        artist_id = artist_data["id"]

        return artist_id