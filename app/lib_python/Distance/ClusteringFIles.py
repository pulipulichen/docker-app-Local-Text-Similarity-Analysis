import networkx as nx
from networkx.algorithms import community
from .GetOutliers import *
import pandas as pd

def ClusteringFIles(df):

  pd.options.display.max_columns = None
  
  outliers = GetOutliers(df)
  
  # G = nx.barbell_graph(5, 1)
  G = nx.Graph()
  df['weight'] = 1/ df['value']
  graph_df = df[['source', 'target', 'weight']]
  elist = list(graph_df.itertuples(index=False))
  G.add_weighted_edges_from(elist)
  
  df_G = nx.to_pandas_edgelist(G)
  print(df_G)

  # communities_generator = community.girvan_newman(G)
  # top_level_communities = next(communities_generator)
  # next_level_communities = next(communities_generator)
  # output = sorted(map(sorted, next_level_communities))
  # print(output)

  # output = community.louvain_communities(G, weight='weight', seed=123)
  # print(output)

  G = nx.petersen_graph()
  df_G = nx.to_pandas_edgelist(G)
  print(df_G)
  output = community.louvain_communities(G, seed=123)
  print(output)