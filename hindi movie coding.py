from math import sqrt

# Sample data
ratings = [
    {'userId': 1, 'movieId': 1, 'rating': 4.0, 'title': 'An Action Hero (2022)'},
    {'userId': 1, 'movieId': 2, 'rating': 2.0, 'title': 'Pathan (2023)'},
    {'userId': 2, 'movieId': 1, 'rating': 4.5, 'title': 'An Action Hero (2022)'},
    {'userId': 2, 'movieId': 2, 'rating': 3.0, 'title': 'Pathan (2023)'},
    {'userId': 3, 'movieId': 1, 'rating': 5.0, 'title': 'An Action Hero (2022)'},
    {'userId': 3, 'movieId': 2, 'rating': 4.0, 'title': 'Pathan (2023)'}
]

# Create user-item matrix
user_item_matrix = {}
for rating in ratings:
    user = rating['userId']
    movie = rating['title']
    if user not in user_item_matrix:
        user_item_matrix[user] = {}
    user_item_matrix[user][movie] = rating['rating']

# Compute cosine similarity
def cosine_similarity(movie1, movie2):
    common_users = [user for user in user_item_matrix if movie1 in user_item_matrix[user] and movie2 in user_item_matrix[user]]
    
    if len(common_users) == 0:
        return 0

    sum1 = sum([user_item_matrix[user][movie1] for user in common_users])
    sum2 = sum([user_item_matrix[user][movie2] for user in common_users])
    sum1_sq = sum([user_item_matrix[user][movie1] ** 2 for user in common_users])
    sum2_sq = sum([user_item_matrix[user][movie2] ** 2 for user in common_users])
    product_sum = sum([user_item_matrix[user][movie1] * user_item_matrix[user][movie2] for user in common_users])
    
    numerator = product_sum
    denominator = sqrt(sum1_sq) * sqrt(sum2_sq)
    
    if denominator == 0:
        return 0

    return numerator / denominator

# Get movie titles
movie_titles = list(set([rating['title'] for rating in ratings]))

# Create similarity matrix
similarity_matrix = {}
for movie1 in movie_titles:
    similarity_matrix[movie1] = {}
    for movie2 in movie_titles:
        if movie1 != movie2:
            similarity_matrix[movie1][movie2] = cosine_similarity(movie1, movie2)

# Function to get recommendations
def get_recommendations(movie_title, similarity_matrix, num_recommendations=5):
    similar_movies = sorted(similarity_matrix[movie_title].items(), key=lambda x: x[1], reverse=True)
    return similar_movies[:num_recommendations]

# Get recommendations for a specific movie
recommendations = get_recommendations('An Action Hero (2022)', similarity_matrix)
print("Recommendations for 'An Action Hero (2022)': 1.5245670324368902")
for movie, score in recommendations:
    print(f"{movie}: {score}")
