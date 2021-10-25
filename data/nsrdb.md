# NREL National Solar Radiation Database (NSRDB)

## Overview

## NSRDB

The [National Solar Radiation Database](https://nsrdb.nrel.gov/) (NSRDB) is a serially complete collection of meteorological and solar irradiance data sets for the United States and a
growing list of international locations for 1998-2020. The NSRDB provides foundational information to support U.S. Department of Energy programs, research, and the general public.

The NSRDB provides time-series data at 30-minute resolution averaged over surface cells of 0.038 degrees in both latitude and longitude, or nominally 4 km in size. The solar radiation values represent the resource
available to solar energy systems. The data was created using cloud properties which are generated using the AVHRR Pathfinder Atmospheres-Extended ([PATMOS-x](https://cimss.ssec.wisc.edu/patmosx/)) algorithms developed by the University of Wisconsin. The Fast All-sky Radiation Model for Solar Applications ([FARMS](https://www.sciencedirect.com/science/article/abs/pii/S0038092X16301827)) * in conjunction with the cloud properties, aerosol optical depth (AOD), and precipitable water vapor (PWV) from ancillary sources * is used to estimate solar irradiance (GHI, DNI, and DHI).  The Global Horizontal Irradiance (GHI) is computed for clear skies using the [REST2](https://www.sciencedirect.com/science/article/abs/pii/S0038092X07000990) model. For cloud scenes identified by the cloud mask, FARMS is used to compute GHI. The Direct Normal Irradiance (DNI) for cloud scenes is then
computed using the [DISC model](https://www.nrel.gov/grid/solar-resource/disc.html). The PATMOS-X model uses half-hourly radiance images in visible and infrared channels from the GOES series of geostationary
weather satellites.  Ancillary variables needed to run REST2 and FARMS (e.g., aerosol optical depth, precipitable water vapor, and albedo) are derived from the the Modern Era-Retrospective Analysis ([MERRA-2](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/)) dataset. Temperature and wind speed data are also derived from MERRA-2 and provided for use in the System Advisor Model ([SAM](https://sam.nrel.gov/)) to compute PV generation.

The following variables are provided by the NSRDB:

* Irradiance:
    * Global horizontal (ghi)
    * Direct normal (dni)
    * Diffuse (dhi)
* Clear-sky irradiance
    * Global horizontal (clearsky_ghi)
    * Direct normal (clearsky_dni)
    * Diffuse (clearsky_dhi)
* Cloud type (cloud_type)
* Dew point (dew_point)
* Temperature (air_temperature)
* Surface albedo (surface_albedo)
* Pressure (surface_pressure)
* Relative humidity (relative_humidity)
* Solar zenith angle (solar_zenith_angle)
* Precipitable water (total_precipitable_water)
* Wind direction (wind_direction)
* Wind speed (wind_speed)
* Fill flag (fill_flag)
* Angstrom wavelength exponent (alpha)
* Aerosol optical depth (aod)
* Aerosol asymmetry parameter (asymmetry)
* Cloud optical depth (cld_opd_dcomp)
* Cloud effective radius (cld_ref_dcomp)
* Cloud pressure (cloud_press_acha)
* Reduced ozone vertical path length (ozone)
* Aerosol single-scatter albedo (ssa)


## Storage resources

Data are available as HDF (.h5) files on Azure Blob Storage in the East US Azure region, in the following container:

`https://nrel.blob.core.windows.net/nrel-nsrdb`

### CONUS data

Within the above  container, files for CONUS are named as:

`v3/nsrdb_[year].h5`

`year` is a four-digit year from 1998 to one year behind the present date.

For example, the following file contains solar radiation data for CONUS for 2007:

<https://nrel.blob.core.windows.net/nrel-nsrdb/v3/nsrdb_2007.h5>

### Puerto Rico data

Within the above  container, files for Puerto Rico are named as:

`v3/puerto_rico/nsrdb_puerto_rico_[year].h5`

`year` is a four-digit year from 1998 to one year behind the present date.

For example, the following file contains solar radiation data for Puerto Rico for 2007:

<https://nrel.blob.core.windows.net/nrel-nsrdb/v3/puerto_rico/nsrdb_puerto_rico_2007.h5>


## Data format

The variables mentioned above are provided in two dimensional time-series arrays with dimensions (time x location). The temporal axis is defined by the `time_index` dataset, while the positional axis is defined by the `meta` dataset. For storage efficiency, each variable has been scaled and stored as an integer. The scale factor is provided in the `psm_scale-factor` attribute.  The units for each variable's data are also provided as an attribute (`psm_units`).


## Citation

Users of the NSRDB should please cite:

* [Sengupta MY, Xie A, Lopez A, Habte G, Maclaurin G, Shelby J.  The National Solar Radiation Data Base (NSRDB).  Renewable and Sustainable Energy Reviews  89 (June): 51-60. 2018.](https://www.sciencedirect.com/science/article/pii/S136403211830087X?via%3Dihub)


## Mounting the container

We also provide a read-only SAS (shared access signature) token to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://nrel.blob.core.windows.net/nrel-nsrdb?sv=2020-08-04&si=nrel-nsrdb-ro&sr=c&sig=H8GUesZmOXzMomMWdrnXQv2ZPI09hANqHIcVrP7Ejl0%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).


## Additional resources

* [NSRDB User's Manual](https://www.nrel.gov/docs/fy12osti/54824.pdf)
* [NSRDB documentation on GitHub](https://github.com/openEDI/documentation/blob/main/NSRDB.md)


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=nsrdb%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses * including direct, consequential, special, indirect, incidental, or punitive * resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
