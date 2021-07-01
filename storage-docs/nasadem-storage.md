### COG files

Data are stored in blobs in the West Europe Azure region, in the following blob container:

`https://nasademeuwest.blob.core.windows.net/nasadem-cog`

Within that container, data are organized according to:

`v001/NASADEM_HGT_[lat_tile][lon_tile].tif`

`lat_tile` is a character ('n' or 's') plus a two-digit latitude value, derived from the latitude represented by each tile.  To find the latitude code for a given latitude, perform a floor() operation, then take the absolute value, then prefix with 'n' for positive latitudes (including zero) and 's' for negative latitudes, and zero-pad to two digits.  For example, the latitude 35.3606 becomes 'n35'.

`lon_tile` is a character ('e' or 'w') plus a three-digit longitude value, derived from the longitude represented by each tile.  To find the longitude code for a given longitude, perform a floor() operation, then take the absolute value, then prefix with 'e' for positive latitudes (including zero) and 'w' for negative latitudes, and zero-pad to three digits.  For example, the longitude 138.72 becomes 'e138'.

Images in this container are stored in [cloud-optimized GeoTIFF](https://www.cogeo.org/) format.

We also provide a read-only SAS (shared access signature) token to allow access to NASADEM data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2020-04-08&si=nasadem-cog-ro&sr=c&sig=RkEC4wi6sOdMEP6uj59wocpwiE4%2BBwrjt5qn5lEFov8%3D`

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

We also provide a read-only SAS (shared access signature) token to allow access to NASADEM data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2019-12-12&si=nasadem-ro&sr=c&sig=6rAbZIvIjQVTov2bGUpqH9T0fzTipRahkooOSf2XCuo%3D`

A full list of NetCDF files is available [here](https://nasademeuwest.blob.core.windows.net/nasadem-nc/v001/index/nasadem_file_list.txt).