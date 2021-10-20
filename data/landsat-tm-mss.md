# Landsat TM and MSS Collection 2

## Overview

The [Landsat](https://landsat.gsfc.nasa.gov/) program has been imaging the Earth since 1972; it provides a comprehensive, continuous archive of the Earth's surface.

This dataset represents the global archive of data from the [thematic mapper](https://landsat.gsfc.nasa.gov/landsat-4-5/tm) (TM) and [multispectral spanner system](https://landsat.gsfc.nasa.gov/multispectral-scanner-system) (MSS) instruments that were carried aboard the [Landsat 1](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-1), [Landsat 2](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-2), [Landsat 3](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-3), [Landsat 4](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-4) and [Landsat 5](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-5) satellites.  MSS data represent the period from 1972-2013 (Landsat 1-5), at 80m resolution.  TM data represent the period from 1982-2012 (Landsat 4-5), at 30m resolution.

Landsat imagery is currently in preview on Azure; email [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=landsat%20question) to request access.


## Storage resources

### Container information

Data are stored in blobs in the West Europe Azure region, in the following blob container:

`https://landsateuwest.blob.core.windows.net/landsat-c2`


### Scene names

Within that container, each scene corresponds to a folder, named according to:

`[level]`/standard/`[sensor]`/`[year]`/`[path]`/`[row]`/[scene name]`

* `[level]` is a processing level ("level-1" or "level-2", always "level-2" for TM data and "level-1" for MSS data)
* `[sensor]` is one of "mss" (Landsat 1-4), "tm" (Landsat 4-5), "etm" (Landsat 7), or "oli-tirs" (Landsat 8), (always "tm" or "mss" for this collection)
* `[year]` is a four-digit year
* `[path]` and `[row]` are three-digit codes representing path/row coordinates in the [Landsat Worldwide Reference System](https://landsat.gsfc.nasa.gov/about/worldwide-reference-system)

`scene name` follows the [Landsat Collection 2 scene name convention](https://www.usgs.gov/faqs/what-naming-convention-landsat-collection-2-level-1-and-level-2-scenes?qt-news_science_products=0#qt-news_science_products):

`LXSS_LLLL_PPPRRR_YYYYMMDD_yyyymmdd_CC_TX`

* `L` is always "L" for "Landsat"
* `X` is a sensor identifier ("C" for OLI/TIRS combined, "O" for OLI-only, "T" for TIRS-only, "E" for ETM+, "T" for TM, or "M" for MSS)
* `SS` is a satellite identifier ("01", "02", "03", "04", "05", "07", or "08")
* `LLLL` is a [processing correction level](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-levels-processing) (L1TP/L1GT/L1GS for level-1 data, L2SP/L2SR for level-2 data)
* `PPP` is a [WRS](https://landsat.gsfc.nasa.gov/about/worldwide-reference-system) path
* `RRR` is a [WRS](https://landsat.gsfc.nasa.gov/about/worldwide-reference-system) row
* `YYYYMMDD` is the acquisition year, month, day
* `yyyymmdd` is the processing year, month, day
* `CC` is the collection number (always "02" in this dataset)
* `TX`is the [collection category](https://www.usgs.gov/media/videos/landsat-collections-what-are-tiers) ("RT" for real-time, "T1" for tier 1, or "T2" for tier 2)

Putting that all together, a complete scene folder for a Landsat 1 MSS image from Nov 22, 1972 looks like:

`https://landsateuwest.blob.core.windows.net/landsat-c2/level-1/standard/mss/1972/004/026/LM01_L1TP_004026_19721122_20200909_02_T2/`

...and a complete scene folder for a Landsat 4 TM image from September 16, 1982 looks like:

`https://landsateuwest.blob.core.windows.net/landsat-c2/level-2/standard/tm/1982/006/027/LT04_L2SP_006027_19820916_20200918_02_T2/`


### MSS file names

#### MSS image files

MSS files follow the [Landsat Level-1 naming convention](https://www.usgs.gov/faqs/what-naming-convention-landsat-collections-level-1-scenes); see the specification for complete documentation of both data and metadata.  The level-1 convention is the same for Collection 1 and Collection 2 data.

This section will provide a short summary of the files within each scene folder.  All filenames are prefixed with the scene ID.

Listing *.tif will enumerate all images, with suffixes indicating bands according to the following:

* `B4`: Band 4 Visible green (0.5-0.6um) 80m
* `B5`: Band 5 Visible red (0.6-0.7um) 80m
* `B6`: Band 6 Near infrared (0.7-0.8um) 80m
* `B7`: Band 7 Near infrared (0.8-1.1um) 80m

For all missions:

* `QA_PIXEL.tif`: [quality assessment band](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-quality-assessment-bands)
* `QA_RADSAT.tif`: [saturation quality assessment image](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-quality-assessment-bands), indicating which sensors 

For example, the band 4 image in the example Landsat 1 MSS scene from above is at:

`https://landsateuwest.blob.core.windows.net/landsat-c2/level-1/standard/mss/1972/004/026/LM01_L1TP_004026_19721122_20200909_02_T2/LM01_L1TP_004026_19721122_20200909_02_T2_B4.TIF`

#### MSS metadata files

* `[sceneID]_MTL.xml`: scene metadata file, in .xml format.  The metadata file includes, among other things, geometry information, a cloud cover percentage, information about sensor saturation, and radiance/reflectance calibration information.
* `[sceneID]_MTL.txt`: the same information in .txt format
* `[sceneID]_MTL.json`: the same information in .json format 
* `[sceneID]_GCP.txt`: ground control point verification file ([specification](https://prd-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/atoms/files/LSDS-286_LandsatMSS-Level1_DFCB-v11.pdf))

#### MSS thumbnails

* `[sceneID]_thumb_large.jpeg`: large RGB thumbnail
* `[sceneID]_thumb_small.jpeg`: small RGB thumbnail


### TM file names

#### TM image files

TM files follow the [Landsat Collection 2 Level-2 naming convention](https://www.usgs.gov/faqs/what-naming-convention-landsat-collection-2-level-1-and-level-2-scenes); see the specification for complete documentation of both data and metadata.

This section will provide a short summary of the files within each scene folder.  All filenames are prefixed with the scene ID.

Listing *.tif will enumerate all images, with suffixes indicating bands according to the following:

* `B1`: Band 1 Visible blue (0.45-0.52um) 30m
* `B2`: Band 2 Visible green (0.52-0.60um) 30m
* `B3`: Band 3 Visible red (0.63-0.69um) 30m
* `B4`: Band 4 Near infrared (0.77-0.90um) 30m
* `B5`: Band 5 Short-wave infrared (1.55-1.75um) 30m
* `B6`: Band 6 Thermal infrared (10.40-12.50um) 30m
* `B7`: Band 7 Short-wave infrared (2.09-2.35um) 30m

For all missions:

* `QA_PIXEL.tif`: [quality assessment band](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-quality-assessment-bands)
* `QA_RADSAT.tif`: [saturation quality assessment image](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-quality-assessment-bands), indicating which sensors 

For example, the band 1 image in the example Landsat 4 TM scene from above is at:

`https://landsateuwest.blob.core.windows.net/landsat-c2/level-2/standard/tm/1982/006/027/LT04_L2SP_006027_19820916_20200918_02_T2/LT04_L2SP_006027_19820916_20200918_02_T2_SR_B4.TIF`

Level-2 filenames end with "_SR_B[N]", indicating "surface reflectance".

Landsat 4-5 Level-2 scenes include the following derived images:

* `[sceneID]_ST_TRAD.tif`: thermal image
* `[sceneID]_ST_URAD.tif`: upwelled radiance image
* `[sceneID]_ST_ATRAN.tif`: atmospheric transmission image
* `[sceneID]_ST_CDIST.tif`: distance (in km) from each pixel to the nearest cloud pixel
* `[sceneID]_ST_DRAD.tif`: downwelled radiance image
* `[sceneID]_ST_EMIS.tif`: emissivity image
* `[sceneID]_ST_EMSD.tif`: emissivity standard deviation
* `[sceneID]_SR_ATMOS_OPACITY.tif`: atmospheric opacity

#### TM metadata files

* `[sceneID]_MTL.xml`: scene metadata file, in .xml format.  The metadata file includes, among other things, geometry information, a cloud cover percentage, information about sensor saturation, and radiance/reflectance calibration information.
* `[sceneID]_MTL.txt`: the same information in .txt format
* `[sceneID]_MTL.json`: the same information in .json format 
* `[sceneID]_ANG.txt`: [angular coefficients file](https://www.usgs.gov/faqs/what-landsat-collections-angle-coefficient-file-and-how-it-used?qt-news_science_products=0#), which allow users to compute solar and sensor viewing angles on a per-pixel basis 

#### TM thumbnails

* `[sceneID]_thumb_large.jpeg`: large RGB thumbnail
* `[sceneID]_thumb_small.jpeg`: small RGB thumbnail


## Sample code

A complete Python example of accessing and plotting Landsat data - using the NASA CMR API to query for scenes of interest - is available in the accompanying [sample notebook](landsat-tm-mss.ipynb).


## Region information

Large-scale processing is best performed in the West Europe Azure region, where the images are stored.  If you are using Landsat data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/landsat_tm_thumb.png" style="width:500px;"><br/><span style='font-size:80%'>Natural-color rendering (Landsat 4 bands 3/2/1) of an area near Auckland, New Zealand, in June 1989.</span>


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=landsat%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.

