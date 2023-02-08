
def SortDistanceDataFrame(files):
  files = files.sort_values(by=['is_outlier', 'cluster'], ascending=False)
  return files