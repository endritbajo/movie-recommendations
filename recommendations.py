__author__ = 'endrit'

from data import critics
from math import sqrt

def euclidean_distance(prefs, person1, person2):
  # get the list of shared items
  si = {}
  for item in prefs[person1]:
    if item in prefs[person2]:
      si[item] = 1;

  # if there are no shared items
  if len(si) == 0: return 0

  sum_of_squares = 0;

  for item in prefs[person1]:
    if item in prefs[person2]:
      sum_of_squares += pow(prefs[person1][item] - prefs[person2][item], 2)

  return 1 / (1 + sum_of_squares)
