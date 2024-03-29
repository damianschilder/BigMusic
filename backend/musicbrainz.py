import requests
import json
from spotify2mb import get_artist_mbid


# creates artist dictionary from Musicbrainz

def musicbrainz_api(spotify_artist_id):
    # convert Spotify artist URI to Musicbrainz artist Identifier
    artist_id = get_artist_mbid(spotify_artist_id)

    album_search_raw = requests.get(f'https://musicbrainz.org/ws/2/artist/{artist_id}?inc=release-groups&fmt=json')
    artist_albums_json = json.loads(album_search_raw.text)

    # album dictionary creator
    album_list = []
    for item in artist_albums_json["release-groups"]:
        temp_dict = {}
        # only include albums that have a release date
        if item["primary-type"] == "Album" and item["first-release-date"]:
            temp_dict.update({"name":item["title"]})
            temp_dict.update({"release_date":item["first-release-date"]})
            # not supported by Musicbrainz
            temp_dict.update({"amount_songs":None})
            temp_dict.update({"musicbrainz_uri":item["id"]})
            # not supported by Musicbrainz
            temp_dict.update({"image":None})
            album_list.append(temp_dict)


    return album_list