"""Create a histogram to show the distribution of order amounts (sales values),
 highlighting how many small vs. large purchases happen — like analyzing order size patterns on Zomato or Swiggy.
 <br><br><em><strong>Hint:</strong> Use plt.hist() and set bins to 10 for a clear distribution.</em>
"""

import matplotlib.pyplot as plt
import pandas as pd

# Load the sales dataset
df = pd.read_csv("D:\Data Analytics\DA--working-with-data-visualization-with-matplotlib\Session-12\sales_data.csv")

# Create the histogram for order amounts
plt.figure(figsize=(10, 6))
plt.hist(df['sales_amount'], bins=10, color="#FF5733", edgecolor='black')
plt.xlabel('Order Amount')
plt.ylabel('Number of Orders')
plt.title('Distribution of Order Amounts')
plt.tight_layout()
plt.show()
