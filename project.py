import pandas as pd
#School Data Input
schldata = pd.read_csv("school.csv", usecols = ['dbn','school_name','graduation_rate',\
                                                    'attendance_rate','pct_stu_enough_variety',\
                                                    'college_career_rate','pct_stu_safe','Postcode'])
schldata = schldata.rename(columns = {'Postcode':'zipcode','pct_stu_enough_variety':'variety_rate','pct_stu_safe':'safety_rate'})
schldata = schldata.fillna(schldata.mean())
schldata = schldata.groupby(['zipcode']).mean().reset_index()
#print(schldata['boro'].unique())


#Air Data Input
airdata = pd.read_csv("air.csv")
delcolumn = ['indicator_data_id','indicator_id','geo_entity_id']
airdata = airdata.rename(columns = {'geo_entity_name':'boro','year_description':'year'})
airdata['boro'] = airdata['boro'].str.upper()
airdata = airdata.drop(delcolumn, axis = 1)
airdata = airdata[airdata['geo_type_name']=='Borough']
airdata['data_valuemessage'] = airdata['data_valuemessage'].apply(pd.to_numeric)
#airdata = airdata[airdata['year'] == '2013']
airdata = airdata.groupby(['boro','name','year']).mean().reset_index()


#Age Data
popdata = pd.read_csv("age.csv", usecols = ['Borough','Age','2015','2020'])
popdata = popdata.rename(columns = {'Borough':'boro'})
popdata['boro'] = popdata['boro'].str.upper()
borolist = list(popdata['boro'].unique())
totallist = popdata[popdata['Age'] == 'Total']

agedata = pd.DataFrame()
for b in borolist:
    pop= popdata[popdata['boro'] == b]
    pop['Current %'] = 100*(pop['2015']/(float(totallist['2015'].where(totallist['boro'] == b).dropna().values)))
    pop['Future %'] = 100*(pop['2020']/(float(totallist['2020'].where(totallist['boro'] == b).dropna().values)))
    agedata = agedata.append(pop,ignore_index = True)

#Combine Air and Age
air_age = airdata.merge(agedata, on = 'boro')
#print(air_age)
yearlist = ['2018','2017','2016','2015']


#noise data
noisedata = pd.read_csv("noise.csv", usecols = ['Reason','Incident Zip','Borough','Created Date'])
noisedata = noisedata.dropna()
noisedata = noisedata.rename(columns = {'Created Date': 'Date','Incident Zip':'zipcode','Borough':'boro','Unique Key':'key'})
noisedata = noisedata[noisedata['Date'].str.contains('2015')]
#noisedata['Date'] = pd.to_datetime(noisedata['Date'])
#noisedata['noise_year'] = noisedata['Date'].dt.year
#noisedata=noisedata[noisedata["noise_year"]==2015]
#noisedata.drop(['noise_year'],axis = 1)
noisedata=noisedata.groupby(['boro','zipcode',"Reason"]).count().reset_index()
#print(noisedata)

#clean Data Input
cleandata = pd.read_csv("cleanliness.csv",usecols = ['Month', 'Borough', 'Acceptable Streets %', 'Acceptable Sidewalks %'])

cleandata = cleandata.rename(columns = {'Acceptable Streets %': 'clean%','Borough':'boro'})
cleandata['boro']=cleandata['boro'].str.upper()
cleandata = cleandata.fillna(cleandata.mean())
cleandata = cleandata[cleandata['Month'].str.contains('2015')]
#cleandata['Month'] = pd.to_datetime(cleandata['Month'])
#cleandata['clean_year'] = cleandata['Month'].dt.year
#cleandata=cleandata[cleandata["clean_year"]==2015]
cleandata = cleandata.groupby(['boro']).mean().reset_index()


#Master Data
nc=noisedata.merge(cleandata,on="boro")
ncaa = nc.merge(air_age,on = "boro")
#ncaap = ncaa.merge(pricedata, on = "boro")
masterData = ncaa.merge(schldata,on = "zipcode")

print(masterData)
