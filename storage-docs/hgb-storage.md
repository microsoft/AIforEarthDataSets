Data are stored in blobs in the West Europe Azure region, in the following blob folder:

`https://cpdataeuwest.blob.core.windows.net/cpdata/raw/2010-harmonized-biomass/global/300m/`

Within that folder, there are four [cloud-optimized GeoTIFF](https://www.cogeo.org/) files:

* aboveground.tif (global above-ground biomass)
* belowground.tif (global below-ground biomass)
* aboveground_uncertainty.tif (uncertainty associated with global above-ground biomass)
* belowground_uncertainty.tif (uncertainty associated with global below-ground biomass)

We also provide a read-only SAS (<a href="https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview">shared access signature</a>) token to allow access to this data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2019-12-12&si=cpdata-ro&sr=c&sig=tqRGrmdYYa9WYkaPi0wWOD0nalRdNGTZNe97GL2enDA%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing is best performed in the West Europe Azure data center, where the data are 
