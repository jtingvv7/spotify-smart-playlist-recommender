def show_menu():
    print("\n")
    print("Spotify Smart Playlist Recommender")
    print("\n")
    print("1. Get Playlist Recommendation")
    print("2. View Available Genres")
    print("3. About Spotify")
    print("4. Exit")

def main():
    show_menu()
    choice = input("Enter your choice:")

    if choice == "1":
        print("Playlist Recommendation")
        
    elif choice == "2":
        print("Available Genres")

    elif choice == "3":
        print("About Spotify")

    elif choice == "4":
        print("Thank you for using Spotify Smart Playlist Recommender!")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()