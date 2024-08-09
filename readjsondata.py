# importing pandas
import pandas as pd

# sample json data
datafile = 'data.json'

# reading sample data with pandas and converting to dataframe
df = pd.read_json(datafile)


# create a function to check status
def status(row):
    if row <= 0:
        results = 'minus Stromverbrauch'
    else:
        results = 'Stromverbrauch'
    return results


# calling the status function on column consumption_kwh and generating a new column Status
df['Status'] = df['consumption_kwh'].apply(status)

# exporting the final table to csv
df.to_csv('Sensor_data.csv', encoding='UTF-8', header=True, index=False, sep=',', decimal='.')
