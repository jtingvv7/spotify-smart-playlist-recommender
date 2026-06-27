import os
import subprocess
import random

history = []

def clear_screen():
    # 'nt' is for windows, 'clear' is for Linux/macOS
    subprocess.run('cls' if os.name == 'nt' else 'clear',shell=True)

def show_menu():
    """Displays the main menu of the application."""
    clear_screen()
    print("\n" + "="*41)
    print(" Spotify Smart Playlist Recommender")
    print("="*41)
    print("1. Get Playlist Recommendation")
    print("2. View Available Genres")
    print("3. View Available Moods")
    print("4. View Recommendation History")
    print("5. About Spotify & Its Innovation")
    print("6. Exit")
    print("="*41)

def get_valid_choice(prompt, valid_choices):
    while True:
        choice = input(prompt)

        if choice in valid_choices:
            return choice
        print("Invalid input. Please try again.\n")

def recommend_playlist():
    """Handles the logic for playlist recommendation based on user inputs."""
    clear_screen()
    print("\n--- Playlist Recommendation ---\n")

    valid_genres = ["1", "2", "3", "4", "5"]
    valid_moods = ["1", "2", "3", "4"]
    valid_durations = ["1", "2", "3"]

    genre_map = {"1": "Pop", "2": "Rock", "3": "Hip-Hop", "4": "Jazz", "5": "Classical"}
    mood_map = {"1": "Happy", "2": "Relaxed", "3": "Energetic", "4": "Sad"}
    duration_map = {"1": "Short", "2": "Medium", "3": "Long"}

    
    print("Choose Genre:")
    print("1. Pop   2. Rock   3. Hip-Hop   4. Jazz   5. Classical")
    genre = get_valid_choice(
        "Enter genre (1-5):",
        valid_genres)

    print("-" * 30)
    
    print("Choose Mood:")
    print("1. Happy   2. Relaxed   3. Energetic   4. Sad")
    mood = get_valid_choice(
        "Enter mood (1-4): ",
        valid_moods)

    print("-" * 30)

    print("Listening Duration:")
    print("1. Short (15 mins)   2. Medium (30-60 mins)   3. Long (2+ hours)")
    duration = get_valid_choice(
        "Enter duration (1-3): ",
        valid_durations)


    recommendations = {

    # ================= Pop =================
    ("1", "1"): {
        "playlist": "Today's Top Hits",
        "artists": [
            "Taylor Swift",
            "Olivia Rodrigo",
            "Sabrina Carpenter"
        ],
        "songs": [
            "Cruel Summer",
            "vampire",
            "Espresso"
        ]
    },

    ("1", "2"): {
        "playlist": "Chill Hits",
        "artists": [
            "Billie Eilish",
            "Lauv",
            "Conan Gray"
        ],
        "songs": [
            "Ocean Eyes",
            "I Like Me Better",
            "Heather"
        ]
    },

    ("1", "3"): {
        "playlist": "Pop Rising",
        "artists": [
            "Dua Lipa",
            "Ariana Grande",
            "Doja Cat"
        ],
        "songs": [
            "Levitating",
            "yes, and?",
            "Paint The Town Red"
        ]
    },

    ("1", "4"): {
        "playlist": "Sad Pop Mix",
        "artists": [
            "Billie Eilish",
            "Lewis Capaldi",
            "Adele"
        ],
        "songs": [
            "What Was I Made For?",
            "Someone You Loved",
            "Easy On Me"
        ]
    },

    # ================= Rock =================
    ("2", "1"): {
        "playlist": "Rock Classics",
        "artists": [
            "Queen",
            "Bon Jovi",
            "Journey"
        ],
        "songs": [
            "Don't Stop Me Now",
            "Livin' On A Prayer",
            "Don't Stop Believin'"
        ]
    },

    ("2", "2"): {
        "playlist": "Soft Rock Drive",
        "artists": [
            "Coldplay",
            "The Script",
            "Imagine Dragons"
        ],
        "songs": [
            "Yellow",
            "Breakeven",
            "Demons"
        ]
    },

    ("2", "3"): {
        "playlist": "Rock Workout",
        "artists": [
            "AC/DC",
            "Linkin Park",
            "Metallica"
        ],
        "songs": [
            "Thunderstruck",
            "Numb",
            "Enter Sandman"
        ]
    },

    ("2", "4"): {
        "playlist": "Acoustic Rock",
        "artists": [
            "Nirvana",
            "Foo Fighters",
            "Pearl Jam"
        ],
        "songs": [
            "Something In The Way",
            "Everlong",
            "Black"
        ]
    },

    # ================= Hip-Hop =================
    ("3", "1"): {
        "playlist": "RapCaviar",
        "artists": [
            "Drake",
            "Travis Scott",
            "Lil Baby"
        ],
        "songs": [
            "God's Plan",
            "SICKO MODE",
            "Drip Too Hard"
        ]
    },

    ("3", "2"): {
        "playlist": "Mellow Bars",
        "artists": [
            "J. Cole",
            "Kendrick Lamar",
            "Logic"
        ],
        "songs": [
            "No Role Modelz",
            "LOVE.",
            "1-800-273-8255"
        ]
    },

    ("3", "3"): {
        "playlist": "Beast Mode",
        "artists": [
            "Eminem",
            "50 Cent",
            "DMX"
        ],
        "songs": [
            "Till I Collapse",
            "In Da Club",
            "X Gon' Give It To Ya"
        ]
    },

    ("3", "4"): {
        "playlist": "Late Night Hip-Hop",
        "artists": [
            "Kendrick Lamar",
            "Post Malone",
            "The Weeknd"
        ],
        "songs": [
            "PRIDE.",
            "Circles",
            "Call Out My Name"
        ]
    },

    # ================= Jazz =================
    ("4", "1"): {
        "playlist": "Jazz Vibes",
        "artists": [
            "Louis Armstrong",
            "Ella Fitzgerald",
            "Frank Sinatra"
        ],
        "songs": [
            "What A Wonderful World",
            "Dream A Little Dream Of Me",
            "Fly Me To The Moon"
        ]
    },

    ("4", "2"): {
        "playlist": "Smooth Jazz",
        "artists": [
            "Kenny G",
            "Dave Koz",
            "George Benson"
        ],
        "songs": [
            "Songbird",
            "You Make Me Smile",
            "Breezin'"
        ]
    },

    ("4", "3"): {
        "playlist": "Jazz Fusion",
        "artists": [
            "Miles Davis",
            "Herbie Hancock",
            "Chick Corea"
        ],
        "songs": [
            "So What",
            "Chameleon",
            "Spain"
        ]
    },

    ("4", "4"): {
        "playlist": "Blue Note Sessions",
        "artists": [
            "John Coltrane",
            "Chet Baker",
            "Bill Evans"
        ],
        "songs": [
            "In A Sentimental Mood",
            "My Funny Valentine",
            "Peace Piece"
        ]
    },

    # ================= Classical =================
    ("5", "1"): {
        "playlist": "Mozart for Joy",
        "artists": [
            "Mozart",
            "Beethoven",
            "Haydn"
        ],
        "songs": [
            "Eine kleine Nachtmusik",
            "Symphony No. 5",
            "The Creation"
        ]
    },

    ("5", "2"): {
        "playlist": "Peaceful Piano",
        "artists": [
            "Ludovico Einaudi",
            "Yiruma",
            "Max Richter"
        ],
        "songs": [
            "Nuvole Bianche",
            "River Flows In You",
            "On The Nature Of Daylight"
        ]
    },

    ("5", "3"): {
        "playlist": "Classical Focus",
        "artists": [
            "Johann Sebastian Bach",
            "Antonio Vivaldi",
            "Philip Glass"
        ],
        "songs": [
            "Cello Suite No.1",
            "Spring",
            "Opening"
        ]
    },

    ("5", "4"): {
        "playlist": "Classical Essentials",
        "artists": [
            "Frédéric Chopin",
            "Claude Debussy",
            "Pyotr Ilyich Tchaikovsky"
        ],
        "songs": [
            "Nocturne Op.9 No.2",
            "Clair de Lune",
            "Swan Lake"
        ]
    }

}

    selection = recommendations.get((genre, mood))
    artist = random.choice(selection["artists"])
    song = random.choice(selection["songs"])

    if duration == "1":
        reason = "Perfect for uplifting your mood during a\nshort 15-minute listening session."
    elif duration == "2":
        reason = "Perfect for uplifting your mood during a\n30–60 minute listening session."
    elif duration == "3":
        reason = "Perfect for uplifting your mood during a\nlong 2+ hour listening session."
    else:
        reason = "Listening duration not recognised."

    if selection:
        clear_screen()
        history.append({
            "genre":genre_map[genre],
            "mood":mood_map[mood],
            "playlist":selection["playlist"],
            "artist":artist,
            "song":song
        })
        print("\n=========================================")
        print(" Spotify Recommendation")
        print("=========================================")
        print("")
        print(f"Genre              : {genre_map[genre]}")
        print("")
        print(f"Mood               : {mood_map[mood]}")
        print("")
        print(f"Duration           : {duration_map[duration]}")
        print("")
        print("Recommended Playlist")
        print(selection["playlist"])
        print("")
        print("Recommended Artist")
        print(artist)
        print("")
        print("Recommended Song")
        print(song)
        print("")
        print("Reason")
        print(reason)
        print("")
        print("=========================================\n")
    else:
        print("\n[Error] Unable to generate a playlist with the given parameters.")
        
    input("Press Enter to return to the main menu...")


