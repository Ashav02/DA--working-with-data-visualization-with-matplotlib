"""Given a scatter plot of movie ratings vs. number of reviews for movies on a streaming platform (like BookMyShow),
 use plt.annotate() to add a text box highlighting the movie with the highest rating.
 <br><br><em><strong>Hint:</strong> Set the 'bbox' parameter in plt.annotate() to create a visible text box.</em>
"""

import matplotlib.pyplot as plt 

# Sample data for the scatter plot
ratings = [7.2, 8.5, 6.8, 9.1, 7.9]
reviews = [1500, 2300, 1200, 3100, 1800]
movie_titles = ['Doomsday', 'Ironman', 'Avengers-Endgame', 'Fast Five', 'Fast and Furious 9']

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(reviews, ratings, c='blue', s=100, alpha=0.7)

# Annotate the movie with the highest rating
max_rating_index = ratings.index(max(ratings))
plt.annotate(f'{movie_titles[max_rating_index]} (Highest Rating)',
             xy=(reviews[max_rating_index], ratings[max_rating_index]),
             xytext=(10, 10),
             textcoords='offset points',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

# Add labels and title
plt.xlabel('Number of Reviews')
plt.ylabel('Ratings')
plt.title('Movie Ratings vs. Number of Reviews')

# Show the plot
plt.show()
