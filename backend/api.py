from flask import Flask
from flask_restful import Api, Resource, reqparse, request
import requests
import json
from flask_cors import CORS

from data_merger import get_artist_results
from album_content import get_album_content


app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

class Album( Resource ):
  def get( self, album ):
    response = get_album_content( album )
    return response

class Artist( Resource ):
  def get( self, artist ):
    response = get_artist_results( artist )
    return response
  
api.add_resource( Album, '/album/<album>' )
api.add_resource( Artist, '/artist/<artist>' )


if __name__ == '__main__':
    app.run(debug= True, threaded= True)