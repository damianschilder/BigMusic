import requests



def get_spotify_credentials():
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

    return headers