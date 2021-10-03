# ASTER L1T

## Overview

The [ASTER](https://terra.nasa.gov/about/terra-instruments/aster) instrument, launched on-board NASA's [Terra](https://terra.nasa.gov/) satellite in 1999, provides multispectral images of the Earth at 15m-90m resolution.  ASTER images provide information about land surface temperature, color, elevation, and mineral composition.

This dataset represents ASTER [L1T](https://lpdaac.usgs.gov/products/ast_l1tv003/) data from 2000-2006.  L1T images have been terrain-corrected and rotated to a north-up UTM projection.  Data are in [cloud-optimized GeoTIFF](https://www.cogeo.org/) format.


## Storage resources

### Container information

Data are stored in blobs in the West Europe Azure region, in the following blob container:

`https://astersa.blob.core.windows.net/aster`


### Scene names

Within the COG container, each scene corresponds to a prefix, named according to:

images/L1T/`[year]`/`[month]`/`[day]`/`[scene name]`

`[year]`, `[month]`, and `[day]` are the four-digit year and two-digit month/day.

`scene name` follows the [ASTER naming convention](https://lpdaac.usgs.gov/data/get-started-data/collection-overview/missions/aster-overview/#aster-naming-conventions):

AST_L1T<span style="background-color:#aaffff;">VVV</span><span style="background-color:#ffaaff;">YYYYMMDHHMMSS</span>_<span style="background-color:#ffffaa;">yyyymmddhhmmss</span>_<span style="background-color:#dddddd;">id</span>

* `VVV` is always "003", for ASTER collection 003
* `MMDDYYYYHHMMSS` is the acquisition month, day, year, hour, minute, second	
* `mmddyyyyhhmmss` is the processing month, day, year, hour, minute, second
* `id` is a unique acquisition identifier.

For example:

`AST_L1T_00306042003004247_20150428235500_35366`

Putting that all together, a complete scene prefix for an ASTER image from June 4, 2003 looks like:

`https://astersa.blob.core.windows.net/aster/images/L1T/2003/06/04/AST_L1T_00306042003004247_20150428235500_35366`


### Image files

All scenes contain one or more of the following files (not all bands are present in all ASTER scenes), separated from the prefix with ".":

* SWIR.tif (ASTER shortwave infrared bands 4, 5, 6, 7, 8, and 9; at 30m resolution)
* VNIR.tif (ASTER visible and near-infrared bands 1, 2, and 3; at 15m resolution)
* TIR.tif (ASTER thermal infrared bands 10, 11, 12, 13, and 14; at 90m resolution)

So, for example, the VNIR COG file for the example scene above is available at:

https://astersa.blob.core.windows.net/aster/images/L1T/2003/06/04/AST_L1T_00306042003004247_20150428235500_35366.VNIR.tif


## Authentication

We also provide a read-only SAS (<a href="https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview">shared access signature</a>) token to allow access to NAIP data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2020-04-08&si=aster-ro&sr=c&sig=sXo9shWJec3H6ezpLPuYo7gVpM%2Bj0jLL0fa7jv%2FUe1M%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).


## Sample code

A complete Python example of accessing and plotting ASTER data - using the NASA CMR API to query for scenes of interest - is available in the accompanying [sample notebook](aster.ipynb).


## Region information

Large-scale processing is best performed in the West Europe Azure region, where the images are stored.  If you are using ASTER data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/aster_800w.png" style="width:500px;">
<br/>
<span style='font-size:80%'>False-color composite (ASTER VNIR bands 3/2/1) of an area near Suruga Bay, Japan.</span>


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=aster%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
