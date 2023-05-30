import requests
import json
import re
from spotify_auth import get_spotify_credentials

# creates dictionary of album content for specific album

def get_album_content(id):


    musicbrainz_regex_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    if re.match(musicbrainz_regex_pattern, id):

        release_group_content_raw = requests.get(f'https://musicbrainz.org/ws/2/release-group/{id}?inc=artists+releases&fmt=json')
        release_group_content_json = json.loads(release_group_content_raw.text)
        release_id = release_group_content_json['releases'][0]['id']

        release_content_raw = requests.get(f'https://musicbrainz.org/ws/2/release/{release_id}?inc=recordings&fmt=json')
        release_content_json = json.loads(release_content_raw.text)



        release_dict = {}
        release_dict.update({"name":release_content_json["title"]})
        release_dict.update({"release_date":release_content_json["date"][0:4]})


        songs_list = []
        songs_dict = {}
        for item in release_content_json['media'][0]['tracks']:
            temp_dict = {}
            temp_dict.update({"position":item["position"]})
            temp_dict.update({"name":item["title"]})
            temp_dict.update({"length":item["length"]})
            temp_dict.update({"musicbrainz_uri":item["id"]})
            songs_list.append(temp_dict)

        release_dict.update({"songs":songs_list})


    elif 'spotify:album' in id:
        # get spotify album id
        # example spotify:album:4MRXGUCB89CliYc7YWICI0 becomes 4MRXGUCB89CliYc7YWICI0
        album_id = id.split(":")[-1]

        headers = get_spotify_credentials()
        album_content = requests.get(f"https://api.spotify.com/v1/albums/{album_id}", headers=headers).json()



        release_dict = {}
        release_dict.update({"name":album_content['name']})
        release_dict.update({"release_date":album_content['release_date'][0:4]})
        release_dict.update({"image":album_content["images"][0]})


        songs_list = []


        for item in album_content['tracks']['items']:
            print()

            temp_dict = {}
            temp_dict.update({"position":item["track_number"]})
            temp_dict.update({"name":item['name']})
            temp_dict.update({"length":item["duration_ms"]})
            temp_dict.update({"spotify_uri":item["id"]})
            songs_list.append(temp_dict)

        release_dict.update({"songs":songs_list})


    return release_dict

