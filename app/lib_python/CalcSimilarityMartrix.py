from itertools import combinations
from fastDamerauLevenshtein import damerauLevenshtein

def CalcSimilarityMartrix(files):
  martix = []

  pairs = list(combinations(range(0, len(files)),2))
  for pair in pairs:
    print(str(pair[0]) + '-' + str(pair[1]))
  
  distance = damerauLevenshtein('ca', 'abc', similarity=False)
  print(distance)
  return True