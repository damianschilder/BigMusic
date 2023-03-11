import requests
from urllib.parse import urlencode

def spotify_caller(query):
    artist_limit = 3
    album_limit = 3


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


    # base URL of all Spotify API endpoints

    API_URL = "https://api.spotify.com/v1/"
    query = {
        "q": query,
        "type": "artist",
        "limit": artist_limit,
    }
    end_point = "search?"
    artist_json = requests.get(f"{API_URL}{end_point}{urlencode(query)}", headers=headers).json()
    
    artist_data = artist_json["artists"]["items"][0]
    artist_name = artist_data["name"]
    artist_id = artist_data["id"]
    #artist_genre = artist_data["genre"]


    artist_json = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}/albums?limit={album_limit}", headers=headers).json()



    albums_list = []
    for item in artist_json["items"]:
        #print(item)
        album_dict = {}
        if item["album_type"] == "album":
            album_dict.update({"Name":item["name"]})
            album_dict.update({"Year":item["release_date"][0:4]})

            albums_list.append(album_dict)

    artist_dict = {}

    artist_dict.update({"artist":({"name":artist_name, "albums":albums_list})})

    return artist_dict, artist_json