from lib_python.ExtractZip import *
ExtractZip()

from lib_python.GetFileList import *
files = GetFileList()

from lib_python.AppendTime import *
files = AppendTime(files)

from lib_python.AppendSize import *
files = AppendSize(files)

# 加上檔案內文

import json
print(json.dumps(files, indent=4, ensure_ascii=False))