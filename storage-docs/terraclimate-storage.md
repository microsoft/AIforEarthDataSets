Data are stored in blobs in the West Europe Azure region, in the following folder:

`https://cpdataeuwest.blob.core.windows.net/cpdata/raw/terraclimate/4000m/raster.zarr`

Data are stored in [Zarr](https://zarr.readthedocs.io/en/stable/) format, indexed by latitude, longitude, and time.  The following variables are available:

* `aet` (actual evapotransporation)
* `def` (climatic water deficit)
* `pdsi` (Palmer Drought Severity Index)
* `pet` (reference evapotransporation)
* `ppt` (acculumated precipitation)
* `ppt_station_influence` (number of stations used for ppt)
* `q` (runoff)
* `soil` (soil moisture at end of month)
* `srad` (downward shortwave radiance flux at the surface)
* `swe` (snow water equivalent at end of month)
* `tmax` (maximum 2m temperature)
* `tmax_station_influence` (number of stations used for tmax)
* `tmin` (minimum 2m temperature)
* `tmin_station_influence` (number of stations used for tmin)
* `vap` (2m vapor pressure)
* `vap_station_influence` (number of stations used for vap)
* `vpd` (vapor pressure deficit)
* `ws` (10m wind speed)

We also provide an API to get read-only SAS (shared access signature) tokens to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://planetarycomputer.microsoft.com/api/sas/v1/token/cpdataeuwest/cpdata`

API documentation is at `https://planetarycomputer.microsoft.com/api/sas/v1/docs`.
Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing is best performed in the West Europe Azure data center, where the data are 
