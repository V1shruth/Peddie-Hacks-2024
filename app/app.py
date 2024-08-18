from flask import Flask, render_template, request, redirect, url_for, session
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

# Spotify API credentials
SPOTIPY_CLIENT_ID = "598d210fb6724e52869a2f0ca9c5c9d5"
SPOTIPY_CLIENT_SECRET = "da2ded1d6e8b4fcca5eff6477968d030"

# Initialize Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Dictonary containing cities with there most famous songs.
# Each song is split into metadata
city_songs = {
    "London": [
        {"title": "London Calling", "artist": "The Clash", "genre": "Rock"},
        {"title": "Waterloo Sunset", "artist": "The Kinks", "genre": "Rock"},
        {"title": "A Day in the Life", "artist": "The Beatles", "genre": "Rock"},
        {"title": "Baker Street", "artist": "Gerry Rafferty", "genre": "Rock"},
        {"title": "West End Girls", "artist": "Pet Shop Boys", "genre": "Pop"},
        {"title": "Streets of London", "artist": "Ralph McTell", "genre": "Pop"},
        {"title": "LDN", "artist": "Lily Allen", "genre": "Pop"},
        {"title": "Sunny Afternoon", "artist": "The Kinks", "genre": "Rock"},
        {"title": "Electric Avenue", "artist": "Eddy Grant", "genre": "Pop"},
        {"title": "London Bridge", "artist": "Fergie", "genre": "Pop"},
        {"title": "London Boy", "artist": "Taylor Swift", "genre": "Pop"},
        {"title": "Werewolves of London", "artist": "Warren Zevon", "genre": "Rock"},
        {"title": "A Foggy Day (In London Town)", "artist": "Ella Fitzgerald", "genre": "Jazz"},
        {"title": "Hometown Glory", "artist": "Adele", "genre": "Pop"},
        {"title": "Itchycoo Park", "artist": "Small Faces", "genre": "Rock"},
        {"title": "Brixton", "artist": "Gallant", "genre": "Pop"},
        {"title": "Lullaby of London", "artist": "The Pogues", "genre": "Rock"},
        {"title": "Primrose Hill", "artist": "John & Beverley Martyn", "genre": "Pop"},
        {"title": "Maybe It's Because I'm a Londoner", "artist": "Davy Jones", "genre": "Pop"},
        {"title": "That's Entertainment", "artist": "The Jam", "genre": "Rock"},
    ],
    "Tokyo": [
        {"title": "Tokyo Drift", "artist": "Teriyaki Boyz", "genre": "Pop"},
        {"title": "Sukiyaki", "artist": "Kyu Sakamoto", "genre": "Pop"},
        {"title": "Shinunoga E-Wa", "artist": "Fujii Kaze", "genre": "Pop"},
        {"title": "Plastic Love", "artist": "Mariya Takeuchi", "genre": "Pop"},
        {"title": "Shibuya-kei", "artist": "Pizzicato Five", "genre": "Pop"},
        {"title": "Tokyo", "artist": "YUI", "genre": "Pop"},
        {"title": "Battle Without Honor or Humanity", "artist": "Tomoyasu Hotei", "genre": "Rock"},
        {"title": "One More Time, One More Chance", "artist": "Masayoshi Yamazaki", "genre": "Pop"},
        {"title": "Fireworks", "artist": "DAOKO x Kenshi Yonezu", "genre": "Pop"},
        {"title": "Hikaru Nara", "artist": "Goose house", "genre": "Pop"},
        {"title": "Tokyo Tower", "artist": "May J.", "genre": "Pop"},
        {"title": "Cherry Blossom Ending", "artist": "Busker Busker", "genre": "Pop"},
        {"title": "Blue Bird", "artist": "Ikimono Gakari", "genre": "Pop"},
        {"title": "Ode to Tokyo", "artist": "Aimer", "genre": "Pop"},
        {"title": "Silhouette", "artist": "KANA-BOON", "genre": "Rock"},
        {"title": "Densha ni Noru", "artist": "Hikaru Utada", "genre": "Pop"},
        {"title": "Sayonara I Love You", "artist": "Shota Shimizu", "genre": "Pop"},
        {"title": "Tokyo Nights", "artist": "Digitalism", "genre": "Pop"},
        {"title": "Tokyo Vampire Hotel", "artist": "tricot", "genre": "Rock"},
        {"title": "Lonely Tokyo", "artist": "Sara Kays", "genre": "Pop"},
    ],
    "New York": [
        {"title": "Empire State of Mind", "artist": "Jay-Z", "genre": "Pop"},
        {"title": "New York, New York", "artist": "Frank Sinatra", "genre": "Jazz"},
        {"title": "No Sleep Till Brooklyn", "artist": "Beastie Boys", "genre": "Rock"},
        {"title": "Autumn in New York", "artist": "Billie Holiday", "genre": "Jazz"},
        {"title": "The Message", "artist": "Grandmaster Flash", "genre": "Pop"},
        {"title": "New York State of Mind", "artist": "Nas", "genre": "Pop"},
        {"title": "Chelsea Morning", "artist": "Joni Mitchell", "genre": "Pop"},
        {"title": "Hotline Bling", "artist": "Drake", "genre": "Pop"},
        {"title": "Welcome to New York", "artist": "Taylor Swift", "genre": "Pop"},
        {"title": "Juicy", "artist": "The Notorious B.I.G.", "genre": "Pop"},
        {"title": "New York Groove", "artist": "Ace Frehley", "genre": "Rock"},
        {"title": "I Love New York", "artist": "Madonna", "genre": "Pop"},
        {"title": "Englishman in New York", "artist": "Sting", "genre": "Rock"},
        {"title": "Manhattan", "artist": "Ella Fitzgerald", "genre": "Jazz"},
        {"title": "Harlem Shuffle", "artist": "Bob & Earl", "genre": "Pop"},
        {"title": "New York City Cops", "artist": "The Strokes", "genre": "Rock"},
        {"title": "The Only Living Boy in New York", "artist": "Simon & Garfunkel", "genre": "Rock"},
        {"title": "New York Minute", "artist": "Don Henley", "genre": "Rock"},
        {"title": "New York City Boy", "artist": "Pet Shop Boys", "genre": "Pop"},
        {"title": "Take the 'A' Train", "artist": "Duke Ellington", "genre": "Jazz"},
    ],
    "New Delhi": [
        {"title": "Delhi-6", "artist": "Rekha Bhardwaj", "genre": "Pop"},
        {"title": "Kajra Re", "artist": "Alisha Chinai", "genre": "Pop"},
        {"title": "Ye Dilli Hai Mere Yaar", "artist": "Kailash Kher", "genre": "Pop"},
        {"title": "Dilliwaali Girlfriend", "artist": "Arijit Singh", "genre": "Pop"},
        {"title": "Kabhi Kabhi Aditi", "artist": "Rashid Ali", "genre": "Pop"},
        {"title": "Delhi Belly", "artist": "Ram Sampath", "genre": "Pop"},
        {"title": "Tunak Tunak Tun", "artist": "Daler Mehndi", "genre": "Pop"},
        {"title": "Dilli", "artist": "A.R. Rahman", "genre": "Pop"},
        {"title": "Chaiyya Chaiyya", "artist": "Sukhwinder Singh", "genre": "Pop"},
        {"title": "Jai Ho", "artist": "A.R. Rahman", "genre": "Pop"},
        {"title": "Dilli Di Kudiyaan", "artist": "Shankar-Ehsaan-Loy", "genre": "Pop"},
        {"title": "Desi Girl", "artist": "Sunidhi Chauhan", "genre": "Pop"},
        {"title": "Aye Hip Hopper", "artist": "Ishq Bector", "genre": "Pop"},
        {"title": "Mundiyan To Bach Ke", "artist": "Panjabi MC", "genre": "Pop"},
        {"title": "Gallan Goodiyaan", "artist": "Shankar Mahadevan", "genre": "Pop"},
        {"title": "High Heels", "artist": "Honey Singh", "genre": "Pop"},
        {"title": "Abhi Toh Party Shuru Hui Hai", "artist": "Badshah", "genre": "Pop"},
    ],
}


genres = set(song["genre"] for songs in city_songs.values() for song in songs)

def get_spotify_track(title, artist):
    query = f"track:{title} artist:{artist}"
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return {
            'id': track['id'],
            'url': track['external_urls']['spotify'],
            'preview_url': track['preview_url']
        }
    return None

@app.route("/", methods=["GET"])
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
        
        # Get Spotify data for each song
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
    