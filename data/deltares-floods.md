# Deltares Global Flood Map

## Overview

[Deltares](https://www.deltares.nl/en/) has produced inundation maps of flood depth using a model that takes into account water level attenuation and is forced by sea level. At the coastline, the model is forced by extreme water levels containing surge and tide from GTSMip6. The water level at the coastline is extended landwards to all areas that are hydrodynamically connected to the coast following a ‘bathtub’ like approach and calculates the flood depth as the difference between the water level and the topography. Unlike a simple 'bathtub' model, this model attenuates the water level over land with a maximum attenuation factor of 0.5 m km-1. The attenuation factor simulates the dampening of the flood levels due to the roughness over land.

In its current version, the model does not account for varying roughness over land and permanent water bodies such as rivers and lakes, and it does not account for the compound effects of waves, rainfall, and river discharge on coastal flooding. It also does not include the mitigating effect of coastal flood protection. Flood extents must thus be interpreted as the area that is potentially exposed to flooding without coastal protection.

See the complete [methodology documentation](https://deltaresfloodssa.blob.core.windows.net/floods/v2021.06/11206409-003-ZWS-0003_v0.1-Planetary-Computer-Deltares-global-flood-docs.pdf) for more information.

### Digital elevation models (DEMs)

This documentation will refer to three DEMs:

* `NASADEM` is the SRTM-derived [NASADEM](https://lpdaac.usgs.gov/products/nasadem_hgtv001/) product.
* `MERITDEM` is the [Multi-Error-Removed Improved Terrain DEM](http://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_DEM/), derived from SRTM and AW3D.
* `LIDAR` is the [Global LiDAR Lowland DTM (GLL_DTM_v1)](https://data.mendeley.com/datasets/v5x4vpnzds/1).

## Storage resources

Data are stored in netCDF files in Azure Blob Storage in the West Europe Azure region, in the following folder:

<https://deltaresfloodssa.blob.core.windows.net/floods/v2021.06/>

Within that folder, data are organized according to one path structure for [global datasets](#global-datasets) and one path structure for [historic event datasets](#historic-event-datasets).

### Global datasets

This collection includes multiple global flood datasets derived from three different DEMs (`NASA`, `MERIT`, and `LIDAR`) and at different resolutions. Not all DEMs have all resolutions:

* `NASADEM` and `MERITDEM` are available at `90m` and `1km` resolutions
* `LIDAR` is available at `5km` resolution

Each global dataset - i.e., each DEM/resolution pair - is in a folder named according to:

`global/[DEM]/[resolution]/`

Within those folders, all files follow the same naming convention:

`GFM_global_[DEM][resolution]_[sealevelyear]slr_rp[returnperiod]_masked.nc`

* `DEM` is the name of the DEM, and will match the folder name; valid DEMs are `NASADEM`, `MERITDEM`, and `LIDAR`.
* `Resolution` is `90m`, `1km`, or `5km`, and will match the folder name.
* `sealevelyear` is the sea level rise scenario, either `2018` or `2050`.
* `returnperiod` is the [return period](https://en.wikipedia.org/wiki/Return_period) in years; valid return periods are `0000`, `0002`, `0005`, `0010`, `0025`, `0050`, `0100`, and `0250`.

For example, a 100 year return period based off of current (2018) sea level rise conditions, derived from NASADEM at 90m resolution can be accessed at:

<https://deltaresfloodssa.blob.core.windows.net/floods/v2021.06/global/NASA/90m/GFM_global_NASADEM90m_2018slr_rp0100_masked.nc>

### Historic event datasets

This collection also includes historical storm event data files that follow similar DEM and resolution conventions. Not all storms events are available for each DEM and resolution combination, but generally follow the format of:

`events/[DEM]_[resolution]-wm_final/[storm_name]_[event_year]_masked.nc`

For example, a flood map for the MERITDEM-derived 90m flood data for the "Omar" storm in 2008 is available at:

<https://deltaresfloodssa.blob.core.windows.net/floods/v2021.06/events/MERITDEM_90m-wm_final/Omar_2008_masked.nc>

### File contents

Both global and historical storm event netCDF files have the same attributes and follow CF-1.6 conventions:

| Variable     | Description                                                          | Dimensions Units |                                |
|--------------|----------------------------------------------------------------------|------------------|--------------------------------|
| `time`       | single time output value, not used (default value of 01-Jan-2010)    | time             | days since 1960-01-01 00:00:00 |
| `lat`        | latitude in WGS84 spherical coordinates                              | lat              | degrees_north                  |
| `lon`        | longitude in WGS84 spherical coordinates                             | lon              | degrees_east                   |
| `projection` | information on the coordinate system (WGS84, EPSG: 4326)             | -                | -                              |
| `inun`       | coastal flooding in water surface height above reference datum (MSL) | lat, lon         | m                              |

## Sample code

A complete Python example of accessing and plotting inundation data is available in the accompanying [sample notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/deltares-floods.ipynb).

## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=deltares-floods%20question).

## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset. To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset. This dataset is provided under the original terms that Microsoft received source data.
