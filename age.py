
import pandas as pd
def BoroAge(a):
    popdata = pd.read_csv("age.csv")
    popdata = popdata.rename(columns = {'Borough':'boro'})
    popdata['boro'] = popdata['boro'].str.upper()
    popdata = popdata[popdata['boro']== a ]
    popdata = popdata[~popdata['Age'].isin(['9-May','14-Oct'])]
    #borolist = list(popdata['boro'].unique())
    #totallist = popdata[popdata['Age'] == 'Total']
    
    #agedata = pd.DataFrame()
    #for b in borolist:
    #    pop= popdata[popdata['boro'] == b]
    #    pop['Current %'] = 100*(pop['2015']/(float(totallist['2015'].where(totallist['boro'] == b).dropna().values)))
    #    pop['Future %'] = 100*(pop['2020']/(float(totallist['2020'].where(totallist['boro'] == b).dropna().values)))
    #    agedata = agedata.append(pop,ignore_index = True)
    
    
    return popdata

