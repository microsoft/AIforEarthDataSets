Data are available in Blob Storage in the West Europe Azure data center<sup>1</sup>, in both [NetCDF](https://www.unidata.ucar.edu/software/netcdf/) and [cloud-optimized GeoTIFF](https://www.cogeo.org/) (COG) format.

NetCDF files (one file per scene) are available in the following containers, for GOES-16 and GOES-17 respectively:

`https://goeseuwest.blob.core.windows.net/noaa-goes16`
`https://goeseuwest.blob.core.windows.net/noaa-goes17`

COG files (one file per band) are available in the following folders, for GOES-16 and GOES-17 respectively:

`https://goeseuwest.blob.core.windows.net/noaa-goes-cogs/goes-16/`
`https://goeseuwest.blob.core.windows.net/noaa-goes-cogs/goes-17/`

Within any of the above, data are named as:

`[product]/[year]/[day]/[hour]/[filename]`

* <i>product</i> is a product name, see the [storage resources page](https://github.com/microsoft/AIforEarthDataSets/blob/main/data/goes-r.md#storage-resources) for a list of available products
* <i>year</i> is a four-digit year
* <i>day</i> is a three-digit day-of-year code, starting with 001
* <i>hour</i> is a two-digit hour-of-day code, starting with 00
* <i>filename</i> encodes the product, date, and time; details are available in the [GOES Users' Guide](https://www.goes-r.gov/products/docs/PUG-L2%2B-vol5.pdf)

For example, this file:

https://goeseuwest.blob.core.windows.net/noaa-goes16/ABI-L2-MCMIPF/2020/003/00/OR_ABI-L2-MCMIPF-M6_G16_s20200030000215_e20200030009534_c20200030010031.nc

...contains data from January 3, 2020, between midnight and 1am UTC (hour 00).

This is the prefix for the same scene in COG format:

https://goeseuwest.blob.core.windows.net/noaa-goes16/ABI-L2-MCMIPF/2020/003/00/OR_ABI-L2-MCMIPF-M6_G16_s20200030000215_e20200030009534_c20200030010031

...and this is the COG file representing the first band from that scene:

https://goeseuwest.blob.core.windows.net/noaa-goes16/ABI-L2-MCMIPF/2020/003/00/OR_ABI-L2-MCMIPF-M6_G16_s20200030000215_e20200030009534_c20200030010031_CMI_C01.tif

Data channels and wavelengths are described [here](https://www.ncdc.noaa.gov/data-access/satellite-data/goes-r-series-satellites/glossary).

Large-scale processing using this dataset is best performed in the West Europe Azure data center, where the data is stored.  If you are using GOES data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.

### East US subset

<sup>1</sup>The following products are also available in the East US Azure data center, in NetCDF format:

* GOES-16 ABI-L1b-RadF
* GOES-16 ABI-L2-MCMIPF
* GOES-16 and GOES-17 GLM-L2-LCFA

Storage containers for this subset are as follows:

`https://goes.blob.core.windows.net/noaa-goes16`
`https://goes.blob.core.windows.net/noaa-goes17`