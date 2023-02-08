from itertools import combinations
from fastDamerauLevenshtein import damerauLevenshtein
import pandas as pd
from CalcDistanceOutlier import *

def CalcDistanceDataFrame(files):
  df = pd.DataFrame()

  pairs = list(combinations(range(0, len(files)),2))
  for pair in pairs:
    # print(str(pair[0]) + '-' + str(pair[1]))
    source = files[pair[0]]
    target = files[pair[1]]
    distance = damerauLevenshtein(source['data'], target['data'], similarity=False)
    record = {
      "source": source["user"],
      "target": target["user"],
      "value": distance
    }
    df = pd.concat([df, pd.DataFrame.from_records([record])])

  # print(df)
  CalcDistanceOutlier(df)
  return df