"""Install Matplotlib in your Python environment and write a script named hello_plot.py
 that creates a simple line plot showing the number of daily steps you walked over the past 7 days.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({"week":['Sun','Mon','Tus','Wed','Thur','Fri','Sat'],
                "Daily_steps":[6000, 7000, 8000, 7500, 6500, 8500, 9000]})

print(df)

#Line Plot showing the number of daily steps

plt.plot(df['week'],df['Daily_steps'], marker="o", color="Red")
plt.xlabel("weekday")
plt.ylabel("Daily steps")
plt.title("Daily steps count")
plt.grid(alpha=0.4)
plt.show()