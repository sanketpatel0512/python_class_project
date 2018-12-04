import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

#Select year and property type
t = 'Mixed Use'
y = 2013

#read and create training dataframe
traindata = pd.read_csv('traindata_'+str(y)+'.csv')
traindata = traindata[traindata['type'] == t]


#read and create testing dataframe
testdata = pd.read_csv('testdata.csv')


#Run and plot correlation chart
df = traindata.drop(['boro','Age','2010','2015','type'],axis = 1)
corcol = df.columns
plt.matshow(df.corr())
plt.xticks(range(len(corcol)), corcol, rotation = 90)
plt.yticks(range(len(corcol)), corcol)
plt.colorbar()
plt.show()


#Run linear regression
Y_train = df['Price/sqft']
X_train = df.drop('Price/sqft',axis = 1)
X_test = testdata.drop(['boro','Age','2010','2015'],axis = 1)

lm = LinearRegression()
lm.fit(X_train,Y_train)
testdata['Predicted Price'] = lm.predict(X_test)

#Compare prediction to actual results
actprice = pd.read_csv('Actual_data.csv')
actprice = actprice[actprice['type'] == t]
actprice = actprice.merge(testdata,on = 'boro')
print(actprice[['boro','Predicted Price','Price/sqft']])
actprice.plot(x = 'boro',y = ['Predicted Price','Price/sqft'])
