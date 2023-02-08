import json
from pyexcel_ods3 import save_data
from collections import OrderedDict

def SaveODS(files, filename):
  # print(json.dumps(files, indent=4, ensure_ascii=False))
  data = OrderedDict() # from collections import OrderedDict

  output = []
  if len(files) > 0:
    output.append(files[0].keys)

  for file in files:
    output.append(file.values())

  print(output)
  data.update({"data": output})
  save_data("input/" + filename + ".ods", data)
