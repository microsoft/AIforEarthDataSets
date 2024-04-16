Data are stored in blobs in the West Europe Azure region, in the following blob folder:

`https://cpdataeuwest.blob.core.windows.net/cpdata/raw/2010-harmonized-biomass/global/300m/`

Within that folder, there are four [cloud-optimized GeoTIFF](https://www.cogeo.org/) files:

* aboveground.tif (global above-ground biomass)
* belowground.tif (global below-ground biomass)
* aboveground_uncertainty.tif (uncertainty associated with global above-ground biomass)
* belowground_uncertainty.tif (uncertainty associated with global below-ground biomass)

We also provide an API to get read-only SAS (shared access signature) tokens to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://planetarycomputer.microsoft.com/api/sas/v1/token/cpdataeuwest/cpdata`

API documentation is at `https://planetarycomputer.microsoft.com/api/sas/v1/docs`.
Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing is best performed in the West Europe Azure data center, where the data are 
