# ASTER L1T

## Overview

The [ASTER](https://terra.nasa.gov/about/terra-instruments/aster) instrument, launched on-board NASA's [Terra](https://terra.nasa.gov/) satellite in 1999, provides multispectral images of the Earth at 15m-90m resolution.  ASTER images provide information about land surface temperature, color, elevation, and mineral composition.

This dataset represents ASTER [L1T](https://lpdaac.usgs.gov/products/ast_l1tv003/) data from 2000-2006.  L1T images have been terrain-corrected and rotated to a north-up UTM projection.

Data are in [cloud-optimized GeoTIFF](https://www.cogeo.org/) format; the original HDF files are temporarily available as well, but will not be maintained permanently.

ASTER imagery is currently in preview on Azure; email [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=aster%20question) to request access.


## Storage resources

### Container information

Data are stored in blobs in the West Europe Azure region, in the following blob container:

`https://astersa.blob.core.windows.net/aster-cogs`

HDF files are temporarily available in the following blob container:

`https://astersa.blob.core.windows.net/aster`


### Scene names

Within the COG container, each scene corresponds to a folder, named according to:

images/L1T/`[year]`/`[month]`/`[day]`/`[scene name]`

* `[year]`, `[month]`, and `[day]` are the four-digit year and two-digit month/day

`scene name` follows the [ASTER naming convention](https://lpdaac.usgs.gov/data/get-started-data/collection-overview/missions/aster-overview/#aster-naming-conventions), with the exception that the "AST_L1T" prefix has been removed.  So scene names look like:

<span style="background-color:#aaffff;">VVV</span><span style="background-color:#ffaaff;">YYYYMMDHHMMSS</span>_<span style="background-color:#ffffaa;">yyyymmddhhmmss</span>_<span style="background-color:#dddddd;">id</span>

* `VVV` is always "003", for ASTER collection 003
* `MMDDYYYYHHMMSS` is the acquisition month, day, year, hour, minute, second	
* `mmddyyyyhhmmss` is the processing month, day, year, hour, minute, second
* `id` is a unique acquisition identifier.

For example:

`00306042003004247_20150428235500_35366`

Putting that all together, a complete scene folder for an ASTER image from June 4, 2003 looks like:

`https://astersa.blob.core.windows.net/aster-cogs/images/L1T/2003/06/04/00306042003004247_20150428235500_35366/`


### ASTER image files

Documentation pending finalization of the still-provisional COG format.


## Sample code

A complete Python example of accessing and plotting ASTER data - using the NASA CMR API to query for scenes of interest - is available in the notebook provided under the &ldquo;data access&rdquo; link.


## Region information

Large-scale processing is best performed in the West Europe Azure region, where the images are stored.  If you are using ASTER data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/aster.png" width=350px;><br/>

<p style="font-size:80%;margin-left:15px;">A <i>mostly</i> cloudless day in Seattle.</p>


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=aster%20question).


## Notices

MICROSOFT PROVIDES AZURE OPEN DATASETS ON AN "AS IS" BASIS. MICROSOFT MAKES NO WARRANTIES, EXPRESS OR IMPLIED, GUARANTEES OR CONDITIONS WITH RESPECT TO YOUR USE OF THE DATASETS. TO THE EXTENT PERMITTED UNDER YOUR LOCAL LAW, MICROSOFT DISCLAIMS ALL LIABILITY FOR ANY DAMAGES OR LOSSES, INCLUDING DIRECT, CONSEQUENTIAL, SPECIAL, INDIRECT, INCIDENTAL OR PUNITIVE, RESULTING FROM YOUR USE OF THE DATASETS. 

This dataset is provided under the original terms that Microsoft received source data. The dataset may include data sourced from Microsoft. 


