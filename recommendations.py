__author__ = 'endrit'

from data import critics
from math import sqrt

# get the ecuclidean distance between person1 and person2
def euclidean_distance(prefs, p1, p2):
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

def pearson_correlation(prefs, p1, p2):
  # get shared list
  si = {}
  for item in prefs[p1]:
    if item in prefs[p2]:
      si[item] = 1

  n = len(si)

  # if there are no ratings in common
  if n == 0: return 0

  # add all preferences
  sum1 = sum([ prefs[p1][it] for it in si ])
  sum2 = sum([ prefs[p2][it] for it in si ])

  # sum the squares
  sum1sq = sum([ pow(prefs[p1][it], 2) for it in si ])
  sum2sq = sum([ pow(prefs[p2][it], 2) for it in si ])

  # sum the products
  psum = sum([ prefs[p1][it] * prefs[p2][it] for it in si ])

  # calculate
  num = psum - (sum1 * sum2 / n)
  den = sqrt((sum1sq - pow(sum1, 2)/n) * (sum2sq - pow(sum2, 2)/n))
  if den == 0: return 0

  return num / den

def pearson_correlation_formula(prefs, p1, p2):
  # get shared list
  si = {}
  for item in prefs[p1]:
    if item in prefs[p2]:
      si[item] = 1

  n = len(si)

  # if there are no ratings in common
  if n == 0: return 0

  # add all preferences
  sum1 = sum([ prefs[p1][it] for it in si ])
  sum2 = sum([ prefs[p2][it] for it in si ])

  # means
  mean1 = sum1 / n
  mean2 = sum2 / n

  num = sum([ (prefs[p1][it] - mean1) * (prefs[p2][it] - mean2) for it in si ])
  den = sqrt(sum([ pow((prefs[p1][it] - mean1), 2) for it in si])) * sqrt(sum([ pow((prefs[p2][it] - mean2), 2) for it in si]))

  if den == 0: return 0

  return num / den


def top_matches(prefs, person, n = 5, similarity = pearson_correlation):
  scores = [ (similarity(prefs, person, other), other) for other in prefs]

  # sort the list to put the highest scores at the top
  scores.sort()
  scores.reverse()

  return scores[0:n]
