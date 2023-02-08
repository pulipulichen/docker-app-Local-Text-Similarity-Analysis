from itertools import combinations
from fastDamerauLevenshtein import damerauLevenshtein
import pandas as pd
from .CalcDistanceOutlier import *
from .ClusteringFIles import *

def CalcDistanceDataFrame(files):
  df = pd.DataFrame()

  pairs = list(combinations(range(0, len(files)),2))
  for pair in pairs:
    print(str(pair[0]) + '-' + str(pair[1]))
    
    source = dict(files.iloc[[pair[0]]])
    print(source)
    continue
    target = dict(files.iloc[[pair[1]]])
    distance = damerauLevenshtein(source['data'], target['data'], similarity=False)
    record = {
      "source": source["user"],
      "target": target["user"],
      "value": distance
    }
    df = pd.concat([df, pd.DataFrame.from_records([record])])
  return False
  # print(df)
  df = CalcDistanceOutlier(df)

  df = ClusteringFIles(df)
  return df