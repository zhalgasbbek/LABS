
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]



def is_high_imdb(movie):
    return movie["imdb"] > 5.5



def high_imdb_movies(movies_list):
    return [movie for movie in movies_list if is_high_imdb(movie)]



def movies_by_category(movies_list, category):
    return [movie for movie in movies_list if movie["category"] == category]



def average_imdb(movies_list):
    if not movies_list:
        return 0  # Avoid division by zero if the list is empty
    total_score = sum(movie["imdb"] for movie in movies_list)
    return total_score / len(movies_list)



def average_imdb_by_category(movies_list, category):
    category_movies = movies_by_category(movies_list, category)
    return average_imdb(category_movies)

"""
# Example usage:
# 1. Check if IMDB score is above 5.5 for a single movie
print(is_high_imdb(movies[0]))  # Example usage for the first movie

# 2. Get a sublist of movies with IMDB score above 5.5
print(high_imdb_movies(movies))
"""
# 3. Get movies under a specific category
print(movies_by_category(movies, "Romance"))

# 4. Compute the average IMDB score for a list of movies
print(average_imdb(movies))

# 5. Compute the average IMDB score for a specific category
print(average_imdb_by_category(movies, "Romance"))
