from musicbrainz import musicbrainz_api
from spotify import spotify_api
# from lastfm import lastfm_api
# TODO implement lastfm with albums instead of release groups
import datetime
import re
import pytz



# convert yyyy-mm-dd or yyyy to utx unix timestamp
def unix_time(artist_dict):
    full_date_pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
    year_date_pattern = re.compile(r"\d{4}")

    for album in artist_dict['albums']:
        release_date = album.get('release_date')
        if release_date and full_date_pattern.match(release_date):
            # Convert release_date to Unix timestamp
            utc_timestamp = datetime.datetime.strptime(release_date, "%Y-%m-%d").replace(tzinfo=pytz.UTC)
            unix_timestamp = int(utc_timestamp.timestamp())
            album['release_date'] = unix_timestamp
        elif year_date_pattern.match(release_date):
            utc_timestamp = datetime.datetime.strptime(release_date, "%Y").replace(tzinfo=pytz.UTC)
            unix_timestamp = int(utc_timestamp.timestamp())
            album['release_date'] = unix_timestamp
        else:
            album['release_date'] = None
    
    return artist_dict


# adds relevance score on specified metrics
def weight_function(artist_dict):
    for album in artist_dict['albums']:
        weight = 0

        if album.get('amount_songs'):
            weight += album['amount_songs'] * 0.01

        if 'spotify_uri' in album:
            weight += 1

        if 'musicbrainz_uri' in album:
            weight += 1

        if 'image' in album:
            weight += 2
        
        # release_date = yyyy-mm-dd
        if len(album.get('release_date')) == 10:
            weight += 1
        # release_date = yyyy
        elif len(album.get('release_date')) == 4:
            weight += 0.5
    
        album['relevance_score'] = weight

    return artist_dict



def get_artist_results(spotify_artist_id):
    spotify_artist_dict = spotify_api(spotify_artist_id)
    spotify_albums_list = spotify_artist_dict["albums"]

    musicbrainz_albums_list = musicbrainz_api(spotify_artist_id)
    #print(spotify_albums_list)

    # deduplicate spotify results
    # spotify_album_list_noduplicates uses same format as spotify_albums_list
    spotify_album_list_noduplicates = []
    seen = set()
    for item in spotify_albums_list:
        album_identifiers = (item["name"],item["release_date"][:4])
        if album_identifiers not in seen:
            seen.add(album_identifiers)
        spotify_album_list_noduplicates.append(item)

    # create identifier list with for each value dictionary with values name and year
    spotify_albums_identifier_list = []
    for item in spotify_album_list_noduplicates:
        current_dict = {}
        current_dict.update({"name":item["name"]})
        current_dict.update({"release_date":item["release_date"][:4]})
        spotify_albums_identifier_list.append(current_dict)

    # get unique musicbrainz results
    musicbrainz_unique_albums_list = []
    for item in musicbrainz_albums_list:
        current_dict = {}
        current_dict.update({"name":item["name"]})
        current_dict.update({"release_date":item["release_date"][:4]}) 
        if not current_dict in spotify_albums_identifier_list:
            musicbrainz_unique_albums_list.append(item)
        # just add musicbrainz uri
        else:
            current_dict.update({"musicbrainz_uri": item["musicbrainz_uri"]})
            album = next((album for album in spotify_album_list_noduplicates if album['release_date'] == item["release_date"] and album['name'] == item["name"]), None)
            if album:
                album.update({'musicbrainz_uri': item["musicbrainz_uri"]})
        spotify_albums_identifier_list.append(current_dict)


    # combine full spotify results and unique musicbrainz results
    combined_albums = spotify_album_list_noduplicates + musicbrainz_unique_albums_list

    # sort album list based on year
    sorted_albums = sorted(combined_albums, key=lambda x: x['release_date'][:4])


    # create new dict for artist and replace albums list with remade albums list
    artist_dict = spotify_artist_dict

    # update albums based on sorted albums
    artist_dict.update({"albums":sorted_albums})

    # adds relevance score on specified metrics to key 'relevance_score' in each album
    artist_dict = weight_function(artist_dict)

    # update time to unix
    artist_dict = unix_time(artist_dict)


    return artist_dict
