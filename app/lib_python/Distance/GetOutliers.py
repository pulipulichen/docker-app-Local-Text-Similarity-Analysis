def GetOutliers(df):
  df = df[df['is_outlier'] == True]

  outliers = []
  sources = df['source']
  targets = df['target']
  outliers = sources.concat(targets)
  outliers = list(set(outliers))

  print(outliers)

  return outliers