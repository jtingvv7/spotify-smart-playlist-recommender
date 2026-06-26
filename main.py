import os
import subprocess

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
    print("3. About Spotify & Its Innovation")
    print("4. Exit")
    print("="*41)

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

    # Input loop for Genre
    while True:
        print("Choose Genre:")
        print("1. Pop   2. Rock   3. Hip-Hop   4. Jazz   5. Classical")
        genre = input("Enter genre (1-5): ")
        if genre in valid_genres:
            break
        print("[Error] Invalid genre. Please try again.\n")

    print("-" * 30)
    
    # Input loop for Mood
    while True:
        print("Choose Mood:")
        print("1. Happy   2. Relaxed   3. Energetic   4. Sad")
        mood = input("Enter mood (1-4): ")
        if mood in valid_moods:
            break
        print("[Error] Invalid mood. Please try again.\n")

    print("-" * 30)

    # Input loop for Duration
    while True:
        print("Listening Duration:")
        print("1. Short (15 mins)   2. Medium (30-60 mins)   3. Long (2+ hours)")
        duration = input("Enter duration (1-3): ")
        if duration in valid_durations:
            break
        print("[Error] Invalid duration. Please try again.\n")

    recommendations = {
        ("1", "1"): {"playlist": "Today's Top Hits", "artist": "Taylor Swift", "song": "Cruel Summer"},
        ("1", "2"): {"playlist": "Chill Hits", "artist": "Ed Sheeran", "song": "Perfect"},
        ("1", "3"): {"playlist": "Pop Rising", "artist": "Dua Lipa", "song": "Levitating"},
        ("1", "4"): {"playlist": "Sad Pop Mix", "artist": "Billie Eilish", "song": "What Was I Made For?"},

        ("2", "1"): {"playlist": "Rock Classics", "artist": "Queen", "song": "Don't Stop Me Now"},
        ("2", "2"): {"playlist": "Soft Rock Drive", "artist": "Coldplay", "song": "Yellow"},
        ("2", "3"): {"playlist": "Rock Workout", "artist": "AC/DC", "song": "Thunderstruck"},
        ("2", "4"): {"playlist": "Acoustic Rock", "artist": "Nirvana", "song": "Something In The Way"},

        ("3", "1"): {"playlist": "RapCaviar", "artist": "Drake", "song": "God's Plan"},
        ("3", "2"): {"playlist": "Mellow Bars", "artist": "J. Cole", "song": "No Role Modelz"},
        ("3", "3"): {"playlist": "Beast Mode", "artist": "Eminem", "song": "Till I Collapse"},
        ("3", "4"): {"playlist": "Late Night Hip-Hop", "artist": "Kendrick Lamar", "song": "PRIDE."},

        ("4", "1"): {"playlist": "Jazz Vibes", "artist": "Louis Armstrong", "song": "What A Wonderful World"},
        ("4", "2"): {"playlist": "Smooth Jazz", "artist": "Kenny G", "song": "Songbird"},
        ("4", "3"): {"playlist": "Jazz Fusion", "artist": "Miles Davis", "song": "So What"},
        ("4", "4"): {"playlist": "Blue Note Sessions", "artist": "John Coltrane", "song": "In A Sentimental Mood"},

        ("5", "1"): {"playlist": "Mozart for Joy", "artist": "Wolfgang Amadeus Mozart", "song": "Eine kleine Nachtmusik"},
        ("5", "2"): {"playlist": "Peaceful Piano", "artist": "Ludovico Einaudi", "song": "Nuvole Bianche"},
        ("5", "3"): {"playlist": "Classical Focus", "artist": "Johann Sebastian Bach", "song": "Cello Suite No. 1"},
        ("5", "4"): {"playlist": "Classical Essentials", "artist": "Frederic Chopin", "song": "Nocturne Op. 9 No. 2"}
    }

    selection = recommendations.get((genre, mood))

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
        print(selection["artist"])
        print("")
        print("Recommended Song")
        print(selection["song"])
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
            about_spotify()

        elif choice == "4":
            clear_screen()
            print("Thank you for using Spotify Smart Playlist Recommender!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()