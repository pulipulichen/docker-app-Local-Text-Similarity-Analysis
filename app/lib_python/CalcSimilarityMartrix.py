from fastDamerauLevenshtein import damerauLevenshtein

def CalcSimilarityMartrix(files):
  distance = damerauLevenshtein('ca', 'abc', similarity=False)
  print(distance)
  return True