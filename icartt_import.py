import PseudoNetCDF as pnc
inpath = '/Users/dhueholt/Documents/ATS621/MER-TOGA_DC8_20171006_R19.ict'
#outpath = '<path-for-output>'
infile = pnc.pncopen(inpath, format = 'ffi1001')
dir(infile)
# Print CDL representation - good for learning dimensions, variables, and properties
# print(infile)
# Optionally, add dimension slicing
# infile = infile.sliceDimensions(<layer-dim-name> = 0)
# infile = infile.applyAlongDimenions(<time-dim-name> = 'mean')
# patches = infile.plot('<varkey>', plottype = 'longitude-latitude')
# patches.axes.figure.savefig('<path-for-figure>')
# infile.save(outpath)
