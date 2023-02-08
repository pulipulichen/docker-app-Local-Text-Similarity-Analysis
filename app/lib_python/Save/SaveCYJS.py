import networkx as nx
import json

def SaveCYJS(G, filename):
  cyjs = nx.cytoscape_data(G)
  cyjs = json.dumps(cyjs, ensure_ascii=False)

  text_file = open('input/' + filename + ".json", "w", encoding='utf-8')
  n = text_file.write(cyjs)
  text_file.close()