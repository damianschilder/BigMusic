## test call to get image of artist
import requests
from urllib.parse import urlencode
from spotify_auth import get_spotify_credentials

spotify_artist_id = "6olE6TJLqED3rqDCT0FyPh"

headers = get_spotify_credentials()
artist_json = requests.get(f"https://api.spotify.com/v1/artists/{spotify_artist_id}", headers=headers).json()
artist_albums_json = requests.get(f"https://api.spotify.com/v1/artists/{spotify_artist_id}/albums?limit=50", headers=headers).json()


artist_dict = {}
artist_dict.update({"name":artist_json["images"][0]})
print(artist_dict)