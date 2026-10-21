"""Use ChatGPT or Copilot to generate Python code that creates a scatter plot of 'number of Flipkart orders' vs 'total amount spent' for 10 users, adds a regression line using numpy polyfit, and displays the plot. Run the generated code and note any errors or changes you had to make.
"""

import numpy as np
import matplotlib.pyplot as plt

# Sample data for 10 users
orders = np.array([1, 3, 2, 5, 4, 6, 7, 3, 8, 5])
spent = np.array([1200, 3500, 2100, 6200, 4800,
                  7100, 8300, 3900, 9500, 5900])

# Calculate regression coefficients
slope, intercept = np.polyfit(orders, spent, 1)

# Generate regression line
x_line = np.linspace(orders.min(), orders.max(), 100)
y_line = slope * x_line + intercept

# Create scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(orders, spent, label="Users", s=60)
plt.plot(
    x_line, y_line,
    label=f"Regression line: y = {slope:.2f}x + ({intercept:.2f})"
)

plt.xlabel("Number of Flipkart Orders")
plt.ylabel("Total Amount Spent (₹)")
plt.title("Flipkart Orders vs Total Amount Spent")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
print(f"Regression equation: y = {slope:.2f}x + {intercept:.2f}")
