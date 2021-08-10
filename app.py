import os # 環境変数
import datetime
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, flash, redirect, render_template, request, jsonify


if not os.environ.get("SPOTIPY_USER_NAME_ID"):
    raise RuntimeError("SPOTIPY_USER_NAME_ID not set")
if not os.environ.get("SPOTIPY_CLIENT_ID"):
    raise RuntimeError("SPOTIPY_CLIENT_ID not set")
if not os.environ.get("SPOTIPY_CLIENT_SECRET"):
    raise RuntimeError("SPOTIPY_CLIENT_SECRET not set")
if not os.environ.get("SPOTIPY_REDIRECT_URI"):
    raise RuntimeError("SPOTIPY_REDIRECT_URI not set")
username = os.environ.get("SPOTIPY_USER_NAME_ID")
client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIPY_REDIRECT_URI")


scope = 'user-library-read user-read-playback-state playlist-read-private user-read-recently-played playlist-read-collaborative playlist-modify-public playlist-modify-private user-follow-modify user-follow-read'

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
spotify = spotipy.Spotify(auth = token)
saved_tracks = spotify.current_user_saved_tracks(limit = 50)
artist = spotify.current_user_followed_artists(limit = 10, after = None)

def take_next_artists(a):
  while True:
    after_num = len(a["artists"]["items"]) - 1
    next_artist = spotify.current_user_followed_artists(limit = 10, after = a["artists"]["items"][after_num]["id"])
    if len(next_artist) < 10:
      for i in range(len(next_artist["artists"]["items"])):
        artist["artists"]["items"].append(next_artist["artists"]["items"][i])
      break
    else:
      for i in range(len(next_artist["artists"]["items"])):
        artist["artists"]["items"].update(next_artist["artists"]["items"][i])
      take_next_artists(next_artist)
  return artist

take_next_artists(artist)

client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)

  # after_num = len(artist["artists"]["items"]) - 1
  # next_artist = spotify.current_user_followed_artists(limit = 10, after = artist["artists"]["items"][len(artist["artists"]["items"]) - 1]["id"])
  # if len(next_artist) == 0:
  #   break
  # else:
  #   artist["artists"]["items"].append(next_artist["artists"]["items"])
  #   take_next_artists(next_artist)

# artist2 = spotify.current_user_followed_artists(limit = 10, after = artist["artists"]["items"][len(artist["artists"]["items"]) - 1]["id"])
# artist["artists"]["items"].append(artist2["artists"]["items"])
# artist3 = spotify.current_user_followed_artists(limit = 10, after = artist2["artists"]["items"][len(artist2["artists"]["items"]) - 1]["id"])
# artist["artists"]["items"].append(artist3["artists"]["items"])
# artist4 = spotify.current_user_followed_artists(limit = 10, after = artist3["artists"]["items"][len(artist3["artists"]["items"]) - 1]["id"])

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
  # return jsonify(artist["artists"]["items"])
  # if request.method == 'POST':
  #   sel_artists = request.form.getlist('selected_artists')
  #   print(sel_artists)
  #   return render_template("index.html", followed_artists = artist["artists"]["items"])
  # else:
  return render_template("index.html", followed_artists = artist["artists"]["items"])


@app.route('/relax')
def relax():
  now = datetime.date.today().strftime("%y%y/%m/%d")
  new_playlist = spotify.user_playlist_create(user = username, name = now + "relax")
  url_list = []
  for track in saved_tracks["items"]:
    feature = spotify.audio_features(track["track"]["id"])
    if feature[0]["loudness"] <= -10 and feature[0]["acousticness"] >= 0.5 and feature[0]["instrumentalness"] >= 0.8:
      url_list.append(track["track"]["external_urls"]["spotify"])
  spotify.user_playlist_add_tracks(username, new_playlist["id"], url_list)
  return redirect("/")

@app.route('/workout')
def workout():
  now = datetime.date.today().strftime("%y%y/%m/%d")
  new_playlist = spotify.user_playlist_create(user = username, name = now + "workout")
  url_list = []
  for track in saved_tracks["items"]:
    feature = spotify.audio_features(track["track"]["id"])
    if feature[0]["tempo"] >= 160 and feature[0]["acousticness"] <= 0.01 and feature[0]["energy"] >= 0.9:
      url_list.append(track["track"]["external_urls"]["spotify"])
  spotify.user_playlist_add_tracks(username, new_playlist["id"], url_list)
  return redirect(new_playlist["external_urls"]["spotify"])

