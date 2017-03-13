from gmusicapi import Mobileclient
import spotipy

# USER INPUT GOES HERE
spotify_username = ""
spotify_token = ""
play_email = ""
play_password = ""
# DO NOT EDIT ANYTHING AFTER THIS LINE

spotify = spotipy.Spotify(auth=spotify_token)
spotify_playlists = spotify.user_playlists(spotify_username)

api = Mobileclient()
api.login(play_email, play_password, Mobileclient.FROM_MAC_ADDRESS)
gpm_playlists = api.get_all_playlists()

if spotify_username == "" or spotify_token == "" or play_email == "" or play_password == "":
    print("Please make sure you have filled out all user input fields!")
else:
    for playlist in spotify_playlists['items']:
        if playlist['owner']['id'] == spotify_username:
            playlist_exists = False
            for gpm_playlist in gpm_playlists:
                if gpm_playlist.get('name') == playlist['name']:
                    playlist_exists = True

            if not playlist_exists:
                api.create_playlist(playlist['name'])
                playlist_exists = True

            print("Currently Moving:", playlist['name'])
            results = spotify.user_playlist(spotify_username, playlist['id'], fields="tracks,next")
            tracks = results['tracks']

            gpm_playlists = api.get_all_playlists();

            for i, item in enumerate(tracks['items']):
                track = item['track']
                search_results = api.search(track['name'], 10).get('song_hits')

                for result in search_results:
                    name = track['name']
                    artist = track['artists'][0]['name']
                    if name in result.get('track').get('title') and artist in result.get('track').get('albumArtist'):
                        for gpm_playlist in gpm_playlists:
                            if gpm_playlist.get('name') == playlist['name']:
                                api.add_songs_to_playlist(gpm_playlist.get('id'), result.get('track').get('storeId'))
                                break
                        break

    print("Playlist conversion has finished.")





