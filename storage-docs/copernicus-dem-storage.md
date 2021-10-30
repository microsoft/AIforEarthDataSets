COG files are stored in blobs in the West Europe Azure region, in the following blob container:

`https://elevationeuwest.blob.core.windows.net/copernicus-dem`

Within that container, data are named according to:

`COP[resolution-m]_hh/Copernicus_DSM_COG_[resolution-arc]_[latitude-string]_00_[longitude-string]_00_DEM.tif`

* `resolution-m` is the data set resolution in meters (30 for the 30m dataset, 90 for the 90m dataset)
* `resolution-arc` is the data set resolution in arc-seconds (10 for the 30m dataset, 30 for the 90m dataset)
* `latitude-string` specifies the lower latitude bound of the tile, as [N|S]nn, e.g. "N03" or "S87"
* `longitude-string` specifies the lower longitude bound of the tile, as [W|E]nnn, e.g. "W160" or "E059"

For example, the following file:

<https://elevationeuwest.blob.core.windows.net/copernicus-dem/COP30_hh/Copernicus_DSM_COG_10_N03_00_W160_00_DEM.tif>

...contains 30m-resolution data for the tile whose lower latitude bound is +3.0 degrees, and whose lower longitude bound is -160.0 degrees.