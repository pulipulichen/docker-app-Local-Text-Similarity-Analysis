#!/usr/bin/python
#-*- coding: utf-8 -*-

# print('hello world')

import os
from pathlib import Path

from zipfile import ZipFile
import json
import subprocess

subprocess.call(['rm', '-rf', 'rm !(\.gitignore)'])

entries = os.listdir('input/')
for entry in entries:
  if entry.endswith('.zip') == False:
    continue

  with ZipFile('input/' + entry, 'r') as zObject:
    zObject.extractall(
        path='cache/')

entries = os.listdir('cache/')
files = []
for entry in entries:
  if os.path.isdir('cache/' + entry) == False:
    continue

  subentries = os.listdir('cache/' + entry)
  max_time = 0
  last_entry = None
  for subentry in subentries:
    time_m = os.path.getmtime('cache/' + entry + '/' + subentry)
    if (time_m > max_time):
      last_entry = 'cache/' + entry + '/' + subentry
  
  if last_entry is not None:
    files.append({
      "user": entry,
      "file": last_entry
    })


from .lib_python.AppendTime import AppendTime
files = AppendTime(files)

# 加上檔案大小
for i, file in enumerate(files):
  file_stats = os.stat(last_entry)
  files[i]['filesize'] = file_stats.st_size / (1024 * 1024)

# 加上檔案內文


print(json.dumps(files, indent=4, ensure_ascii=False))