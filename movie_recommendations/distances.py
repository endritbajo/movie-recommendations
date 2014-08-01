from math import sqrt

def euclidean_distance(data, p1, p2):
  # get the list of shared items
  si = {}
  for item in data[person1]:
    if item in data[person2]:
      si[item] = 1;

  # if there are no shared items
  if len(si) == 0: return 0

  sum_of_squares = 0;

  for item in data[person1]:
    if item in data[person2]:
      sum_of_squares += pow(data[person1][item] - data[person2][item], 2)

  return 1 / (1 + sum_of_squares)

def pearson_correlation(data, p1, p2):
  # get shared list
  si = {}
  for item in data[p1]:
    if item in data[p2]:
      si[item] = 1

  n = len(si)

  # if there are no common items
  if n == 0: return 0

  # add all item values
  sum1 = sum([ data[p1][it] for it in si ])
  sum2 = sum([ data[p2][it] for it in si ])

  # sum the squares
  sum1sq = sum([ pow(data[p1][it], 2) for it in si ])
  sum2sq = sum([ pow(data[p2][it], 2) for it in si ])

  # sum the products
  psum = sum([ data[p1][it] * data[p2][it] for it in si ])

  # calculate
  num = psum - (sum1 * sum2 / n)
  den = sqrt((sum1sq - pow(sum1, 2)/n) * (sum2sq - pow(sum2, 2)/n))
  if den == 0: return 0

  return num / den
