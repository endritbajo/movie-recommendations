__author__ = 'endrit bajo'

import urllib2

data_url = "http://files.grouplens.org/datasets/movielens/ml-100k/u.data"
movies_url = "http://files.grouplens.org/datasets/movielens/ml-100k/u.item"

def getmovies():
  movies = {}
  # get movies
  movies_file = urllib2.urlopen(movies_url)
  for line in movies_file:
    (id, title) = line.split('|')[0:2]
    movies[id] = title
  return movies

def getratings_by_user():
  data = {}
  # get user ratings
  data_file = urllib2.urlopen(data_url)
  for line in data_file:
    (user, movieid, rating, ts) = line.split('\t')
    data.setdefault(user, {})
    data[user][movieid] = int(rating)

  return data

def getratings_by_movie():
  data = {}
  # get user ratings
  data_file = urllib2.urlopen(data_url)
  for line in data_file:
    (user, movieid, rating, ts) = line.split('\t')
    data.setdefault(movieid, {})
    data[movieid][user] = int(rating)

  return data
