"""Add a main title 'Monthly Data Usage Trend' and label the X-axis as 'Month' and Y-axis as 'Data Used (GB)' to a line chart showing your mobile data usage for the past 6 months.
<br><br><em><strong>Hint:</strong> Use plt.title(), plt.xlabel(), and plt.ylabel().</em>
"""

import matplotlib.pyplot as plt

months = ['Jan','Feb','March','April','May','June']
data_used = [25, 30, 45, 27, 35, 32]

plt.plot(months, data_used, marker="o", color='orange')
plt.xlabel("Months")
plt.ylabel("Data Used(GB)")
plt.title("Monthly Data Usage Trend")
plt.grid(alpha=0.4)
plt.show()