from spotify import spotify_caller
from musicbrainz import musicbrainz_caller


query = "Portishead"

# get JSON

spotify_return = spotify_caller(query)

spotify_results = spotify_return[0]
spotify_album_data = spotify_return[1]
musicbrainz_results = musicbrainz_caller(query)

#print(f"Spotify results: {spotify_results}")
#print(f"Musicbrainz results: {musicbrainz_results}\n")

# combine album results
spotify_albums = spotify_results["artist"]["albums"]
musicbrainz_albums = musicbrainz_results["artist"]["albums"]
combined_albums = spotify_albums + musicbrainz_albums

#print(combined_albums)

# remove duplicate albums
seen = set()
duplicates_removed = []
for d in combined_albums:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        duplicates_removed.append(d)

# sort based on year
sorted_albums = sorted(duplicates_removed, key=lambda x: x['Year'])



# update albums
spotify_results["artist"]["albums"] = sorted_albums
#print(spotify_results)

##################################
# check for unique values
spotify_list = []
for item in spotify_albums:
    spotify_list.append(str(item))


print(spotify_list)

musicbrainz_list = []
for item in musicbrainz_albums:
    musicbrainz_list.append(str(item)) 

unique_spotify = list(set(spotify_list) - set(musicbrainz_list))
print(f"\nUnique values in Spotify: {list(set(spotify_list) - set(musicbrainz_list))}")
print(f"\nUnique values in Musicbrainz: {list(set(musicbrainz_list) - set(spotify_list))}")


##################################
spotify_albums_results = []
for item in spotify_album_data["items"]:
    name = item["name"]
    year = item["release_date"][0:4]
    for album in list(spotify_list):
        print(album)


print(spotify_albums_results)
