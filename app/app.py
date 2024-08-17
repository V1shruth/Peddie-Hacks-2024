from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data (replace with your actual data)
city_songs = {
    "New York": [
        {"title": "Empire State of Mind", "artist": "Jay-Z", "genre": "Hip Hop"},
        {"title": "New York, New York", "artist": "Frank Sinatra", "genre": "Jazz"},
    ],
    "London": [
        {"title": "London Calling", "artist": "The Clash", "genre": "Punk Rock"},
        {"title": "Waterloo Sunset", "artist": "The Kinks", "genre": "Rock"},
    ],
}

genres = set(song["genre"] for songs in city_songs.values() for song in songs)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        selected_genre = request.form["genre"]
        
        if user_input in city_songs:
            playlist = city_songs[user_input]
            if selected_genre:
                playlist = [song for song in playlist if song["genre"] == selected_genre]
            
            return render_template("index.html", city=user_input, playlist=playlist, genres=genres)
    
    return render_template("index.html", genres=genres)

if __name__ == "__main__":
    app.run(debug=True)