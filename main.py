import os
import subprocess

def clear_screen():
    # 'nt' is for windows, 'clear' is for Linux/macOS
    subprocess.run('cls' if os.name == 'nt' else 'clear',shell=True)

def show_menu():
    clear_screen()
    print("\n")
    print("Spotify Smart Playlist Recommender")
    print("\n")
    print("1. Get Playlist Recommendation")
    print("2. View Available Genres")
    print("3. About Spotify")
    print("4. Exit")

def recommend_playlist():

    print("\nPlaylist Recommendation")

    # let user choose genre
    print("\nChoose Genre")
    print("1. Pop")
    print("2. Rock")
    print("3. Hip-Hop")
    print("4. Jazz")
    print("5. Classical")
    genre = input("Enter genre: ")

    # let user choose mood
    print("\nChoose Mood")
    print("1. Happy")
    print("2. Relaxed")
    print("3. Energetic")
    print("4. Sad")
    mood = input("Enter mood: ")

    # let user choose duration
    print("\nListening Duration")
    print("1. Short")
    print("2. Medium")
    print("3. Long")
    duration = input("Enter duration: ")

    # recommendation rules
    recommendations = {
        ("1", "1"): "Today's Top Hits",
        ("1", "2"): "Chill Hits",
        ("1", "3"): "Pop Rising",
        ("1", "4"): "Sad Pop Mix",

        ("2", "1"): "Rock Classics",
        ("2", "2"): "Soft Rock Drive",
        ("2", "3"): "Rock Workout",
        ("2", "4"): "Acoustic Rock",

        ("3", "1"): "RapCaviar",
        ("3", "2"): "Mellow Bars",
        ("3", "3"): "Beast Mode",
        ("3", "4"): "Late Night Hip-Hop",

        ("4", "1"): "Jazz Vibes",
        ("4", "2"): "Smooth Jazz",
        ("4", "3"): "Jazz Fusion",
        ("4", "4"): "Blue Note Sessions",

        ("5", "1"): "Mozart for Joy",
        ("5", "2"): "Peaceful Piano",
        ("5", "3"): "Classical Focus",
        ("5", "4"): "Classical Essentials"
    }

    playlist = recommendations.get((genre, mood))

    if duration == "1":
        reason = "Perfect for a short listening session."
    elif duration == "2":
        reason = "Great for your daily commute or study break."
    elif duration == "3":
        reason = "Ideal for long study or work sessions."
    else:
        reason = "Listening duration not recognised."

    if playlist:
        print("\n====================")
        print("Spotify Recommendation")
        print("\n")
        print("Recommended Playlist :", playlist)
        print("         Reason      :", reason)
    else:
        print("\nInvalid genre or mood selection.")


def view_genres():
    print("\nAvailable Genres")

    print("1. Pop")
    print("2. Rock")
    print("3. Hip-Hop")
    print("4. Jazz")
    print("5. Classical")

    genre = input("\nEnter your choice:")
    print("You selected:", genre)

def about_spotify():
    print("\nSpotify is a digital music streaming service.")
    print("It recommends music based on user preferences,")
    print("including genre, mood and listening habits.")

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