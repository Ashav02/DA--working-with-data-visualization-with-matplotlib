"""Build a pie chart showing the percentage of time you spend on 4 different apps (Instagram, YouTube, WhatsApp, Spotify) 
in a day and save the chart as a PDF using plt.savefig().
"""

import matplotlib.pyplot as plt

# Sample data for app usage
apps = ['Instagram', 'YouTube', 'WhatsApp', 'Spotify']
time_spent = [2, 3, 1.5, 1]  

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(time_spent, labels=apps, autopct='%1.1f%%', startangle=90, colors=['#E1306C', '#FF0000', '#25D366', '#1DB954'])
plt.title('Daily App Usage Distribution', fontsize=16, fontweight='bold')
plt.savefig('daily_app_usage.pdf', format='pdf')
plt.show()
