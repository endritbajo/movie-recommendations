__author__ = 'endrit bajo'

import distances

"""
  Returns users with similar tastes (user-based filtering)
"""
def similar_users(data, person,
                  similarity = distances.pearson_correlation,
                  n = 5):
  items = [(similarity(data, person, other), other) for other in data if other != person]

  items.sort()
  items.reverse()

  return items[0:5]

"""
  Returns a list of recommended movies (user-based filtering)
"""
def recommended_movies(data,
                       person,
                       similarity = distances.pearson_correlation,
                       n = 5):

  # total movie score
  total_score = {}
  # total movie similarities
  total_similarities = {}

  for user in data:
    if user == person: continue

    sim = similarity(data, person, user)

    # ignore score of zero or lower
    if sim <= 0: continue

    for (movie, rating) in data[user].items():
        # if user has not yet seen the movie
        if movie not in data[person] or rating == 0:
          # similarity * score
          total_score.setdefault(movie, 0)
          total_score[movie] += rating * sim
          # sum of similarities
          total_similarities.setdefault(movie, 0)
          total_similarities[movie] += sim

  movies = [(total / total_similarities[movie], movie)
                for (movie, total) in total_score.items()]

  movies.sort()
  movies.reverse()

  return movies[0:n]
