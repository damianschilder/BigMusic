
import musicbrainzngs

musicbrainzngs.set_useragent("BigMusic", 1.0)

# updates spotify artist uri to musicbrainz MBID
# example 6olE6TJLqED3rqDCT0FyPh becomes 5b11f4ce-a62d-471e-81fc-a69a8278c7da


def make_spotify_url(spotify_id, spotify_type="artist"):
    spotify_type = 'artist'
    return "https://open.spotify.com/{0}/{1}".format(spotify_type, spotify_id)




def get_artist_mbid(spotify_id):
    spotify_url = make_spotify_url(spotify_id, "artist")
    try:
        mb_url = musicbrainzngs.browse_urls(spotify_url,
                                            includes=["artist-rels"])
    except musicbrainzngs.musicbrainz.ResponseError:
        return "URL doesn't exist."

    if "artist-relation-list" in mb_url["url"]:
        artists = mb_url["url"]["artist-relation-list"]
        if len(artists) == 1:
            return artists[0]["artist"]["id"]
        elif len(artists) > 1:
            return "More than one associated artist."
    else:
        return "No associated artists."


