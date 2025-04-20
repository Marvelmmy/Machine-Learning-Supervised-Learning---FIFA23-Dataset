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

