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
        "tracks": [
            {"artist": "Taylor Swift", "song": "Cruel Summer"},
            {"artist": "Olivia Rodrigo", "song": "vampire"},
            {"artist": "Sabrina Carpenter", "song": "Espresso"}
        ]
    },

    ("1", "2"): {
        "playlist": "Chill Hits",
        "tracks": [
            {"artist": "Billie Eilish", "song": "Ocean Eyes"},
            {"artist": "Lauv", "song": "I Like Me Better"},
            {"artist": "Conan Gray", "song": "Heather"}
        ]
    },

    ("1", "3"): {
        "playlist": "Pop Rising",
        "tracks": [
            {"artist": "Dua Lipa", "song": "Levitating"},
            {"artist": "Ariana Grande", "song": "yes, and?"},
            {"artist": "Doja Cat", "song": "Paint The Town Red"}
        ]
    },

    ("1", "4"): {
        "playlist": "Sad Pop Mix",
        "tracks": [
            {"artist": "Billie Eilish", "song": "What Was I Made For?"},
            {"artist": "Lewis Capaldi", "song": "Someone You Loved"},
            {"artist": "Adele", "song": "Easy On Me"}
        ]
    },

    # ================= Rock =================
    ("2", "1"): {
        "playlist": "Rock Classics",
        "tracks": [
            {"artist": "Queen", "song": "Don't Stop Me Now"},
            {"artist": "Bon Jovi", "song": "Livin' On A Prayer"},
            {"artist": "Journey", "song": "Don't Stop Believin'"}
        ]
    },

    ("2", "2"): {
        "playlist": "Soft Rock Drive",
        "tracks": [
            {"artist": "Coldplay", "song": "Yellow"},
            {"artist": "The Script", "song": "Breakeven"},
            {"artist": "Imagine Dragons", "song": "Demons"}
        ]
    },

    ("2", "3"): {
        "playlist": "Rock Workout",
        "tracks": [
            {"artist": "AC/DC", "song": "Thunderstruck"},
            {"artist": "Linkin Park", "song": "Numb"},
            {"artist": "Metallica", "song": "Enter Sandman"}
        ]
    },

    ("2", "4"): {
        "playlist": "Acoustic Rock",
        "tracks": [
            {"artist": "Nirvana", "song": "Something In The Way"},
            {"artist": "Foo Fighters", "song": "Everlong"},
            {"artist": "Pearl Jam", "song": "Black"}
        ]
    },

    # ================= Hip-Hop =================
    ("3", "1"): {
        "playlist": "RapCaviar",
        "tracks": [
            {"artist": "Drake", "song": "God's Plan"},
            {"artist": "Travis Scott", "song": "SICKO MODE"},
            {"artist": "Lil Baby", "song": "Drip Too Hard"}
        ]
    },

    ("3", "2"): {
        "playlist": "Mellow Bars",
        "tracks": [
            {"artist": "J. Cole", "song": "No Role Modelz"},
            {"artist": "Kendrick Lamar", "song": "LOVE."},
            {"artist": "Logic", "song": "1-800-273-8255"}
        ]
    },

    ("3", "3"): {
        "playlist": "Beast Mode",
        "tracks": [
            {"artist": "Eminem", "song": "Till I Collapse"},
            {"artist": "50 Cent", "song": "In Da Club"},
            {"artist": "DMX", "song": "X Gon' Give It To Ya"}
        ]
    },

    ("3", "4"): {
        "playlist": "Late Night Hip-Hop",
        "tracks": [
            {"artist": "Kendrick Lamar", "song": "PRIDE."},
            {"artist": "Post Malone", "song": "Circles"},
            {"artist": "The Weeknd", "song": "Call Out My Name"}
        ]
    },

    # ================= Jazz =================
    ("4", "1"): {
        "playlist": "Jazz Vibes",
        "tracks": [
            {"artist": "Louis Armstrong", "song": "What A Wonderful World"},
            {"artist": "Ella Fitzgerald", "song": "Dream A Little Dream Of Me"},
            {"artist": "Frank Sinatra", "song": "Fly Me To The Moon"}
        ]
    },

    ("4", "2"): {
        "playlist": "Smooth Jazz",
        "tracks": [
            {"artist": "Kenny G", "song": "Songbird"},
            {"artist": "Dave Koz", "song": "You Make Me Smile"},
            {"artist": "George Benson", "song": "Breezin'"}
        ]
    },

    ("4", "3"): {
        "playlist": "Jazz Fusion",
        "tracks": [
            {"artist": "Miles Davis", "song": "So What"},
            {"artist": "Herbie Hancock", "song": "Chameleon"},
            {"artist": "Chick Corea", "song": "Spain"}
        ]
    },

    ("4", "4"): {
        "playlist": "Blue Note Sessions",
        "tracks": [
            {"artist": "John Coltrane", "song": "In A Sentimental Mood"},
            {"artist": "Chet Baker", "song": "My Funny Valentine"},
            {"artist": "Bill Evans", "song": "Peace Piece"}
        ]
    },

    # ================= Classical =================
    ("5", "1"): {
        "playlist": "Mozart for Joy",
        "tracks": [
            {"artist": "Mozart", "song": "Eine kleine Nachtmusik"},
            {"artist": "Beethoven", "song": "Symphony No. 5"},
            {"artist": "Haydn", "song": "The Creation"}
        ]
    },

    ("5", "2"): {
        "playlist": "Peaceful Piano",
        "tracks": [
            {"artist": "Ludovico Einaudi", "song": "Nuvole Bianche"},
            {"artist": "Yiruma", "song": "River Flows In You"},
            {"artist": "Max Richter", "song": "On The Nature Of Daylight"}
        ]
    },

    ("5", "3"): {
        "playlist": "Classical Focus",
        "tracks": [
            {"artist": "Johann Sebastian Bach", "song": "Cello Suite No.1"},
            {"artist": "Antonio Vivaldi", "song": "Spring"},
            {"artist": "Philip Glass", "song": "Opening"}
        ]
    },

    ("5", "4"): {
        "playlist": "Classical Essentials",
        "tracks": [
            {"artist": "Frédéric Chopin", "song": "Nocturne Op.9 No.2"},
            {"artist": "Claude Debussy", "song": "Clair de Lune"},
            {"artist": "Pyotr Ilyich Tchaikovsky", "song": "Swan Lake"}
        ]
    }

}

    selection = recommendations.get((genre, mood))
    track = random.choice(selection["tracks"])
    artist = track["artist"]
    song = track["song"]

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
        print("Recommended Playlist:")
        print(selection["playlist"])
        print("")
        print("Recommended Song:")
        print(song)
        print("Artist:")
        print(artist)
        print("")
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