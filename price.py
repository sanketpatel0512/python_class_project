import pandas as pd
import numpy as np
def ZipPrice():

    pricedata = pd.DataFrame()
    res = [' A5 ', ' A9 ', ' A7 ', ' A4 ', ' B1 ', ' C3 ', ' C4 ', ' C7 ',\
           ' C1 ', ' C2 ', ' C5 ',' C0 ', ' D1 ', ' D6 ', ' D7 ', ' D5 ', \
           ' D9 ',' B3 ', ' B9 ', ' RR ', ' D3 ', ' D2 ' , ' B2 ', ' A1 ', ' C9 ']
    mix = [' S4 ', ' S2 ', ' S3 ', ' S9 ', ' S5 ',' S1 ',' S0 ']
    com = [' L9 ', ' O8 ', ' O9 ', ' L2 ', ' O7 ', ' HR ', ' K5 ', ' H6 ',\
           ' K7 ',' H2 ', ' H3 ', ' H8 ', ' H1 ', ' H5 ', ' L8 ', ' O3 ', \
           ' O5 ', ' O6 ', ' K4 ', ' O4 ', ' K1 ', ' K2 ',' L1 ', ' L3 ', \
           ' K9 ', ' O2 ']
    ind = [' E1 ', ' G2 ', ' G1 ', ' G9 ', ' G3 ', ' GW ', ' G8 ', ' E9 ']
    civ = [' M3 ', ' I1 ',' I9 ', ' P2 ', ' W8 ', ' J6 ', ' W4 ', ' J3 ',\
           ' W1 ', ' P5 ', ' W1 ', ' M9 ', ' W7 ', ' I7 ', ' N9 ', ' I6 ',\
           ' W3 ',' I5 ',' J9 ',' M1 ',' N2 ']
    oth = [' Z4 ',' Z9 ']
    files = ['2010_manhattan.csv','2010_bronx.csv','2010_brooklyn.csv','2010_queens.csv','2010_statenisland.csv',\
             '2011_manhattan.csv','2011_bronx.csv','2011_brooklyn.csv','2011_queens.csv','2011_statenisland.csv',\
             '2012_manhattan.csv','2012_bronx.csv','2012_brooklyn.csv','2012_queens.csv','2012_statenisland.csv',\
             '2013_manhattan.csv','2013_bronx.csv','2013_brooklyn.csv','2013_queens.csv','2013_statenisland.csv',\
             '2014_manhattan.csv','2014_bronx.csv','2014_brooklyn.csv','2014_queens.csv','2014_statenisland.csv',\
             '2015_manhattan.csv','2015_bronx.csv','2015_brooklyn.csv','2015_queens.csv','2015_statenisland.csv']
    year = 2010
    for i in range(len(files)):
        
        m = pd.read_csv(files[i], usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
        m = m.dropna() # drop any row if one of the column is empty
        m = m[m['SALE PRICE']!= 0]
        m = m[m['GROSS SQUARE FEET']!= 0]
        m['Price/sqft'] = m['SALE PRICE']/m['GROSS SQUARE FEET']
        m = m.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['Price/sqft'].mean().reset_index()
        m = m.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
        if (i+1)%5 == 0:
            year = year + 1
        m['year'] = year
        pricedata = pricedata.append(m)

    borolist = ['MANHATTAN','BRONX','BROOKLYN','QUEENS','STATEN ISLAND']
    for i in range(5):
        mask = pricedata.boro == i+1
        column_name = 'boro'
        pricedata.loc[mask, column_name] = borolist[i]
    #classlist = list(pricedata['BUILDING CLASS AT TIME OF SALE'].unique())
    #print (classlist)
    
    conditions = [pricedata['BUILDING CLASS AT TIME OF SALE'].isin(res),\
                  pricedata['BUILDING CLASS AT TIME OF SALE'].isin(mix),\
                  pricedata['BUILDING CLASS AT TIME OF SALE'].isin(com),\
                  pricedata['BUILDING CLASS AT TIME OF SALE'].isin(ind),\
                  pricedata['BUILDING CLASS AT TIME OF SALE'].isin(civ),\
                  pricedata['BUILDING CLASS AT TIME OF SALE'].isin(oth)]
    choices = ['Residential', 'Mixed Use','Commercial','Industrial','Civic Use','Other']
    
    pricedata['Type'] = np.select(conditions, choices, default='black')
    #pricedata = pricedata.drop(['BUILDING CLASS AT TIME OF SALE'],axis = 1)
    #pricedata = pricedata[pricedata['zipcode'] == z]
    pricedata = pricedata[pricedata['Type'] == 'black']
    typelist = pricedata['BUILDING CLASS AT TIME OF SALE'].unique()
    #pricedata = pricedata.groupby(['boro','zipcode','year','Type','BUILDING CLASS AT TIME OF SALE']).mean().reset_index() 
    return typelist
 

