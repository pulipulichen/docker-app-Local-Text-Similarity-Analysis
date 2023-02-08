import networkx as nx

def AddOutlierAttribute(G, outliers):
  nodes = G.nodes
  print(nodes)

  outliers_dict = {}
  for node in nodes:
    outliers_dict[node] = node.isin(outliers)

  print(outliers_dict)
  # for outlier in outliers:
  #   nx.set_node_attributes(G, (), name="is_outlier")
  return G