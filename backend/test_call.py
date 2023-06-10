from data_merger import get_artist_results
from album_content import get_album_content

# example artist call
artist_call = get_artist_results('6olE6TJLqED3rqDCT0FyPh')
print(artist_call)

# example album call using Spotify album URI
album_content = get_album_content('spotify:album:1KVGLuPtrMrLlyy4Je6df7')
print(album_content)

# example album call using MBID
album_content = get_album_content('f1afec0b-26dd-3db5-9aa1-c91229a74a24')
print(album_content)
