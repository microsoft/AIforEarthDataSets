# NOAA Global Forecast System (GFS)

## Overview

The NOAA [Global Forecast System](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs) (GFS) is a weather forecast model produced by the National Centers for Environmental Prediction (NCEP). Dozens of atmospheric and land-soil variables are available through this dataset, from temperatures, winds, and precipitation to soil moisture and atmospheric ozone concentration. The entire globe is covered by the GFS at a base horizontal resolution of 18 miles (28 kilometers) between grid points, which is used by the operational forecasters who predict weather out to 16 days in the future. Horizontal resolution drops to 44 miles (70 kilometers) between grid point for forecasts between one week and two weeks.

Data are retained for 30 days.

This dataset is available on Azure thanks to the [NOAA Big Data Program](https://www.noaa.gov/organization/information-technology/big-data-program).


## Storage resources

Data are stored primarily in [GRIB](https://en.wikipedia.org/wiki/GRIB) format.

GRIB files are stored as blobs in the East US Azure region, in the following blob container:

`https://noaarap.blob.core.windows.net/gfs`

Within that container, top-level folders are named as:

`[product].[date]`

* `product` is one of:
  * `gfs`: forecast data from the [Global Forecast System](https://www.nco.ncep.noaa.gov/pmb/products/gfs/#GFS) (GFS)
  * `gdas`: forecast data gridded with the [Global Data Assimilation System](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-data-assimilation-system-gdas) (GDAS)
  * `gfsmos`: model output statistics from the [GFS MOS](https://www.weather.gov/mdl/mos_gfsmos_home) suite
  * `sst`: sea surface temperature forecasts produced by the [NCEP Sea Surface Temperature](https://www.nco.ncep.noaa.gov/pmb/products/sst/) (SST) models
  * `enkfgdas`: data assimilated using the [GSI Hybrid/4DenVar Data Assimilation](https://dtcenter.ucar.edu/com-GSI/users/docs/presentations/2017_tutorial/D3-L12_GSI_Hybrid4DEnVarDA_Kleist.pdf) system
  
* `date` is the model execution date in YYYYMMDD format

File format within a folder varies by product; documentation for the primary products (GFS and GFS-GDAS) can be found at:

* [GFS](https://www.nco.ncep.noaa.gov/pmb/products/gfs/#GFS)
* [GFS-GDAS](https://www.nco.ncep.noaa.gov/pmb/products/gfs/#GDAS)


## Region information

Large-scale processing is best performed in the East US Azure region, where the data are stored.  If you are using RAP data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Mounting the container

We also provide a read-only SAS (shared access signature) token to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://noaagfs.blob.core.windows.net/gfs?sv=2020-04-08&si=gfs-ro&sr=c&sig=SWziOkDMW1m51hyMoZSamZrd3NePmsQ51ljmioi7nCA%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).


## Contact

For any data delivery issues or any questions in general, please contact the NOAA Big Data Program Team at [`noaa.bdp@noaa.gov`](mailto:noaa.bdp@noaa.gov?subject=azure%20rap%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
