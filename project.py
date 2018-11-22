import pandas as pd
#School Data Input
schldata = pd.read_csv("schoolzip.csv", usecols = ['dbn','school_name','boro','graduation_rate',\
                                                    'attendance_rate','pct_stu_enough_variety',\
                                                    'college_career_rate','pct_stu_safe','Postcode'])
schldata = schldata.rename(columns = {'pct_stu_enough_variety':'variety_rate','pct_stu_safe':'safety_rate'})
schldata = schldata.fillna(schldata.mean())

#Air Data Input
airdata = pd.read_csv("Air_Quality.csv")
delcolumn = ['indicator_data_id','indicator_id','geo_entity_id']
airdata = airdata.drop(delcolumn, axis = 1)
airdata = airdata[airdata['geo_type_name']=='Borough']
airdata['data_valuemessage'] = airdata['data_valuemessage'].apply(pd.to_numeric)
airdata = airdata.groupby(['geo_entity_name','name','year_description']).mean().reset_index()

#Age Data
popdata = pd.read_csv("Population.csv", usecols = ['Borough','Age','2015','2020'])
borolist = list(popdata['Borough'].unique())
totallist = popdata[popdata['Age'] == 'Total']
#print(float(totallist['2015'].where(totallist['Borough'] == 'Bronx').dropna().values))
agedata = pd.DataFrame()
for b in borolist:
    pop= popdata[popdata['Borough'] == b]
    pop['Current %'] = 100*(pop['2015']/(float(totallist['2015'].where(totallist['Borough'] == b).dropna().values)))
    pop['Future %'] = 100*(pop['2020']/(float(totallist['2020'].where(totallist['Borough'] == b).dropna().values)))
    agedata = agedata.append(pop,ignore_index = True)
print(agedata)

#crimedata
crimedata = pd.read_csv("NYPD_Complaint_Data_Historic with attributes.csv", usecols = ['CMPLNT_FR_Date','BORO_NM','OFNS_DESC',"LAW_CAT_CD","CMPLNT_NUM"])
crimedata = crimedata.rename(columns = {'CMPLNT_FR_Date':'Date',\
                                        'OFNS_DESC':'Offense',\
                                        'LAW_CAT_CD':'Lawtype','BORO_NM':'Borough'})
crimedata = crimedata.dropna()
#crimedata= = crimedata["COMPLNT_FR_Date"]
crimedata['Date'] = pd.to_datetime(crimedata['Date'])
crimedata['year'] = crimedata['Date'].dt.year
crimedata=crimedata.groupby(['Borough','Offense',"Lawtype"]).count().reset_index()
print(crimedata)

#cleanlinessdata
cleandata = pd.read_csv("Scorecard_Ratings.csv",usecols = ['Month', 'Borough', 'Acceptable Streets %', 'Acceptable Sidewalks %'])

cleandata = cleandata.rename(columns = {'Borough': 'Boro',\
                                        'Acceptable Streets %': 'clean%'})
cleandata = cleandata.fillna(cleandata.mean())
cleandata['Month'] = pd.to_datetime(cleandata['Month'])
cleandata['year'] = cleandata['Month'].dt.year
cleandata = cleandata.groupby(['Boro','year']).mean()
print(cleandata)

# Sale Price Data

pricedata = pd.DataFrame()

m = pd.read_csv("rollingsales_manhattan.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
m = m.dropna() # drop any row if one of the column is empty
m = m[m['SALE PRICE']!= 0]
m = m[m['GROSS SQUARE FEET']!= 0]
m['Price/sqft'] = m['SALE PRICE']/m['GROSS SQUARE FEET']
m = m.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['Price/sqft'].mean().reset_index()
pricedata = pricedata.append(m)

bx = pd.read_csv("rollingsales_bronx.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
bx = bx.dropna() # drop any row if one of the column is empty
bx = bx[bx['SALE PRICE']!= 0]
bx = bx[bx['GROSS SQUARE FEET']!= 0]
bx['Price/sqft'] = bx['SALE PRICE']/bx['GROSS SQUARE FEET']
bx = bx.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['Price/sqft'].mean().reset_index()
pricedata = pricedata.append(bx)

bl = pd.read_csv("rollingsales_brooklyn.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
bl = bl.dropna() # drop any row if one of the column is empty
bl = bl[bl['SALE PRICE']!= 0]
bl = bl[bl['GROSS SQUARE FEET']!= 0]
bl['Price/sqft'] = bl['SALE PRICE']/bl['GROSS SQUARE FEET']
bl = bl.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['Price/sqft'].mean().reset_index()
pricedata = pricedata.append(bl)

q = pd.read_csv("rollingsales_queens.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
q = q.dropna() # drop any row if one of the column is empty
q = q[q['SALE PRICE']!= 0]
q = q[q['GROSS SQUARE FEET']!= 0]
q['Price/sqft'] = q['SALE PRICE']/q['GROSS SQUARE FEET']
q = q.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['Price/sqft'].mean().reset_index()
pricedata = pricedata.append(q)

s = pd.read_csv("rollingsales_statenisland.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
s = s.dropna() # drop any row if one of the column is empty
s = s[s['SALE PRICE']!= 0]
s = s[s['GROSS SQUARE FEET']!= 0]
s['Price/sqft'] = s['SALE PRICE']/s['GROSS SQUARE FEET']
s = s.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['Price/sqft'].mean().reset_index()
pricedata = pricedata.append(s)

print(pricedata)

# Noise Data
noisedata = pd.read_csv("311_Noise_in_NYC(marked).csv", usecols = ['Reason','Incident Zip','City','Borough','Resolution Action Date'])
noisedata = noisedata.dropna()
noisedata['Resolution Action Date'] = pd.to_datetime(noisedata['Resolution Action Date'])
noisedata['year'] = noisedata['Resolution Action Date'].dt.year
noisedata=noisedata.groupby(['Borough','Incident Zip',"Reason",'year']).count().reset_index()
print(noisedata)
