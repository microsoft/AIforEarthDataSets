# NOAA Rapid Refresh (RAP)

## Overview

The NOAA [Rapid Refresh](https://www.nco.ncep.noaa.gov/pmb/products/rap/) (RAP) is a NOAA/NCEP operational weather prediction system comprised primarily of a numerical forecast model and analysis/assimilation system to initialize that model. It covers North America and is run with a horizontal resolution of 13 km and 50 vertical layers. The RAP was developed to serve users needing frequently updated short-range weather forecasts, including those in the US aviation community and US severe weather forecasting community. The model is run for every hour of the day; it is integrated to 51 hours for the 03/09/15/21 UTC cycles and to 21 hours for every other cycle. The RAP uses the ARW core of the [WRF model](https://www.mmm.ucar.edu/weather-research-and-forecasting-model) and the [Gridpoint Statistical Interpolation](https://ral.ucar.edu/solutions/products/gridpoint-statistical-interpolation-gsi) (GSI) analysis.  The analysis is aided with the assimilation of cloud and hydrometer data to improve short-range cloud and precipitation forecasts.

Data are retained for 30 days.

This dataset is available on Azure thanks to the [NOAA Open Data Dissemination (NODD) Program](https://www.noaa.gov/information-technology/open-data-dissemination).


## Storage resources

Data are stored in [GRIB](https://en.wikipedia.org/wiki/GRIB) format.

GRIB files are stored as blobs in the East US Azure region, in the following blob container:

`https://noaarap.blob.core.windows.net/rap`

Within that container, files are named as:

`rap.[year][month][day]/[product][year][month][day]/rap.t[CC]z.[variable]f[FH].grib2`

* `year` is a four-digit year
* `month` is a two-digit month (one-indexed)
* `day` is a two-digit day (one-indexed)
* `CC` is the cycle run hour (00 to 23)
* `variable` is the output variable (awp130pgrb awp252prgb, awp236prgb, awp130bgrb, awp252brgb, awip32, awp242, awp200, awp243, wrfmsl, wrfprs, or wrfnat); see the [RAP documentation](https://www.nco.ncep.noaa.gov/pmb/products/rap/) for definitions)
* `FH` represents the forecast hour (00 to 21 for standard cycles, 00 to 51 for extended-forecast cycles (03, 09, 15, 21))

For example, for the file:

<https://noaarap.blob.core.windows.net/rap/rap.20211013/rap.t00z.awip32f01.grib2>

* Year: 2021
* Month: 10
* Day: 13
* CC (cycle run): 00
* Variable: awip32
* FH (forecast hour): 01


## Region information

Large-scale processing is best performed in the East US Azure region, where the data are stored.


## Mounting the container

We also provide an API to get read-only SAS (shared access signature) tokens to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://planetarycomputer.microsoft.com/api/sas/v1/token/noaarap/rap`

API documentation is at `https://planetarycomputer.microsoft.com/api/sas/v1/docs`.
Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).


## Contact

For questions, please contact the NOAA Open Data Dissemination (NODD) Program Team at [`nodd@noaa.gov`](mailto:nodd@noaa.gov?subject=azure%20rap%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
