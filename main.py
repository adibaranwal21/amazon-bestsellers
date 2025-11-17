import pandas as pd

df = pd.read_csv('bestsellers.csv')

df.drop_duplicates(inplace=True)

df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
# Renames columns

df["Price"] = df["Price"].astype(float) # Converts prices to floats