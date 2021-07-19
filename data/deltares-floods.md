# Deltares Global Flood Map

## Overview

[Deltares](https://www.deltares.nl/en/) has produced inundation maps of flood
depth using a geographic information system-based inundation model that takes
into account water level attenuation and is forced by sea level. At the
coastline, the model is forced by extreme water levels containing surge and tide
from GTSMip6. The water level at the coastline is extended landwards to all
areas that are hydrodynamically connected to the coast following a ‘bathtub’
like approach and calculates the flood depth as the difference between the water
level and the topography. Unlike a simple ‘bathtub’ model, this model attenuates
the water level over land with a maximum attenuation factor of 0.5 m km-1
consistent with other studies (Vafeidis et al., 2018). The attenuation factor
simulates the dampening of the flood levels due to the roughness over land.  In
its current version, the model does not account for varying roughness over land
and permanent water bodies such as rivers and lakes.

The model does not account for the compound effects of waves, rainfall and river
discharge on coastal flooding. It also does not include the mitigating effect of
coastal flood protection. Flood extents must thus be interpreted as the area
that is potentially exposed to flooding without coastal protection.

## Storage resources

Data are stored in netCDF files in Azure Blob Storage in the West Europe Azure region, in the following blob container:

<https://deltaresfloodssa.blob.core.windows.net/floods/v2021.06/>

Within that container, data are organized under several directories representing covered regions:

### Global datasets

There are multiple global flood datasets derived from different DEMs and at different resolutions. Not all DEMs have all resolutions:

- `NASA` and `MERIT` are available at `90m` and `1km` resolutions
- `LIDAR` is available at `5km` resolution

All DEM

`global/[DEM]/[resolution]/`

Within those directories, all files follow the same naming convention:

`GFM_global_[DEM][resolution]_[sealevelyear]slr_rp[returnperiod]_masked.nc`

...for example

`GFM_global_MERIT1km_2050slr_rp0050.nc`

Valid return periods (RP) are: `0000`, `0002`, `0005`, `0010`, `0025`, `0050`, `0100`, and `0250`.

Valid sea level rise years (SLR) are: `2018` and `2050`.

For example, a 100 year return period based off of current SLR conditions (2018), derived from NASADEM at 90m resolution can be accessed at:

`/floods/v2021.06/global/NASA/90m/GFM_global_NASADEM90m_2018slr_rp0100_masked.nc`

### Historic event datasets

Also included in the `floods` container are historical storm event data files that follow similar DEM and resolution conventions. Not all storms events are available for each DEM and resolution combination, but generally follow the format of:

`[DEM]_[resolution]-wm_final/[storm_name]_[event_year]_masked.nc`

...for example:

`/floods/v2021.06/MERIT_90m-wm_final/Omar_2008_masked.nc`

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

A complete Python example of accessing and plotting inundation data is available in the accompanying [sample notebook](deltares-floods.ipynb).

## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=deltares-floods%20question).

## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset. To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset. This dataset is provided under the original terms that Microsoft received source data.
