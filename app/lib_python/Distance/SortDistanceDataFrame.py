
def SortDistanceDataFrame(files):
  files.sort_values(by=['is_outlier', 'cluster'])
  return files