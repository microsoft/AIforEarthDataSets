# NOAA Global Hydro Estimator

## Overview

Global rainfall estimates in 15-minute intervals.

The NOAA [Global Hydro Estimator](https://www.ospo.noaa.gov/Products/atmosphere/ghe/index.html) (GHE) program produces estimates of global (between -60° and +60° latitude) precipitation every 15 minutes, at ~4km resolution.  Estimates are derived from satellite imagery and data from NOAA's [Global Forecast System](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs); details about the GHE algorithm are available [here](https://www.ospo.noaa.gov/Products/atmosphere/ghe/algo.html).

This dataset is available on Azure thanks to the [NOAA Open Data Dissemination (NODD) Program](https://www.noaa.gov/information-technology/open-data-dissemination).


## Storage resources

Data are stored in blobs in gzip'd [NetCDF](https://www.unidata.ucar.edu/software/netcdf/) format in the East US data center, in the following blob container:

`https://ghe.blob.core.windows.net/noaa-ghe`

Within that container, data are named as:

`[product]/[year]/[month]/[day]/[filename]`

* <i>product</i> is a product name; this should always be "rainfall"
* <i>year</i> is a four-digit year
* <i>month</i> is a two-digit month-of-year code, starting with 01
* <i>day</i> is a two-digit day-of-month code, starting with 01
* <i>filename</i> encodes the product, date, and time, with the last four digits encoding 24-hour time on 15-minute boundaries

For example, this filename:

`https://ghe.blob.core.windows.net/noaa-ghe/rain_rate/2020/04/02/NPR.GEO.GHE.v1.S202004020030.nc.gz`

...contains the 15-minute rainfall estimate for April 2, 2020, at 00:30 UTC.

Latitude and longitude are not perfectly uniformly sampled, so an additional file is available to specify the precise lat/lon grid associated with all GHE files (~160MB):

<https://ghe.blob.core.windows.net/noaa-ghe/NPR.GEO.GHE.v1.Navigation.netcdf.gz>

We also provide an API to get read-only SAS (shared access signature) tokens to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://planetarycomputer.microsoft.com/api/sas/v1/token/ghe/noaa-ghe`

API documentation is at `https://planetarycomputer.microsoft.com/api/sas/v1/docs`.
Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing using this dataset is best performed in the East US Azure data center, where the data is stored.


## Sample code

A complete Python example of accessing and plotting a GHE image (i.e., an instantaneous global estimate) is available in the accompanying [sample notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/ghe.ipynb).


## Pretty picture

<img alt="ghe plot" src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/ghe.png" style="width:350px;"><br/>

<p style="font-size:80%;margin-left:15px;">Global daily precipitation on April 9, 2020.</p>


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=ghe%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
