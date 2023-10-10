from UserRatings import UserRatings
from Movie_df import Movies

class MovieRecommender():

    def __init__(self, userid: int) -> None:
        self.userid = userid
        self.ratings = self.get_ratings()

    def get_ratings(self):
        ratings = []
        userdf = UserRatings()
        for index, row in userdf.df.iterrows():
            if(row['userId'] == self.userid):
                ratings.append((row['movieId'], row['rating']))
        return ratings
    
    def print_movies_review_and_rating(self):
        movies = Movies()
        for movie in self.ratings:
            row = movies.df.loc[movies.df['movieId'] == movie[0]]
            print(row['movieId'].to_string(index=False), row['title'].to_string(index=False), movie[1])

if __name__ == "__main__":
    MR = MovieRecommender(1)
    MR.print_movies_review_and_rating()
