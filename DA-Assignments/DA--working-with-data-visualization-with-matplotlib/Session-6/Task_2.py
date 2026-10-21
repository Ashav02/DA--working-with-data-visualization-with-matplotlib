"""Create a scatter plot showing 'amount spent on Zomato orders' vs 'number of orders placed' for 12 friends,
and label each point with the friend's name.<br><br><em><strong>Hint:</strong> Use the 'annotate' function in matplotlib to add labels.</em>
"""

import matplotlib.pyplot as plt

# Fictional data for 12 friends
friends = ['Ashav', 'Sneha', 'Diya', 'Harsh', 'Fenil', 'Savan', 'Dipu', 'Megha', 'Tejas', 'Dhaval', 'Abhi', 'Jugal']
amount_spent = [120, 250, 300, 150, 200, 400, 350, 180, 220, 270, 310, 190]
number_of_orders = [3, 5, 6, 4, 5, 8, 7, 4, 5, 6, 7, 4]

# Create a scatter plot
plt.scatter(amount_spent, number_of_orders, color='orange', edgecolor='black', alpha=0.7)
# Annotate each point with the friend's name
for i, friend in enumerate(friends):
    plt.annotate(friend, (amount_spent[i], number_of_orders[i]), textcoords="offset points", xytext=(0,10), ha='center')    

plt.xlabel('Amount Spent on Zomato Orders')
plt.ylabel('Number of Orders Placed')
plt.title('Scatter Plot of Zomato Orders by Friends')
plt.grid(alpha=0.3)
plt.show()
