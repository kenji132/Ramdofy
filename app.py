import os # 環境変数
import datetime
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, flash, redirect, render_template, request, jsonify,session

app = Flask(__name__)

#環境変数の設定
if not os.environ.get("SPOTIPY_USER_NAME_ID"):
    raise RuntimeError("SPOTIPY_USER_NAME_ID not set")
if not os.environ.get("SPOTIPY_CLIENT_ID"):
    raise RuntimeError("SPOTIPY_CLIENT_ID not set")
if not os.environ.get("SPOTIPY_CLIENT_SECRET"):
    raise RuntimeError("SPOTIPY_CLIENT_SECRET not set")
if not os.environ.get("SPOTIPY_REDIRECT_URI"):
    raise RuntimeError("SPOTIPY_REDIRECT_URI not set")
if not os.environ.get("SECRET_KEY"):
    raise RuntimeError("SECRET_KEY not set")
username = os.environ.get("SPOTIPY_USER_NAME_ID")
client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIPY_REDIRECT_URI")
app.secret_key = os.environ.get("SECRET_KEY")

#SpotifyAPIの利用スコープの設定
scope = 'user-library-read user-read-playback-state playlist-read-private user-read-recently-played playlist-read-collaborative playlist-modify-public playlist-modify-private user-follow-modify user-follow-read'

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
spotify = spotipy.Spotify(auth = token)
saved_tracks = spotify.current_user_saved_tracks(limit = 50)
artist = spotify.current_user_followed_artists(limit = 10, after = None)

# ユーザーがフォローしていアーティストを１つの配列にまとめる関数
def take_next_artists(a):
  while True:
    after_num = len(a["artists"]["items"]) - 1
    next_artist = spotify.current_user_followed_artists(limit = 10, after = a["artists"]["items"][after_num]["id"])
    if len(next_artist["artists"]["items"]) < 10:
      for i in range(len(next_artist["artists"]["items"])):
        a["artists"]["items"].append(next_artist["artists"]["items"][i])
      break
    else:
      for i in range(len(next_artist["artists"]["items"])):
        a["artists"]["items"].append(next_artist["artists"]["items"][i])
      take_next_artists(a)
  return a

# artist配列にフォローしているアーティストをまとめた
take_next_artists(artist)

client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)


@app.route('/', methods = ['GET'])
def index():
  return render_template("index.html", followed_artists = artist["artists"]["items"])


@app.route('/relax', methods=['GET', 'POST'])
def relax():
  if request.method == 'POST':
    url_list = []
    data_list = []
    for track in saved_tracks["items"]:
      feature = spotify.audio_features(track["track"]["id"])
      if feature[0]["loudness"] <= -10 and feature[0]["acousticness"] >= 0.5 and feature[0]["instrumentalness"] >= 0.8:
        url_list.append(track["track"]["external_urls"]["spotify"])
        data_list.append(track["track"])
    if len(url_list) == 0:
      flash("条件に当てはまる曲は見つけられませんでした", "failed")
      return render_template("relax.html")
    flash("以下の曲が条件に当てはまりました", "success")
    now = datetime.date.today().strftime("%Y/%m/%d")
    NAME = now + "relax"
    return render_template('confirm.html', data = data_list, url = url_list, name = NAME)
  else:
    return render_template("relax.html")



@app.route('/workout', methods=['GET', 'POST'])
def workout():
  if request.method == 'POST':
    tempo = request.form.get('tempo')
    url_list = []
    data_list = []
    if tempo == '':
      flash("テンポを入力してください","failed")
      return render_template("workout.html")
    elif int(tempo) <= 0:
      flash("テンポは0以上で入力してください","failed")
      return render_template("workout.html")
    for track in saved_tracks["items"]:
      feature = spotify.audio_features(track["track"]["id"])
      if (feature[0]["tempo"] >= (float(tempo) - 5) and feature[0]["tempo"] <= (float(tempo) + 5)) and feature[0]["acousticness"] <= 0.01 and feature[0]["energy"] >= 0.9:
        url_list.append(track["track"]["external_urls"]["spotify"])
        data_list.append(track["track"])
    if len(url_list) == 0:
      flash("条件に当てはまる曲は見つけられませんでした", "failed")
      return render_template("workout.html")
    flash("以下の曲が条件に当てはまりました", "success")
    now = datetime.date.today().strftime("%Y/%m/%d")
    NAME = now + "workout"
    return render_template('confirm.html', data = data_list, url = url_list, name = NAME)
  else:
    return render_template("workout.html")



@app.route('/confirm', methods=['GET','POST'])
def confirm():
  if request.method == 'POST':
    url_list = request.form.getlist('urls')
    flash("以下の曲が条件に当てはまりました", "success")
    playlist_name = request.form.get("playlist_name")
    new_playlist = spotify.user_playlist_create(user = username, name = playlist_name)
    spotify.user_playlist_add_tracks(username, new_playlist["id"], url_list)
    return redirect(new_playlist["external_urls"]["spotify"])
  else:
    return render_template('confirm.html')



@app.route('/favorite', methods=['GET', 'POST'])
def favorite():
  if request.method == 'POST':
    url_list = []
    data_list = []
    sel_artists = request.form.getlist('selected_artists')
    if len(sel_artists) != 3:
      flash("アーティストを3組選んでください", "failed")
      return render_template("favorite.html", followed_artists = artist["artists"]["items"])
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
            url_list.append(track["external_urls"]["spotify"])
            data_list.append(track)
            if cnt == 5:
              break
      flash("以下の曲が条件に当てはまりました", "success")
      now = datetime.date.today().strftime("%Y/%m/%d")
      NAME = now + "new_song"
      return render_template('confirm.html', data = data_list, url = url_list, name = NAME)
  else:
    return render_template("favorite.html", followed_artists = artist["artists"]["items"])

