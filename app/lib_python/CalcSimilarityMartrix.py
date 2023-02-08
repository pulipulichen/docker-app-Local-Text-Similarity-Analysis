from itertools import combinations
from fastDamerauLevenshtein import damerauLevenshtein

def CalcSimilarityMartrix(files):
  distance_list = []

  pairs = list(combinations(range(0, len(files)),2))
  for pair in pairs:
    print(str(pair[0]) + '-' + str(pair[1]))
    source = files[pair[0]]
    target = files[pair[1]]
    distance = damerauLevenshtein(source['data'], target['data'], similarity=False)
    distance_list.append({
      "source": source["user"],
      "target": target["user"],
      "value": distance
    })

  print(distance_list)
  return True