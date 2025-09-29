import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample movie ratings data
data = {
    'userId': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5],
    'movieId': [101, 102, 103, 101, 104, 102, 103, 104, 101, 103, 102, 104],
    'rating': [5, 3, 4, 4, 5, 2, 4, 5, 3, 4, 4, 5]
}

ratings = pd.DataFrame(data)

# Create user-item matrix
user_movie_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

# Compute cosine similarity between users
user_similarity = cosine_similarity(user_movie_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

def recommend_movies(user_id, user_movie_matrix, user_similarity_df, top_n=3):
    # Get similarity scores for the user
    sim_scores = user_similarity_df[user_id]
    
    # Exclude the user itself
    sim_scores = sim_scores.drop(user_id)
    
    # Sort users by similarity score
    similar_users = sim_scores.sort_values(ascending=False)
    
    weighted_ratings = pd.Series(dtype=np.float64)
    
    for sim_user, similarity_score in similar_users.items():
        sim_user_ratings = user_movie_matrix.loc[sim_user]
        weighted_ratings = weighted_ratings.add(sim_user_ratings * similarity_score, fill_value=0)
    
    weighted_ratings /= similar_users.sum()
    
    # Movies not rated by target user
    user_ratings = user_movie_matrix.loc[user_id]
    unrated_movies = user_ratings[user_ratings == 0].index
    
    recommendations = weighted_ratings.loc[unrated_movies]
    recommendations = recommendations.sort_values(ascending=False)
    
    return recommendations.head(top_n)

if __name__ == "__main__":
    user_to_recommend = 1
    recommendations = recommend_movies(user_to_recommend, user_movie_matrix, user_similarity_df, top_n=3)
    
    print(f"Top {len(recommendations)} recommended movies for User {user_to_recommend}:")
    print(recommendations)
