movies_data = [
    {'name': 'The Matrix', 'director': 'Wachowskis', 'year': '1995'}
]


def menu():
    menu_string = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie and 'q' to quit: "
    user_input = input(menu_string)

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies_data)
        elif user_input == 'f':
            find_movie()
        elif user_input == 'q':
            print('Stopping program')
        else:
            print('input is invalid')

        user_input = input(menu_string)


def add_movie():
    name = input('Enter the movie name: ')
    director = input('Enter the movie director: ')
    year = input('Enter the movie release year: ')

    movie = {
        'name': name,
        'director': director,
        'year': year
    }

    movies_data.append(movie)


def show_movies(movies):
    for movie in movies:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}\n")


def find_movie():
    property = input("What property of the movie are you looking for? ")
    value = input("What are you searching for? ")

    found_movies = find_by_attribute(movies_data, value, lambda x: x[property])
    show_movies(found_movies)


def find_by_attribute(items, value, finder):
    found = []

    for i in items:
        if finder(i) == value:
            found.append(i)

    return found


menu()