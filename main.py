import pandas as pd

df = pd.read_csv('bestsellers.csv')

df.drop_duplicates(inplace=True)

df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
# Renames columns

df["Price"] = df["Price"].astype(float) # Converts prices to floats

author_counts = df['Author'].value_counts() # Rating of authors
print(author_counts)

avg_rating_by_genre = df.groupby("Genre")["Rating"].mean() # Rating of each genre
print(avg_rating_by_genre)