import numpy as np

def CalcDistanceOutlier(df):
  # print(len(find_outliers_IQR(df['value'])))

  values = df['value']
  q1=values.quantile(0.25)
  q3=values.quantile(0.75)
  IQR=q3-q1
  down_bound = q1-1.5*IQR
  up_bound = q3+1.5*IQR

  # print(df[(df['value'] < down_bound | df['value'] > up_bound)])

  print(df)

  return df