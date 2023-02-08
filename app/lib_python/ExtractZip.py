import os
from zipfile import ZipFile

import subprocess

def ExtractZip():
  subprocess.call(['mv', '/cache/.gitignore', '/tmp'])
  subprocess.call(['rm', '-rf', '/cache/*'])
  subprocess.call(['mv', '/tmp/.gitignore', '/cache/'])

  entries = os.listdir('input/')
  for entry in entries:
    if entry.endswith('.zip') == False:
      continue

    with ZipFile('input/' + entry, 'r') as zObject:
      zObject.extractall(
          path='cache/')
    return os.path.splitext(entry)[0]