"""Add value annotations to your category bar chart to display the exact sales amount above each bar,
 then export the chart as a PNG image file named 'category_sales_kpi.png'.
"""

import pandas as pd
import matplotlib.pyplot as plt

#load Database
df = pd.read_csv("D:\Data Analytics\DA--working-with-data-visualization-with-matplotlib\Session-12\sales_data.csv")

# Group by category and sum the sales
category_sales = df.groupby('category')['sales_amount'].sum().reset_index()

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(category_sales['category'], category_sales['sales_amount'], color="#33FF57")

# Add value annotations
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height,
             f'Rs.{height:.2f}',
             ha='center', va='bottom')

# Customize the chart
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.title('Category-wise Sales KPI')
plt.xticks(rotation=45)
plt.tight_layout()

# Export the chart
plt.savefig('category_sales_kpi.png', dpi=300, bbox_inches='tight')
plt.show()