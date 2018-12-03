import pandas as pd

#School Data Input
def ZipSchool(z):
    schldata = pd.read_csv("school.csv", usecols = ['dbn','school_name','graduation_rate',\
                                                    'attendance_rate','pct_stu_enough_variety',\
                                                    'college_career_rate','pct_stu_safe','Postcode'])
    schldata = schldata.rename(columns = {'Postcode':'zipcode','pct_stu_enough_variety':'variety_rate','pct_stu_safe':'safety_rate'})
    schldata = schldata.fillna(schldata.mean())
    schldata = schldata.groupby(['zipcode']).mean().reset_index()
    schldata = schldata[schldata['zipcode'] == z]
    return schldata
