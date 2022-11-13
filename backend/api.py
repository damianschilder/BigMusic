from flask import Flask
from flask_restful import Api, Resource, reqparse, request
import requests
import json

app = Flask(__name__)
api = Api(app)

class MusicBrainz( Resource ):
  def get( self ):
    return {'Endpoint': 'musicbrainz'}


class Spotify( Resource ):
  def get( self ):
    return {'Endpoint': 'Spotify'}


class Discogs( Resource ):
  def get( self ):
    return {'Endpoint': 'Discogs'}

# Open powershell and try this command:'curl http://127.0.0.1:5000/search/kanye' and you should see 'Kanye West' as a result.
class Search( Resource ):
  def get( self, query ):
    url = f'https://musicbrainz.org/ws/2/artist?query={ query }&limit=1&fmt=json'
    r = requests.get( url )

    data = json.loads(r.content.decode('utf-8'))
    print(data)
    return [ data['artists'][0]['name'], data['artists'][0]['id']]

api.add_resource( MusicBrainz, '/musicbrainz' )
api.add_resource( Spotify, '/spotify' )
api.add_resource( Discogs, '/discogs' )
api.add_resource( Search, '/search/<query>' )



if __name__ == '__main__':
    app.run(debug=True)