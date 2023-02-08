import os
from zipfile import ZipFile

import subprocess

def ExtractZip():
  subprocess.run(['mv', './cache/files/.gitignore', '/tmp'], capture_output=True)
  subprocess.run(['rm', '-rf', './cache/files'], capture_output=True)
  subprocess.run(['mkdir', '-p', './cache/files'], capture_output=True)
  subprocess.run(['mv', '/tmp/.gitignore', './cache/files/'], capture_output=True)

  entries = os.listdir('input/')
  for entry in entries:
    if entry.endswith('.zip') == False:
      continue

    with ZipFile('input/' + entry, 'r') as zObject:
      zObject.extractall(
          path='cache/files/')

    filename = os.path.splitext(entry)[0]
    if os.path.isdir('cache/files/' + filename):
      subprocess.run(['mv', './cache/files/' + filename + '/*', './cache/files/'], capture_output=True)
      subprocess.run(['rm', '-rf', './cache/files/' + filename], capture_output=True)
    return os.path.splitext(entry)[0]