import pandas as pd
#Crime data 
def BoroCrime(b):


    crimedata = pd.read_csv("crime.csv", usecols = ['CMPLNT_FR_Date','BORO_NM',"LAW_CAT_CD","CMPLNT_NUM"])
    crimedata = crimedata.rename(columns = {'CMPLNT_NUM':'CMPLT_COUNT','CMPLNT_FR_Date':'Date',\
                                        'LAW_CAT_CD':'Lawtype','BORO_NM':'boro'})
    crimedata = crimedata.dropna()
    crimedata = crimedata[crimedata['boro'] == b]
    crimedata['Date'] = pd.to_datetime(crimedata['Date'])
    crimedata['year'] = crimedata['Date'].dt.year
    crimedata = crimedata.drop(['Date'],axis = 1)
    crimedata=crimedata[crimedata["year"]>=2010]  
    crimedata=crimedata.groupby(['boro','year']).count().reset_index()
    return crimedata
