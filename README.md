# SpotiPlay

First things first I'm completely new to Python and this is the first project I have ever made in it. If there is any ways for me to improve this please let me know!

## Requirements:
* [Python](https://www.python.org/downloads/) - Built on 3.6, tested and works on 2.7.9, not sure about earlier versions
* [gmusicapi](https://github.com/simon-weber/gmusicapi)
  * `pip install gmusicapi`
* [spotipy](https://github.com/plamere/spotipy)
  * `pip install spotipy`
  
## Use:
1. You need a Spotify [OAuth Token](https://developer.spotify.com/web-api/console/get-current-user-playlists/)
  * Visit the OAuth link I provided
  * Click "Get OAuth Token" ![](http://i.imgur.com/OUWmqZc.png) 
  * Make sure "Playlist Read Private" is checked, then "Request Token" ![](http://i.imgur.com/fJH76YM.png)

2. Edit "SpotiPlay.py" input the required information in lines 5-8.

3. Run "SpotiPlay.py" with `python SpotiPlay.py` to move all of your Spotify Playlists to Google Play Music

#### THIS IS NOT PERFECT. WITH HOW IT WORKS IT MAY NOT FIND THE CORRECT SONG AND ADD A COMPLETELY DIFFERENT SONG WITH A SIMILAR TITLE
