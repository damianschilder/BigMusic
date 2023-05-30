import requests
def lastfm_api(musicbrainz_album_id):
    LF_API_KEY = "b8479fa415d359aaf7e74143adfff0e7"
    #LFalbum = "I never liked you"
    #LFartist = "Future"
    LFlanguage = "en"
    musicbrainz_album_id = "a885cfae-1025-344c-8326-dea2094b2683"

    #url = f"http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={LF_API_KEY}&artist={LFartist}&album={LFalbum}&lang={LFlanguage}&format=json"
    url = f"http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={LF_API_KEY}&mbid={musicbrainz_album_id}&lang={LFlanguage}&format=json"
    response = requests.get(url)

    data = response.json()
    LFbio_text = data["album"]["wiki"]
    #LFbio = data["album"]["wiki"]["summary"] Te korte text.
    print(LFbio_text)
    return LFbio_text


lastfm_api('a885cfae-1025-344c-8326-dea2094b2683')