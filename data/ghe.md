# NOAA Global Hydro Estimator

## Overview

Global rainfall estimates in 15-minute intervals.

The NOAA [Global Hydro Estimator](https://www.ospo.noaa.gov/Products/atmosphere/ghe/index.html) (GHE) program produces estimates of global (between -60° and +60° latitude) precipitation every 15 minutes, at ~4km resolution.  Estimates are derived from satellite imagery and data from NOAA's [Global Forecast System](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs); details about the GHE algorithm are available [here](https://www.ospo.noaa.gov/Products/atmosphere/ghe/algo.html).

This dataset is available on Azure thanks to the [NOAA Big Data Program](https://www.noaa.gov/organization/information-technology/big-data-program).


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

We also provide a read-only SAS (shared access signature) token to allow access to GHE data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2020-04-08&si=noaa-ghe-ro&sr=c&sig=q9K1gGIRSmhbDcm27PEXo%2F%2BYGK8%2BkYhuiCJvZbOPdOs%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing using this dataset is best performed in the East US Azure data center, where the data is stored.  If you are using GHE data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Sample code

A complete Python example of accessing and plotting a GHE image (https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/i.e., an instantaneous global estimate) is available in the accompanying [sample notebook](ghe.ipynb).


## Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/ghe.png" style="width:350px;"><br/>

<p style="font-size:80%;margin-left:15px;">Global daily precipitation on April 9, 2020.</p>


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=ghe%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.

