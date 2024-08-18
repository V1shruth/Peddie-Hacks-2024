from flask import Flask, render_template, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import csv

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Spotify API credentials
SPOTIPY_CLIENT_ID = "598d210fb6724e52869a2f0ca9c5c9d5"
SPOTIPY_CLIENT_SECRET = "da2ded1d6e8b4fcca5eff6477968d030"

# Initialize Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Load city songs from CSV file
city_songs = {}

with open('city_songs.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        city = row['city']
        song_data = {
            "title": row['title'],
            "artist": row['artist'],
            "genre": row['genre']
        }
        if city not in city_songs:
            city_songs[city] = []
        city_songs[city].append(song_data)

# Extract unique genres from the songs
genres = set(song["genre"] for songs in city_songs.values() for song in songs)

def get_spotify_track(title, artist):
    query = f"track:{title} artist:{artist}"
    try:
        results = sp.search(q=query, type='track', limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            return {
                'id': track['id'],
                'url': track['external_urls']['spotify'],
                'preview_url': track['preview_url']
            }
    except Exception as e:
        print(f"Error searching for track: {e}")
    return None

@app.route("/")
def index():
    return render_template("index.html", genres=genres)

@app.route("/generate_playlist", methods=["POST"])
def generate_playlist():
    data = request.json
    city = data.get('city')
    selected_genres = data.get('genres', [])
    
    if city in city_songs:
        playlist = city_songs[city]
        if selected_genres:
            playlist = [song for song in playlist if song["genre"] in selected_genres]
        
        spotify_playlist = []
        for song in playlist:
            spotify_data = get_spotify_track(song['title'], song['artist'])
            if spotify_data:
                song_data = {
                    'title': song['title'],
                    'artist': song['artist'],
                    'id': spotify_data['id'],
                    'url': spotify_data['url'],
                    'preview_url': spotify_data['preview_url']
                }
                spotify_playlist.append(song_data)
        
        return jsonify(spotify_playlist)
    
    return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)
