import networkx as nx
from networkx.algorithms import community
from .GetOutliers import *

def ClusteringFIles(df):

  outliers = GetOutliers(df)
  
  # G = nx.barbell_graph(5, 1)
  G = nx.Graph()
  elist = list(df.itertuples(index=False))
  G.add_weighted_edges_from(elist)

  communities_generator = community.girvan_newman(G)
  top_level_communities = next(communities_generator)
  next_level_communities = next(communities_generator)
  output = sorted(map(sorted, next_level_communities))
  print(output)