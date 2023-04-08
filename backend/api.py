from flask import Flask
from flask_restful import Api, Resource, reqparse, request
import requests
import json
from flask_cors import CORS

from data_merger import get_artist_results

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

class MusicBrainz( Resource ):
  def get( self ):
    return 'hoi' 


class Spotify( Resource ):
  def get( self ):
    return {'Endpoint': 'Spotify'}

class Discogs( Resource ):
  def get( self ):
    return {'Endpoint': 'Discogs'}

class LastFM( Resource ):
  def get( self ):
    return {'Endpoint': 'LastFM'}

# Open powershell and try this command:'curl http://127.0.0.1:5000/search/kanye' and you should see 'Kanye West' as a result.
class Search( Resource ):
  def get( self, query ):
    artist_call = get_artist_results('6olE6TJLqED3rqDCT0FyPh')
    return artist_call

api.add_resource( MusicBrainz, '/musicbrainz' )
api.add_resource( Spotify, '/spotify' )
api.add_resource( Discogs, '/discogs' )
api.add_resource( Search, '/search/<query>' )
api.add_resource( LastFM, '/lastfm' )



if __name__ == '__main__':
    app.run(debug= True, threaded= True)