import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
df = pd.read_csv("data.csv")

# Display all columns
pd.set_option("display.max_columns", None)

# Group data by 'title' and sum the numerical columns
df_grouped = df.groupby("title").sum()

# Sort by 'price' to get the top 10
df_top10 = df_grouped.nlargest(10, 'price')

# Display the filtered data with prices
print("Top 10 Titles by Price:")
print(df_top10[['price']])

# Plot bar chart for 'price' of the top 10 titles
plt.figure(figsize=(10, 6))
df_top10['price'].plot(kind="bar", color="skyblue")
plt.title("Top 10 Titles by Price")
plt.xlabel("Book Title")
plt.ylabel("Price")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Plot bar chart for 'page_count' of the top 10 titles
plt.figure(figsize=(10, 6))
df_top10['page_count'].plot(kind="bar", color="lightcoral")
plt.title("Top 10 Titles by Page Count")
plt.xlabel("Book Title")
plt.ylabel("Page Count")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Display a box plot of the top 10 data
df_top10.plot(kind="box")
plt.title("Boxplot of Numerical Columns for Top 10 Titles")

# Show all plots
plt.show()
