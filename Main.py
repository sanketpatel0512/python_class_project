
import price as p
import crime as c
import school as s
import age as a
import noise as n
import clean as cl

boro = 'MANHATTAN'
z = 10002
crime = c.BoroCrime(boro)
#crime.groupby('Lawtype')['CMPLT_COUNT'].plot(x = 'year')

price = p.ZipPrice()
print(price)
school = s.ZipSchool(z)
#print (school)
age = a.BoroAge(boro)
#print(age)
totpop = age['2015'][age['Age'] == 'Total'].values[0]
#print(totpop)
crime['rate'] = (crime['CMPLT_COUNT']/totpop)*100
crime = crime.drop(['CMPLT_COUNT','Lawtype'], axis = 1)
#print (crime)
noise = n.ZipNoise(z)
#print(noise)
clean = cl.BoroClean(boro)
#print (clean)
'''
masterdata = crime.merge(age, on = 'boro')
masterdata = masterdata.merge(clean, on = 'boro')
masterdata = masterdata.merge(noise, on = 'boro')
masterdata = masterdata.merge(price, on = 'zipcode')
masterdata = masterdata.merge(school, on = 'zipcode')
print(masterdata)
'''