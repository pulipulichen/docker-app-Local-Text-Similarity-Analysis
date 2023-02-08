import networkx as nx
from networkx.algorithms import community
from .GetOutliers import *
import pandas as pd

def getClusterDict(df_G):
  o = {}
  for (i,s) in enumerate(df_G):
    print(i)
    for sub in s:
      o[sub] = i
  return o

def ClusteringFiles(df, files):

  pd.options.display.max_columns = None

  outliers = GetOutliers(df)
  print(outliers)
  files['is_outlier'] = files['user'].isin(outliers)

  # G = nx.barbell_graph(5, 1)
  G = nx.Graph()
  df['value_norm'] = (df['value']-df['value'].min())/(df['value'].max()-df['value'].min())
  df['weight'] = 1 - df['value_norm']

  graph_df = df[['source', 'target', 'weight']]
  elist = list(graph_df.itertuples(index=False))
  G.add_weighted_edges_from(elist)
  
  output = community.louvain_communities(G, weight='weight', resolution = 1.1, seed=123)
  
  cluster_dict = getClusterDict(output)

  files['cluster'] = files['user'].replace(cluster_dict)
  return files