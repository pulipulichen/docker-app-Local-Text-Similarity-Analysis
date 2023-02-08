import networkx as nx

def AddOutlierAttribute(G, outliers):
  nodes = G.nodes
  print(nodes)
  # for outlier in outliers:
  #   nx.set_node_attributes(G, (), name="is_outlier")
  return G