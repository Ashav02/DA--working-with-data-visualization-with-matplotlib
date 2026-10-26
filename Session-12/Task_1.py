"""Download a sample sales dataset (for example, from Kaggle or use a small CSV you create) with columns like product,
 category, date, and sales amount. Load it into a Pandas DataFrame and display the first 5 rows to verify the data.
"""

import pandas as pd

df = pd.read_csv("D:\Data Analytics\DA--working-with-data-visualization-with-matplotlib\Session-12\sales_data.csv")

print(df.head())