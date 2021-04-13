# Daymet

## Overview

Estimates of daily weather parameters in North America on a one-kilometer grid, with monthly and annual summaries.

[Daymet](https://daymet.ornl.gov/) provides measurements of near-surface meteorological conditions; the main purpose of Daymet is provide data estimates where no instrumentation exists.
This dataset provides Daymet Version 4 data for North America, including the island areas of Hawaii and Puerto Rico (which are available as files separate from the continental land mass). Daymet output variables include minimum temperature, maximum temperature, precipitation, shortwave radiation, vapor pressure, snow water equivalent, and day length. The dataset covers the period from January 1, 1980 to the present. Each year is processed individually at the close of a calendar year. Daymet variables are continuous surfaces provided as individual files, by variable and year, at 1-kilometer spatial resolution and daily temporal resolution. Data are in a Lambert Conformal Conic projection for North America and are distributed in Zarr format and netCDF format compliant with [Climate and Forecast (CF) metadata conventions (version 1.6)](http://cfconventions.org/).  

We also provide the [monthly](https://daac.ornl.gov/DAYMET/guides/Daymet_V4_Monthly_Climatology.html) and [annual](https://daac.ornl.gov/DAYMET/guides/Daymet_V4_Annual_Climatology.html) climate summaries.


## Storage resources 

Data are stored in blobs in the West Europe Azure region, in two formats: [Zarr](https://zarr.readthedocs.io/) and netCDF, in the following blob containers:

* `https://daymeteuwest.blob.core.windows.net/daymet-zarr`
* `https://daymeteuwest.blob.core.windows.net/daymet-nc`

We recommend the Zarr format if you're analyzing part or all of the data directly from Azure Blob Storage, without downloading the data locally.
If you're downloading an entire block of the data, a specific variable for a specific time period, then either Zarr or netCDF format is appropriate.

Sample notebooks are provided to demonstrate both approaches to accessing Daymet data:

* [Zarr notebok](daymet-zarr.ipynb)
* [NetCDF notebok](daymet-nc.ipynb)


## Zarr Layout

Zarr files are named as:

`daymet-zarr/[frequency]/[region]`.zarr

* `frequency` is one of (`daily`, `monthly`, `annual`)
* `region` is one of (`hi`, `na`, and `pr`), for Hawaii, North America (continental), and Puerto Rico, respectively

All of the data variables (`tmin`, `tmax`, etc.) are available within each group.  See below for documentation of the available variables.

For example:

* `daymet-zarr/daily/hi.zarr` (Hawaii at daily frequency)
* `daymet-zarr/monthly/na.zarr` (North America at monthly frequency)
* `daymet-zarr/annual/pr.zarr` (Puerto Rico at daily frequency)


## netCDF Layout

There are three folders at the root level of the `daymet-nc` container:

* `daymet-nc/daymet_v4_daily` (daily variables)
* `daymet-nc/daymet_v4_monthly` (monthly summaries)
* `daymet-nc/daymet_v4_annual` (annual summaries)

Within the `daily` folder, files are named as:

`daymet_v4_daily_[region]_[variable]_[year].nc`

`region` is `hi`, `na`, or `pr`, for Hawaii, North America, or Puerto Rico, respectively.

For example:

`daymet-nc/daymet_v4_daily/daymet_v4_daily_hi_prcp_1980.nc`

...contains daily precipitation data for Hawaii in 1980.

Within the `monthly` and `annual` folders, filed are named as:

`daymet_v4_[variable]_[aggregation]_[region]_[year].nc`

`aggregation` is one of:

* `monttl` (monthly totals, `monthly` folder only)
* `monavg` (monthly averages, `monthly` folder only)
* `annttl` (annual totals, `annual` folder only)
* `annavg` (annual averages, `annual` folder only)

For example:

* `daymet-nc/daymet_v4_daily/daymet_v4_daily_hi_prcp_1980.nc` (daily precipitation in Hawaii for 1980)
* `daymet-nc/daymet_v4_monthly/daymet_v4_prcp_monttl_pr_1980.nc` (monthly total precipitation in Puerto Rico in 1980)
* `daymet-nc/daymet_v4_annual/daymet_v4_prcp_annavg_na_1980.nc` (annual average precipitation for North America in 1980)

See the [Daymet User Guide](https://daac.ornl.gov/DAYMET/guides/Daymet_V4_Monthly_Climatology.html) for more details.


## Variables

The following variables are available:

* tmin (minimum temperature)
* tmax (maximum temperature)
* prcp (precipitation)
* srad (shortwave radiation)
* vp (vapor pressure)
* swe (snow water equivalent)
* dayl (day length, daily frequency data only)


## Access

We also provide a read-only SAS (shared access signature) token to allow access to Daymet data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2019-12-12&si=daymet-ro&sr=c&sig=V85jbO5Ajj46%2BOwM3SYIA2MfXFvr8qq6Hvse3U9kJfc%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing using this dataset is best performed in the West Europe Azure data center, where the data is stored.  If you are using Daymet data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/aiforearth) to support your compute requirements.

A copy of the Daymet v4 NetCDF data is also available in the East US Azure region, and will be maintained there until at least the end of 2021, but we encourage users to migrate to the West Europe copy.  The East US data is in the following container:

`https://daymet.blob.core.windows.net/daymet-nc`


## Citation

If you use this data in a publication, please cite one of the following (depending on whether you're using daily, monthly, or annual data):

* Thornton, M.M., R. Shrestha, Y. Wei, P.E. Thornton, S. Kao, and B.E. Wilson. 2020. Daymet: Daily Surface Weather Data on a 1-km Grid for North America, Version 4. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1840
* Thornton, M.M., R. Shrestha, Y. Wei, P.E. Thornton, S. Kao, and B.E. Wilson. 2020. Daymet: Monthly Climate Summaries on a 1-km Grid for North America, Version 4. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1855
* Thornton, M.M., R. Shrestha, Y. Wei, P.E. Thornton, S. Kao, and B.E. Wilson. 2020. Daymet: Annual Climate Summaries on a 1-km Grid for North America, Version 4. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1852

See the Oak Ridge National Laboratory Distributed Active Archive Center (ORNL DAAC)'s [Data Use and Citations Policy](https://daac.ornl.gov/citation_policy.html) for more information.


## Resources

The following resources and references may be helpful when working with the Daymet dataset:

* [Project site](https://daymet.ornl.gov/)<br/>
* [Daily user guide](https://daac.ornl.gov/DAYMET/guides/Daymet_Daily_V4.html)<br/>
* [Monthly user guide](https://daac.ornl.gov/DAYMET/guides/Daymet_V4_Monthly_Climatology.html)<br/>
* [Annual user guide](https://daac.ornl.gov/DAYMET/guides/Daymet_V4_Annual_Climatology.html)<br/>


## Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/daymet.png" width=200px;><br/>

<p style="font-size:80%;margin-left:15px;">Average daily maximum temperature in Hawaii in 2017.</p>


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=daymet%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.

