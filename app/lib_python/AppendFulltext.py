
import os

# import parser object from tike
from tika import parser  

from diskcache import Cache 
cache = Cache()

def extractContentFromFile(file):
  if file in cache:
    return cache[file]

  print('Parsing file: ' + file)
  parsed_file = parser.from_file(file)
  data = parsed_file['content'] 

  data = data.replace('\n', ' ')
  while data.find('  ') != -1:
    data = data.replace('  ', ' ')
    
  cache[file] = data
  return data

def AppendFulltext(files):
  # 加上檔案大小
  for i, file in enumerate(files):
    data = extractContentFromFile(file['file'])
    
    # Printing of content 
    files[i]['data_length'] = len(data)
    files[i]['data'] = data
  return files
