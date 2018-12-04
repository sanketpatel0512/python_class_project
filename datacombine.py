
import crime as c
import school as s
import age as a
import noise as n
import clean as cl

#Function to import Data for various attributes
def Data(y):
    school = s.ZipSchool()

    noise = n.ZipNoise(y)

    masterdata = noise.merge(school, on = 'zipcode')
    masterdata = masterdata.drop(['zipcode','year'], axis = 1)
    masterdata = masterdata.groupby('boro').agg({'graduation_rate': 'mean','attendance_rate': 'mean',\
                             'variety_rate': 'mean','college_career_rate': 'mean','safety_rate':'mean','Noise Rate': 'sum'}).reset_index()

    age = a.BoroAge()
    totpop = age[age['Age'] == 'Total']
    

    crime = c.BoroCrime(y)
    crime = crime.drop(['year','Lawtype'], axis = 1)
    masterdata = masterdata.merge(totpop, on = 'boro')
    masterdata = masterdata.merge(crime, on = 'boro')


    clean = cl.BoroClean(y)

    masterdata = masterdata.merge(clean, on = 'boro')

    if y <= 2012:
        masterdata['Crime Rate'] = masterdata['Crime Rate']/masterdata['2010']*100000
        masterdata['Noise Rate'] = masterdata['Noise Rate']/masterdata['2010']*100000
    else:
        masterdata['Crime Rate'] = masterdata['Crime Rate']/masterdata['2015']*100000
        masterdata['Noise Rate'] = masterdata['Noise Rate']/masterdata['2015']*100000

    

    return masterdata

