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

We also provide a read-only SAS (<a href="https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview">shared access signature</a>) token to allow access to this data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2019-12-12&si=cpdata-ro&sr=c&sig=tqRGrmdYYa9WYkaPi0wWOD0nalRdNGTZNe97GL2enDA%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing is best performed in the West Europe Azure data center, where the data are stored.  If you are using this data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.