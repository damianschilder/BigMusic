from spotify import spotify_caller
from musicbrainz import musicbrainz_caller


query = "Nirvana"

# get JSON
spotify_results = spotify_caller(query)
musicbrainz_results = musicbrainz_caller(query)

#print(f"Spotify results: {spotify_results}")
#print(f"Musicbrainz results: {musicbrainz_results}\n")

# combine album results
spotify_albums = spotify_results["artist"]["albums"]
musicbrainz_albums = musicbrainz_results["artist"]["albums"]
combined_albums = spotify_albums + musicbrainz_albums



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


# creates new dictionary with spotify results as basis
final_response = spotify_results
final_response.update({"artist":({"albums":sorted_albums})})

print(f"FINAL RESPONSE {final_response}")



##################################
# check for unique values
spotify_list = []
for item in spotify_albums:
    spotify_list.append(str(item))

musicbrainz_list = []
for item in musicbrainz_albums:
    musicbrainz_list.append(str(item)) 
#print(f"Musicbrainz list {musicbrainz_list}")



print(f"\nUnique values in Spotify: {list(set(spotify_list) - set(musicbrainz_list))}")
print(f"\nUnique values in Musicbrainz: {list(set(musicbrainz_list) - set(spotify_list))}")
##################################

