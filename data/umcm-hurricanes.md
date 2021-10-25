# University of Miami Coupled Model (UMCM) for Hurricanes Ike and Sandy

## Overview

The University of Miami Coupled Model (UMCM) is a coupled model that integrates atmospheric, wave, and ocean components to produce wind, wave, and current data. Atmospheric data is produced using the [Weather Research and Forecasting](https://www.mmm.ucar.edu/weather-research-and-forecasting-model) model (WRF), wave data is produced using the [University of Miami Wave Model](https://umwm.org/) (UMWM), and ocean current data is produced using the
[Hybrid Coordinate Ocean Model](https://www.hycom.org/) (HYCOM).

The model was used to study offshore wind conditions during [Hurricane Ike](https://en.wikipedia.org/wiki/Hurricane_Ike) and [Hurricane Sandy](https://en.wikipedia.org/wiki/Hurricane_Sandy); this dataset - provided by the [Open Energy Data Initiative](https://openei.org/wiki/Open_Energy_Data_Initiative_(OEDI)) (OEDI) - represents the output of that modeling run.

## Model information

The time resolution for each model run is as follows:

* Hurricane Ike
  * 1 sample/hour from 9/8/2008 12:00:00 UTC to 9/12/2008 6:00:00 UTC
  * 1 sample/10 minutes from 9/12/2008 6:00:00 UTC to 9/13/2008 9:00:00 UTC
* Hurricane Sandy
  * 1 sample/10 minutes from 10/28/2012 00:10:00 UTC to 10/31/2012 00:00:00 UTC

The following variables were extracted from the HYCOM model:

* bathymetry
* ocean_mixed_layer_thickness-ilt
* ocean_mixed_layer_thickness-mlt
* sea_water_potential_density at all depths
* sea_water_salinity at all depths
* sea_surface_elevation
* eastward_sea_water_velocity
* northward_sea_water_velocity
* upward_sea_water_velocity
* sea_water_temperature
* depth

The following variables were extracted from the WRF and UMWM models:

* cd
* cgmxx
* cgmxy
* cgmyy
* dcg
* dcg0
* dcp
* dcp0
* depth
* dwd
* dwl
* dwp
* momx
* momy
* mss
* mwd
* mwl
* mwp
* rhoa
* rhow
* seamask
* swh
* tailatmx
* tailatmy
* tailocnx
* tailocny
* taux_bot
* taux_form
* taux_form_1
* taux_form_2
* taux_form_3
* taux_ocn
* taux_skin
* taux_snl
* tauy_bot
* tauy_form
* tauy_form_1
* tauy_form_2
* tauy_form_3
* tauy_ocn
* tauy_skin
* tauy_snl
* u_stokes at all depths
* uc
* ust
* v_stokes at all depths
* vc
* wdir
* wspd

## Storage resources

The UMCM data is stored in HDF format in Azure Blob Storage in the East US Azure region, in the following folder:

`https://nrel.blob.core.windows.net/oedi/umcm/`

The primary files, containing temporally and spatially coherent time-series data for each hurricane are:

* <https://nrel.blob.core.windows.net/oedi/umcm/ike.h5> (for Hurricane Ike)
* <https://nrel.blob.core.windows.net/oedi/umcm/sandy.h5> (for Hurricane Sandy)

Raw output from the HYCOM, UMWM, and WRF models are available in the folders:

`https://nrel.blob.core.windows.net/oedi/umcm/[hurricane]/[model]`

* `hurricane` is one of "ike" or "sandy"
* `model` is one of "hycom", "umwm", or "wrf"

## Data Format

The UMCM data is stored in HDF datasets by variable and depth (when available).  Each dataset is composed of a 3D data cube with dimensions (time, latitude, longitude). The positional values of each dimension are available in the datasets:

* `time_index`
* `latitude`
* `longitude`

Additional location metadata is available in the `meta` table.

## Mounting the container

We also provide a read-only SAS (shared access signature) token to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://nrel.blob.core.windows.net/oedi?sv=2020-08-04&si=oedi-ro&sr=c&sig=O%2BQvKRV9uYuK36WzVRoCJdFO%2BRifXO8aIGqbS%2F3llPs%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).


## Citation

Users of the UMCM model data should cite the following:

* [Kim E, Manuel L, Curcic M, Chen SS, Phillips C, Veers P.  On the Use of Coupled Wind, Wave, and Current Fields in the Simulation of Loads on BottomSupported Offshore Wind Turbines during Hurricanes (Technical Report, NREL/TP-5000-65283), Golden, CO: National Renewable Energy Laboratory. 2016.](https://www.nrel.gov/docs/fy16osti/65283.pdf)


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=nlcd%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
