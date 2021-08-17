# Ramdofy
This is CS50's final project.
#### Video Demo: 
https://youtu.be/HHHyoYSWX_k
#### Description:
It is a web application that uses Spotify's Web API to automatically create a playlist that suits your mood based on the information of songs registered as favorites in your Spotify account and the artists you follow. In addition, the Spotify API has a function called AudioFeaturesObject that outputs a numerical value indicating the characteristics of the song as JSON, and creates a playlist with reference to that numerical value.
You can automatically create three types of playlists: when you want to relax (Relax), when you want to exercise (Workout), and when you want to listen to music from a new artist you don't know (Favorite).

Technologies used:<br>
Backend: Python,Flask<br>
Frontend: Tailwind CSS

SpotifyのWebAPIを用いて、自身のSpotifyアカウントでお気に入りに登録している曲やフォローしているアーティストの情報をもとに、今の気分にあったプレイリストを自動で作成するWebアプリです。
また、Spotify APIには、AudioFeaturesObjectという曲の特徴を示す数値をJSONとして出力する機能があり、その数値も参考にしてプレイリストを作ります。<br>
リラックスしたい時(Relax)、運動をしたい時(Workout)、自分の知らない新しいアーティストの音楽を聴きたい時(Favorite)の3種類のプレイリストを自動作成できます。

使用技術<br>
Backend: Python,Flask<br>
Frontend: Tailwind CSS

How to launch this application
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

使い方
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

CS50 Final Project - Homework framework
The project is a webpage where teachers can create assignments for students. The implementation is fairly simple, to keep the project scope in check. I wanted to make a project like this to expand my knowledge of Node JS and of techniques like buffer piping from database to client, role based authentications, etc.

Technologies used:

Node JS
Express JS
bcryptjs
passport
sqlite3
ejs
other small libraries or packages
How the webpage works?
The idea is simple. The user can register either as student or teacher. During registration you need to enter these fields:

Email
Name
Password: it is checked to match, must be at least 6 symbols long and is hashed after checks are done
Checkbox for what type of user you will be (student or teacher)
Student registration allows you to access student dashboard, where you can see created homework. Entering the homework you can upload a file. Once the teacher grades and reviews your submission it will appear instead of .

For teachers, teacher dashboard is unlocked, where they can create a homework and see student's which submitted homework. When accessing the homework, teacher can download the submitted file and then write a review and grade it.

Routing
Each route checks if the user is authenticated. It means if correct mail and password were supplied and what role it has. So for example a teacher cannot enter /students/homeworks/1 route. The same is for student, he cannot enter teacher dashboard route.

Sessions
The webpage uses sessions to confirm that user is registered. Once the user logins, his credentials are checked with bcrypt and Passport JS library. Once everything passes a session is created (serialized and deserialized) and stored in the cookies. The server attaches user to subsequent requests, so the back-end can easily access the details, like roles: student, teacher.

Database
Database stores all users, homework, student submissions. The tables, like student submissions uses foreign keys to relate users to submitted homework. Moreover, homework table uses foreign keys to relate the homework to a teacher.

Possible improvements
As all applications this one can also be improved. Possible improvements:

Have administrator account which confirms user identity, so that student could not register as a teacher
Ability to change account details
Have a way for teacher to upload videos to explain the assignment
Notificaitons to email about new homeworks or submissions
How to launch application
Check that you have Node version 8+
Clone the code: git clone https://github.com/RokasDie/cs50-final-project.git
Run command prompt in the folder and run npm install to install all dependencies
Once installed run command npm start
In your browser go to localhost:3000
You are ready to go!
