import os
from zipfile import ZipFile

import subprocess

def ExtractZip():
  print(subprocess.run(['ls', './cache'], capture_output=True))
  print(subprocess.run(['mv', './cache/.gitignore', '/tmp'], capture_output=True))
  print(subprocess.run(['rm', '-rf', './cache'], capture_output=True))
  print(subprocess.run(['mkdir', '-p', './cache'], capture_output=True))
  print(subprocess.run(['mv', '/tmp/.gitignore', './cache/'], capture_output=True))
  print(subprocess.run(['ls', './cache'], capture_output=True))

  return False
  entries = os.listdir('input/')
  for entry in entries:
    if entry.endswith('.zip') == False:
      continue

    with ZipFile('input/' + entry, 'r') as zObject:
      zObject.extractall(
          path='cache/')
    return os.path.splitext(entry)[0]