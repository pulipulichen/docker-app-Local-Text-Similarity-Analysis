# print('hello world')

import os
from pathlib import Path

entries = os.listdir('input/')
for entry in entries:
  print(entry)
  file_stats = os.stat('input/' + entry)
  print(file_stats.st_size)