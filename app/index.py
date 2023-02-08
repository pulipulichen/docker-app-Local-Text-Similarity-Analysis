# print('hello world')

import os
from pathlib import Path

from zipfile import ZipFile

entries = os.listdir('input/')
for entry in entries:
  if entry.endswith('.zip') == False:
    continue

  with ZipFile('input/' + entry, 'r') as zObject:
    zObject.extractall(
        path='cache/')