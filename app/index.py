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
df = CalcDistanceDataFrame(files)

from lib_python.Distance.CalcDistanceOutlier import *
df = CalcDistanceOutlier(df)

from lib_python.Distance.GetOutliers import *
outliers = GetOutliers(df)
files['is_outlier'] = files['user'].isin(outliers)

from lib_python.Distance.BuildNetwork import *
G = BuildNetwork(df)

from lib_python.Distance.ClusteringFiles import *
cluster_dict = ClusteringFiles(G)
files['cluster'] = files['user'].replace(cluster_dict)

from lib_python.Distance.AddOutlierAttribute import *
G = AddOutlierAttribute(G, outliers)

from lib_python.Save.SaveCYJS import *
SaveCYJS(G, filename)

from lib_python.Save.SaveODS import *
SaveODS(files, filename)
