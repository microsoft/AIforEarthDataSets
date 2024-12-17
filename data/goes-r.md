# NOAA GOES-R

Some of these datasets are also queryable through the [Planetary Computer's STAC API](https://planetarycomputer.microsoft.com/catalog?filter=goes). We recommend getting the URLs in Blob Storage through the STAC API wherever possible.

## Overview

Weather imagery from the GOES-16, GOES-17, and GOES-18 satellites.

The [GOES-R](https://www.goes-r.gov/) (Geostationary Operational Environmental Satellite) program images weather phenomena from a set of satellites in geostationary orbits.  The GOES-16 and GOES-17 satellites are the first two of four planned GOES-R satellites.

This dataset currently includes eleven level-2 products from the Advanced Baseline Imager (ABI) instrument, and one level-2 product from the Geostationary Lightning Mapper (GLM) instrument.  We may on-board other GOES-16 and GOES-17 products on request; please contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=goes%20question) if you are interested in using additional GOES data on Azure.

This dataset is available on Azure thanks to the [NOAA Open Data Dissemination (NODD) Program](https://www.noaa.gov/information-technology/open-data-dissemination).

GOES-R data is also available as a collection in the [Planetary Computer Data Catalog](https://planetarycomputer.microsoft.com/dataset/goes-cmi).

See these introductory slides for more overview information:
- [English](https://www.goes-r.gov/downloads/resources/documents/Beginners_Guide_to_GOES-R_Series_Data.pdf)
- [Spanish](https://github.com/NOAA-Big-Data-Program/bdp-data-docs/blob/main/GOES/QuickGuides/Spanish/Guia%20introductoria%20para%20datos%20de%20la%20serie%20GOES-R%20V1.1%20FINAL2%20-%20Copy.pdf)


## Products available

The following GOES-R products are available on Azure, for both GOES-16 and GOES-17:

* ABI-L2-CMIPC (Advanced Baseline Imager Level 2 Cloud and Moisture Imagery CONUS)
* ABI-L2-CMIPF (Advanced Baseline Imager Level 2 Cloud and Moisture Imagery Full Disk)
* ABI-L2-CMIPM (Advanced Baseline Imager Level 2 Cloud and Moisture Imagery Mesoscale)
* ABI-L2-FDCC (Advanced Baseline Imager Level 2 Fire (Hot Spot Characterization) CONUS)
* ABI-L2-FDCF (Advanced Baseline Imager Level 2 Fire (Hot Spot Characterization) Full Disk)
* ABI-L2-LSTC (Advanced Baseline Imager Level 2 Land Surface Temperature CONUS)
* ABI-L2-LSTF (Advanced Baseline Imager Level 2 Land Surface Temperature Full Disk)
* ABI-L2-LSTM (Advanced Baseline Imager Level 2 Land Surface Temperature Mesoscale)
* ABI-L2-MCMIPC (Advanced Baseline Imager Level 2 Cloud and Moisture Imagery CONUS)
* ABI-L2-MCMIPF (Advanced Baseline Imager Level 2 Cloud and Moisture Imagery Full Disk)
* ABI-L2-MCMIPM (Advanced Baseline Imager Level 2 Cloud and Moisture Imagery Mesoscale)
* ABI-L2-RRQPEF (Advanced Baseline Imager Level 2 Rainfall Rate (Quantitative Precipitation Estimate) Full Disk)
* ABI-L2-SSTF (Advanced Baseline Imager Level 2 Sea Surface (Skin) Temperature Full Disk)
* GLM-L2-LCFA (Geostationary Lightning Mapper Level 2 Lightning Detection)


## Storage resources

Data are available in Blob Storage in the West Europe Azure data center<sup>1</sup>, in both [NetCDF](https://www.unidata.ucar.edu/software/netcdf/) and [cloud-optimized GeoTIFF](https://www.cogeo.org/) (COG) format.

NetCDF files (one file per scene) are available in the following containers, for GOES-16, GOES-17, and GOES-18 respectively:

`https://goeseuwest.blob.core.windows.net/noaa-goes16`<br/>
`https://goeseuwest.blob.core.windows.net/noaa-goes17`<br/>
`https://goeseuwest.blob.core.windows.net/noaa-goes18`

COG files (one file per band) are available in the following folders, for GOES-16, GOES-17, and GOES-18 respectively:

`https://goeseuwest.blob.core.windows.net/noaa-goes-cogs/goes-16/`<br/>
`https://goeseuwest.blob.core.windows.net/noaa-goes-cogs/goes-17/`<br/>
`https://goeseuwest.blob.core.windows.net/noaa-goes-cogs/goes-18/`

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

Large-scale processing using this dataset is best performed in the West Europe Azure data center, where the data is stored.

### East US subset

<sup>1</sup>The following products are also available in the East US Azure data center, in NetCDF format:

* GOES-16 ABI-L1b-RadF
* GOES-16 ABI-L2-MCMIPF
* GOES-16 and GOES-17 GLM-L2-LCFA

Storage containers for this subset are as follows:

`https://goes.blob.core.windows.net/noaa-goes16`<br/>
`https://goes.blob.core.windows.net/noaa-goes17`


## Authentication

NetCDF files do not require authentication; COG files require a [Shared Access Signature](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview) token, available via our [Planetary Computer token API](https://planetarycomputer.microsoft.com/docs/concepts/sas/).


## Sample code

A complete Python example of accessing and plotting a GOES-16 image is available in the accompanying [sample notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/goes-r-abi-l2-mcmipf.ipynb).


## Citation

If you use this data in a publication, please cite as:

GOES-R Series Program, (2019): NOAA GOES-R Series Advanced Baseline Imager (ABI) Level 0 Data. [indicate subset used]. NOAA National Centers for Environmental Information. doi:10.25921/tvws-w071.


## Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/goes-16.png" style="width:350px;"><br/>

<p style="font-size:80%;margin-left:15px;">Moisture imagery of the Americas on Jan 2, 2020.</p>


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=goes%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
