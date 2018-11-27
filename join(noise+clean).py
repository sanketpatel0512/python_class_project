import pandas as pd

#noise data
noisedata = pd.read_csv("Noise.csv", usecols = ['Reason','Incident Zip','Borough','Resolution Action Date'])
noisedata = noisedata.dropna()
noisedata = noisedata.rename(columns = {'Resolution Action Date': 'Date','Incident Zip':'zipcode','Borough':'boro','Unique Key':'key'})
noisedata['Date'] = pd.to_datetime(noisedata['Date'])
noisedata['year'] = noisedata['Date'].dt.year
noisedata=noisedata[noisedata["year"]<=2018]
noisedata=noisedata.groupby(['boro','zipcode',"Reason",'year']).count().reset_index()

#Air Data Input
cleandata = pd.read_csv("Cleanliness.csv",usecols = ['Month', 'Borough', 'Acceptable Streets %', 'Acceptable Sidewalks %'])

cleandata = cleandata.rename(columns = {'Acceptable Streets %': 'clean%','Borough':'boro'})
cleandata['boro']=cleandata['boro'].str.upper()
cleandata = cleandata.fillna(cleandata.mean())
cleandata['Month'] = pd.to_datetime(cleandata['Month'])
cleandata['year'] = cleandata['Month'].dt.year
cleandata=cleandata[cleandata["year"]>=2010]
cleandata = cleandata.groupby(['boro','year']).mean().reset_index()

c=noisedata.merge(cleandata,on="boro")
print(c)
