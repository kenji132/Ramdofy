# Ramdofy
This is CS50's final project.
#### Video Demo: 
https://youtu.be/HHHyoYSWX_k
#### Description:
It is a web application that uses Spotify's Web API to automatically create a playlist that suits your mood based on the information of songs registered as favorites in your Spotify account and the artists you follow. In addition, the Spotify API has a function called AudioFeaturesObject that outputs a numerical value indicating the characteristics of the song as JSON, and creates a playlist with reference to that numerical value.
You can automatically create three types of playlists: when you want to relax (Relax), when you want to exercise (Workout), and when you want to listen to music from a new artist you don't know (Favorite).

#### Technologies used:<br>
Backend: Python,Flask,other small libraries or packages<br>
Frontend: Tailwind CSS

##### Pages<br>
・index<br>
・relax<br>
・workout<br>
・favorite<br>
・confirm

You can open the index page by accessing /. Press the Relax button on the index page to redirect to /relax, and press the Select button to redirect to /confirm to create the perfect playlist when you want to relax.<br>
Similarly, pressing the Workout button on the index page redirects to /workout, entering the tempo, and pressing the select button redirects to /confirm, creating the perfect playlist when you want to exercise with a song that is close to the tempo you entered.<br>
Finally, when you press the Favorite button on the index page, you will be redirected to /favorite and the artists you are following will be displayed, so if you select 3 groups that suit your mood from the displayed artists, /confirm It redirects to and automatically puts songs of artists similar to the selected artist into a playlist.<br>


#### How to launch this application
1. `git clone https://github.com/kenji132/Ramdofy.git`
2. Download TailwindCSS
3. Export Your spotify's SPOTIPY_USER_NAME_ID、SPOTIPY_CLIENT_ID、SPOTIPY_CLIENT_SECRET、SPOTIFY_REDIRECT_URL and SECRET_KEY<br>
(example)<br>
`export SPOTIPY_USER_NAME_ID='aaaaaaaaaaaa'`<br>
`export SPOTIPY_CLIENT_ID='aaaaaaaaaaa'`<br>
`export SPOTIPY_CLIENT_SECRET='aaaaaaaaaaaaa'`<br>
`export SPOTIPY_REDIRECT_URI='aaaaaaaaaaaaaa'`<br>
`export SECRET_KEY='aaaaaaaaaaaaaaaaaaaaaaaaaaa'`<br>
4. flask run and access http://127.0.0.1:5000/ 
5. Welcome to Ramdofy!!!

## 日本語ver
#### ビデオ デモ: 
https://youtu.be/HHHyoYSWX_k

#### 説明:
SpotifyのWebAPIを用いて、自身のSpotifyアカウントでお気に入りに登録している曲やフォローしているアーティストの情報をもとに、今の気分にあったプレイリストを自動で作成するWebアプリです。
また、Spotify APIには、AudioFeaturesObjectという曲の特徴を示す数値をJSONとして出力する機能があり、その数値も参考にしてプレイリストを作ります。<br>
リラックスしたい時(Relax)、運動をしたい時(Workout)、自分の知らない新しいアーティストの音楽を聴きたい時(Favorite)の3種類のプレイリストを自動作成できます。

#### 使用技術<br>
Backend: Python,Flask,other small libraries or packages<br>
Frontend: Tailwind CSS

##### 画面<br>
・index<br>
・relax<br>
・workout<br>
・favorite<br>
・confirm

/にアクセスすれば、indexページを開くことができます。indexページのRelaxボタンを押すと/relaxにリダイレクトし、選ぶボタンを押すと/confirmにリダイレクトし、リラックスしたいときにぴったりなプレイリストが作成できます。<br>
同様に、indexページのWorkoutボタンを押すと/workoutにリダイレクトし、テンポを入力し、選ぶボタンを押すと/confirmにリダイレクトし、入力したテンポに近い曲で運動したいときにぴったりなプレイリストが作成できます。<br>
最後に、indexページのFavoriteボタンを押すと、/favoriteにリダイレクトし、自分がフォローしているアーティストが表示されるので、表示されたアーティストの中から今の気分に合う3組を選ぶと/confirmにリダイレクトし、選んだアーティストに似ているアーティストの曲を自動でプレイリストにまとめてくれます。<br>

#### 使い方
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


