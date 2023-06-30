import requests


# authorises in order to do Spotify API calls
def get_spotify_credentials():
    CLIENT_ID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    CLIENT_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
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
