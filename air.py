import pandas as pd

def AirBoro(c):
    
    airdata = pd.read_csv("air.csv")
    delcolumn = ['indicator_data_id','indicator_id','geo_entity_id']
    airdata = airdata.rename(columns = {'geo_entity_name':'boro','year_description':'year'})  
    airdata['boro'] = airdata['boro'].str.upper()
    
    airdata = airdata.drop(delcolumn, axis = 1)
    airdata = airdata[airdata['geo_type_name']=='Borough']
    airdata['data_valuemessage'] = airdata['data_valuemessage'].apply(pd.to_numeric)
    #airdata = airdata[airdata['year'] == '2013']
    airdata = airdata[airdata['boro'] == c]
    airdata = airdata.groupby(['boro','name','year']).mean().reset_index()
    return airdata

