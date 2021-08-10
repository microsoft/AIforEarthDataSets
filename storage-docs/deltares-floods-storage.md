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