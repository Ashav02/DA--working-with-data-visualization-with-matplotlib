"""Create a pie chart representing the percentage of different payment methods (UPI, Card, Wallet, Cash)
used on an e-commerce app (like Flipkart), and add a legend positioned at the lower right corner of the plot.
"""

import matplotlib.pyplot as plt

payment_methods = ['UPI', 'Card', 'Wallet', 'Cash']
percentages = [40, 30, 20, 10]

# Create the pie chart

plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=payment_methods, autopct='%1.1f%%', startangle=90, colors=['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9'])
plt.title('Payment Methods Distribution', fontsize=16, fontweight='bold')

# Add a legend positioned at the lower right corner
plt.legend(payment_methods, loc='lower right', fontsize=10)

plt.tight_layout()
plt.show()