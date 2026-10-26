"""Plot a line chart to visualize monthly sales trends over a year, using the date column to group sales by month.
 Add a title and axis labels to make the chart presentation-ready.
"""

import pandas as pd
import matplotlib.pyplot as plt

#Load Database

df = pd.read_csv("D:\Data Analytics\DA--working-with-data-visualization-with-matplotlib\Session-12\sales_data.csv")

# Group by month and sum the sales
df['date'] = pd.to_datetime(df['date'])

# Group by month and sum the sales
monthly_sales = df.groupby(df['date'].dt.to_period('M'))['sales_amount'].sum().reset_index()

# Create the line chart
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales['date'].astype(str), monthly_sales['sales_amount'], marker='o', linestyle='-', color="#2ED09A")
plt.xlabel('Month')
plt.ylabel('Total Sales Amount')
plt.title('Monthly Sales Trends Over a Year')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

