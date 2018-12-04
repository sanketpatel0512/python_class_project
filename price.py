import pandas as pd
import numpy as np
def ZipPrice(y):

    pricedata = pd.DataFrame()
    res = [' A5 ', ' A9 ', ' A7 ', ' A4 ', ' B1 ', ' C3 ', ' C4 ', ' C7 ',\
           ' C1 ', ' C2 ', ' C5 ',' C0 ', ' D1 ', ' D6 ', ' D7 ', ' D5 ', \
           ' D9 ',' B3 ', ' B9 ', ' RR ', ' D3 ', ' D2 ' , ' B2 ', ' A1 ', \
           ' C9 ',' A2 ',' A3 ',' A0 ',' A6 ', ' A8 ',' C6 ',' D4 ',' D8 ',\
           ' D0 ',' R0 ', ' C8 ',' R1 ', ' R9 ',' R4 ']
    mix = [' S4 ', ' S2 ', ' S3 ', ' S9 ', ' S5 ',' S1 ',' S0 ']
    com = [' L9 ', ' O8 ', ' O9 ', ' L2 ', ' O7 ', ' HR ', ' K5 ', ' H6 ',\
           ' K7 ',' H2 ', ' H3 ', ' H8 ', ' H1 ', ' H5 ', ' L8 ', ' O3 ', \
           ' O5 ', ' O6 ', ' K4 ', ' O4 ', ' K1 ', ' K2 ',' L1 ', ' L3 ', \
           ' K9 ', ' O2 ',' O1 ',' K6 ',' H9 ',' H4 ',' K3 ',' HS ',' HB ']
    ind = [' E1 ', ' G2 ', ' G1 ', ' G9 ', ' G3 ', ' GW ', ' G8 ', ' E9 ',\
           ' E3 ',' E7 ',' E2 ', ' E4 ',' G5 ',' G4 ',' G6 ',' G7 ',' G0 ',\
           ' GU ',' F5 ',' F9 ',' F1 ',' F4 ',' F2 ',' F8 ',' T9 ']
    civ = [' M3 ', ' I1 ',' I9 ', ' P2 ', ' W8 ', ' J6 ', ' W4 ', ' J3 ',\
           ' W1 ', ' P5 ', ' W1 ', ' M9 ', ' W7 ', ' I7 ', ' N9 ', ' I6 ',\
           ' W3 ',' I5 ',' J9 ',' M1 ',' N2 ',' M2 ',' W9 ',' I4 ',' M4 ',\
           ' P7 ',' J1 ',' P8 ',' W2 ',' P9 ',' J8 ',' W6 ',' J4 ',' P1 ',\
           ' P6 ',' P3 ',' J5 ',' I2 ',' J2 ',' N3 ',' N4 ',' Q1 ',' Q2 ',\
           ' Q8 ',' Q9 ',' Q3 ']
    oth = [' Z4 ',' Z9 ',' Z2 ',' Z3 ',' Z0 ',' Z8 ',' Z5 ',' Z1 ']
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
    
    
    conditions = [pricedata['BUILDING CLASS AT TIME OF SALE'].isin(res),\
                  pricedata['BUILDING CLASS AT TIME OF SALE'].isin(mix),\
                  pricedata['BUILDING CLASS AT TIME OF SALE'].isin(com),\
                  pricedata['BUILDING CLASS AT TIME OF SALE'].isin(ind),\
                  pricedata['BUILDING CLASS AT TIME OF SALE'].isin(civ),\
                  pricedata['BUILDING CLASS AT TIME OF SALE'].isin(oth)]
    choices = ['Residential', 'Mixed Use','Commercial','Industrial','Civic Use','Other']
    
    pricedata['type'] = np.select(conditions, choices, default='black')
    pricedata = pricedata.drop(['BUILDING CLASS AT TIME OF SALE'],axis = 1)
    pricedata = pricedata[pricedata['year'] == y]
    pricedata = pricedata.drop(pricedata['year'])
    pricedata = pricedata.groupby(['boro','zipcode','type']).mean().reset_index() 
    return pricedata
 

