import pandas as pd

df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)
# Dropping unnecessary columns to save ram and time
df.drop(["author", "rating", "voters", "publisher", "page_count", "published_date"], axis=1, inplace=True)
# Dropping all the void/NULL values
df.dropna(axis=1)
# Grouping
df_group = df.groupby("title").sum()
# Taking over the books with the price greater than 0
fliter = df_group[df_group['price'] > 1]
# Displays the types of data within df
print(df.dtypes)


print("The mean/average of the price is: ")
print(fliter.price.mean())
print("The maxium for the dataset is: ")
print(fliter.price.max())
print("The minium for the dataset is: ")
print(fliter.price.min())
print("The range of the dataset is: ")
print(fliter.price.min(), end="-")
print(fliter.price.max(), end="")
