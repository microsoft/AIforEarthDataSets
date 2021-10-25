# NOAA U.S. Climate Normals

## Overview

The [U.S. Climate Normals](https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals) are a suite of data products that provide information about typical climate conditions for thousands of locations across the United States. Normals act both as a ruler to compare today's weather and tomorrow's forecast, and as a predictor of conditions in the near future. The official normals are calculated for a uniform 30-year period, and consist of annual/seasonal, monthly, daily, and hourly averages and statistics of temperature, precipitation, and other climatological variables from almost 15,000 U.S. weather stations. 

The [National Centers for Environmental Information](https://www.ncei.noaa.gov/) (NCEI) generates the official U.S. normals every 10 years in keeping with the needs of our user community and the requirements of the World Meteorological Organization (WMO) and National Weather Service (NWS). The 1991–2020 U.S. Climate Normals are the latest in a series of decadal normals first produced in the 1950s. These data allow travelers to pack the right clothes, farmers to plant the best crop varieties, and utilities to plan for seasonal energy usage. Many other important economic decisions that are made beyond the predictive range of standard weather forecasts are either based on or influenced by climate normals.

This dataset is available on Azure thanks to the [NOAA Big Data Program](https://www.noaa.gov/organization/information-technology/big-data-program).


## Storage resources

Data are stored in the East US Azure data center, in .csv format, in the following bob container:

`https://noaanormals.blob.core.windows.net/climate-normals`

Within that container, files are named as:

`normals-[frequency]/[year_range]/access/[station].csv`

* `frequency` is one of annualseasonal, daily, hourly, monthly
* `year_range` is one of "1981-2010", "1991-2020", "2006-2020"

For example, the hourly data for the 1991-2020 period from station AQW00061705 is in the following file:

<https://noaanormals.blob.core.windows.net/climate-normals/normals-hourly/1991-2020/access/AQW00061705.csv>


### File formats

Formats vary slightly across the daily, hourly, monthly, and annual/seasonal folders.

* The .csv format for the daily data is described at:

  <https://noaanormals.blob.core.windows.net/climate-normals/normals-daily/doc/NORMAL_DLY_documentation.pdf>
  
* The .csv format for the hourly data is described at:

  <https://noaanormals.blob.core.windows.net/climate-normals/normals-hourly/doc/NORMAL_HLY_documentation.pdf>
  
* The .csv format for the annual/seasonal data is described at:

  <https://noaanormals.blob.core.windows.net/climate-normals/normals-monthly/doc/NORMAL_MLY_documentation.pdf>

* The .csv format for the annual/seasonal data is described at:

  <https://noaaisd.blob.core.windows.net/noaa-isd/pub/data/noaa/isd-format-document.pdf>


## Region information

Large-scale processing is best performed in the East US Azure region, where the data are stored.  If you are using this data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Contact

For questions, please contact the NOAA Big Data Program Team at [`noaa.bdp@noaa.gov`](mailto:noaa.bdp@noaa.gov?subject=azure%20climatenormals%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
