import pandas as pd

df = pd.read_csv("movie_dataset.csv")
df.head()

#Question 1
highest_rated_movie = df.loc[df['Rating'].idxmax(), 'Title']
print(highest_rated_movie)

#Question 2
df.dropna()
ave = df['Revenue (Millions)'].mean()
print(ave)

#Question 3
filter_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_rev = filter_df['Revenue (Millions)'].mean()
print(average_rev)

#Question 4
movie_released = len(df[df['Year'] == 2016])
print(movie_released)

#Question 5
movie_ChrisNolan = (df['Director'] == 'Christopher Nolan').sum()
print(movie_ChrisNolan)

#Question 6
high_rating_ = (df['Rating'] >= 8.0).sum()
print(high_rating_)

#Question 7
chris_movies = df[df['Director'] == 'Christopher Nolan']
median_rating_chirs_movies = chris_movies['Rating'].median()
print(median_rating_chirs_movies)

#Question 8
average_rating_by_year = df.groupby('Year')['Rating'].mean()

year_highest = average_rating_by_year.idxmax()
print(year_highest)

#Question 9
movies_in_2006 = (df['Year'] == 2006).sum()
movies_in_2016 = (df['Year'] == 2016).sum()


percentage_increase = ((movies_in_2016 - movies_in_2006) / movies_in_2006) * 100
print(percentage_increase)

#Question 10
all_actors = df['Actors'].str.split(', ', expand=True).stack()

most_common_actor = all_actors.mode()[0]

print(most_common_actor)

#Question 11
all_genre = df['Genre'].str.split(', ', expand=True).stack()


Genres = all_genre.value_counts()
print(Genres)

#Question 12
correlation_matrix = df[['Rank', 'Rating']].corr()
print(correlation_matrix)

"""
1. Positive correlation between Revenue and Votes
2. Positive correlation between Revenue and Runtime
3. No strong correlation between Rating and other features 4. Positive correlation between Rating and Metascore
5. No strong correlation between Year and other feature

Reflected in the runtime, the directors should ensure the storyline captivates the audience. Directors should aim for positive metascore reviews as they do influence the audiences perception of the film. Directors should prefer quality over release year. Therefore prioritising high quality content than solely focusing on the release year.
"""
