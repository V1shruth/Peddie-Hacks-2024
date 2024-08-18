import csv

# The city_songs dictionary
city_songs = {
    "London": [
        {"title": "London Calling", "artist": "The Clash", "genre": "Pop"},
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

# Open a new CSV file in write mode
with open('city_songs.csv', 'w', newline='') as csvfile:
    # Define the field names (columns) for the CSV
    fieldnames = ['city', 'title', 'artist', 'genre']
    
    # Create a writer object with the field names
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header row (column names)
    writer.writeheader()
    
    # Iterate through each city and its songs
    for city, songs in city_songs.items():
        for song in songs:
            # Add the city name to each song dictionary
            song['city'] = city
            # Write the song dictionary to the CSV file
            writer.writerow(song)

print("CSV file 'city_songs.csv' created successfully.")