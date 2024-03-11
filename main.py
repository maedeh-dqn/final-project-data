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
    
def question_2():
    New_data = get_data()
    distribution_per_year = New_data["release_year"].value_counts()
    distribution_per_year.plot(kind="bar", figsize=(10, 10))
    plt.ylabel('Frequency')
    plt.title('Release Trend')
    plt.show()
    
def question_3():
    New_data = get_data()
    df = New_data[["release_year", "runtime"]]
    df = df.drop(df[df["runtime"] == 0].index)
    Ave_runtime_per_year_df = df.groupby("release_year").mean().reset_index()
    Ave_runtime_per_year_df.to_csv(".\Question_3.csv")
    
def question_4():
    New_data = get_data()
    df = New_data[["release_year", "runtime"]]
    df = df.drop(df[df["runtime"] == 0].index)
    Ave_runtime_per_year_df = df.groupby("release_year").mean().reset_index()
    Ave_runtime_per_year_df["hour_min_format"] = pd.to_datetime(Ave_runtime_per_year_df.runtime, unit="m").dt.strftime("%H:%M")
    Ave_runtime_per_year_df.to_csv(".\Question_4.csv")
    
def question_5_part_a():
    New_data = get_data()
    sho_lo_df = New_data[["original_title", "runtime"]]
    sho_lo_df = sho_lo_df.drop(sho_lo_df[sho_lo_df["runtime"] == 0].index)

    Minimum_runtimes = pd.DataFrame(columns=["original_title", "runtime"])
    sho_lo_df = sho_lo_df.sort_values("runtime")

    min = sho_lo_df.iloc[0].get("runtime")

    for index, row in sho_lo_df.iterrows():
        if row.get("runtime") > min:
            break
        else:
            Minimum_runtimes.loc[index] = row

    Minimum_runtimes.to_csv(".\Question_5_PartA.csv")
    
question_5_part_a()