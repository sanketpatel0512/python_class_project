import pandas as pd

def ZipNoise(z):
    noisedata = pd.read_csv("noise.csv", usecols = ['Reason','Incident Zip','Borough','Created Date'])
    noisedata = noisedata.dropna()
    noisedata = noisedata.rename(columns = {'Created Date': 'Compl_count','Incident Zip':'zipcode','Borough':'boro','Unique Key':'key'})
    noisedata = noisedata[noisedata['zipcode'] == z]
    noisedata = noisedata[noisedata['Compl_count'].str.contains('|'.join(['2015','2016','2017','2018']))]
    noisedata['Compl_count'] = pd.to_datetime(noisedata['Compl_count'])
    noisedata['year'] = noisedata['Compl_count'].dt.year
    #noisedata=noisedata[noisedata["year"]==2015]
    #noisedata.drop(['noise_year'],axis = 1)
    
    noisedata=noisedata.groupby(['boro','zipcode','year',"Reason"]).count().reset_index()
    return noisedata

