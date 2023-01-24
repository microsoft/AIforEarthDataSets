# NOAA GOES Rainfall Rate and Quantitative Precipitation Estimation (RRQPE)

## Overview

The GOES Advanced Baseline Imager (ABI) produces a Rainfall Rate and Quantitative Precipitation Estimation (RRQPE) that are maps of expected rainfall rate and precipitation.

The [GOES-R](https://www.goes-r.gov/) (Geostationary Operational Environmental Satellite) program images weather phenomena from a set of satellites in geostationary orbits.  The GOES-16, GOES-17 and GOES-18 satellites are the first three of four planned GOES-R satellites.

This dataset is available on Azure thanks to the [NOAA Open Data Dissemination](https://www.noaa.gov/information-technology/open-data-dissemination) Program.

The ABI Rainfall Rate / QPE product assigns each earth-navigated pixel  a rainfall rate  ranging from 0 to
100 mm/h.
Only infrared channels are used to determine the rainfall rate.
The rainfall rate product is generated for every ABI Full Disk (FD) of the Earth every 15 minutes whether the satellite is in Scan Mode 3 or 4.

Source: https://www.ncdc.noaa.gov/sites/default/files/attachments/ABI_L2_RRQPE_Provisional_ReadMe.pdf

See these introductory slides for more overview information:
- [English](https://www.goes-r.gov/downloads/resources/documents/Beginners_Guide_to_GOES-R_Series_Data.pdf)
- [Spanish](https://github.com/NOAA-Big-Data-Program/bdp-data-docs/blob/main/GOES/QuickGuides/Spanish/Guia%20introductoria%20para%20datos%20de%20la%20serie%20GOES-R%20V1.1%20FINAL2%20-%20Copy.pdf)


## Storage resources

Data are available in Blob Storage in the West Europe Azure data center<sup>1</sup>, in both [NetCDF](https://www.unidata.ucar.edu/software/netcdf/) and [cloud-optimized GeoTIFF](https://www.cogeo.org/) (COG) format.

NetCDF files (one file per scene) are available in the following containers, for GOES-16 and GOES-17 respectively:

`https://goeseuwest.blob.core.windows.net/noaa-goes16`<br/>
`https://goeseuwest.blob.core.windows.net/noaa-goes17`<br/>
`https://goeseuwest.blob.core.windows.net/noaa-goes18`

COG files (one file per band) are available in the following folders, for GOES-16 and GOES-17 respectively:

`https://goeseuwest.blob.core.windows.net/noaa-goes-cogs/goes-16/`<br/>
`https://goeseuwest.blob.core.windows.net/noaa-goes-cogs/goes-17/`<br/>
`https://goeseuwest.blob.core.windows.net/noaa-goes-cogs/goes-18/`

Within any of the above, data are named as:

`[product]/[year]/[day]/[hour]/[filename]`

* <i>product</i> is `ABI-L2-RRQPEF`
* <i>year</i> is a four-digit year
* <i>day</i> is a three-digit day-of-year code, starting with 001
* <i>hour</i> is a two-digit hour-of-day code, starting with 00
* <i>filename</i> encodes the product, date, and time

Details are available in the [GOES Users' Guide](https://www.goes-r.gov/products/docs/PUG-L2%2B-vol5.pdf)

Large-scale processing using this dataset is best performed in the West Europe Azure data center, where the data is stored.

## Authentication

Access requires a [Shared Access Signature](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview) token, available via our [Planetary Computer token API](https://planetarycomputer.microsoft.com/docs/concepts/sas/).


## Citation

If you use this data in a publication, please cite as:

GOES-R Series Program, (2019): NOAA GOES-R Series Advanced Baseline Imager (ABI) Level 0 Data. [indicate subset used]. NOAA National Centers for Environmental Information. doi:10.25921/tvws-w071.


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
