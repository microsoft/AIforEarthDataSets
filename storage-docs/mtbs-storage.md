Data are stored in blobs in the West Europe Azure region, in the following blob folder:

`https://cpdataeuwest.blob.core.windows.net/cpdata/raw/mtbs`

Within that container, data are organized according to:

[region]/30m/severity/[year].tif

`region` is the spatial domain; currently `conus` or `ak`.

`year` is four digit year (e.g. 2017).

Images are stored in cloud optimized GeoTIFF format.

We also provide an API to get read-only SAS (shared access signature) tokens to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://planetarycomputer.microsoft.com/api/sas/v1/token/cpdataeuwest/cpdata`

API documentation is at `https://planetarycomputer.microsoft.com/api/sas/v1/docs`.
Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing is best performed in the West Europe Azure data center, where the data are 
