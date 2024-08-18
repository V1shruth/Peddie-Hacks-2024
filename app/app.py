from flask import Flask, render_template, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import csv

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Spotify API credentials (used to authenticate with the Spotify API)
SPOTIPY_CLIENT_ID = "598d210fb6724e52869a2f0ca9c5c9d5"
SPOTIPY_CLIENT_SECRET = "da2ded1d6e8b4fcca5eff6477968d030"

# Initialize Spotify client using the client credentials flow
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Load city songs data from a CSV file into a dictionary
city_songs = {}

# Open and read the CSV file containing song data
with open('city_songs.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)  # Use DictReader to read rows as dictionaries
    for row in reader:
        city = row['city']  # Extract city name from the current row
        # Store song metadata in a dictionary
        song_data = {
            "title": row['title'],
            "artist": row['artist'],
            "genre": row['genre']
        }
        # If the city is not already in the dictionary, add it
        if city not in city_songs:
            city_songs[city] = []
        # Append the song data to the list for the corresponding city
        city_songs[city].append(song_data)

# Extract unique genres from the songs for use in genre selection
genres = set(song["genre"] for songs in city_songs.values() for song in songs)

# Function to search for a track on Spotify based on title and artist
def get_spotify_track(title, artist):
    query = f"track:{title} artist:{artist}"  # Construct search query
    try:
        results = sp.search(q=query, type='track', limit=1)  # Search for the track on Spotify
        if results['tracks']['items']:
            track = results['tracks']['items'][0]  # Get the first result
            return {
                'id': track['id'],
                'url': track['external_urls']['spotify'],
                'preview_url': track['preview_url']
            }
    except Exception as e:
        print(f"Error searching for track: {e}")  # Print any errors encountered
    return None  # Return None if no track is found or an error occurs

# Route for the main index page
@app.route("/")
def index():
    return render_template("index.html", genres=genres)  # Render the index page with genres data

# Route for generating a playlist based on selected city and genres
@app.route("/generate_playlist", methods=["POST"])
def generate_playlist():
    data = request.json  # Parse JSON data from the request
    city = data.get('city')  # Get the selected city
    selected_genres = data.get('genres', [])  # Get the selected genres
    
    if city in city_songs:  # Check if the city has songs in the database
        playlist = city_songs[city]  # Retrieve songs for the selected city
        if selected_genres:
            # Filter songs by the selected genres
            playlist = [song for song in playlist if song["genre"] in selected_genres]
        
        spotify_playlist = []
        for song in playlist:
            # Get Spotify data for each song
            spotify_data = get_spotify_track(song['title'], song['artist'])
            if spotify_data:
                # Store the song data along with Spotify links
                song_data = {
                    'title': song['title'],
                    'artist': song['artist'],
                    'id': spotify_data['id'],
                    'url': spotify_data['url'],
                    'preview_url': spotify_data['preview_url']
                }
                spotify_playlist.append(song_data)
        
        # Return the generated playlist as a JSON response
        return jsonify(spotify_playlist)
    
    # Return an empty JSON response if no songs are found
    return jsonify([])

# Main entry point for the Flask application
if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode for development
