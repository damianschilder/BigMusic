from musicbrainz import musicbrainz_api
from spotify import spotify_api

#spotify_artist_id = '6liAMWkVf5LH7YR9yfFy1Y'

def get_artist_results(spotify_artist_id):
    spotify_artist_dict = spotify_api(spotify_artist_id)
    spotify_albums_list = spotify_artist_dict["albums"]

    musicbrainz_albums_list = musicbrainz_api(spotify_artist_id)


    # deduplicate spotify results
    # spotify_album_list_noduplicates uses same format as spotify_albums_list
    spotify_album_list_noduplicates = []
    seen = set()
    for item in spotify_albums_list:
        album_identifiers = (item["name"],item["release_date"][:4])
        if album_identifiers not in seen:
            seen.add(album_identifiers)
            spotify_album_list_noduplicates.append(item)


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
        spotify_albums_identifier_list.append(current_dict)


    # combine full spotify results and unique musicbrainz results
    combined_albums = spotify_album_list_noduplicates + musicbrainz_unique_albums_list

    # sort album list based on year
    sorted_albums = sorted(combined_albums, key=lambda x: x['release_date'][:4])


    # create new dict for artist and replace albums list with remade albums list
    artist_dict = spotify_artist_dict

    spotify_artist_dict.update({"albums":sorted_albums})
    
    return artist_dict
