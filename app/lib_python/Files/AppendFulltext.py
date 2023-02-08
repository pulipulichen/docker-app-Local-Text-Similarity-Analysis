
import os

# import parser object from tike
from tika import parser  

from sqlite_cache.sqlite_cache import SqliteCache
sql_cache = SqliteCache('cache')

def extractContentFromFile(file):
  if sql_cache.get(file) != None:
    return sql_cache.get(file)

  print('Parsing file: ' + file)
  parsed_file = parser.from_file(file)
  data = parsed_file['content'] 

  data = data.replace('\n', ' ')
  while data.find('  ') != -1:
    data = data.replace('  ', ' ')
    
  sql_cache.set(file, data)
  return data

def AppendFulltext(files):
  for i, file in enumerate(files):
    data = extractContentFromFile(file['file'])
    
    # Printing of content 
    files[i]['data_length'] = len(data)
    files[i]['data'] = data
  return files
