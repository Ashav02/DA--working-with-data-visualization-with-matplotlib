"""Plot a time series line chart showing your daily Paytm wallet balance over the last 14 days using Matplotlib.
Format the x-axis to display dates in 'DD MMM' format (e.g., '12 Jun').
"""


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

daily_balance = [500, 450, 600, 550, 700, 650, 800, 750, 900, 850, 1000, 950, 1100, 1050]

#Generate a list of dates for the last 14 days
dates = pd.date_range(end=pd.Timestamp.today(), periods=14)   

#Create the time series line chart
plt.figure(figsize=(10, 5))
plt.plot(dates, daily_balance, marker='o', linestyle='-', color='blue')
plt.xlabel('Date')
plt.ylabel('Wallet Balance (Rs.)')
plt.title('Daily Paytm Wallet Balance')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()