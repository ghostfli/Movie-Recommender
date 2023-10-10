import pandas as pd

"""
The goal of this class is to create an object which has access to data about the 
users reviews. All data is from grouplens.org. Specifically the 100k dataset of users
"""

class UserRatings():

    def __init__(self) -> None:
        #Read from a csv file containing top 250 imdb movies and data
        df = pd.read_csv('./ratings.csv')
        df = df[["userId", "movieId", "rating"]]
        self.df = df

    def print_df_head(self):
        print(self.df.head())

        

if __name__ == "__main__":
    movies = UserRatings()
    movies.print_df_head()