# NOAA Monthly US Climate Gridded Dataset (NClimGrid)

## Overview

The NOAA [Monthly U.S. Climate Gridded Dataset](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00332) (NClimGrid) consists of four climate variables derived from the [Global Historical Climatology Network](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily) daily dataset (GHCN-D): maximum temperature, minimum temperature, average temperature, and precipitation. Each file provides monthly values in a 5x5 lat/lon grid for the Continental United States. Monthly data is available from 1895 to the present; daily data is available from 1951 to the present.

On an annual basis, approximately one year of "final" nClimGrid will be submitted to replace the initially supplied "preliminary" data for the same time period. Users should be sure to ascertain which level of data is required for their research.

This dataset is available on Azure thanks to the [NOAA Big Data Program](https://www.noaa.gov/organization/information-technology/big-data-program).


## Storage resources

### Monthly data

Monthly data are stored in [NetCDF](https://www.unidata.ucar.edu/software/netcdf/) format; daily data are stored in NetCDF and .csv formats.  Two identical blob containers are available, one in the West Europe Azure data center, and one in the East US Azure data center:

`https://nclimgridwesteurope.blob.core.windows.net/nclimgrid`
`https://nclimgrideastus.blob.core.windows.net/nclimgrid`

Within each container, there are four files representing monthly climate history, named as:

`nclimgrid-monthly/nclimgrid_[variable].nc`

...where "variable" is one of:

* `prcp`: precipitation
* `tavg`: average temperature
* `tmax`: maximum temperature
* `tmin`: minimum temperature

Each NetCDF file represents the complete climatalogical history for that variable; these files are updated in place once a month.

### Daily data

Daily files are named as:

`nclimgrid-daily/beta/by-month/[year]/[month]/[variable]-[year][month]-grd-scaled.nc`

...for the gridded data, or:

`nclimgrid-daily/beta/by-month/[year]/[month]/[variable]-[year][month]-[type]-scaled.csv`

...for the un-gridded source data.  For un-gridded data:

* `variable` is one of prcp, tavg, tmin, or tmax
* `type` is the region type, one of:
  * cen: census tract
  * cns: contiguous US
  * cty: counties
  * div: climate divisions
  * hc1: hydrologic unit code
  * nca: NCA regions
  * reg: NCEI regions
  * ste: state
  * wfo: weather forecast office
  
Detailed documentation of the daily data .csv format is here:

<https://www1.ncdc.noaa.gov/pub/data/daily-grids/docs/nclimdiv-description.pdf>

## Region information

Large-scale processing is best performed in the West Europe or East US Azure regions, where the data are 


## Contact

For questions, please contact the NOAA Big Data Program Team at [`noaa.bdp@noaa.gov`](mailto:noaa.bdp@noaa.gov?subject=azure%20nclimgrid%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
