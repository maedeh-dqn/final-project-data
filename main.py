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
    
def question_5_part_b():
    New_data = get_data()
    sho_lo_df = New_data[["original_title", "runtime"]]
    sho_lo_df = sho_lo_df.drop(sho_lo_df[sho_lo_df["runtime"] == 0].index)
    Maximum_runtime = sho_lo_df.loc[sho_lo_df["runtime"].idxmax()]
    print(Maximum_runtime)
    
def question_6_part_a():
    New_data = get_data()
    sho_lo_each_year = New_data[["original_title", "release_year", "runtime"]]
    sho_lo_each_year = sho_lo_each_year.drop(sho_lo_each_year[sho_lo_each_year["runtime"] == 0].index)
    sho_lo_each_year = sho_lo_each_year.sort_values('runtime')

    sho_lo_each_year_grouped = sho_lo_each_year.groupby("release_year")

    Minimum_runtimes_each_year = pd.DataFrame(columns=["original_title", "release_year", "runtime"])
    Minimum_runtimes_each_year_index = 0

    for group_name, group_items in sho_lo_each_year_grouped:
        min = group_items.iloc[0].get("runtime")
        for row_index, row in group_items.iterrows():
            if row.get("runtime") > min:
                break
            else:
                Minimum_runtimes_each_year.loc[Minimum_runtimes_each_year_index] = row
                Minimum_runtimes_each_year_index += 1

    Minimum_runtimes_each_year.to_csv(".\Question_6_PartA.csv")
    
def question_6_part_b():
    New_data = get_data()
    sho_lo_each_year = New_data[["original_title", "release_year", "runtime"]]
    sho_lo_each_year = sho_lo_each_year.drop(sho_lo_each_year[sho_lo_each_year["runtime"] == 0].index)
    sho_lo_each_year = sho_lo_each_year.sort_values('runtime', ascending=False)

    sho_lo_each_year_grouped = sho_lo_each_year.groupby("release_year")

    Maximum_runtimes_each_year = pd.DataFrame(columns=["original_title", "release_year", "runtime"])
    Maximum_runtimes_each_year_index = 0

    for group_name, group_items in sho_lo_each_year_grouped:
        max = group_items.iloc[0].get("runtime")
        for row_index, row in group_items.iterrows():
            if row.get("runtime") < max:
                break
            else:
                Maximum_runtimes_each_year.loc[Maximum_runtimes_each_year_index] = row
                Maximum_runtimes_each_year_index += 1

    Maximum_runtimes_each_year.to_csv(".\Question_6_PartB.csv")  
    
def question_7():
    New_data = get_data()
    runtime_distribution_per_year = New_data[['release_year', 'runtime']]
    runtime_distribution_per_year = runtime_distribution_per_year.drop(runtime_distribution_per_year[runtime_distribution_per_year["runtime"] == 0].index)
    runtime_distribution_per_year = runtime_distribution_per_year.groupby('release_year').sum().reset_index()
    #print(runtime_distribution_per_year.sort_values('runtime'))
    runtime_distribution_per_year.runtime.plot.hist(bins=10, figsize=(10, 10), edgecolor='black', alpha= 0.6, color='yellow')
    plt.title('Rutime Distribution (1960-2015)')
    plt.xlabel('Runtime')
    plt.show()
        
def question_8():
    New_data = get_data()
    budget_alloc_df = New_data[['budget', 'release_year']]
    budget_alloc_df = budget_alloc_df.drop(budget_alloc_df[budget_alloc_df ['budget'] < 500000].index).sort_values('budget').reset_index()
    mean_budget_alloc = budget_alloc_df['budget'].mean()
    print(f'The Average Budget Allocated to Movies During 1960-2015 is: {mean_budget_alloc}')
       
