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
crimedata = pd.read_csv("NYPD_Complaint_Data_Historic.csv", usecols = ['CMPLNT_TO_Date','BORO_NM','LAW_CAT_CD','CMPLNT_FR_Date'])
                                                    
crimedata = crimedata.rename(columns = {'CMPLNT_TO_Date':'complaint_end',\
                                        'CMPLNT_FR_Date':'complaint_start',\
                                        'LAW_CAT_CD':'lawtype','BORO_NM':'Boro'})
crimedata = crimedata.fillna(crimedata.mean())
