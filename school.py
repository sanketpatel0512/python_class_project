import pandas as pd

#School Data Input
def ZipSchool():
    schldata = pd.read_csv("school.csv", usecols = ['dbn','school_name','graduation_rate',\
                                                    'attendance_rate','pct_stu_enough_variety',\
                                                    'college_career_rate','pct_stu_safe','Postcode'])
    schldata = schldata.rename(columns = {'Postcode':'zipcode','pct_stu_enough_variety':'variety_rate','pct_stu_safe':'safety_rate'})
    schldata = schldata.fillna(schldata.mean())
    schldata[['graduation_rate','attendance_rate',\
              'variety_rate','college_career_rate','safety_rate']] = schldata[['graduation_rate','attendance_rate','variety_rate','college_career_rate','safety_rate']].multiply(100)
    schldata = schldata.groupby(['zipcode']).mean().reset_index()
    
    return schldata
