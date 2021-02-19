### MODIS MCD43A4

#### Overview

Satellite imagery from the Moderate Resolution Imaging Spectroradiometer (MODIS).

[MODIS](https://modis.gsfc.nasa.gov/) provides Earth observation data in a wide spectral range, from 1999 to the present.  The MODIS satellites image the Earth every one to two days, though individual products derived from MODIS data may have lower temporal resolutions.  MODIS is administered by the [National Aeronautics and Space Administration](https://www.nasa.gov/) (NASA) and the [US Geological Survey](https://www.usgs.gov/) (USGS). We currently mirror the MCD43A4 (500m-resolution global daily surface reflectance) product on Azure dating back to 2000, and we will be on-boarding select additional MODIS products.

#### Storage resources

Data are stored in blobs in the East US data center, in the following blob container:

`https://modissa.blob.core.windows.net/modis`

Within that container, data are organized according to:

`[product]/[htile]/[vtile]/[daynum]/[filename]`

`product` is the MODIS product name; currently `MCD43A4` is available on Azure.

`htile` and `vtile` refer to tile numbers in the [MODIS sinusoidal grid system](https://modis-land.gsfc.nasa.gov/MODLAND_grid.html).  The notebook available under &ldquo;Data Access&rdquo; demonstrates one way to map latitude and longitude into this grid system.

`daynum` is a four-digit year plus a three-digit day of year (from 001 to 365), e.g. `2019001` represents January 1, 2019.

...for example, the folder:

`MCD43A4/00/08/2019010`

...contains images from Jan 10, 2019.

Images are stored in GeoTIFF format, with one image per MODIS channel.  The mapping from channels to spectral bands is product-specific; for MCD43A4, mappings are available [here](https://lpdaac.usgs.gov/products/mcd43a4v006/).

As per that document, spectral band 1 corresponds channel 7 for MCD43A4, so in the above directory, the file:

`MCD43A4.A2019001.h00v08.006.2019010201703.hdf_07.tiff`

...contains information from spectral band 1.

A complete Python example of accessing and plotting a MODIS image is available in the notebook provided under &ldquo;<a href="https://azure.microsoft.com/en-us/services/open-datasets/catalog/modis?tab=data-access">data access</a>&rdquo;.

We also provide a read-only SAS (shared access signature) token to allow access to MODIS data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`st=2019-07-26T22%3A24%3A15Z&se=2032-07-27T22%3A24%3A00Z&sp=rl&sv=2018-03-28&sr=c&sig=ENT24qUY%2BlxL93XMykFQwfq4ctHDPLmYPDaaAn7YI3Q%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

MODIS data can consume hundreds of terabytes, so large-scale processing is best performed in the East US Azure data center, where the images are stored.  If you are using MODIS data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


#### Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/modis.png" width=350px;><br/>

<p style="font-size:80%;margin-left:15px;">Imagery of the Chicago area on May 15, 2019.</p>


#### Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=modis%20question).


#### Notices

MICROSOFT PROVIDES AZURE OPEN DATASETS ON AN "AS IS" BASIS. MICROSOFT MAKES NO WARRANTIES, EXPRESS OR IMPLIED, GUARANTEES OR CONDITIONS WITH RESPECT TO YOUR USE OF THE DATASETS. TO THE EXTENT PERMITTED UNDER YOUR LOCAL LAW, MICROSOFT DISCLAIMS ALL LIABILITY FOR ANY DAMAGES OR LOSSES, INCLUDING DIRECT, CONSEQUENTIAL, SPECIAL, INDIRECT, INCIDENTAL OR PUNITIVE, RESULTING FROM YOUR USE OF THE DATASETS. 

This dataset is provided under the original terms that Microsoft received source data. The dataset may include data sourced from Microsoft. 


