## Calculates reactivities for given coefficient and concentrations files
# the react_frame variable is a pandas dataframe containing UTC start/stop, temperature,
# reactivities for all individual species, VOC reactivity, non-VOC reactivity, and
# total reactivity
#
# To use, point inpath_coeff at a csv coefficient file and inpath_conc at the
# corresponding ICARTT (.ict) file, and change the outfile to what filename you
# want to save to. The output is saved as a csv file.

# OH_ATHOS is the one we need

import PseudoNetCDF as pnc
import pandas as pd
import numpy as np
# import time # for debugging

## Concentrations and coefficient file inputs and desired output filename
inpath_coeff = '/Users/dhueholt/Documents/ATS621/OH_Coefficients_Flight2_corrected.csv'
inpath_conc = '/Users/dhueholt/Documents/ATS621/archive_download_0/MER-TOGA_DC8_20170129_R18.ict'
outfile = '/Users/dhueholt/Documents/ATS621/OH_Reactivities_Flight_test.csv'

## Import data
infile_coeff = pd.read_csv(inpath_coeff, sep=',',header=0) #import coefficients as dataframe
infile_conc = pnc.pncopen(inpath_conc, format = 'ffi1001') #import concentrations as pncopen

# print(infile_coeff.values)
# print(infile_conc)
# Manually verify times are the same
# print(infile_coeff.UTC_Start)
# print(infile_conc.variables['UTC_Start'])

## Calculate stuff
oh_mixrat = infile_conc.variables['OH_ATHOS'].data
pressures = infile_conc.variables['StaticPressure_GMI'].data * 100 #pressure in Pa
Av = 6.0221409 * 10**23
R = 8.314
number_dens = np.divide((Av * pressures),(R * infile_conc.variables['T']))
number_dens_cm3 = np.divide(number_dens, 10**(6))
oh_numbden = oh_mixrat * 10**(-12) * number_dens_cm3 # [OH] in stuff per cm3
oh_numbden[oh_numbden < 0] = np.nan #actually, concentrations should never be negative
print(oh_numbden)

rownum = infile_coeff.UTC_Start.size
colnum = infile_coeff.columns.size
coeff_values = infile_coeff.iloc[:,3:colnum].values
calc_reactivities = np.transpose(np.transpose(coeff_values) * oh_numbden)
print(calc_reactivities)

react_frame = infile_coeff.copy(deep=True) #this way we keep header and metadata
for kc in range(3,colnum):
    #is there a better way to do this? probably! does this work? yep!
    react_frame.iloc[:,kc] = calc_reactivities[:,kc-3]
# this produces a dataframe with the same header as before, including the time and temperature information
# Advantage of this approach is it's easily interpretable and we can use rowsum, etc
# access individual species with reactivities_frame
# print(infile_coeff)
# print(react_frame)

other_keys = ["UTC_Start", "UTC_Stop_TOGA", "T"]
non_voc_keys = ["H2_UCATS", "CO_UCATS", "H2O2_CIT", "O3_UCATS", "SO2_CIT", "NO_GMI", "NO2_GMI"]
voc_keys = []

for key in infile_coeff.columns:
    if key in other_keys or key in non_voc_keys:
        continue
    else:
        voc_keys.append(key)
# print(voc_keys)

react_frame['voc_react'] = react_frame.loc[:,voc_keys].sum(axis=1)
react_frame['non_voc_react'] = react_frame.loc[:,non_voc_keys].sum(axis=1)
react_frame['total_react'] = react_frame.loc[:,voc_keys+non_voc_keys].sum(axis=1)
#Can calculate for arbitrary list of species! Make list of keys, then use same syntax

print(react_frame) #print the reactivities dataframe to the terminal
react_frame.to_csv(outfile) #save reactivities as csv
