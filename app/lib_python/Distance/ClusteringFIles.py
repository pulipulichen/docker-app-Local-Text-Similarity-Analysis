from networkx.algorithms import community
from .GetOutliers import *

def ClusteringFIles(df):

  outliers = GetOutliers(df)
  G = nx.barbell_graph(5, 1)
  communities_generator = community.girvan_newman(G)
  top_level_communities = next(communities_generator)
  next_level_communities = next(communities_generator)
  output = sorted(map(sorted, next_level_communities))
  print(output)