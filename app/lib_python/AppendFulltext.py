
import os

# import parser object from tike
from tika import parser  

def AppendSize(files):
  # 加上檔案大小
  for i, file in enumerate(files):
    parsed_file = parser.from_file(file['file'])
      
    # saving content of pdf
    # you can also bring text only, by parsed_pdf['text'] 
    # parsed_pdf['content'] returns string 
    data = parsed_file['content'] 
      
    # Printing of content 
    files[i]['data_length'] = len(data)
  return files
