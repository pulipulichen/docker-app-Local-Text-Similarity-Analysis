from itertools import combinations
from fastDamerauLevenshtein import damerauLevenshtein

def CalcSimilarityMartrix(files):
  martix = []

  combinations = list(combinations(range(0, len(files)),2))
  for combination in combinations:
    print(combination[0] + '-' + combination[1])
  
  distance = damerauLevenshtein('ca', 'abc', similarity=False)
  print(distance)
  return True