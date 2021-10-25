# NOAA Global Ensemble Forecast System (GEFS)

## Overview

The NOAA [Global Ensemble Forecast System](https://www.ncei.noaa.gov/products/weather-climate-models/global-ensemble-forecast) (GEFS) is a weather forecast model made up of 21 separate forecasts, or ensemble members. The National Centers for Environmental Prediction (NCEP) started the GEFS to address uncertainty in weather observations, which are used to initialize weather forecast models. The GEFS attempts to quantify the amount of uncertainty in a forecast by generating an ensemble of multiple forecasts from the original observations.  With global coverage, GEFS is produced four times a day with weather forecasts going out to 16 days.

Data are retained for 30 days.

This dataset is available on Azure thanks to the [NOAA Big Data Program](https://www.noaa.gov/organization/information-technology/big-data-program).


## Storage resources

Data are stored primarily in [GRIB](https://en.wikipedia.org/wiki/GRIB) format.

GRIB files are stored as blobs in the East US Azure region, in the following blob container:

`https://noaagefs.blob.core.windows.net/gefs`

Within that container, six-hourly forecast folders are named as:

`gfs.[date]/[cycle]`

* `date` is the model execution date in YYYYMMDD format
* `cycle` is a six-hourly cycle, one of [00,06,12,18]

Each forecast cycle folder contains three subfolders:

* `atmos`
* `chem`
* `wave`

File naming conventions vary across subfolders; details for each subfolder follow.

### `atmos` naming conventions

Each `atmos` folder contains three subfolders with forecast data:

* `pgrb2ap5`
* `pgrb2bp5`
* `pgrb2sp25`

Example URL:

<https://noaagefs.blob.core.windows.net/gefs/gefs.20210827/06/atmos/pgrb2ap5/geavg.t06z.pgrb2a.0p50.f009>

### `chem` naming conventions

Each `chem` folder contains two subfolders:

* `pgrb2ap25`
* `pgrb2ap5`

Example URL:

<https://noaagefs.blob.core.windows.net/gefs/gefs.20210827/06/chem/pgrb2ap5/gefs.chem.t06z.a3d_0p50.f006.grib2>

### `wave` naming conventions

Each `wave` folder contains two subfolders:

* `gridded`
* `station`

Example URLs:

<https://noaagefs.blob.core.windows.net/gefs/gefs.20210827/06/wave/gridded/gefs.wave.t06z.c00.global.0p25.f003.grib2>

<https://noaagefs.blob.core.windows.net/gefs/gefs.20210827/06/wave/station/gefs.wave.t06z.bull_tar>
<https://noaagefs.blob.core.windows.net/gefs/gefs.20210827/06/wave/station/gefs.wave.t06z.station_tar>


## Region information

Large-scale processing is best performed in the East US Azure region, where the data are stored.  If you are using this data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Mounting the container

We also provide a read-only SAS (shared access signature) token to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://noaagefs.blob.core.windows.net/gefs?sv=2020-08-04&si=gefs-ro&sr=c&sig=ZaQx5Zq5GFj8LqXmVYy4KVZ3NttXovbdwVLAQ9%2B57%2Fw%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).


## Contact

For questions, please contact the NOAA Big Data Program Team at [`noaa.bdp@noaa.gov`](mailto:noaa.bdp@noaa.gov?subject=azure%20gefs%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
