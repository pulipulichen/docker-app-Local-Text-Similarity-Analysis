from itertools import combinations
from fastDamerauLevenshtein import damerauLevenshtein

def CalcSimilarityMartrix(files):
  martix = []

  print(list(combinations(range(0, len(files)),2)))

  distance = damerauLevenshtein('ca', 'abc', similarity=False)
  print(distance)
  return True