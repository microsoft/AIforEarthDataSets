# GFS Warm Start Initial Conditions

## Overview

Warm start initial conditions for the NOAA Global Forecast System.

The NOAA [Global Forecast System](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs) (GFS) Warm Start Initial Conditions are produced by the [National Centers for Environmental Prediction](https://www.ncep.noaa.gov/) (NCEP) to run operational deterministic medium-range numerical weather predictions.   The GFS is built with the [GFDL Finite­Volume Cubed-Sphere Dynamical Core](https://www.gfdl.noaa.gov/fv3/) (FV3) and the [Grid-Point Statistical Interpolation](https://ral.ucar.edu/solutions/products/gridpoint-statistical-interpolation-gsi) (GSI) data assimilation system.  The current operational GFS is run at 64 layers in the vertical dimension extending from the surface to the upper stratosphere, and on six cubic-sphere tiles at the C768 or 13-km horizontal resolution.  A new version of the GFS that has 127 layers extending to the mesopause will be implemented for operation on February 3, 2021.  These initial conditions are made available four times per day for running forecasts at the 00Z, 06Z, 12Z and 18Z cycles.


## Storage resources 

<i>Overview</i>

Data are stored in blobs in the East US Azure region, in the following blob container:

`https://gfswarmstart.blob.core.windows.net/gfs-warmstart-v15`

Within that container, folders are named as:

`product.yyyymmdd`

...where `product` is either "gdas" or "gfs".  

For each cycle, the dataset contains the first guess of the atmosphere states found in the directory gdas.yyyymmdd/hh/RESTART, which are 6-hour GDAS forecasts from the last cycle, and atmospheric analysis increments and surface analysis for the current cycle found in the directory gfs.yyyymmdd/hh, which are produced by the data assimilation systems.  

To run a gfs forecast, the model needs to read in the 6-hour forecasts from the last GDAS cycle, the analysis increments from the current gfs cycle, and the updated surface analysis from the current gfs cycle.  

<i>GDAS folder contents</i>

Within a gdas folder, folders for each six-hourly update are named as:

`gdas.yyyymmdd/hh`

...where `hh` is one of 00, 06, 12, or 18, corresponding to the four daily updates.  Each of those folders contains a single folder called "RESTART", which contains NetCDF files, named as:

`gdas.yyyymmdd/hh/RESTART/yyyymmdd.hh0000.[variable](.tile[tile_number]).nc`

When present, `tile_number` is a tile number from 1 to 6.

`variable` is one of:

* fv_core.res (model vertical hybrid coordinate)
* fv_core.res.tileN (atmospheric state variables)
* sfcanl_data.tileN (surface state variables after surface cycle update used by GDAS forecast)
* fv_srf_wnd.res.tileN (surface winds)
* fv_tracer.res.tileN (tracers)
* phy_data.tileN (physics tendencies)
* sfc_data.tileN (surface state variables)

So, for example, this file:

`https://gfswarmstart.blob.core.windows.net/gfs-warmstart-v15/gdas.20201213/00/RESTART/20201213.060000.fv_srf_wnd.res.tile3.nc`

...contains surface wind data over tile 3, from hour 6 on December 13, 2020.

<i>GFS folder contents</i>

Within a gfs folder, files are named as:

`gfs.yyyymmdd/hh/RESTART/yyyymmdd.hh0000.sfcanl_data.tile[tile_number].nc`

...where `hh` is one of 00, 06, 12, or 18, corresponding to the four daily updates and `tile_number` is a tile number from 1 to 6.

For example, this file:

`https://gfswarmstart.blob.core.windows.net/gfs-warmstart-v15/gfs.20210101/12/RESTART/20210101.120000.sfcanl_data.tile3.nc`

...contains a GFS prediction for tile 3, from hour 12 on January 1, 202021.


We also provide a read-only SAS (shared access signature) token to allow access to GFS Warm Start data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2019-12-12&si=gfs-warmstart-noaa-ro&sr=c&sig=Efen5WbiL6gBTjKCH2RbgScCzwdaefM3apytS7ar4M4%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing using this dataset is best performed in the East US 2 Azure data center, where the data is stored.


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
