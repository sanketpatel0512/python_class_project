import datacombine as m
import price as p

#Function to import price data
def Price(y):
        price = p.ZipPrice(y)
        price = price.drop(['zipcode','year'], axis = 1)
        price = price.groupby(['boro','type']).mean().reset_index()
        return price

#Create Training data files for 2013,2014
y = [2013,2014]

for i in y:
    traindata = m.Data(i)
    trainprice = Price(i)
    traindata = traindata.merge(trainprice, on = 'boro')
    traindata.to_csv('traindata_'+str(i)+'.csv')

#Create Test data file for 2015
testdata = m.Data(2015)
testdata.to_csv('testdata.csv')

#Create Actual Price file for comparison
actdata = Price(2015)
actdata.to_csv('Actual_data.csv')
