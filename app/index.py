from lib_python.ExtractZip import *
filename = ExtractZip()

from lib_python.Files.GetFileDataFrame import *
files = GetFileDataFrame()

from lib_python.Files.AppendTime import *
files = AppendTime(files)

from lib_python.Files.AppendSize import *
files = AppendSize(files)

from lib_python.Files.AppendFulltext import *
files = AppendFulltext(files)

from lib_python.Distance.CalcDistanceDataFrame import *
distance_df = CalcDistanceDataFrame(files)

from lib_python.SaveODS import *
SaveODS(files, filename)
