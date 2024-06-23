import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
ratings = pd.read_csv('movie_ratings.csv')

# Create the user-item matrix
user_item_matrix = ratings.pivot_table(index='userId', columns='title', values='rating')

# Compute the cosine similarity matrix
item_similarity = cosine_similarity(user_item_matrix.T.fillna(0))

# Create a DataFrame from the similarity matrix
item_similarity_df = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)

def get_recommendations(movie_title, similarity_matrix, num_recommendations=5):
    # Get the similarity scores for the given movie
    similar_movies = similarity_matrix[movie_title].sort_values(ascending=False)
    
    # Exclude the movie itself from the list of recommendations
    similar_movies = similar_movies.drop(movie_title)
    
    return similar_movies.head(num_recommendations)

# Get recommendations for a specific movie
recommendations = get_recommendations('Toy Story (1995)', item_similarity_df)
print(recommendations)
