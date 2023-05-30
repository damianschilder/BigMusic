from data_merger import get_artist_results
from album_content import get_album_content

# Nirvana call from spotify artist uri
#artist_call = get_artist_results('6olE6TJLqED3rqDCT0FyPh')
#print(artist_call)
#print("\n\n\n\n\n")


#artist_call = get_artist_results('4tZwfgrHOc3mvqYlEYSvVi')
#print(artist_call)
#print("\n")


#artist_call = get_artist_results('1DXylZlWbVvlckNqwvjTEt')
#print(artist_call)




# example spotify album call
album_content = get_album_content('spotify:album:6yaiubHHJy8N8QcHy3julo')
#album_content = get_album_content(artist_call['albums'][1]['spotify_uri'])

#print(album_content)
#print("\n\n\n\n\n\n\n\n\n\n\n\n\n")

# example musicbrainz album call
#album_content = get_album_content('f1afec0b-26dd-3db5-9aa1-c91229a74a24')
#album_content = get_album_content(artist_call['albums'][0]['musicbrainz_uri'])

#print(album_content)

# 

# Neutral Milk Hotel call
#print(get_artist_results('2ooIqOf4X2uz4mMptXCtie'))

# John Williams (gitarist)
#print(get_artist_results('6mBYeMZZUhJKEvRXagJYzY'))
