import requests
from urllib.parse import urlencode
from spotify_auth import get_spotify_credentials


# creates artist dictionary from Spotify

def spotify_api(spotify_artist_id):
    headers = get_spotify_credentials()

    artist_json = requests.get(f"https://api.spotify.com/v1/artists/{spotify_artist_id}", headers=headers).json()
    artist_albums_json = requests.get(f"https://api.spotify.com/v1/artists/{spotify_artist_id}/albums?limit=50", headers=headers).json()
    #print(artist_albums_json)


    # album dictionary creator
    album_list = []
    for item in artist_albums_json["items"]:
        temp_dict = {}
        if item["album_group"] == "album":
            temp_dict.update({"name":item["name"]})
            temp_dict.update({"release_date":item["release_date"]})
            temp_dict.update({"amount_songs":item["total_tracks"]})
            temp_dict.update({"spotify_uri":item["uri"]})
            temp_dict.update({"spotify_url":item["external_urls"]})
            temp_dict.update({"image":item["images"][0]})
            album_list.append(temp_dict)


    artist_dict = {}
    artist_dict.update({"name":artist_json["name"]})
    artist_dict.update({"genres":artist_json["genres"]})
    artist_dict.update({"popularity":artist_json["popularity"]})
    artist_dict.update({"albums":album_list})

    #print(artist_dict)

    return artist_dict
