__author__ = 'endrit bajo'

import distances

"""
  Given an item, it returns items similar to each other (similar movies or similar users).
  The data is a dictionary structured in the following way:

  data = {
    user1 : {movie1: rating1, movie2: rating2, ... movien: ratingn}
    ...
    usern : {movie1:rating1, movie2: rating2, ... movien: ratingn}
  }

  If you want similar users.

  data = {
    movie1 : {user1: rating1, user2: rating2, ... usern: ratingn}
    ...
    movien : {user1: rating1, user2: rating2, ... usern: ratingn}
  }

  If you want similar items.

"""
def similar_items(data, myitem,
                  similarity = distances.pearson_correlation,
                  n = 5):
  items = [(similarity(data, myitem, other), other)
              for other in data if other != myitem]

  items.sort()
  items.reverse()

  return items[0:n]


"""
  Given a user, it returns a list of recommended movies.
  The data is a dictionary structured in the following way:

  data = {
    user1 : {movie1: rating1, movie2: rating2, ... movien: ratingn}
    ...
    usern : {movie1:rating1, movie2: rating2, ... movien: ratingn}
  }

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
