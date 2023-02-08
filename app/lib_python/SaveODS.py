import json
from pyexcel_ods3 import save_data
from collections import OrderedDict

def SaveODS(files, filename):
  # print(json.dumps(files, indent=4, ensure_ascii=False))
  data = OrderedDict() # from collections import OrderedDict
  data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})
  data.update({"Sheet 2": [["row 1", "row 2", "row 3"]]})
  save_data("input/" + filename + ".ods", data)
