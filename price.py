import pandas as pd

def ZipPrice(z):

    pricedata = pd.DataFrame()

    m = pd.read_csv("salesprice_manhattan.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
    m = m.dropna() # drop any row if one of the column is empty
    m = m[m['SALE PRICE']!= 0]
    m = m[m['GROSS SQUARE FEET']!= 0]
    m['Price/sqft'] = m['SALE PRICE']/m['GROSS SQUARE FEET']
    m = m.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['Price/sqft'].mean().reset_index()
    m = m.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
    pricedata = pricedata.append(m)

    bx = pd.read_csv("salesprice_bronx.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
    bx = bx.dropna() # drop any row if one of the column is empty
    bx = bx[bx['SALE PRICE']!= 0]
    bx = bx[bx['GROSS SQUARE FEET']!= 0]
    bx['Price/sqft'] = bx['SALE PRICE']/bx['GROSS SQUARE FEET']
    bx = bx.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['Price/sqft'].mean().reset_index()
    bx = bx.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
    pricedata = pricedata.append(bx)
    
    bl = pd.read_csv("salesprice_brooklyn.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
    bl = bl.dropna() # drop any row if one of the column is empty
    bl = bl[bl['SALE PRICE']!= 0]
    bl = bl[bl['GROSS SQUARE FEET']!= 0]
    bl['Price/sqft'] = bl['SALE PRICE']/bl['GROSS SQUARE FEET']
    bl = bl.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['Price/sqft'].mean().reset_index()
    bl = bl.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
    pricedata = pricedata.append(bl)
    
    q = pd.read_csv("salesprice_queens.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
    q = q.dropna() # drop any row if one of the column is empty
    q = q[q['SALE PRICE']!= 0]
    q = q[q['GROSS SQUARE FEET']!= 0]
    q['Price/sqft'] = q['SALE PRICE']/q['GROSS SQUARE FEET']
    q = q.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['Price/sqft'].mean().reset_index()
    q = q.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
    pricedata = pricedata.append(q)
    
    s = pd.read_csv("salesprice_statenisland.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
    s = s.dropna() # drop any row if one of the column is empty
    s = s[s['SALE PRICE']!= 0]
    s = s[s['GROSS SQUARE FEET']!= 0]
    s['Price/sqft'] = s['SALE PRICE']/s['GROSS SQUARE FEET']
    s = s.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['Price/sqft'].mean().reset_index()
    s = s.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
    pricedata = pricedata.append(s)
    borolist = ['MANHATTAN','BRONX','BROOKLYN','QUEENS','STATEN ISLAND']
    for i in range(5):
        mask = pricedata.boro == i+1
        column_name = 'boro'
        pricedata.loc[mask, column_name] = borolist[i]
    pricedata = pricedata[pricedata['zipcode'] == z]
    return pricedata
