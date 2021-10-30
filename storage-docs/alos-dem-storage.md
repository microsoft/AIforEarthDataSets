COG files are stored in blobs in the West Europe Azure region, in the following blob container:

`https://ai4edataeuwest.blob.core.windows.net/alos-dem`

Within that container, data are named according to:

`AW3D30_globa/ALPSMLC30_[latitude-string][longitude-string]_DSM.tif`

* `latitude-string` specifies the lower latitude bound of the tile, as [N|S]nnn, e.g. "N016" or "001"
* `longitude-string` specifies the lower longitude bound of the tile, as [W|E]nnn, e.g. "W011" or "E020"

For example, the following file:

<https://ai4edataeuwest.blob.core.windows.net/alos-dem/AW3D30_global/ALPSMLC30_N015W011_DSM.tif>

...contains data for the tile whose lower latitude bound is 15 degrees, and whose lower longitude bound is -11 degrees.