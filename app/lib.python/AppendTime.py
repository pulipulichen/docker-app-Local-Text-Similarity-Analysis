import os
from datetime import datetime
# 加上修改時間
def AppendTime(files):

  for i, file in enumerate(files):
    time = os.path.getmtime(file['file'])
    time = datetime.fromtimestamp(time).strftime('%m/%d %H:%M:%S')
    files[i]['modified_time'] = time

  return files
