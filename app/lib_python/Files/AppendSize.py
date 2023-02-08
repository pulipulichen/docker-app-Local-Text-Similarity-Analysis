
import os

def AppendSize(files):
  # 加上檔案大小
  for i, file in enumerate(files):
    file_stats = os.stat(file['file'])
    files[i]['filesize'] = file_stats.st_size / (1024 * 1024)
  return files
