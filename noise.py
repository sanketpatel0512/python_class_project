import pandas as pd

def ZipNoise(y):
    noisedata = pd.read_csv("noise.csv", usecols = ['Reason','Incident Zip','Borough','Created Date'])
    noisedata = noisedata.dropna()
    noisedata = noisedata.rename(columns = {'Created Date': 'Noise Rate','Incident Zip':'zipcode','Borough':'boro','Unique Key':'key'})
    
    noisedata = noisedata[noisedata['Noise Rate'].str.contains('|'.join(['2010','2011','2012','2013','2014','2015']))]
    noisedata['Noise Rate'] = pd.to_datetime(noisedata['Noise Rate'])
    noisedata['year'] = noisedata['Noise Rate'].dt.year
    noisedata = noisedata[noisedata['year'] == y]
    
    noisedata = noisedata.groupby(['boro','zipcode','year',"Reason"]).count().reset_index()
    noisedata = noisedata.drop(['Reason'],axis = 1)
    noisedata = noisedata.groupby(['boro','zipcode','year']).sum().reset_index()
    return noisedata

