# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title=title
        self.seasons=seasons
        self.genres=", ".join(genres)
        self.rating=[]

    def rate(self, rating: int):
        self.rating.append(rating)

    def __str__(self):
        if not self.rating:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {self.genres}\nno ratings"
        return f"{self.title} ({self.seasons} seasons)\ngenres: {self.genres}\n{len(self.rating)} ratings, average {sum(self.rating)/len(self.rating):.1f} points"


def minimum_grade(rating: float, series_list: list):
    aux_list=[]
    for i in range (len(series_list)):
        soma=sum(series_list[i].rating)/len(series_list[i].rating)
 
        if soma>rating:
            aux_list.append(series_list[i])
    return aux_list
            


def includes_genre(genre: str, series_list: list):
    aux_list=[]
    for i in range(len(series_list)):
        if genre in series_list[i].genres:
            aux_list.append(series_list[i])
    return aux_list

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)