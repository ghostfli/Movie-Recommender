from UserRatings import UserRatings
from Movie_df import Movies

class MovieRecommender():

    def __init__(self, userid: int) -> None:
        self.userid = userid
        self.ratings = self.get_ratings()
        self.genre_vector = []
        

    def get_ratings(self):
        ratings = []
        userdf = UserRatings()
        for index, row in userdf.df.iterrows():
            if(row['userId'] == self.userid):
                ratings.append((row['movieId'], row['rating']))
        return ratings
    
    def print_movie_genre_and_rating(self):
        movies = Movies()
        for movie in self.ratings:
            row = movies.df.loc[movies.df['movieId'] == movie[0]]
            print(row['movieId'].to_string(index=False), row['title'].to_string(index=False), row['genres'].to_string(index=False), movie[1])

    def print_genre_vector(self):
        for tuple in self.genre_vector:
            print(tuple)


    def create_genre_vector(self):
        genre_vec = []
        movies = Movies()
        for movie in self.ratings:
            row = movies.df.loc[movies.df['movieId'] == movie[0]]
            #Split genre by | delimeters
            genres = row['genres'].to_string(index=False).split('|')
            for genre in genres:
                tuple_exists = False
                for genre_list in genre_vec:
                    if (genre_list[0] == genre):
                        #Indicates we have found a existing tuple for this genre
                        tuple_exists = True
                        #genre_tuple[1] : contains sum of ratings for this genre
                        genre_list[1] += movie[1]
                        #genre_tuple[2] : number of ratings for this genre
                        genre_list[2] += 1
                        #genre_tuple[3] : genre_tuple[1] / genre_tuple[2]
                        genre_list[3] = genre_list[1] / genre_list[2]
                        break

                if (tuple_exists == False):
                    #Create a tuple then
                    new_list = [genre, movie[1], 1, movie[1]]
                    genre_vec.append(new_list)
                
            
        self.genre_vector = genre_vec




if __name__ == "__main__":
    MR = MovieRecommender(1)
    #MR.print_movie_genre_and_rating()
    MR.create_genre_vector()
    MR.print_genre_vector()
