import requests
import json


def musicbrainz_caller(query):
    artist_limit = 3
    album_limit = 5
    artist_search = requests.get(f'https://musicbrainz.org/ws/2/artist?query={query}&limit={artist_limit}&fmt=json')
    # retrieve text from JSON
    artist_json = json.loads(artist_search.text)

    # select first artist
    artist_data = artist_json["artists"][0]
    artist_name = artist_data["name"]
    artist_id = artist_data["id"]


    album_search = requests.get(f'https://musicbrainz.org/ws/2/artist/{artist_id}?inc=release-groups&fmt=json')
    album_json = json.loads(album_search.text)
    album_data = album_json["release-groups"]

    albums_list = []
    for item in album_data[0:album_limit]:
        album_dict = {}
        if item["primary-type"] == "Album":
            album_dict.update({"Name":item["title"]})
            album_dict.update({"Year":item["first-release-date"][0:4]})
            albums_list.append(album_dict)


    artist_dict = {}

    artist_dict.update({"artist":({"name":artist_name, "albums":albums_list})})

    return artist_dict

