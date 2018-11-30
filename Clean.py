import pandas as pd
#cleanlinessdata
def BoroClean(a):
    cleandata = pd.read_csv("cleanliness.csv",usecols = ['Month', 'Borough', 'Acceptable Streets %', 'Acceptable Sidewalks %'])
    
    cleandata = cleandata.rename(columns = {'Acceptable Streets %': 'clean%','Borough':'boro'})
    cleandata['boro']=cleandata['boro'].str.upper()
    cleandata = cleandata[cleandata['boro'] == a]
    cleandata = cleandata.fillna(cleandata.mean())
    cleandata = cleandata[cleandata['Month'].str.contains('2015')]
#cleandata['Month'] = pd.to_datetime(cleandata['Month'])
#cleandata['clean_year'] = cleandata['Month'].dt.year
#cleandata=cleandata[cleandata["clean_year"]==2015]
    cleandata = cleandata.groupby(['boro']).mean().reset_index()
    return cleandata



