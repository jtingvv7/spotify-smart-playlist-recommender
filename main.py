def show_menu():
    print("\n")
    print("Spotify Smart Playlist Recommender")
    print("\n")
    print("1. Get Playlist Recommendation")
    print("2. View Available Genres")
    print("3. About Spotify")
    print("4. Exit")

def recommend_playlist():
    print("\nPlaylist Recommendation")

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
    show_menu()
    choice = input("Enter your choice:")

    if choice == "1":
        recommend_playlist()
        
    elif choice == "2":
        view_genres()

    elif choice == "3":
        about_spotify()

    elif choice == "4":
        print("Thank you for using Spotify Smart Playlist Recommender!")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()