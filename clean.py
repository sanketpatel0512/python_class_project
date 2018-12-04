
import pandas as pd
#cleanlinessdata
def BoroClean(y):
    cleandata = pd.read_csv("cleanliness.csv",usecols = ['Month', 'Borough', 'Acceptable Streets %', 'Acceptable Sidewalks %'])
    
    cleandata = cleandata.rename(columns = {'Acceptable Streets %': 'clean%','Borough':'boro'})
    cleandata['boro']=cleandata['boro'].str.upper()

    cleandata = cleandata.fillna(cleandata.mean())
    cleandata = cleandata[cleandata['Month'].str.contains(str(y))]

    cleandata = cleandata.groupby(['boro']).mean().reset_index()
    return cleandata