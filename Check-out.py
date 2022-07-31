import os
#from statistics import mean, median
#from pandas import read_csv #, DataFrame

# DOWNLOAD FILES

CSV_FILES = [
    {"filepath": "products.csv", "url": "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.csv"},
]
for csv_file in CSV_FILES:
    if not os.path.isfile(csv_file["filepath"]):
        print("DOWNLOADING", csv_file["filepath"])
        url = csv_file["url"]
        # FYI: this wget command is a terminal command, NOT python
        # ... in colab, we can execute terminal commands by prefixing them with an exclamation point
        # ... students are not responsible for knowing terminal commands like this
        !wget -q $url 