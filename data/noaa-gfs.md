# NOAA Global Forecast System (GFS)

## Overview

The NOAA [Global Forecast System](https://www.emc.ncep.noaa.gov/emc/pages/numerical_forecast_systems/gfs.php) (GFS) is a global numerical weather prediction system containing a global computer model and variational analysis run by the U.S. National Weather Service (NWS). The model is divided into 127 vertical layers extending from the surface to the mesopause (~80km).   The entire globe is covered by the GFS at a base horizontal resolution of 13 kilometers between grid points. The GFS is run operationally four times a day and produces forecasts for up to 16 days in advance. Hundreds Of atmospheric and land-soil variables are available through this dataset, from temperatures, winds, and precipitation to soil moisture and atmospheric ozone concentration. 

The current operational GFS is an atmospheric model coupled to a near sea surface temperature model (NSST) over the ocean and lakes, a thermodynamic ice model,  and a land/soil model elsewhere.   Changes are regularly made to the GFS to improve its performance and forecast accuracy. It is a constantly evolving and improving weather prediction model.

Data are retained for 30 days.

This dataset is available on Azure thanks to the [NOAA Big Data Program](https://www.noaa.gov/organization/information-technology/big-data-program).


## Storage resources

Data are stored primarily in [GRIB](https://en.wikipedia.org/wiki/GRIB) format.

GRIB files are stored as blobs in the East US Azure region, in the following blob container:

`https://noaagfs.blob.core.windows.net/gfs`

Within that container, top-level folders are named as:

`[product].[date]`

* `product` is one of:
  * `gfs`: forecast data from the [Global Forecast System](https://www.nco.ncep.noaa.gov/pmb/products/gfs/#GFS) (GFS)
  * `gdas`: forecast data gridded with the [Global Data Assimilation System](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-data-assimilation-system-gdas) (GDAS)
  * `gfsmos`: model output statistics from the [GFS MOS](https://www.weather.gov/mdl/mos_gfsmos_home) suite
  * `sst`: sea surface temperature forecasts produced by the [NCEP Sea Surface Temperature](https://www.nco.ncep.noaa.gov/pmb/products/sst/) (SST) models
  * `enkfgdas`: data assimilated using the [GSI Hybrid/4DEnVar Data Assimilation](https://dtcenter.ucar.edu/com-GSI/users/docs/presentations/2017_tutorial/D3-L12_GSI_Hybrid4DEnVarDA_Kleist.pdf) system
  
* `date` is the model execution date in YYYYMMDD format

File format within a folder varies by product; documentation for the primary products (GFS and GFS-GDAS) can be found at:

* [GFS](https://www.nco.ncep.noaa.gov/pmb/products/gfs/#GFS)
* [GFS-GDAS](https://www.nco.ncep.noaa.gov/pmb/products/gfs/#GDAS)


## Region information

Large-scale processing is best performed in the East US Azure region, where the data are stored.  If you are using this data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Mounting the container

We also provide a read-only SAS (shared access signature) token to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://noaagfs.blob.core.windows.net/gfs?sv=2020-04-08&si=gfs-ro&sr=c&sig=SWziOkDMW1m51hyMoZSamZrd3NePmsQ51ljmioi7nCA%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).


## Contact

For questions, please contact the NOAA Big Data Program Team at [`noaa.bdp@noaa.gov`](mailto:noaa.bdp@noaa.gov?subject=azure%20gfs%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
