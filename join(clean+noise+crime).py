import pandas as pd
#Noise Data Input
noisedata = pd.read_csv("Noise.csv", usecols = ['Reason','Incident Zip','Borough',\
                        'Resolution Action Date'])
noisedata = noisedata.dropna()
noisedata = noisedata.rename(columns = {'Resolution Action Date': 'Date','Incident Zip':'zipcode',\
                                        'Borough':'boro','Unique Key':'key'})
noisedata['Date'] = pd.to_datetime(noisedata['Date'])
noisedata['year'] = noisedata['Date'].dt.year
noisedata=noisedata[noisedata["year"]<=2015]
noisedata=noisedata.groupby(['boro','zipcode',"Reason",'year']).count().reset_index()
#print(noisedata)

#Air Data Input
cleandata = pd.read_csv("Cleanliness.csv",usecols = ['Month', 'Borough', 'Acceptable Streets %', \
                                                           'Acceptable Sidewalks %'])

cleandata = cleandata.rename(columns = {'Acceptable Streets %': 'clean%','Borough':'boro'})
cleandata['boro']=cleandata['boro'].str.upper()
cleandata = cleandata.fillna(cleandata.mean())
cleandata['Month'] = pd.to_datetime(cleandata['Month'])
cleandata['year'] = cleandata['Month'].dt.year
cleandata=cleandata[cleandata["year"]>=2010]
cleandata = cleandata.groupby(['boro','year']).mean().reset_index()
#print(cleandata)

#Crime Data Input
crimedata = pd.read_csv("Crime.csv", usecols = ['CMPLNT_FR_Date','BORO_NM','OFNS_DESC',"LAW_CAT_CD","CMPLNT_NUM"])
crimedata = crimedata.rename(columns = {'CMPLNT_FR_Date':'Date',\
                                        'OFNS_DESC':'Offense',\
                                        'LAW_CAT_CD':'Lawtype','BORO_NM':'boro'})
crimedata = crimedata.dropna()
crimedata['Date'] = pd.to_datetime(crimedata['Date'])
crimedata['year'] = crimedata['Date'].dt.year
crimedata=crimedata[crimedata["year"]>=2010]
crimedata=crimedata.groupby(['boro','Offense',"Lawtype"]).count().reset_index()
#print(crimedata)

c=noisedata.merge(cleandata,on="boro")
d=c.merge(crimedata, on="boro")
print(d)
