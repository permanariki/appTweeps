import os
from flask import request, Flask, blueprints
from flask_cors import CORS
from resources.tweeps import tweeps_api


app = Flask(__name__)
CORS(app)
app.register_blueprint(tweeps_api, url_prefix = '/api/v1/')

@app.route('/')
def online():
    return "ONLINE"

if __name__ == '__main__':
    app.run(debug=True, host=os.getenv('HOST'), port=os.getenv('PORT'))