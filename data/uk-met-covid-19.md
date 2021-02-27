# UK Met Office Global Weather Data for COVID-19 Analysis

## Overview

This data is for COVID-19 researchers to explore relationships between COVID-19 and environmental factors.

For more information see our [blog post](https://medium.com/informatics-lab/met-office-and-partners-offer-data-and-platform-for-covid-19-researchers-83848ac55f5f). If you require compute resources to process this data [we might be able to help](https://medium.com/informatics-lab/met-office-and-partners-offer-data-and-platform-for-covid-19-researchers-83848ac55f5f).

# Stay up to date

Stay up to date with new datasets, corrections, redactions, and other important information by subscribing to this data set's [mailing list](https://groups.google.com/forum/#!forum/met-office-covid-19-data-and-platform-updates/join).

## License

Users are required to acknowledge the Met Office as the source of these data by including the following attribution statement in any resulting products, publications or applications: “Contains Met Office data licensed under the Open Government Licence v3.0”.

This data is made available under the [Open Government License](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).


## About the data

Global and high-resolution UK [numerical weather model output](https://www.metoffice.gov.uk/research/approach/modelling-systems/unified-model/weather-forecasting) from the [UK Met Office](https://www.metoffice.gov.uk/). Data is from the very early time steps of the model following data assimilation, as such this data approximates a whole-Earth observation dataset.

The following variables are available:

- `t1o5m` = Air temperature at 1.5m in $K$
- `sh` = Specific humidity at 1.5m in $kg/kg$ (kg of water vapor in kg of air)
- `sw` = Short wave radiation in $W m^{-2}$ (surrogate for sunshine)
- `precip` = Precipitation flux in $kg m^{-2} s^{-1}$ (multiply by 3600 to get $mm / hr$)
- `rain` = Rain flux in $kg m^{-2} s^{-1}$ (multiply by 3600 to get $mm / hr$)
- `pmsl` = Air pressure at mean sea level in $Pa$
- `snow` = Stratiform snowfall flux in $kg m^{-2} s^{-1}$ (multiply by 3600 to get $mm / hr$)
- `windspeed` = Wind speed in $m s^{-1}$
- `windgust` = Wind gust in $m s^{-1}$
- `cldbase` = Cloud base altitude in $feet$
- `cldfrac` = Cloud area fraction assuming maximum random overlap (unitless: 0-1)

Output of the Met Office UK air quality model [AQUM](https://www.metoffice.gov.uk/research/weather/atmospheric-dispersion/atmospheric-composition) is also available. This includes the following variables:

- `daqi` = Daily Air Quality Index, an integer from 1-10
- `no2` = Nitrogen dioxide concentration, in$µg m^{-3}$
- `o3` = Ozone concentration, in $µg m^{-3}$
- `so2` = Sulphur dioxide concentration, in $µg m^{-3}$
- `pm2p5` = Concentration of particulate matter less than 2.5 microns diameter, in $µg m^{-3}$
- `pm10` = Concentration of particulate matter less than 10 microns diameter, in $µg m^{-3}$

This data is made available as NetCDF files.

Global and UK model data updated is available from 01 Jan 2020 onwards. The dataset is updated daily for the previous day.

For detailed information about how this data is generated and the particulars of the parameters please see the technical references:

- [Meterological data reference](https://metdatasa.blob.core.windows.net/covid19-response/README_data_processing.pdf)
- [Air quality reference](https://metdatasa.blob.core.windows.net/covid19-response/README_data_air_quality.html)

There are some additional post-processed data aggregations over COVID-19 reporting regions in the UK and USA made available as CSV files. More details below.


## Storage location

This dataset is stored in the East US 2 Azure region. Allocating compute resources in East US 2 is recommended for affinity. 


## Quick links

- [Announcement by the Met Office](https://medium.com/informatics-lab/met-office-and-partners-offer-data-and-compute-platform-for-covid-19-researchers-83848ac55f5f) making this data available in response to the [RAMP](https://epcced.github.io/ramp/) initiative, asking for assistance in tackling to the COVID-19 pandemic.

- You can browse the data we have made available on Azure [here](https://metdatasa.blob.core.windows.net/covid19-response/index.html).

- This data is made available under the [Open Government License](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

- More data is coming! Please subscribe to our [Google Groups mailing list](https://groups.google.com/forum/#!forum/met-office-covid-19-data-and-platform-updates/join) to receive updates when that data is available.

- Please contact us at [covid19@informaticslab.co.uk](mailto:covid19@informaticslab.co.uk) if you have any questions or requests for additional data.


## Data volumes, retention, and update frequency 

The gridded data is updated daily for the previous day.

As of 18/04/20 the dataset totals approximately 352G. It grows weekly by approximately 22G a week.

We intend to retain and make this data available as long as we believe it's useful in planing the response to the COVID-19 pandemic.

# Quick start

The data is hosted on Microsoft Azure through their AI for Earth initiative. You can access the data in many ways, such as:


## Point and click

Open the [index file](https://metdatasa.blob.core.windows.net/covid19-response/index.html) in your browser. You will see a list of links to datafiles which you can download by clicking on them in your browser.


## Azure Blob libraries

There is a range of libraries in a range of languages for working with Azure Blobs. See the [Azure Blob documentation](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-overview) for more information.


## Downloading with AzCopy

There are lots of files, so we suggest installing `azcopy` command line tool, which you can download [here](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10#download-azcopy). This lets you download [whole directories](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-blobs?toc=/azure/storage/blobs/toc.json#download-the-contents-of-a-directory) or multiple files [using wildcards](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-blobs?toc=/azure/storage/blobs/toc.json#use-wildcard-characters-1).

For example...

To download the file global_daily_precip_max_20200101.nc to the current directory:<br/>
`azcopy cp https://metdatasa.blob.core.windows.net/covid19-response/metoffice_global_daily/precip_max/global_daily_precip_max_20200101.nc .`

To download the contents of /metoffice_ukv_daily/snow_mean/ to ukv_daily_snow_mean/:<br/>
`azcopy cp 'https://metdatasa.blob.core.windows.net/covid19-response/metoffice_ukv_daily/snow_mean/*' ukv_daily_snow_mean/`

To download all the US state county-averaged meteorology data which match the pattern us_55\*.csv:<br/>
`azcopy cp  --recursive  --include-pattern 'us_55*.csv' https://metdatasa.blob.core.windows.net/covid19-response/regional_subset_data/us_data/ .` 


## How the data is organised

### `metoffice_global_daily/`

...contains the Met Office daily global gridded data files.  There is a directory for each variable.

Each file is named according to `global_daily_{variable}_{statistic}_{YYYYMMDD}.nc`, for example:

`metoffice_global_daily/precip_max/global_daily_precip_max_20200101.nc`

...contains the gridded maximum precipitation data from Jan 1, 2020.

### `metoffice_global_hourly/`

...contains the Met Office hourly global gridded data files.

Each file is named according to `global_hourly_{variable}_global_{YYYYMMDD}.nc`, for example:

`metoffice_global_hourly/precip/global_hourly_precip_20200101.nc`

...contains gridded hourly precipitation data from Jan 1, 2020.

### `metoffice_ukv_daily/`

...contains the Met Office daily UKV gridded data files.

Each file is named according to `ukv_daily_{variable}_{statistic}_{YYYYMMDD}.nc`.

### `metoffice_ukv_hourly/`

...contains the Met Office hourly UKV gridded data files.

Each file is named according to `ukv_hourly_{variable}_{YYYYMMDD}.nc`.

### `metoffice_aqum_daily/`

...contains the Met Office daily AQUM gridded data files.

Each file is named according to `aqum_daily_{variable}_{statistic}_{YYYYMMDD}.nc`.

### `metoffice_aqum_hourly/`

...contains the Met Office hourly AQUM gridded data files.

Each file is named according to `aqum_hourly_{variable}_{YYYYMMDD}.nc`.

### `regional_subset_data/`

...contains processed regional daily values for the UK, the USA, Italy, Brazil, Vietnam, and Uganda as `.csv` files.

Processed files represent the period from Jan 1 to Apr 19, 2020.  Files were processed by subsetting the gridded Met Office global daily files using shapefiles for each region, taking the latitude-longitude mean value for each variable in each region for each date and saving those values as a table in a `.csv` file.

Each file in this directory (one .csv file per region) is named according to `{shapefile_name}/{shapefile_name}_metoffice_global_daily_bbox_{start_date}-{end_date}.csv`.

For example, the file:

`regional_subset_data/gadm36Uganda2/gadm36Uganda2_metoffice_global_daily_20200101-20200419.csv`

...represents processed data for Uganda.

### `shapefiles/`

Contains shapefiles for the UK, the USA, Italy, Brazil, Uganda, and Vietnam.

  - `UK/` = UK COVID-19 reporting regions
  - `USA/` = USA state counties
  - `Italy/` = [GADM v3.6](https://gadm.org/download_country_v3.html) administrative level 2 for Italy
  - `Brazil/` = [GADM v3.6](https://gadm.org/download_country_v3.html) administrative level 2 for Brazil
  - `Uganda/` = [GADM v3.6](https://gadm.org/download_country_v3.html) administrative level 2 for Uganda
  - `Vietnam/` = [GADM v3.6](https://gadm.org/download_country_v3.html) administrative level 2 for Vietnam

Where possible, filenames are as described. However, given the short time frames in which this data has been made available, minor variations in filename descriptions may occur. Filenames should still be accurately descriptive of the data. If you find issues with any filenames, or the data itself, please contact us at [covid19@informaticslab.co.uk](mailto:covid19@informaticslab.co.uk).


## Getting help and contact

For help or additional data requests please contact us at [covid19@informaticslab.co.uk](mailto:covid19@informaticslab.co.uk).


## Notices

MICROSOFT PROVIDES AZURE OPEN DATASETS ON AN "AS IS" BASIS. MICROSOFT MAKES NO WARRANTIES, EXPRESS OR IMPLIED, GUARANTEES OR CONDITIONS WITH RESPECT TO YOUR USE OF THE DATASETS. TO THE EXTENT PERMITTED UNDER YOUR LOCAL LAW, MICROSOFT DISCLAIMS ALL LIABILITY FOR ANY DAMAGES OR LOSSES, INCLUDING DIRECT, CONSEQUENTIAL, SPECIAL, INDIRECT, INCIDENTAL OR PUNITIVE, RESULTING FROM YOUR USE OF THE DATASETS. 
