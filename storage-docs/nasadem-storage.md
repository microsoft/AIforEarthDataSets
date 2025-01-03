### COG files

Data are stored in blobs in the West Europe Azure region, in the following blob container:

`https://nasademeuwest.blob.core.windows.net/nasadem-cog`

Within that container, data are named according to:

`v001/NASADEM_HGT_[lat_tile][lon_tile].tif`

`lat_tile` is a character ('n' or 's') plus a two-digit latitude value, derived from the latitude represented by each tile.  To find the latitude code for a given latitude, perform a floor() operation, then take the absolute value, then prefix with 'n' for positive latitudes (including zero) and 's' for negative latitudes, and zero-pad to two digits.  For example, the latitude 35.3606 becomes 'n35'.

`lon_tile` is a character ('e' or 'w') plus a three-digit longitude value, derived from the longitude represented by each tile.  To find the longitude code for a given longitude, perform a floor() operation, then take the absolute value, then prefix with 'e' for positive latitudes (including zero) and 'w' for negative latitudes, and zero-pad to three digits.  For example, the longitude 138.72 becomes 'e138'.

Images in this container are stored in [cloud-optimized GeoTIFF](https://www.cogeo.org/) format.

We also provide an API to get read-only SAS (shared access signature) tokens to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://planetarycomputer.microsoft.com/api/sas/v1/token/nasademeuwest/nasadem-cog`

API documentation is at `https://planetarycomputer.microsoft.com/api/sas/v1/docs`.
A full list of COG files is available [here](https://nasademeuwest.blob.core.windows.net/nasadem-cog/v001/index/nasadem_cog_list.txt).


### NetCDF files

Data are stored in blobs in the West Europe Azure region, in the following blob container:

`https://nasademeuwest.blob.core.windows.net/nasadem-nc`

Within that container, data are organized according to:

`v001/NASADEM_NC_[lat_tile][lon_tile].[extension]`

`lat_tile` and `lon_tile` are as per above.

For each tile, filenames with three extensions are present:

* 1.jpg (a preview image)
* nc (the data itself)
* nc.xml (tile creation metadata)

Images in this container are stored in [NetCDF](https://en.wikipedia.org/wiki/NetCDF) format.

We also provide an API to get read-only SAS (shared access signature) tokens to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://planetarycomputer.microsoft.com/api/sas/v1/token/nasademeuwest/nasadem-nc`

API documentation is at `https://planetarycomputer.microsoft.com/api/sas/v1/docs`.
A full list of NetCDF files is available [here](https://nasademeuwest.blob.core.windows.net/nasadem-nc/v001/index/nasadem_file_list.txt).