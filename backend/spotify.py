import requests
from urllib.parse import urlencode


def spotify_api(spotify_artist_id):
    CLIENT_ID = '7d9d65e360c9416ab3a37681a5d7ed8e'
    CLIENT_SECRET = '53e9e6ce5431435c8519bb8af86bc137'
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    # POST
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })
    # convert the response to JSON
    auth_response_data = auth_response.json()
    # save the access token
    access_token = auth_response_data['access_token']
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    API_URL = "https://api.spotify.com/v1/"
    end_point = "artists/"
    artist_json = requests.get(f"https://api.spotify.com/v1/artists/{spotify_artist_id}", headers=headers).json()
    artist_albums_json = requests.get(f"https://api.spotify.com/v1/artists/{spotify_artist_id}/albums", headers=headers).json()



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

    return artist_dict