def question_9():
    New_data = get_data()
    revenue_alloc_df = New_data[['revenue', 'release_year']]
    revenue_alloc_df = revenue_alloc_df.drop(revenue_alloc_df[revenue_alloc_df ['revenue'] < 500000].index).sort_values('revenue').reset_index()
    mean_revenue_alloc = revenue_alloc_df['revenue'].mean()
    print(f'The Average Revenue Allocated to Movies During 1960-2015 is: {mean_revenue_alloc}')
    
def question_10():
    New_data = get_data()
    budget_revenue_alloc_df = New_data[['release_year', 'budget', 'revenue']].sort_values('revenue', ascending=True)
    budget_revenue_alloc_df.drop(budget_revenue_alloc_df[budget_revenue_alloc_df ['budget'] < 500000].index, inplace=True)
    budget_revenue_alloc_df.drop(budget_revenue_alloc_df[budget_revenue_alloc_df ['revenue'] < 500000].index, inplace=True)
    mean_budget_revenue_df = budget_revenue_alloc_df.groupby('release_year').mean().reset_index()
    mean_budget_revenue_df.to_csv(".\Question_10.csv")
 
def question_11():
    New_data = get_data()   
    budget_revenue_alloc_df = New_data[['release_year', 'budget', 'revenue']].sort_values('revenue', ascending=True)
    budget_revenue_alloc_df.drop(budget_revenue_alloc_df[budget_revenue_alloc_df ['budget'] < 500000].index, inplace=True)
    budget_revenue_alloc_df.drop(budget_revenue_alloc_df[budget_revenue_alloc_df ['revenue'] < 500000].index, inplace=True)
    mean_budget_revenue_df = budget_revenue_alloc_df.groupby('release_year').mean().reset_index()
    mean_budget_revenue_df.plot.scatter(x='budget', y='revenue', s=100, c='black', alpha= 0.6 )
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Budget Vs. Revenue')
    plt.show()

def question_13():
    New_data = get_data()
    profit_df = New_data[['original_title', 'release_year', 'budget', 'revenue']]
    profit_df.drop(profit_df[profit_df ['budget'] < 500000].index, inplace=True)
    profit_df.drop(profit_df[profit_df ['revenue'] < 500000].index, inplace=True)
    profit_df['profit'] = profit_df["revenue"] - profit_df["budget"]
    #profit_df_sorted = profit_df.sort_values('profit', ascending=False)
    profit_df.to_csv(".\Question_13.csv")
    most_profitable_ever = profit_df.loc[profit_df["profit"].idxmax()]
    print(f'The most profitable movie is:\n {most_profitable_ever}')

def question_14():
    New_data = get_data()
    profit_df = New_data[['original_title', 'release_year', 'budget', 'revenue']]
    profit_df.drop(profit_df[profit_df ['budget'] < 500000].index, inplace=True)
    profit_df.drop(profit_df[profit_df ['revenue'] < 500000].index, inplace=True)
    profit_df['profit'] = profit_df["revenue"] - profit_df["budget"]   
    profit_df_grouped = profit_df.groupby('release_year')
    most_profitable_each_year = pd.DataFrame(columns=['original_title', 'release_year', 'budget', 'revenue', 'profit'])
    most_profitable_each_year_index = 0
    for group_name, group_items in profit_df_grouped:
        max_item = group_items.sort_values('profit', ascending=False).iloc[0]
        most_profitable_each_year.loc[most_profitable_each_year_index] = max_item
        most_profitable_each_year_index += 1

    most_profitable_each_year.to_csv(".\Question_14.csv")

question_14()
        
def question_16():
    New_data = get_data()
    top_5_VC_df = New_data[['original_title', 'release_year', 'vote_count']].sort_values('vote_count', ascending=False).reset_index().head(5)
    top_5_VC_df.to_csv(".\Question_16.csv")
       
def question_17():
    New_data = get_data()
    top_5_VA_df = New_data[['original_title', 'release_year', 'vote_average']].sort_values('vote_average', ascending=False).reset_index().head(5)
    top_5_VA_df.to_csv(".\Question_17.csv")
    
    
    
