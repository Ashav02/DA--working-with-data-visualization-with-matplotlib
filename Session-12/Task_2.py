"""Using Matplotlib, create a bar chart that shows total sales for each product category 
(like 'Electronics', 'Clothing', 'Groceries'), similar to how Flipkart or Myntra might track category performance.
"""

import pandas as pd
import matplotlib.pyplot as plt

#load Database

df = pd.read_csv("D:\Data Analytics\DA--working-with-data-visualization-with-matplotlib\Session-12\sales_data.csv")

# Group by category and sum the sales
category_sales = df.groupby('category')['sales_amount'].sum().reset_index()

# Create the bar chart
plt.figure(figsize=(10, 6))

plt.bar(category_sales['category'], category_sales['sales_amount'], color="#FF5733")
plt.xlabel('Product Category')
plt.ylabel('Total Sales Amount')
plt.title('Total Sales by Product Category')
plt.tight_layout()
plt.show()