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

result = read_csv("products.csv")
print(result)