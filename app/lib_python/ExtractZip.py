import os
from zipfile import ZipFile

import subprocess

def ExtractZip():
  subprocess.call(['rm', '-rf', 'rm !(\.gitignore)'])

  entries = os.listdir('input/')
  for entry in entries:
    if entry.endswith('.zip') == False:
      continue

    with ZipFile('input/' + entry, 'r') as zObject:
      zObject.extractall(
          path='cache/')