@app.route('/favorite', methods=['GET', 'POST'])
def favorite():
  if request.method == 'POST':
    now = datetime.date.today().strftime("%y%y/%m/%d")
    new_playlist = spotify.user_playlist_create(user = username, name = now + "new_song")
    url_list = []
    sel_artists = request.form.getlist('selected_artists')
    print(sel_artists)
    if len(sel_artists) != 3:
      flash("アーティストを3組選んでください")
      redirect("/favorite")
    else:
      for id in sel_artists:
        result = spotify.artist_related_artists(id)
        arts = result["artists"]
        artist_cnt = 0
        for a in arts:
          artist_cnt += 1
          unique_id = a["id"]
          top_tracks = spotify.artist_top_tracks(unique_id)
          cnt = 0
          if artist_cnt == 3: 
            break
          for track in top_tracks["tracks"]:
            cnt += 1
            # print(track["name"])
            url_list.append(track["external_urls"]["spotify"])
            if cnt == 5:
              break
        # artist1 = result["artists"][0]
        # print(result["artists"])
        # name = artist1["name"]
        # print()
        # unique_id = artist1["id"]
        # top_tracks = spotify.artist_top_tracks(unique_id)
        # cnt = 0
        # for track in top_tracks["tracks"]:
        #   cnt += 1
        #   # print(track["name"])
        #   url_list.append(track["external_urls"]["spotify"])
        #   if cnt == 5:
        #     break

      # print(url_list)
      spotify.user_playlist_add_tracks(username, new_playlist["id"], url_list)

    return redirect(new_playlist["external_urls"]["spotify"])
  else:
    # return jsonify(artist["artists"]["items"])
    return render_template("favorite.html", followed_artists = artist["artists"]["items"])



  # lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
  # cl_uri = 'spotify:artist:0A7d0PJxaLO7CGI94ht6PX'
  # usao_uri = 'spotify:artist:25iPl8VJFDu38JMFF6uMXI'


  if list_type == "relax":
    url_list = []
    for track in saved_tracks["items"]:
      feature = spotify.audio_features(track["track"]["id"])
      if feature[0]["loudness"] <= -10 and feature[0]["acousticness"] >= 0.5 and feature[0]["instrumentalness"] >= 0.8:
        url_list.append(track["track"]["external_urls"]["spotify"])
  #       # spotify.user_playlist_add_tracks(user = username, playlist_id = new_playlist["id"], tracks = track["track"]["id"])
  #       # return jsonify(track['track'])
  # elif list_type == "workout":
  #   url_list = []
  #   for track in saved_tracks["items"]:
  #     feature = spotify.audio_features(track["track"]["id"])
  #     if feature[0]["tempo"] >= 160 and feature[0]["acousticness"] <= 0.01 and feature[0]["energy"] >= 0.9:
  #       print(track['track']['name'])

        
    # print('energy    : ')
    # print(feature[0]["energy"])
    # print(feature[0]["mode"])
    # print('loudness    : ')
    # print(feature[0]["loudness"])
    # print('mode    : ')
    # print(feature[0]["mode"])
    # print('acousticness    : ')
    # print(feature[0]["acousticness"])
    # print('instrumentalness    : ')
    # print(feature[0]["instrumentalness"])
    # print('liveness    : ')
    # print(feature[0]["liveness"])
    # print('valence    : ')
    # print(feature[0]["valence"])
    # print('tempo   : ')
    # print(feature[0]["tempo"])
    # print()

  # spotify.user_playlist_add_tracks(username, new_playlist["id"], url_list)

  
  # spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

  # return jsonify(new_playlist["id"])


  # return jsonify(saved_tracks["items"])
  
  
# for track in results['tracks'][:10]:
#     print('track    : ')
# print(track['name'])
#     print('audio    : ')
# print(track['preview_url'])
#     print('cover art: ')
# print(track['album']['images'][0]['url'])
#     print()