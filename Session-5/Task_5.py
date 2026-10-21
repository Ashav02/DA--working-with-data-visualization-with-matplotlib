"""You are given a histogram code that plots Flipkart product prices, but the bins are not showing expected groupings.
Debug the code by adjusting the bins parameter so that prices between 100-500, 501-1000, 1001-2000, and 2001-5000 are each in their own bin.
<br><br><em><strong>Hint:</strong> Use the 'bins' parameter with a list of bin edges.</em>
"""

import matplotlib.pyplot as plt

prices = [150, 250, 350, 450, 550, 650, 750, 850, 950, 1050,
          1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950,
          4150, 4250, 4350, 4450, 4550, 4650, 4750, 4850, 4950]

# Adjust bins to show expected groupings
plt.hist(prices, bins=[100, 500, 1000, 2000, 5000], color='green', edgecolor='black', alpha=0.7)
plt.xlabel('Product Prices')
plt.ylabel('Frequency')
plt.title('Histogram of Flipkart Product Prices')
plt.grid(alpha=0.3)
plt.show()