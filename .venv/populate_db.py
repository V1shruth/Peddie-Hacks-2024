from app import create_app, db
from app.models import City, Song

app = create_app()

with app.app_context():
    # Add Cities
    new_york = City(name='New York')
    tokyo = City(name='Tokyo')
    paris = City(name='Paris')

    db.session.add(new_york)
    db.session.add(tokyo)
    db.session.add(paris)

    # Add Songs
    song1 = Song(title='Song A', artist='Artist A', genre='Pop', popularity=90, city=new_york)
    song2 = Song(title='Song B', artist='Artist B', genre='Rock', popularity=85, city=tokyo)
    song3 = Song(title='Song C', artist='Artist C', genre='Jazz', popularity=80, city=paris)

    db.session.add(song1)
    db.session.add(song2)
    db.session.add(song3)

    db.session.commit()


# to execute the script in the terminal to populate the database (when complete) type this: 'python populate_db.py' 