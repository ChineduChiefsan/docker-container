import csv
import pandas as pd

fileadd= 'Data_files\\city_housing.csv'
# with open(fileadd, 'r', encoding='UTF-8') as cs:
#     pass
#     print(cs.readlines())

def create_state(city):
    cities_= ''
    for values in city:
            cities_ = values[0:2]
    return cities_


df = pd.read_csv(fileadd)
for values in df['city']:
    df['state'] = values[0:2]
    #print(df)


print(df['city'])

