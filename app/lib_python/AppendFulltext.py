
import os

# import parser object from tike
from tika import parser  

def AppendFulltext(files):
  # 加上檔案大小
  for i, file in enumerate(files):
    parsed_file = parser.from_file(file['file'])
      
    # saving content of pdf
    # you can also bring text only, by parsed_pdf['text'] 
    # parsed_pdf['content'] returns string 
    data = parsed_file['content'] 

    data = data.replace('\n', ' ')
    while data.find('  ') != -1:
      data = data.replace('  ', ' ')
      
    # Printing of content 
    files[i]['data_length'] = len(data)
    files[i]['data'] = data
  return files
