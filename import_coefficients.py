# Import csv files

# import numpy as np
#
file_path = '/Users/dhueholt/Documents/ATS621/OH_Rate_Coefficients_1.csv'

## Numpy isn't great for reading this sort of format as it doesn't thrive with headers
# data_table = np.genfromtxt(file_path, delimiter=',')
# data_headers = np.genfromtxt(file_path, delimiter=',',dtype=None)
# data_headers = data_headers[0,:]
#
# print(data_table)
# print(data_headers)

## Pandas approach
import pandas as pd
data_table = pd.read_csv(file_path, sep=',',header=0)

print(data_table.values)
# from dir(data_table) it looks like there are column/row based sums, will try that approach first
