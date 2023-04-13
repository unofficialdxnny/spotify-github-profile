import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up the Spotify API client using the client ID, client secret, and redirect URI
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="your_client_id", client_secret="your_client_secret", redirect_uri="http://localhost:8080/callback/", scope="user-read-playback-state"))

# Get the user's currently playing track
track = sp.current_playback()

# Print the track name and artist
if track is not None and 'item' in track:
    track_name = track['item']['name']
    artist_name = track['item']['artists'][0]['name']
    print(f"Now playing: {track_name} by {artist_name}")
else:
    print("No track currently playing.")
