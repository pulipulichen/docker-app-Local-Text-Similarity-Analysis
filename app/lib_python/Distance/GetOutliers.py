def GetOutliers(df):
  df = df[df['is_outlier'] == True]
  print(df)