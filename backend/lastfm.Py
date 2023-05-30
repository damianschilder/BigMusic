import requests
def lastfm_api(musicbrainz_album_id):
    LF_API_KEY = "b8479fa415d359aaf7e74143adfff0e7"

    LFlanguage = "en"
    #musicbrainz_album_id = "a885cfae-1025-344c-8326-dea2094b2683"


    url = f"http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={LF_API_KEY}&mbid={musicbrainz_album_id}&lang={LFlanguage}&format=json"
    response = requests.get(url)

    data = response.json()
    LFbio_text = data["album"]["wiki"]
    return LFbio_text['summary']


print(lastfm_api('a885cfae-1025-344c-8326-dea2094b2683'))