# NOAA Climate Forecast System (CFS)

## Overview

The NOAA [Climate Forecast System](https://cfs.ncep.noaa.gov/) (CFS) is a model representing the global interaction between Earth's oceans, land, and atmosphere. Produced under guidance from the National Centers for Environmental Prediction (NCEP), this model offers hourly data with a horizontal resolution down to one-half of a degree (approximately 56 km) around Earth for many variables. CFS assimilates observations from data sources including surface observations, upper air balloon observations, aircraft observations, and satellite observations.

Forecasts are generated four times a day - at the 0, 6, 12, and 18 UTC cycles - out to nine months.  Three additional forecasts - out to one season - are generated at the 0 UTC cycle, and three additional forecasts - out to 45 days - are generated at the 6, 12, and 18 UTC cycles, for a total of 16 CFS runs (forecasts) each day.  See [this CFS presentation](https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_docs/Operational.CFSv2.info.ppt) for a more detailed description of the CFS cycles.

Data are retained for 30 days.

This dataset is available on Azure thanks to the [NOAA Open Data Dissemination (NODD) Program](https://www.noaa.gov/information-technology/open-data-dissemination).


## Storage resources

Data are stored in [GRIB](https://en.wikipedia.org/wiki/GRIB) format as blobs in the East US Azure region, in the following blob container:

`https://noaacfs.blob.core.windows.net/cfs`

Forecasts are updated every six hours.  Within the above container, each forecast is available in a folder named:

`cfs.yyyymmdd/hh`

* yyyymmdd is the year, month, and day
* hh is the six-hourly forecast cycle, one of 00, 06, 12, or 18

Each forecast cycle folder contains nine subfolders:

* 6hrly_grib_[01,02,03,04]
* time_grib_[01,02,03,04]
* monthly_grib_01

The `6hrly_grib_YY` folders contain forecasts every 6 hours from model initialization time, out to X months, with X at most 9.

The `time_grib_YY` folders contain the same forecasts as the `6hrly` folders, partitioned differently.  In the `time_grib_YY` folders, data is binned with all forecast valid times (6-hr increments from model initialization time out to X months) present in one file, but for only one output variable per file. For example, z500.01.2021110100.daily.grb2 contains only the 500mb height forecasts from Nov 1 out to May 31, in six-hour increments

The `monthly_grib_YY` folders contain 6-hr averaged across all forecast days within a month. For example, pgbf.01.2021110100.202203.avrg.grib.grb2 contains average of variables, from the Nov 1 model runs, averaged from the individual forecast days for each variable within March 2022.  Averages are created for each of the four valid times each day (00, 06, 12, 18), and a daily average is also created.

01, 02, 03, and 04 indicate an ensemble member.

All subfolders will make use of the following variables in filenames:

* FLXF (surface, radiative fluxes)
* PGBF (3D pressure level, 1-degree resolution)
* OCNH (3D ocean data, 0.5-degree resolution)
* OCNF (3D ocean data, 1-degree resolution)
* IPVF (3D isentropic level data, 1-degree resolution)

File naming convention variables among the three subfolder types.


### `6hrly` subfolders

Within each "6hrly" subfolder, data are named according to:

`[variable][YYYYMMDD].[ensemble-member].[yyyymmddhh].grb2`

* YYYYMMDDHH is the forecast hour.
* yyyymmddhh is the initial hour of the forecast cycle.
* [ensemble-member] is the ensemble member, and will always match the containing folder

For example, this file:

<https://noaacfs.blob.core.windows.net/cfs/cfs.20210821/12/6hrly_grib_01/flxf2021101106.01.2021082112.grb2>

...contains six-hourly surface/flux information predicted for 2021.10.11:06:00, generated at 2021.08.21:12:00.


### `monthly` subfolder

Within each "monthly" subfolder, data are named according to:

`[variable].[ensemble-member].[yyyymmddhh].[YYMM].avrg.grib.[NN]z.grb2`

* [ensemble-member] is always 01 for monthly data for the 6, 12, and 18 UTC cycles, but may be 01, 02, 03, or 04 for the 0 UTC cycle.
* yyyymmddhh is the initial hour of the forecast cycle.
* YYMM is the forecast month

For example, this file:

<https://noaacfs.blob.core.windows.net/cfs/cfs.20210821/00/monthly_grib_01/flxf.01.2021082100.202109.avrg.grib.grb2>

...contains surface/flux information predicted for the month 2021.09, generated at 2021.08.21:00:00.


### `time` subfolders

Documentation pending.


## Region information

Large-scale processing is best performed in the East US Azure region, where the data are stored.


## Mounting the container

We also provide an API to get read-only SAS (shared access signature) tokens to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://planetarycomputer.microsoft.com/api/sas/v1/token/noaacfs/cfs`

API documentation is at `https://planetarycomputer.microsoft.com/api/sas/v1/docs`.
Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).


## Contact

For questions, please contact the NOAA Open Data Dissemination (NODD) Program Team at [`nodd@noaa.gov`](mailto:nodd@noaa.gov?subject=azure%20cfs%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