def view_genres():
    """Displays the list of supported music genres."""
    clear_screen()
    print("\n--- Available Genres ---")
    print("1. Pop - Catchy melodies and upbeat rhythms.")
    print("2. Rock - Strong beats and electric guitars.")
    print("3. Hip-Hop - Rhythmic music and rhyming speech.")
    print("4. Jazz - Improvisation and swing rhythms.")
    print("5. Classical - Orchestral and traditional compositions.")
    input("\nPress Enter to return to the main menu...")

def view_moods():
    clear_screen()
    print("\n--- Available Moods ---")
    print("1. Happy")
    print("2. Relaxed")
    print("3. Energetic")
    print("4. Sad")
    input("\nPress Enter to return to the main menu...")

def view_history():
    clear_screen()
    print("\n--- Recommendation History ---")
    if not history:
        print("No recommendation history available.")
    else:
        for i, item in enumerate(history, start=1):
            print(f"Recommendation {i}")
            print("-" * 40)
            print(f"Genre     : {item['genre']}")
            print(f"Mood      : {item['mood']}")
            print(f"Duration  : {item['duration']}")
            print(f"Playlist  : {item['playlist']}")
            print(f"Artist    : {item['artist']}")
            print(f"Song      : {item['song']}")
            print("-" * 40)

    input("\nPress Enter to return...")


def about_spotify():
    """Explains the connection between Spotify and the Disruptive Innovation Model."""
    clear_screen()
    print("\n--- About Spotify & Disruptive Innovation ---")
    print("Spotify is a leading digital music streaming service. As discussed in")
    print("Part 1 of our project, Spotify represents Clayton Christensen's")
    print("Disruptive Innovation Model. It disrupted the traditional physical")
    print("record market (CDs/Vinyl) and early digital downloading models (like")
    print("iTunes) by offering a subscription-based, on-demand streaming service.")
    print("This program mimics its core algorithm by recommending playlists")
    print("based on user preferences, genre, mood, and listening habits.")
    input("\nPress Enter to return to the main menu...")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice:")

        if choice == "1":
            recommend_playlist()
        
        elif choice == "2":
            view_genres()

        elif choice == "3":
            view_moods()

        elif choice == "4":
            view_history()

        elif choice == "5":
            about_spotify()

        elif choice == "6":
            clear_screen()
            print("Thank you for using Spotify Smart Playlist Recommender!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()