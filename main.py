import os
import subprocess
import random

# ─────────────────────────────────────────────
#  ANSI COLOR CODES  (Spotify-inspired)
# ─────────────────────────────────────────────
GREEN  = "\033[38;2;29;185;84m"    # Spotify Green  #1DB954
WHITE  = "\033[97m"
GREY   = "\033[90m"
YELLOW = "\033[93m"
RED    = "\033[91m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RESET  = "\033[0m"

history = []

# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────
def clear_screen():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

def divider():
    print(GREEN + "  =================================================" + RESET)

def thin_divider():
    print(GREY + "  -------------------------------------------------" + RESET)

def press_enter():
    input(GREY + "\n  Press Enter to return to the main menu..." + RESET)

def get_valid_choice(prompt, valid_choices):
    while True:
        choice = input(GREEN + "  >> " + WHITE + prompt + RESET + " ")
        if choice in valid_choices:
            return choice
        print(YELLOW + "  ⚠  Invalid input. Please try again.\n" + RESET)

# ─────────────────────────────────────────────
#  SCREEN 1: MAIN MENU
# ─────────────────────────────────────────────
def show_menu():
    clear_screen()
    print()
    divider()
    print(GREEN + BOLD +
          "      ___  ___  ___ ______ __  ____  __  __ \n"
          "     / __\\/ _ \\/ _ \\__  __/  \\/ _  \\/ _\\/ /\n"
          "     \\__ \\/ ___/ // / / / / /\\/ / / /\\ \\/ / \n"
          "    /____/_/  /____/ /_/ /_/  /_____/_/\\_/  \n"
          + RESET)
    print(GREEN + "        ♫   Smart Playlist Recommender   ♫\n" + RESET)
    divider()
    print()
    print(GREEN + "  [ 1 ]  " + WHITE + "Get Playlist Recommendation" + RESET)
    print(GREEN + "  [ 2 ]  " + WHITE + "View Available Genres" + RESET)
    print(GREEN + "  [ 3 ]  " + WHITE + "View Available Moods" + RESET)
    print(GREEN + "  [ 4 ]  " + WHITE + "View Recommendation History" + RESET)
    print(GREEN + "  [ 5 ]  " + WHITE + "About Spotify & Its Innovation" + RESET)
    print(GREEN + "  [ 6 ]  " + WHITE + "Exit" + RESET)
    print()
    divider()
    print()

# ─────────────────────────────────────────────
#  SCREEN 2: RECOMMENDATION FLOW
# ─────────────────────────────────────────────
def recommend_playlist():
    clear_screen()
    print()
    divider()
    print(GREEN + BOLD + "  ♫  PLAYLIST RECOMMENDATION\n" + RESET)
    divider()

    genre_map    = {"1": "Pop", "2": "Rock", "3": "Hip-Hop", "4": "Jazz", "5": "Classical"}
    mood_map     = {"1": "Happy", "2": "Relaxed", "3": "Energetic", "4": "Sad"}
    duration_map = {"1": "Short (15 mins)", "2": "Medium (30–60 mins)", "3": "Long (2+ hours)"}

    # ── STEP 1: GENRE ──
    print()
    print(WHITE + "  STEP 1 of 3   Choose Genre\n" + RESET)
    print(GREEN + "  [ 1 ]  " + WHITE + "Pop" + RESET)
    print(GREEN + "  [ 2 ]  " + WHITE + "Rock" + RESET)
    print(GREEN + "  [ 3 ]  " + WHITE + "Hip-Hop" + RESET)
    print(GREEN + "  [ 4 ]  " + WHITE + "Jazz" + RESET)
    print(GREEN + "  [ 5 ]  " + WHITE + "Classical" + RESET)
    print()
    genre = get_valid_choice("Enter genre (1-5):", ["1","2","3","4","5"])

    # ── STEP 2: MOOD ──
    clear_screen()
    print()
    divider()
    print(GREEN + BOLD + "  ♫  PLAYLIST RECOMMENDATION\n" + RESET)
    divider()
    print()
    print(WHITE + "  STEP 2 of 3   Choose Mood\n" + RESET)
    print(GREEN + "  [ 1 ]  " + WHITE + "Happy      :D" + RESET)
    print(GREEN + "  [ 2 ]  " + WHITE + "Relaxed    ~" + RESET)
    print(GREEN + "  [ 3 ]  " + WHITE + "Energetic  !!" + RESET)
    print(GREEN + "  [ 4 ]  " + WHITE + "Sad        :(" + RESET)
    print()
    mood = get_valid_choice("Enter mood (1-4):", ["1","2","3","4"])

    # ── STEP 3: DURATION ──
    clear_screen()
    print()
    divider()
    print(GREEN + BOLD + "  ♫  PLAYLIST RECOMMENDATION\n" + RESET)
    divider()
    print()
    print(WHITE + "  STEP 3 of 3   Listening Duration\n" + RESET)
    print(GREEN + "  [ 1 ]  " + WHITE + "Short      (15 mins)" + RESET)
    print(GREEN + "  [ 2 ]  " + WHITE + "Medium     (30–60 mins)" + RESET)
    print(GREEN + "  [ 3 ]  " + WHITE + "Long       (2+ hours)" + RESET)
    print()
    duration = get_valid_choice("Enter duration (1-3):", ["1","2","3"])

    # ── RECOMMENDATION DICTIONARY ──
    recommendations = {
        # ── Pop ──
        ("1","1"): {"playlist":"Today's Top Hits",    "artists":["Taylor Swift","Olivia Rodrigo","Sabrina Carpenter"],         "songs":["Cruel Summer","vampire","Espresso"]},
        ("1","2"): {"playlist":"Chill Hits",           "artists":["Billie Eilish","Lauv","Conan Gray"],                         "songs":["Ocean Eyes","I Like Me Better","Heather"]},
        ("1","3"): {"playlist":"Pop Rising",           "artists":["Dua Lipa","Ariana Grande","Doja Cat"],                       "songs":["Levitating","yes, and?","Paint The Town Red"]},
        ("1","4"): {"playlist":"Sad Pop Mix",          "artists":["Billie Eilish","Lewis Capaldi","Adele"],                     "songs":["What Was I Made For?","Someone You Loved","Easy On Me"]},
        # ── Rock ──
        ("2","1"): {"playlist":"Rock Classics",        "artists":["Queen","Bon Jovi","Journey"],                                "songs":["Don't Stop Me Now","Livin' On A Prayer","Don't Stop Believin'"]},
        ("2","2"): {"playlist":"Soft Rock Drive",      "artists":["Coldplay","The Script","Imagine Dragons"],                   "songs":["Yellow","Breakeven","Demons"]},
        ("2","3"): {"playlist":"Rock Workout",         "artists":["AC/DC","Linkin Park","Metallica"],                           "songs":["Thunderstruck","Numb","Enter Sandman"]},
        ("2","4"): {"playlist":"Acoustic Rock",        "artists":["Nirvana","Foo Fighters","Pearl Jam"],                        "songs":["Something In The Way","Everlong","Black"]},
        # ── Hip-Hop ──
        ("3","1"): {"playlist":"RapCaviar",            "artists":["Drake","Travis Scott","Lil Baby"],                           "songs":["God's Plan","SICKO MODE","Drip Too Hard"]},
        ("3","2"): {"playlist":"Mellow Bars",          "artists":["J. Cole","Kendrick Lamar","Logic"],                          "songs":["No Role Modelz","LOVE.","1-800-273-8255"]},
        ("3","3"): {"playlist":"Beast Mode",           "artists":["Eminem","50 Cent","DMX"],                                    "songs":["Till I Collapse","In Da Club","X Gon' Give It To Ya"]},
        ("3","4"): {"playlist":"Late Night Hip-Hop",   "artists":["Kendrick Lamar","Post Malone","The Weeknd"],                 "songs":["PRIDE.","Circles","Call Out My Name"]},
        # ── Jazz ──
        ("4","1"): {"playlist":"Jazz Vibes",           "artists":["Louis Armstrong","Ella Fitzgerald","Frank Sinatra"],         "songs":["What A Wonderful World","Dream A Little Dream Of Me","Fly Me To The Moon"]},
        ("4","2"): {"playlist":"Smooth Jazz",          "artists":["Kenny G","Dave Koz","George Benson"],                        "songs":["Songbird","You Make Me Smile","Breezin'"]},
        ("4","3"): {"playlist":"Jazz Fusion",          "artists":["Miles Davis","Herbie Hancock","Chick Corea"],                 "songs":["So What","Chameleon","Spain"]},
        ("4","4"): {"playlist":"Blue Note Sessions",   "artists":["John Coltrane","Chet Baker","Bill Evans"],                   "songs":["In A Sentimental Mood","My Funny Valentine","Peace Piece"]},
        # ── Classical ──
        ("5","1"): {"playlist":"Mozart for Joy",       "artists":["Mozart","Beethoven","Haydn"],                                "songs":["Eine kleine Nachtmusik","Symphony No. 5","The Creation"]},
        ("5","2"): {"playlist":"Peaceful Piano",       "artists":["Ludovico Einaudi","Yiruma","Max Richter"],                   "songs":["Nuvole Bianche","River Flows In You","On The Nature Of Daylight"]},
        ("5","3"): {"playlist":"Classical Focus",      "artists":["Johann Sebastian Bach","Antonio Vivaldi","Philip Glass"],    "songs":["Cello Suite No.1","Spring","Opening"]},
        ("5","4"): {"playlist":"Classical Essentials", "artists":["Frederic Chopin","Claude Debussy","Pyotr Tchaikovsky"],      "songs":["Nocturne Op.9 No.2","Clair de Lune","Swan Lake"]},
    }

    selection = recommendations.get((genre, mood))
    if not selection:
        print(RED + "\n  [Error] Unable to generate a playlist." + RESET)
        press_enter()
        return

    artist = random.choice(selection["artists"])
    song   = random.choice(selection["songs"])

    duration_reason = {
        "1": "Great for a quick 15-minute mood boost.",
        "2": "Perfect for a 30–60 minute focused session.",
        "3": "Ideal for a long 2+ hour deep listening journey.",
    }

    # Save to history
    history.append({
        "genre":    genre_map[genre],
        "mood":     mood_map[mood],
        "duration": duration_map[duration],
        "playlist": selection["playlist"],
        "artist":   artist,
        "song":     song,
    })

    # ── RESULTS SCREEN ──
    clear_screen()
    print()
    divider()
    print(GREEN + BOLD + "  ♫  YOUR RECOMMENDATION\n" + RESET)
    divider()
    print()
    print(GREY   + "  Genre     :  " + RESET + WHITE + genre_map[genre] + RESET)
    print(GREY   + "  Mood      :  " + RESET + WHITE + mood_map[mood] + RESET)
    print(GREY   + "  Duration  :  " + RESET + WHITE + duration_map[duration] + RESET)
    print()
    thin_divider()
    print()
    print(GREEN + "  +-------------------------------------------------+")
    print("  |                                                 |")
    print("  |  " + RESET + WHITE + BOLD + "Playlist  :  " + RESET + WHITE
          + selection["playlist"].ljust(35) + GREEN + "|")
    print(GREEN + "  |  " + RESET + WHITE + BOLD + "Artist    :  " + RESET + WHITE
          + artist.ljust(35) + GREEN + "|")
    print(GREEN + "  |  " + RESET + WHITE + BOLD + "Song      :  " + RESET + WHITE
          + song.ljust(35) + GREEN + "|")
    print(GREEN + "  |                                                 |")
    print("  +-------------------------------------------------+" + RESET)
    print()
    print(YELLOW + "  Why this pick:" + RESET)
    print(WHITE  + "  " + duration_reason[duration] + RESET)
    print()
    divider()
    press_enter()

# ─────────────────────────────────────────────
#  SCREEN 3: VIEW GENRES
# ─────────────────────────────────────────────
def view_genres():
    clear_screen()
    print()
    divider()
    print(GREEN + BOLD + "  ♫  AVAILABLE GENRES\n" + RESET)
    divider()
    print()
    genres = [
        ("Pop",       "Catchy melodies and upbeat rhythms."),
        ("Rock",      "Strong beats and electric guitars."),
        ("Hip-Hop",   "Rhythmic music and rhyming speech."),
        ("Jazz",      "Improvisation and swing rhythms."),
        ("Classical", "Orchestral and traditional compositions."),
    ]
    for i, (name, desc) in enumerate(genres, 1):
        print(GREEN + f"  [ {i} ]  " + WHITE + BOLD + f"{name}" + RESET)
        print(GREY  + f"         {desc}" + RESET)
        print()
    divider()
    press_enter()

# ─────────────────────────────────────────────
#  SCREEN 4: VIEW MOODS
# ─────────────────────────────────────────────
def view_moods():
    clear_screen()
    print()
    divider()
    print(GREEN + BOLD + "  ♫  AVAILABLE MOODS\n" + RESET)
    divider()
    print()
    moods = [
        ("Happy",     "Upbeat, joyful, feel-good energy.      :D"),
        ("Relaxed",   "Calm, easy-listening, low-energy.      ~"),
        ("Energetic", "High-tempo, hype, workout-ready.       !!"),
        ("Sad",       "Emotional, melancholic, reflective.    :("),
    ]
    for i, (name, desc) in enumerate(moods, 1):
        print(GREEN + f"  [ {i} ]  " + WHITE + BOLD + f"{name}" + RESET)
        print(GREY  + f"         {desc}" + RESET)
        print()
    divider()
    press_enter()

# ─────────────────────────────────────────────
#  SCREEN 5: HISTORY
# ─────────────────────────────────────────────
def view_history():
    clear_screen()
    print()
    divider()
    print(GREEN + BOLD + "  ♫  RECOMMENDATION HISTORY\n" + RESET)
    divider()
    print()

    if not history:
        print(GREY + "  No history yet. Get your first recommendation!\n" + RESET)
    else:
        for i, item in enumerate(history, 1):
            print(GREEN + f"  Recommendation #{i}" + RESET)
            print(GREY  + "  " + "-"*43 + RESET)
            print(WHITE + f"  Genre     :  " + RESET + item["genre"])
            print(WHITE + f"  Mood      :  " + RESET + item["mood"])
            print(WHITE + f"  Duration  :  " + RESET + item["duration"])
            print(WHITE + f"  Playlist  :  " + RESET + item["playlist"])
            print(GREEN + f"  Artist    :  " + RESET + item["artist"])
            print(GREEN + f"  Song      :  " + RESET + item["song"])
            print()

    divider()
    press_enter()

# ─────────────────────────────────────────────
#  SCREEN 6: ABOUT
# ─────────────────────────────────────────────
def about_spotify():
    clear_screen()
    print()
    divider()
    print(GREEN + BOLD + "  ♫  ABOUT SPOTIFY & DISRUPTIVE INNOVATION\n" + RESET)
    divider()
    print()
    print(WHITE + "  Spotify is a leading digital music streaming service.\n" + RESET)
    print(WHITE + "  As discussed in Part 1 of our project, Spotify\n"
                  "  represents Clayton Christensen's Disruptive\n"
                  "  Innovation Model.\n" + RESET)
    thin_divider()
    print()
    print(GREY + "  How Spotify disrupted the market:\n" + RESET)
    disruptions = [
        "Replaced physical CDs and vinyl records.",
        "Disrupted digital downloads (e.g. iTunes).",
        "Introduced subscription-based on-demand streaming.",
        "Used data-driven personalisation at scale.",
        "Made music accessible globally on any device.",
    ]
    for d in disruptions:
        print(GREEN + "    •  " + WHITE + d + RESET)
    print()
    thin_divider()
    print()
    print(GREY + "  This program mimics Spotify's core recommendation\n"
                 "  algorithm by suggesting playlists based on genre,\n"
                 "  mood, and listening habits.\n" + RESET)
    divider()
    press_enter()

# ─────────────────────────────────────────────
#  MAIN LOOP
# ─────────────────────────────────────────────
def main():
    while True:
        show_menu()
        choice = input(GREEN + "  >> " + WHITE + "Enter your choice (1-6): " + RESET + " ")
        print()

        if   choice == "1": recommend_playlist()
        elif choice == "2": view_genres()
        elif choice == "3": view_moods()
        elif choice == "4": view_history()
        elif choice == "5": about_spotify()
        elif choice == "6":
            clear_screen()
            print()
            divider()
            print(GREEN + BOLD + "  Thanks for using Spotify Playlist Recommender!  ♫\n" + RESET)
            print(WHITE + "  Keep streaming. Keep discovering.\n" + RESET)
            divider()
            print()
            break
        else:
            print(YELLOW + "  ⚠  Invalid choice. Please enter 1–6.\n" + RESET)

if __name__ == "__main__":
    main()