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

#Population Data Input
popdata = pd.read_csv("Population.csv")

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

# Property Valuation Data
value = pd.read_csv("PropertyValuation.csv", usecols = ['BBLE','B','BLDGCL','STORIES','FULLVAL','AVTOT','ZIP','YEAR'])
value = value.rename(columns = {'BBLE':'ID','B':'Borough','BLDGCL':'Building_Class', 'STORIES':'#ofStories', 'FULLVAL':'Market_Value',\
'AVTOT':'Actual_Total_Value'})

# Noise Data
noisedata = pd.read_csv("311_Noise_in_NYC(marked).csv", usecols = ['Reason','Incident Zip','City','Borough','Resolution Action Date'])
noisedata = noisedata.dropna()
noisedata['Resolution Action Date'] = pd.to_datetime(noisedata['Resolution Action Date'])
noisedata['year'] = noisedata['Resolution Action Date'].dt.year
noisedata=noisedata.groupby(['Borough','Incident Zip',"Reason",'year']).count().reset_index()
print(noisedata)
