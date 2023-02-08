import os
from zipfile import ZipFile

import subprocess

def ExtractZip():
  print(subprocess.call(['mv', '/cache/.gitignore', '/tmp']))
  print(subprocess.call(['rm', '-rf', '/cache/*']))
  print(subprocess.call(['mv', '/tmp/.gitignore', '/cache/']))

  entries = os.listdir('input/')
  for entry in entries:
    if entry.endswith('.zip') == False:
      continue

    with ZipFile('input/' + entry, 'r') as zObject:
      zObject.extractall(
          path='cache/')
    return os.path.splitext(entry)[0]