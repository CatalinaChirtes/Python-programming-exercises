MOVIES_FILE = "movies.txt"


def display_main_menu() -> None:
    print("----------------------------------------------------------\n")
    print("Movie Management System Main Menu\n")
    print("1. Add a movie")
    print("2. Display all movies")
    print("3. Search for a movie")
    print("4. Remove a movie")
    print("5. Exit")
    print()


# Function to read the movies from the file
def read_movies_from_file() -> list:
    try:
        with open(MOVIES_FILE, "r") as file:
            movies = [line.strip().split(",") for line in file.readlines()]
            movies = [(movie[0], float(movie[1])) for movie in movies]
        return movies
    except FileNotFoundError:
        return []


# Function to write a movie to the file
def write_movies_to_file(movies: list) -> None:
    with open(MOVIES_FILE, "w") as file:
        for movie in movies:
            file.write(f"{movie[0]},{movie[1]}\n")


# Function to add a movie to the list of movies
def add_movie() -> None:
    while True:
        title = input("Enter the movie title: ")
        rank = input("Enter the movie rank: ")
        movies = read_movies_from_file()
        title_exists = any(movie[0] == title for movie in movies)

        try:
            rank = float(rank)
            if 1 <= rank <= 10:
                if not title_exists:
                    movies.append((title, rank))
                    write_movies_to_file(movies)
                    print(f"\n'{title}' added successfully.\n")
                    break
                else:
                    print(f"\n'{title}' already exists. Please type another one.\n")
            else:
                print("\nThe entered rank is not between 1 and 10. Please enter a valid number.\n")
        except ValueError:
            print("\nThe entered rank is not a valid input. Please enter a valid number for the rank.\n")


# Function to display all movies
def display_movies() -> None:
    movies = read_movies_from_file()
    if movies:
        print("All the available movies:")
        for idx, movie in enumerate(movies, start=1):
            print(f"Movie no {idx}: \n    Title: {movie[0]} \n    Rank: {movie[1]}\n")
    else:
        print("No movies available.\n")


# Function to search for a specific movie
def search_movie() -> None:
    search_title = input("Enter the title of the movie you are searching for: ")
    movies = read_movies_from_file()
    found_movies = [movie for movie in movies if movie[0] == search_title]
    if found_movies:
        print("\nSearch result:")
        for movie in found_movies:
            print(f"Title: {movie[0]} \nRank: {movie[1]}\n")
    else:
        print("\nMovie not found.\n")


# Function to remove a specific movie
def remove_movie() -> None:
    while True:
        remove_title = input("Enter the title to remove: ")
        movies = read_movies_from_file()
        title_exists = any(movie[0] == remove_title for movie in movies)

        if title_exists:
            updated_movies = [movie for movie in movies if movie[0] != remove_title]
            write_movies_to_file(updated_movies)
            print(f"\n'{remove_title}' removed successfully.\n")
            break
        else:
            print(f"\n'{remove_title}' doesn't exist. Please type another one.\n")


# Function to exit the program
def exit_option() -> None:
    exit("Exiting the movie management system. Thanks for coming by :)")


def error_handler() -> None:
    print("Invalid option. Please try again.\n")


main_actions = {
    "1": add_movie,
    "2": display_movies,
    "3": search_movie,
    "4": remove_movie,
    "5": exit_option
}


if __name__ == "__main__":
    movies_list = read_movies_from_file()
    while True:
        display_main_menu()
        option = input("Enter an option between 1 and 5: ")
        print()
        main_action = main_actions.get(option, error_handler)
        main_action()
