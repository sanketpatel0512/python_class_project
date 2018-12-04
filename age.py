
import pandas as pd
def BoroAge():
    popdata = pd.read_csv("age.csv", usecols = ['Borough','Age','2010','2015'])
    popdata = popdata.rename(columns = {'Borough':'boro'})
    popdata['boro'] = popdata['boro'].str.upper()
    popdata = popdata[~popdata['boro'].isin(['NYC TOTAL'])]
    popdata = popdata[~popdata['Age'].isin(['9-May','14-Oct'])]

    return popdata

