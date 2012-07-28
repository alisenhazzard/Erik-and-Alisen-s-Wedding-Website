# ==============================================================================
# app.py
#   A backend example for the proto demo.  Will serve up data and static pages
#
# ==============================================================================
import flask
import pymongo 
import redis
import json

# ==============================================================================
#
# Setup flask app
#
# ==============================================================================
app = flask.Flask(__name__)

ENV = 'develop'
PORT = 8080

'''
DB_CONNECTION = pymongo.Connection('localhost', 27017)
DB = DB_CONNECTION.vasir_site

#Settings from config
PORT = getattr(settings, 'PORT', 8080)
ENV = getattr(settings, 'ENV', 'develop')

#Get redis connection
redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)
CACHE_PREFIX = 'erikandalisen:'
'''

# ==============================================================================
#
# Static Endpoints
#
# ==============================================================================
def render_skeleton(template_name='index.html', **kwargs):
    '''Base render func, everything get passed through here
    '''
    return flask.render_template(template_name, **kwargs)

@app.route('/')
def index():
    #Get latest posts
    return render_skeleton('home.html') 

@app.route('/our_story/')
def our_story():
    return render_skeleton('our_story.html')

@app.route('/wedding_party/')
def wedding_party():
    return render_skeleton('wedding_party.html')

@app.route('/guest_info/')
def guest_info():
    return render_skeleton('guest_info.html')

@app.route('/registry/')
def registry():
    return render_skeleton('registry.html')

@app.route('/guest_book/')
def guest_book():
    return render_skeleton('guest_book.html')

# ==============================================================================
#
# Run server
#
# ==============================================================================
if __name__ == "__main__":
    if ENV == 'develop':
        app.debug = True
    app.run(port=PORT)
