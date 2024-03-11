import pandas as pd
import matplotlib.pyplot as plt

def get_data():
    Main_data = pd.read_csv(".\imdb_movies.csv")

    #Checking descriptive statistics for some of the variables
    descriptive_stat = Main_data[["popularity", "budget", "revenue", "runtime", "vote_count", "vote_average", "budget_adj", "revenue_adj",]].describe()  
    descriptive_stat.to_csv('.\Descriptive_Statistics.csv')

    #Remove missing values
    check_nulls = Main_data.isnull()
    #There was no missing data (:

    #Remove duplicates
    New_data = Main_data.drop_duplicates()
    #only one duplcate found :)

    #In New_data I am going to delete some of the columns: Cast Homepage Director Tagline Keywords Overview Release_date
    return New_data.drop(["cast", "homepage", "director", "tagline", "keywords", "overview", "release_date"],axis=1)

def question_1():
    New_data = get_data()
    distribution_per_year = New_data["release_year"].value_counts()
    distribution_per_year.to_csv('.\Question_1.csv')
    
question_1()