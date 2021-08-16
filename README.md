# Ramdofy
This is CS50's final project.
#### 説明
SpotifyのWebAPIを用いて、自身のSpotifyアカウントでお気に入りに登録している曲やフォローしているアーティストの情報をもとに、今の気分にあったプレイリストを自動で作成するWebアプリです。
また、Spotify APIには、AudioFeaturesObjectという曲の特徴を示す数値をJSONとして出力する機能があり、その数値も参考にしてプレイリストを作ります。<br>
リラックスしたい時(Relax)、運動をしたい時(Workout)、自分の知らない新しいアーティストの音楽を聴きたい時(Favorite)の3種類のプレイリストを自動作成できます。


#### 使用技術
バックエンド: Python,Flask<br>
フロントエンド: Tailwind CSS

#### How to use
1. `git clone https://github.com/kenji132/Ramdofy.git`を実行する
2. TailwindCSSのmain.cssをsrc/cssに配置する
3. 自身のspotifyのSPOTIPY_USER_NAME_ID、SPOTIPY_CLIENT_ID、SPOTIPY_CLIENT_SECRET、SPOTIFY_REDIRECT_URLとターミナルでランダムに作成したSECRET_KEYをexport文を用いてターミナルに打ち込む。<br>
(例)<br>
`export SPOTIPY_USER_NAME_ID='aaaaaaaaaaaa'`<br>
`export SPOTIPY_CLIENT_ID='aaaaaaaaaaa'`<br>
`export SPOTIPY_CLIENT_SECRET='aaaaaaaaaaaaa'`<br>
`export SPOTIPY_REDIRECT_URI='aaaaaaaaaaaaaa'`<br>
`export SECRET_KEY='aaaaaaaaaaaaaaaaaaaaaaaaaaa'`<br>
4. flask runを実行し、http://127.0.0.1:5000/ にアクセスしてください。
5. Welcome to Ramdofy!!!
