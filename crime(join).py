crimedata = pd.read_csv("Crime.csv", usecols = ['CMPLNT_FR_Date','BORO_NM','OFNS_DESC',"LAW_CAT_CD","CMPLNT_NUM"])
crimedata = crimedata.rename(columns = {'CMPLNT_FR_Date':'Date',\
                                        'OFNS_DESC':'Offense',\
                                        'LAW_CAT_CD':'Lawtype','BORO_NM':'boro'})
crimedata = crimedata.dropna()
crimedata['Date'] = pd.to_datetime(crimedata['Date'])
crimedata['year'] = crimedata['Date'].dt.year
crimedata=crimedata[crimedata["year"]>=2010]
crimedata=crimedata.groupby(['boro','Offense',"Lawtype"]).count().reset_index()
