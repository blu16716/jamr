# from google.appengine.ext import ndb
# import jinja2
# import os
# import webapp2
# import urllib2
# import json
# import urllib
# import spotipy
# import sys
# import spotipy.util as util
#
# class loginHandler(webabb2.RequestHandler):
#     def get(self):
#         scope = 'user-library-read'
#
#         if len(sys.argv) > 1:
#             username = sys.argv[1]
#         else:
#             print "Usage: %s username" % (sys.argv[0],)
#             sys.exit()
#
#         token = util.prompt_for_user_token(username, scope)
#
#         if token:
#             sp = spotipy.Spotify(auth=token)
#             results = sp.current_user_saved_tracks()
#             for item in results['items']:
#                 track = item['track']
#                 print track['name'] + ' - ' + track['artists'][0]['name']
#         else:
#             print "Can't get token for", username