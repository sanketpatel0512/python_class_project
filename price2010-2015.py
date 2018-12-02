
import pandas as pd
#2015
pricedata2015 = pd.DataFrame()

m = pd.read_csv("2015_manhattan.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
m = m.dropna() # drop any row if one of the column is empty
m['SALE PRICE'] = pd.to_numeric(m['SALE PRICE'])
m['GROSS SQUARE FEET'] = pd.to_numeric(m['GROSS SQUARE FEET'])
m = m[m['SALE PRICE']!= 0]
m = m[m['GROSS SQUARE FEET'] != 0]
m['2015Price/sqft'] = m['SALE PRICE']/m['GROSS SQUARE FEET']
m = m.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2015Price/sqft'].mean().reset_index()
m = m.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2015 = pricedata2015.append(m)

bx = pd.read_csv("2015_bronx.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
bx = bx.dropna() # drop any row if one of the column is empty
bx['SALE PRICE'] = pd.to_numeric(bx['SALE PRICE'])
bx['GROSS SQUARE FEET'] = pd.to_numeric(bx['GROSS SQUARE FEET'])
bx = bx[bx['SALE PRICE']!= 0]
bx = bx[bx['GROSS SQUARE FEET']!= 0]
bx['2015Price/sqft'] = bx['SALE PRICE']/bx['GROSS SQUARE FEET']
bx = bx.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2015Price/sqft'].mean().reset_index()
bx = bx.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2015 = pricedata2015.append(bx)

bl = pd.read_csv("2015_brooklyn.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
bl = bl.dropna() # drop any row if one of the column is empty
bl['SALE PRICE'] = pd.to_numeric(bl['SALE PRICE'])
bl['GROSS SQUARE FEET'] = pd.to_numeric(bl['GROSS SQUARE FEET'])
bl = bl[bl['SALE PRICE']!= 0]
bl = bl[bl['GROSS SQUARE FEET']!= 0]
bl['2015Price/sqft'] = bl['SALE PRICE']/bl['GROSS SQUARE FEET']
bl = bl.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2015Price/sqft'].mean().reset_index()
bl = bl.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2015 = pricedata2015.append(bl)

q = pd.read_csv("2015_queens.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
q = q.dropna() # drop any row if one of the column is empty
q['SALE PRICE'] = pd.to_numeric(q['SALE PRICE'])
q['GROSS SQUARE FEET'] = pd.to_numeric(q['GROSS SQUARE FEET'])
q = q[q['SALE PRICE']!= 0]
q = q[q['GROSS SQUARE FEET']!= 0]
q['2015Price/sqft'] = q['SALE PRICE']/q['GROSS SQUARE FEET']
q = q.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2015Price/sqft'].mean().reset_index()
q = q.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2015 = pricedata2015.append(q)

s = pd.read_csv("2015_statenisland.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
s = s.dropna() # drop any row if one of the column is empty
s['SALE PRICE'] = pd.to_numeric(s['SALE PRICE'])
s['GROSS SQUARE FEET'] = pd.to_numeric(s['GROSS SQUARE FEET'])
s = s[s['SALE PRICE']!= 0]
s = s[s['GROSS SQUARE FEET']!= 0]
s['2015Price/sqft'] = s['SALE PRICE']/s['GROSS SQUARE FEET']
s = s.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2015Price/sqft'].mean().reset_index()
s = s.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2015 = pricedata2015.append(s)

#2014
pricedata2014 = pd.DataFrame()

m = pd.read_csv("2014_manhattan.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
m = m.dropna() # drop any row if one of the column is empty
m['SALE PRICE'] = pd.to_numeric(m['SALE PRICE'])
m['GROSS SQUARE FEET'] = pd.to_numeric(m['GROSS SQUARE FEET'])
m = m[m['SALE PRICE']!= 0]
m = m[m['GROSS SQUARE FEET'] != 0]
m['2014Price/sqft'] = m['SALE PRICE']/m['GROSS SQUARE FEET']
m = m.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2014Price/sqft'].mean().reset_index()
m = m.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2014 = pricedata2014.append(m)

bx = pd.read_csv("2014_bronx.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
bx = bx.dropna() # drop any row if one of the column is empty
bx['SALE PRICE'] = pd.to_numeric(bx['SALE PRICE'])
bx['GROSS SQUARE FEET'] = pd.to_numeric(bx['GROSS SQUARE FEET'])
bx = bx[bx['SALE PRICE']!= 0]
bx = bx[bx['GROSS SQUARE FEET']!= 0]
bx['2014Price/sqft'] = bx['SALE PRICE']/bx['GROSS SQUARE FEET']
bx = bx.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2014Price/sqft'].mean().reset_index()
bx = bx.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2014 = pricedata2014.append(bx)

bl = pd.read_csv("2014_brooklyn.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
bl = bl.dropna() # drop any row if one of the column is empty
bl['SALE PRICE'] = pd.to_numeric(bl['SALE PRICE'])
bl['GROSS SQUARE FEET'] = pd.to_numeric(bl['GROSS SQUARE FEET'])
bl = bl[bl['SALE PRICE']!= 0]
bl = bl[bl['GROSS SQUARE FEET']!= 0]
bl['2014Price/sqft'] = bl['SALE PRICE']/bl['GROSS SQUARE FEET']
bl = bl.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2014Price/sqft'].mean().reset_index()
bl = bl.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2014 = pricedata2014.append(bl)

q = pd.read_csv("2014_queens.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
q = q.dropna() # drop any row if one of the column is empty
q['SALE PRICE'] = pd.to_numeric(q['SALE PRICE'])
q['GROSS SQUARE FEET'] = pd.to_numeric(q['GROSS SQUARE FEET'])
q = q[q['SALE PRICE']!= 0]
q = q[q['GROSS SQUARE FEET']!= 0]
q['2014Price/sqft'] = q['SALE PRICE']/q['GROSS SQUARE FEET']
q = q.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2014Price/sqft'].mean().reset_index()
q = q.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2014 = pricedata2014.append(q)

s = pd.read_csv("2014_statenisland.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
s = s.dropna() # drop any row if one of the column is empty
s['SALE PRICE'] = pd.to_numeric(s['SALE PRICE'])
s['GROSS SQUARE FEET'] = pd.to_numeric(s['GROSS SQUARE FEET'])
s = s[s['SALE PRICE']!= 0]
s = s[s['GROSS SQUARE FEET']!= 0]
s['2014Price/sqft'] = s['SALE PRICE']/s['GROSS SQUARE FEET']
s = s.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2014Price/sqft'].mean().reset_index()
s = s.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2014 = pricedata2014.append(s)

#2013
pricedata2013 = pd.DataFrame()

m = pd.read_csv("2013_manhattan.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
m = m.dropna() # drop any row if one of the column is empty
m['SALE PRICE'] = pd.to_numeric(m['SALE PRICE'])
m['GROSS SQUARE FEET'] = pd.to_numeric(m['GROSS SQUARE FEET'])
m = m[m['SALE PRICE']!= 0]
m = m[m['GROSS SQUARE FEET'] != 0]
m['2013Price/sqft'] = m['SALE PRICE']/m['GROSS SQUARE FEET']
m = m.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2013Price/sqft'].mean().reset_index()
m = m.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2013 = pricedata2013.append(m)

bx = pd.read_csv("2013_bronx.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
bx = bx.dropna() # drop any row if one of the column is empty
bx['SALE PRICE'] = pd.to_numeric(bx['SALE PRICE'])
bx['GROSS SQUARE FEET'] = pd.to_numeric(bx['GROSS SQUARE FEET'])
bx = bx[bx['SALE PRICE']!= 0]
bx = bx[bx['GROSS SQUARE FEET']!= 0]
bx['2013Price/sqft'] = bx['SALE PRICE']/bx['GROSS SQUARE FEET']
bx = bx.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2013Price/sqft'].mean().reset_index()
bx = bx.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2013 = pricedata2013.append(bx)

bl = pd.read_csv("2013_brooklyn.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
bl = bl.dropna() # drop any row if one of the column is empty
bl['SALE PRICE'] = pd.to_numeric(bl['SALE PRICE'])
bl['GROSS SQUARE FEET'] = pd.to_numeric(bl['GROSS SQUARE FEET'])
bl = bl[bl['SALE PRICE']!= 0]
bl = bl[bl['GROSS SQUARE FEET']!= 0]
bl['2013Price/sqft'] = bl['SALE PRICE']/bl['GROSS SQUARE FEET']
bl = bl.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2013Price/sqft'].mean().reset_index()
bl = bl.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2013 = pricedata2013.append(bl)

q = pd.read_csv("2013_queens.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
q = q.dropna() # drop any row if one of the column is empty
q['SALE PRICE'] = pd.to_numeric(q['SALE PRICE'])
q['GROSS SQUARE FEET'] = pd.to_numeric(q['GROSS SQUARE FEET'])
q = q[q['SALE PRICE']!= 0]
q = q[q['GROSS SQUARE FEET']!= 0]
q['2013Price/sqft'] = q['SALE PRICE']/q['GROSS SQUARE FEET']
q = q.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2013Price/sqft'].mean().reset_index()
q = q.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2013 = pricedata2013.append(q)

s = pd.read_csv("2013_statenisland.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
s = s.dropna() # drop any row if one of the column is empty
s['SALE PRICE'] = pd.to_numeric(s['SALE PRICE'])
s['GROSS SQUARE FEET'] = pd.to_numeric(s['GROSS SQUARE FEET'])
s = s[s['SALE PRICE']!= 0]
s = s[s['GROSS SQUARE FEET']!= 0]
s['2013Price/sqft'] = s['SALE PRICE']/s['GROSS SQUARE FEET']
s = s.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2013Price/sqft'].mean().reset_index()
s = s.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2013 = pricedata2013.append(s)

#2012
pricedata2012 = pd.DataFrame()

m = pd.read_csv("2012_manhattan.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
m = m.dropna() # drop any row if one of the column is empty
m['SALE PRICE'] = pd.to_numeric(m['SALE PRICE'])
m['GROSS SQUARE FEET'] = pd.to_numeric(m['GROSS SQUARE FEET'])
m = m[m['SALE PRICE']!= 0]
m = m[m['GROSS SQUARE FEET'] != 0]
m['2012Price/sqft'] = m['SALE PRICE']/m['GROSS SQUARE FEET']
m = m.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2012Price/sqft'].mean().reset_index()
m = m.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2012 = pricedata2012.append(m)

bx = pd.read_csv("2012_bronx.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
bx = bx.dropna() # drop any row if one of the column is empty
bx['SALE PRICE'] = pd.to_numeric(bx['SALE PRICE'])
bx['GROSS SQUARE FEET'] = pd.to_numeric(bx['GROSS SQUARE FEET'])
bx = bx[bx['SALE PRICE']!= 0]
bx = bx[bx['GROSS SQUARE FEET']!= 0]
bx['2012Price/sqft'] = bx['SALE PRICE']/bx['GROSS SQUARE FEET']
bx = bx.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2012Price/sqft'].mean().reset_index()
bx = bx.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2012 = pricedata2012.append(bx)

bl = pd.read_csv("2012_brooklyn.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
bl = bl.dropna() # drop any row if one of the column is empty
bl['SALE PRICE'] = pd.to_numeric(bl['SALE PRICE'])
bl['GROSS SQUARE FEET'] = pd.to_numeric(bl['GROSS SQUARE FEET'])
bl = bl[bl['SALE PRICE']!= 0]
bl = bl[bl['GROSS SQUARE FEET']!= 0]
bl['2012Price/sqft'] = bl['SALE PRICE']/bl['GROSS SQUARE FEET']
bl = bl.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2012Price/sqft'].mean().reset_index()
bl = bl.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2012 = pricedata2012.append(bl)

q = pd.read_csv("2012_queens.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
q = q.dropna() # drop any row if one of the column is empty
q['SALE PRICE'] = pd.to_numeric(q['SALE PRICE'])
q['GROSS SQUARE FEET'] = pd.to_numeric(q['GROSS SQUARE FEET'])
q = q[q['SALE PRICE']!= 0]
q = q[q['GROSS SQUARE FEET']!= 0]
q['2012Price/sqft'] = q['SALE PRICE']/q['GROSS SQUARE FEET']
q = q.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2012Price/sqft'].mean().reset_index()
q = q.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2012 = pricedata2012.append(q)

s = pd.read_csv("2012_statenisland.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
s = s.dropna() # drop any row if one of the column is empty
s['SALE PRICE'] = pd.to_numeric(s['SALE PRICE'])
s['GROSS SQUARE FEET'] = pd.to_numeric(s['GROSS SQUARE FEET'])
s = s[s['SALE PRICE']!= 0]
s = s[s['GROSS SQUARE FEET']!= 0]
s['2012Price/sqft'] = s['SALE PRICE']/s['GROSS SQUARE FEET']
s = s.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2012Price/sqft'].mean().reset_index()
s = s.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2012 = pricedata2012.append(s)

#2011
pricedata2011 = pd.DataFrame()

m = pd.read_csv("2011_manhattan.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
m = m.dropna() # drop any row if one of the column is empty
m['SALE PRICE'] = pd.to_numeric(m['SALE PRICE'])
m['GROSS SQUARE FEET'] = pd.to_numeric(m['GROSS SQUARE FEET'])
m = m[m['SALE PRICE']!= 0]
m = m[m['GROSS SQUARE FEET'] != 0]
m['2011Price/sqft'] = m['SALE PRICE']/m['GROSS SQUARE FEET']
m = m.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2011Price/sqft'].mean().reset_index()
m = m.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2011 = pricedata2011.append(m)

bx = pd.read_csv("2011_bronx.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
bx = bx.dropna() # drop any row if one of the column is empty
bx['SALE PRICE'] = pd.to_numeric(bx['SALE PRICE'])
bx['GROSS SQUARE FEET'] = pd.to_numeric(bx['GROSS SQUARE FEET'])
bx = bx[bx['SALE PRICE']!= 0]
bx = bx[bx['GROSS SQUARE FEET']!= 0]
bx['2011Price/sqft'] = bx['SALE PRICE']/bx['GROSS SQUARE FEET']
bx = bx.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2011Price/sqft'].mean().reset_index()
bx = bx.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2011 = pricedata2011.append(bx)

bl = pd.read_csv("2011_brooklyn.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
bl = bl.dropna() # drop any row if one of the column is empty
bl['SALE PRICE'] = pd.to_numeric(bl['SALE PRICE'])
bl['GROSS SQUARE FEET'] = pd.to_numeric(bl['GROSS SQUARE FEET'])
bl = bl[bl['SALE PRICE']!= 0]
bl = bl[bl['GROSS SQUARE FEET']!= 0]
bl['2011Price/sqft'] = bl['SALE PRICE']/bl['GROSS SQUARE FEET']
bl = bl.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2011Price/sqft'].mean().reset_index()
bl = bl.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2011 = pricedata2011.append(bl)

q = pd.read_csv("2011_queens.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
q = q.dropna() # drop any row if one of the column is empty
q['SALE PRICE'] = pd.to_numeric(q['SALE PRICE'])
q['GROSS SQUARE FEET'] = pd.to_numeric(q['GROSS SQUARE FEET'])
q = q[q['SALE PRICE']!= 0]
q = q[q['GROSS SQUARE FEET']!= 0]
q['2011Price/sqft'] = q['SALE PRICE']/q['GROSS SQUARE FEET']
q = q.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2011Price/sqft'].mean().reset_index()
q = q.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2011 = pricedata2011.append(q)

s = pd.read_csv("2011_statenisland.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
s = s.dropna() # drop any row if one of the column is empty
s['SALE PRICE'] = pd.to_numeric(s['SALE PRICE'])
s['GROSS SQUARE FEET'] = pd.to_numeric(s['GROSS SQUARE FEET'])
s = s[s['SALE PRICE']!= 0]
s = s[s['GROSS SQUARE FEET']!= 0]
s['2011Price/sqft'] = s['SALE PRICE']/s['GROSS SQUARE FEET']
s = s.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2011Price/sqft'].mean().reset_index()
s = s.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2011 = pricedata2011.append(s)

#2010
pricedata2010 = pd.DataFrame()

m = pd.read_csv("2010_manhattan.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
m = m.dropna() # drop any row if one of the column is empty
m['SALE PRICE'] = pd.to_numeric(m['SALE PRICE'])
m['GROSS SQUARE FEET'] = pd.to_numeric(m['GROSS SQUARE FEET'])
m = m[m['SALE PRICE']!= 0]
m = m[m['GROSS SQUARE FEET'] != 0]
m['2010Price/sqft'] = m['SALE PRICE']/m['GROSS SQUARE FEET']
m = m.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2010Price/sqft'].mean().reset_index()
m = m.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2010 = pricedata2010.append(m)

bx = pd.read_csv("2010_bronx.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
bx = bx.dropna() # drop any row if one of the column is empty
bx['SALE PRICE'] = pd.to_numeric(bx['SALE PRICE'])
bx['GROSS SQUARE FEET'] = pd.to_numeric(bx['GROSS SQUARE FEET'])
bx = bx[bx['SALE PRICE']!= 0]
bx = bx[bx['GROSS SQUARE FEET']!= 0]
bx['2010Price/sqft'] = bx['SALE PRICE']/bx['GROSS SQUARE FEET']
bx = bx.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2010Price/sqft'].mean().reset_index()
bx = bx.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2010 = pricedata2010.append(bx)

bl = pd.read_csv("2010_brooklyn.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
bl = bl.dropna() # drop any row if one of the column is empty
bl['SALE PRICE'] = pd.to_numeric(bl['SALE PRICE'])
bl['GROSS SQUARE FEET'] = pd.to_numeric(bl['GROSS SQUARE FEET'])
bl = bl[bl['SALE PRICE']!= 0]
bl = bl[bl['GROSS SQUARE FEET']!= 0]
bl['2010Price/sqft'] = bl['SALE PRICE']/bl['GROSS SQUARE FEET']
bl = bl.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2010Price/sqft'].mean().reset_index()
bl = bl.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedat2010a = pricedata2010.append(bl)

q = pd.read_csv("2010_queens.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
q = q.dropna() # drop any row if one of the column is empty
q['SALE PRICE'] = pd.to_numeric(q['SALE PRICE'])
q['GROSS SQUARE FEET'] = pd.to_numeric(q['GROSS SQUARE FEET'])
q = q[q['SALE PRICE']!= 0]
q = q[q['GROSS SQUARE FEET']!= 0]
q['2010Price/sqft'] = q['SALE PRICE']/q['GROSS SQUARE FEET']
q = q.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2010Price/sqft'].mean().reset_index()
q = q.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2010 = pricedata2010.append(q)

s = pd.read_csv("2010_statenisland.csv", usecols = ['BOROUGH', 'ZIP CODE','GROSS SQUARE FEET','BUILDING CLASS AT TIME OF SALE','SALE PRICE'])
s = s.dropna() # drop any row if one of the column is empty
s['SALE PRICE'] = pd.to_numeric(s['SALE PRICE'])
s['GROSS SQUARE FEET'] = pd.to_numeric(s['GROSS SQUARE FEET'])
s = s[s['SALE PRICE']!= 0]
s = s[s['GROSS SQUARE FEET']!= 0]
s['2010Price/sqft'] = s['SALE PRICE']/s['GROSS SQUARE FEET']
s = s.groupby(['BOROUGH','ZIP CODE','BUILDING CLASS AT TIME OF SALE'])['2010Price/sqft'].mean().reset_index()
s = s.rename(columns = {'ZIP CODE':'zipcode','BOROUGH':'boro'})
pricedata2010 = pricedata2010.append(s)


a=pricedata2015.merge(pricedata2014,on='zipcode')
b=a.merge(pricedata2013,on='zipcode')
c=b.merge(pricedata2012,on='zipcode')
d=c.merge(pricedata2011,on='zipcode')
masterprice=d.merge(pricedata2010,on='zipcode')

masterprice.to_csv('price2010-2015.csv')
