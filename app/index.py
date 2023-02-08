from lib_python.ExtractZip import *
filename = ExtractZip()

from lib_python.GetFileList import *
files = GetFileList()

from lib_python.AppendTime import *
files = AppendTime(files)

from lib_python.AppendSize import *
files = AppendSize(files)

from lib_python.AppendFulltext import *
files = AppendFulltext(files)

from lib_python.CalcSimilarityMartrix import *
matrix = CalcSimilarityMartrix(files)

from lib_python.SaveODS import *
SaveODS(files, filename)
