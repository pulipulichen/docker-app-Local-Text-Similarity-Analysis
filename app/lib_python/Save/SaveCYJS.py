import networkx as nx

def SaveCYJS(G, filename):
  cyjs = nx.cytoscape_data(G)

  text_file = open(filename + ".cyjs", "w")
  n = text_file.write(cyjs)
  text_file.close()