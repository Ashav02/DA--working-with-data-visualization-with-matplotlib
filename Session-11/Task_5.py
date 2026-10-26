"""Export a Matplotlib chart as a PDF, then verify the PDF opens correctly and the chart looks sharp (not blurry) at 200% zoom.
 If the image looks pixelated, try exporting again with a higher DPI setting and compare the results.
"""

import matplotlib.pyplot as plt

# Sample data for monthly sales
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 200, 180, 220, 250, 300]

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(months, sales, color="#FF5733")
plt.xlabel('Months')
plt.ylabel('Sales (in thousands)')
plt.title('Monthly Sales for the First Half of the Year')
plt.savefig('monthly_sales.pdf', format='pdf', dpi=300)
plt.tight_layout()
plt.show()