# Write your solution here
def find_movies(database: list, search_term: str):
    movies=[]
    for dictionary in database:
        if search_term.lower() in dictionary['name'].lower():
            movies.append(dictionary)
    return movies
        


