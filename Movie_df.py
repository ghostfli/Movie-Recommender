import pandas as pd

"""
The goal of this class is to create an object which has access to data about the 
most popular 250 movies from Imdb. This data will then be usable for our purpose
of creating a recommendation system.

Desired Data: 
-Title
-Directors
-main actors
-genre
"""

class Movies():

    def __init__(self) -> None:
        #Read from a csv file containing top 250 imdb movies and data
        df = pd.read_csv('./movies.csv')
        self.df = df

    def print_df_head(self):
        print(self.df.head())

        
