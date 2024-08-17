from flask import Flask, render_template, request

app = Flask(__name__)

# Dictonary containing cities with there most famous songs.
# Each song is split into metadata
city_songs = {
    "London": [
        {"title": "London Calling", "artist": "The Clash", "genre": "Rock"},
        {"title": "Waterloo Sunset", "artist": "The Kinks", "genre": "Rock"},
        {"title": "A Day in the Life", "artist": "The Beatles", "genre": "Rock"},
        {"title": "Baker Street", "artist": "Gerry Rafferty", "genre": "Rock"},
        {"title": "West End Girls", "artist": "Pet Shop Boys", "genre": "Pop"},
        {"title": "Streets of London", "artist": "Ralph McTell", "genre": "Folk"},
        {"title": "LDN", "artist": "Lily Allen", "genre": "Pop"},
        {"title": "Sunny Afternoon", "artist": "The Kinks", "genre": "Rock"},
        {"title": "Electric Avenue", "artist": "Eddy Grant", "genre": "Reggae"},
        {"title": "London Bridge", "artist": "Fergie", "genre": "Hip Hop"},
        {"title": "London Boy", "artist": "Taylor Swift", "genre": "Pop"},
        {"title": "Werewolves of London", "artist": "Warren Zevon", "genre": "Rock"},
        {"title": "A Foggy Day (In London Town)", "artist": "Ella Fitzgerald", "genre": "Jazz"},
        {"title": "Hometown Glory", "artist": "Adele", "genre": "Soul"},
        {"title": "Itchycoo Park", "artist": "Small Faces", "genre": "Rock"},
        {"title": "Brixton", "artist": "Gallant", "genre": "R&B"},
        {"title": "Lullaby of London", "artist": "The Pogues", "genre": "Rock"},
        {"title": "Primrose Hill", "artist": "John & Beverley Martyn", "genre": "Folk"},
        {"title": "Maybe It's Because I'm a Londoner", "artist": "Davy Jones", "genre": "Reggae"},
        {"title": "That's Entertainment", "artist": "The Jam", "genre": "Rock"},
    ],
    "Tokyo": [
        {"title": "Tokyo Drift", "artist": "Teriyaki Boyz", "genre": "Hip Hop"},
        {"title": "Sukiyaki", "artist": "Kyu Sakamoto", "genre": "Pop"},
        {"title": "Shinunoga E-Wa", "artist": "Fujii Kaze", "genre": "J-Pop"},
        {"title": "Plastic Love", "artist": "Mariya Takeuchi", "genre": "City Pop"},
        {"title": "Shibuya-kei", "artist": "Pizzicato Five", "genre": "J-Pop"},
        {"title": "Tokyo", "artist": "YUI", "genre": "J-Pop"},
        {"title": "Battle Without Honor or Humanity", "artist": "Tomoyasu Hotei", "genre": "Rock"},
        {"title": "One More Time, One More Chance", "artist": "Masayoshi Yamazaki", "genre": "Ballad"},
        {"title": "Fireworks", "artist": "DAOKO x Kenshi Yonezu", "genre": "J-Pop"},
        {"title": "Hikaru Nara", "artist": "Goose house", "genre": "J-Pop"},
        {"title": "Tokyo Tower", "artist": "May J.", "genre": "J-Pop"},
        {"title": "Cherry Blossom Ending", "artist": "Busker Busker", "genre": "K-Pop"},
        {"title": "Blue Bird", "artist": "Ikimono Gakari", "genre": "J-Pop"},
        {"title": "Ode to Tokyo", "artist": "Aimer", "genre": "J-Pop"},
        {"title": "Silhouette", "artist": "KANA-BOON", "genre": "J-Rock"},
        {"title": "Densha ni Noru", "artist": "Hikaru Utada", "genre": "Pop"},
        {"title": "Sayonara I Love You", "artist": "Shota Shimizu", "genre": "R&B"},
        {"title": "Tokyo Nights", "artist": "Digitalism", "genre": "Electronic"},
        {"title": "Tokyo Vampire Hotel", "artist": "tricot", "genre": "Math Rock"},
        {"title": "Lonely Tokyo", "artist": "Sara Kays", "genre": "Indie Pop"},
    ],
    "New York": [
        {"title": "Empire State of Mind", "artist": "Jay-Z", "genre": "Hip Hop"},
        {"title": "New York, New York", "artist": "Frank Sinatra", "genre": "Jazz"},
        {"title": "No Sleep Till Brooklyn", "artist": "Beastie Boys", "genre": "Hip Hop"},
        {"title": "Autumn in New York", "artist": "Billie Holiday", "genre": "Jazz"},
        {"title": "The Message", "artist": "Grandmaster Flash", "genre": "Hip Hop"},
        {"title": "New York State of Mind", "artist": "Nas", "genre": "Hip Hop"},
        {"title": "Chelsea Morning", "artist": "Joni Mitchell", "genre": "Folk"},
        {"title": "Hotline Bling", "artist": "Drake", "genre": "R&B"},
        {"title": "Welcome to New York", "artist": "Taylor Swift", "genre": "Pop"},
        {"title": "Juicy", "artist": "The Notorious B.I.G.", "genre": "Hip Hop"},
        {"title": "New York Groove", "artist": "Ace Frehley", "genre": "Rock"},
        {"title": "I Love New York", "artist": "Madonna", "genre": "Pop"},
        {"title": "Englishman in New York", "artist": "Sting", "genre": "Rock"},
        {"title": "Manhattan", "artist": "Ella Fitzgerald", "genre": "Jazz"},
        {"title": "Harlem Shuffle", "artist": "Bob & Earl", "genre": "R&B"},
        {"title": "New York City Cops", "artist": "The Strokes", "genre": "Rock"},
        {"title": "The Only Living Boy in New York", "artist": "Simon & Garfunkel", "genre": "Folk Rock"},
        {"title": "New York Minute", "artist": "Don Henley", "genre": "Rock"},
        {"title": "New York City Boy", "artist": "Pet Shop Boys", "genre": "Dance Pop"},
        {"title": "Take the 'A' Train", "artist": "Duke Ellington", "genre": "Jazz"},
    ],
    "New Delhi": [
        {"title": "Delhi-6", "artist": "Rekha Bhardwaj", "genre": "Bollywood"},
        {"title": "Kajra Re", "artist": "Alisha Chinai", "genre": "Bollywood"},
        {"title": "Ye Dilli Hai Mere Yaar", "artist": "Kailash Kher", "genre": "Bollywood"},
        {"title": "Dilliwaali Girlfriend", "artist": "Arijit Singh", "genre": "Bollywood"},
        {"title": "Kabhi Kabhi Aditi", "artist": "Rashid Ali", "genre": "Bollywood"},
        {"title": "Delhi Belly", "artist": "Ram Sampath", "genre": "Bollywood"},
        {"title": "Tunak Tunak Tun", "artist": "Daler Mehndi", "genre": "Pop"},
        {"title": "Dilli", "artist": "A.R. Rahman", "genre": "Bollywood"},
        {"title": "Chaiyya Chaiyya", "artist": "Sukhwinder Singh", "genre": "Bollywood"},
        {"title": "Jai Ho", "artist": "A.R. Rahman", "genre": "Bollywood"},
        {"title": "Dilli Di Kudiyaan", "artist": "Shankar-Ehsaan-Loy", "genre": "Bollywood"},
        {"title": "Desi Girl", "artist": "Sunidhi Chauhan", "genre": "Bollywood"},
        {"title": "Aye Hip Hopper", "artist": "Ishq Bector", "genre": "Hip Hop"},
        {"title": "Mundiyan To Bach Ke", "artist": "Panjabi MC", "genre": "Bhangra"},
        {"title": "Gallan Goodiyaan", "artist": "Shankar Mahadevan", "genre": "Bollywood"},
        {"title": "High Heels", "artist": "Honey Singh", "genre": "Hip Hop"},
        {"title": "Abhi Toh Party Shuru Hui Hai", "artist": "Badshah", "genre": "Hip Hop"},
    ],
}

#selcects songs after criteria is chosen
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
