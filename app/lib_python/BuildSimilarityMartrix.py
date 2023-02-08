from fastDamerauLevenshtein import damerauLevenshtein

def BuildSimilarityMartrix(files):
  distance = damerauLevenshtein('ca', 'abc', similarity=False)
  return True