# NOAA Climate Data Records (CDRs)

## Overview

NOAA's [Climate Data Records](https://www.ncei.noaa.gov/products/climate-data-records) (CDRs) are robust, sustainable, and scientifically sound climate records that provide trustworthy information on how, where, and to what extent the land, oceans, atmosphere, and ice sheets are changing. NOAA CDRs are vetted using standards established by the National Research Council (NRC).  Climate Data Records are created by merging data from surface, atmosphere, and space-based systems across decades.  This process allows analysis of the underlying climate trends within the data and permits users to identify economic and scientific value in these records.  The [National Centers for Environmental Information](https://ncei.noaa.gov) (NCEI) maintains and extends CDRs by applying the same methods to present-day satellite measurements.

CDRs vary in the time period they represent, but each CDR has an earliest date between 1979 and 2000.

CDRs are broken into four categories:

* [<b>Atmospheric</b>](https://www.ncei.noaa.gov/products/climate-data-records/atmospheric) CDRs are measurements of several global variables to help characterize the atmosphere at or just above the land and ocean surface, as well as other upper-air composition variables.
* [<b>Fundamental</b>](https://www.ncei.noaa.gov/products/climate-data-records/fundamental) CDRs are composed of sensor data (e.g. calibrated radiances and temperatures) that have been improved and quality-controlled over time, together with ancillary calibration data.
* [<b>Oceanic</b>](https://www.ncei.noaa.gov/products/climate-data-records/oceanic) CDRs are measurements of oceans and seas, including surface, subsurface, and frozen-state variables.
* [<b>Terrestrial</b>](https://www.ncei.noaa.gov/products/climate-data-records/terrestrial) CDRs are composed of terrestrial sensor data that have been improved and quality-controlled over time, together with ancillary calibration data.

This dataset is available on Azure thanks to the [NOAA Big Data Program](https://www.noaa.gov/organization/information-technology/big-data-program).


## Storage resources

Data are stored in [NetCDF](https://www.unidata.ucar.edu/software/netcdf/) format; each CDR is in an individual blob container in the following storage account:

`https://noaacdr.blob.core.windows.net`

NetCDF structure and file naming conventions vary slightly across data sets; see below for documentation of individual CDRs, along with links to their original documentation.  However, most CDRs use one of the following naming conventions:

`noaacdr.blob.core.windows.net/[product]/data/[year]/[filename].nc
`noaacdr.blob.core.windows.net/[product]/data/[year]/[month]/[filename].nc

`product` is a short name for one of the CDRs, and also specifies the blob container name.  A list of products and their associated container names is below.

For example, the following NetCDF file contains information from the "Leaf Area Index" (leaf-area-index-fapar) product for January 1st, 2003:

[https://noaacdr.blob.core.windows.net/leaf-area-index-fapar/data/2003/AVHRR-Land_v005_AVH15C1_NOAA-16_<span style="background-color:yellow;">20030101</span>_c20180830231613.nc](https://noaacdr.blob.core.windows.net/leaf-area-index-fapar/data/2003/AVHRR-Land_v005_AVH15C1_NOAA-16_20030101_c20180830231613.nc)

The highlighted text indicates the date, and occurs in most NetCDF file names.


### Available products

Parentheses indicate product short names, which correspond to container names as per above.

* <a href="https://www.ncei.noaa.gov/products/climate-data-records/avhrr-aerosol-optical-thickness">AVHRR Aerosol Optical Thickness</a> (aerosol-optical-thickness)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/cloud-properties-isccp">Cloud Properties - ISCCP</a> (cloud-properties-isccp)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/extended-avhrr-polar-pathfinder">Extended AVHRR Polar Pathfinder</a> (polar-pathfinder-extended)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/hydrological-properties">Hydrological Properties</a> (hydrological-properties)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/ocean-heat-fluxes">Ocean Heat Fluxes</a> (ocean-heatflux)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/ocean-near-surface-atmosphere">Ocean Near-Surface Atmospheric Properties</a> (ocean-nearsurface-atmos-profiles)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/outgoing-longwave-radiation-daily">Outgoing Longwave Radiation - Daily</a> (outgoing-longwave-radiation-daily)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/outgoing-longwave-radiation-monthly">Outgoing Longwave Radiation - Monthly</a> (outgoing-longwave-radiation-monthly)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/ozone-esrl">Ozone - ESRL</a> (ozone-esrl)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/precipitation-cmorph">Precipitation - CMORPH</a> (precip-cmorph)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/precipitation-gpcp-daily">Precipitation - GPCP Daily</a> (precip-gpcp-daily)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/precipitation-gpcp-monthly">Precipitation - GPCP Monthly</a> (precip-gpcp-monthly)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/precipitation-nexrad-qpe">Precipitation - NEXRAD QPE</a> (precip-nexrad-qpe)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/precipitation-persiann">Precipitation - PERSIANN</a> (precip-persiann)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/solar-spectral-irradiance">Solar Spectral Irradiance</a> (solar-spectral-irradiance)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/total-solar-irradiance">Total Solar Irradiance</a> (total-solar-irradiance)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/geostationary-IR-channel-brightness-temperature">Geostationary IR Channel Brightness Temperature - GridSat-B1</a> (gridsat-b1)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/mean-layer-temperature-noaa">Mean Layer Temperature - NOAA</a> (mean-layer-temp)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/mean-layer-temperature-rss">Mean Layer Temperature - RSS</a> (mean-layer-temp-rss)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/mean-layer-temperature-uah">Mean Layer Temperature - UAH</a> (mean-layer-temp-uah)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/mean-layer-temperature-ucar-lower-strat">Mean Layer Temperature - UCAR (Lower Stratosphere)</a> (mean-layer-temp-lower-strat)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/mean-layer-temperature-ucar">Mean Layer Temperature - UCAR (Upper Troposphere and Lower Stratosphere)</a> (mean-layer-temp-upper-trop-lower-strat)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/ssmis-brightness-temperature-csu">SSM/I(S) Brightness Temperature - CSU</a> (microwave-imager-brit-temp-csu)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/ssmis-brightness-temperature-rss">SSMI/S Brightness Temperature - RSS</a> (microwave-imager-brit-temp-rss)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/global-ocean-heat-content">Global Ocean Heat Content</a> (ocean-heat-content)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/pathfinder-sea-surface-temperature">Pathfinder Sea Surface Temperature</a> (sea-surface-temp-pathfinder)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/sea-ice-concentration">Sea Ice Concentration</a> (sea-ice-concentration)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/sea-surface-temperature-optimum-interpolation">Sea Surface Temperature - Optimum Interpolation</a> (sea-surface-temp-optimum-interpolation)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/sea-surface-temperature-whoi">Sea Surface Temperature - WHOI</a> (sea-surface-temp-whoi)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/leaf-area-index-and-fapar">Leaf Area Index and FAPAR</a> (leaf-area-index-fapar)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/normalized-difference-vegetation-index">Normalized Difference Vegetation Index</a> (ndvi)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/snow-cover-extent">Snow Cover Extent (Northern Hemisphere)</a> (snow-cover-ext-north)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/msu-brightness-temperature-noaa">MSU Brightness Temperature - NOAA</a> (msu-brit-temp)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/avhrr-polar-pathfinder">AVHRR Polar Pathfinder</a> (polar-pathfinder-fcdr)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/hirs-ch12-brightness-temperature">HIRS CH12 Brightness Temperature</a> (ir-water-vapor-brit-temp)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/amsu-brightness-temperature-noaa">AMSU Brightness Temperature - NOAA</a> (microwave-brit-temp)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/amsu-b-and-mhs-brightness-temperature">AMSU-B and MHS Brightness Temperature</a> (microwave-humidity-sounder-brit-temp)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/amsu-a-brightness-temperature">AMSU-A Brightness Temperature</a> (microwave-temp-sounder-brit-temp)
* <a href="https://www.ncei.noaa.gov/products/climate-data-records/avhrr-reflectance-patmos">AVHRR Reflectance - PATMOS-x</a> (patmosx-radiances-and-clouds)


## Region information

Large-scale processing is best performed in the East US Azure region, where the data are 


## Contact

For questions, please contact the NOAA Big Data Program Team at [`noaa.bdp@noaa.gov`](mailto:noaa.bdp@noaa.gov?subject=azure%20cdr%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
