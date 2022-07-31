import os
from statistics import mean, median
from pandas import read_csv , DataFrame

# DOWNLOAD FILES

CSV_FILES = [
    {"filepath": "products.csv", "url": "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.csv"},
]
for csv_file in CSV_FILES:
    if not os.path.isfile(csv_file["filepath"]):
        print("DOWNLOADING", csv_file["filepath"])
        url = csv_file["url"]
        !wget -q $url 

df = read_csv("products.csv")
print(len(df))
print(df.head())

for index, row in df.iterrows():
    print(row["name"], to_usd(row["price"]))