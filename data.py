#importing libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt #if you want to visualize the data 

#inserting the data 
df = pd.read_csv('FIFA23_official_data.csv.zip',index_col='ID')
#to check the null datas 
df.isnull().sum()
# Fill the empty cell with data or drop the column
df.drop(columns=[df.drop(columns=['Name', 'Photo', 'Nationality', 
                                  'Flag', 'Club','Club Logo',
                                  'Position','Joined',	'Loaned From',
                                  'Preferred Foot','Work Rate',	'Body Type',
                                  'Real Face','Best Overall Rating','Contract Valid Until' ], inplace=True)])
#changing the datatypes from str to int 
#value
def value_to_float(value):
    value = value.replace('€', '')
    if 'M' in value:
        return float(value.replace('M', '')) * 1000000
    elif 'K' in value:
        return float(value.replace('K', '')) * 1000
    else:
        try:
            return float(value)
        except:
            return 0
df['Value'] = df['Value'].apply(value_to_float)
#wage
def wage_to_float(wage):
  wage = wage.replace('€', '')
  if 'K' in wage:
    return float(wage.replace('K',''))*1000
  else:
    try:
      return float(wage)
    except:
      return 0 
df['Wage'] = df['Wage'].apply(wage_to_float)
#height 
df['height'] = df['height'].str.replace('cm','')
df['height'] = df['height'].astype(float)
#weight
df['weight'] = df['weight'].str.replace('kg', '')
df['weight'] = df['weight'].astype(float)
#release clause
def release_clause_to_float(release_clause):
    if pd.isnull(release_clause):
        return 0
    release_clause = release_clause.replace('€', '')
    if 'M' in release_clause:
        return float(release_clause.replace('M', '')) * 1000000
    elif 'K' in release_clause:
        return float(release_clause.replace('K', '')) * 1000
    else:
        try:
            return float(release_clause)
        except:
            return 0
df['Release Clause'] = df['Release Clause'].apply(release_clause_to_float)
mean_kit = df['Kit Number'].mean()
df['Kit Number'].fillna(mean_kit,inplace=True)
