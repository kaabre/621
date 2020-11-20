# 621
621 (ATS Chem) group project 

## Convert ICARTT to true netCDF using PseudoNetCDF
### Setup
1. Make sure you have the PseudoNetCDF package installed from [https://github.com/barronh/pseudonetcdf](https://github.com/barronh/pseudonetcdf)
2. Make sure the NetCDF4 package is installed. Use `conda install -c anaconda netcdf4` to install if not

### Convert!
1. Open a terminal. Navigate to the folder where the data is store. 
2. Use the following command: `pncgen -f ffi1001 input.ict output.nc` where `input` is the ICARTT filename and `output` is what you want the netCDF file to be called
3. Profit! This netCDF file can now be easily imported using Python or MATLAB or read at the terminal using `ncdump`
