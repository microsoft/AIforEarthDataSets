# Landsat 8 Collection 2 Level-2

## Overview

The [Landsat](https://landsat.gsfc.nasa.gov/) program has been imaging the Earth since 1972; it provides a comprehensive, continuous archive of the Earth's surface.

This dataset represents the global archive of Level-2 [Landsat 8](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-8) data from [Landsat Collection 2](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2).  Landsat 4, 5, and 7 data are in progress.  Because there is some latency before Level-2 data is available, a rolling window of recent Level-1 data is available as well.  Images are stored in [cloud-optimized GeoTIFF](https://www.cogeo.org/) format.

Landsat imagery is currently in preview on Azure; email [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=landsat%20question) to request access.


## Storage resources

### Container information

Data are stored in blobs in the West Europe Azure region, in the following blob container:

`https://landsateuwest.blob.core.windows.net/landsat-c2`


### Scene names

Within that container, each scene corresponds to a folder, named according to:

`[level]`/standard/`[sensor]`/`[year]`/`[path]`/`[row]`/[scene name]`

* `[level]` is "level-1" or "level-2"
* `[sensor]` is "oli-tirs" (Landsat 8), "etm" (Landsat 7), or "tm" (Landsat 4/5)
* `[year]` is a four-digit year
* `[path]` and `[row]` are three-digit codes representing path/row coordinates in the [Landsat Worldwide Reference System](https://landsat.gsfc.nasa.gov/about/worldwide-reference-system)

`scene name` follows the [Landsat Collection 2 scene name convention](https://www.usgs.gov/faqs/what-naming-convention-landsat-collection-2-level-1-and-level-2-scenes?qt-news_science_products=0#qt-news_science_products):

`LXSS_LLLL_PPPRRR_YYYYMMDD_yyyymmdd_CC_TX`

* `L` is always "L" for "Landsat"
* `X` is a sensor identifier ("C" for OLI/TIRS combined, "O" for OLI-only, "T" for TIRS-only, "E" for ETM+, "T" for TM, or "M" for MSS)
* `SS` is a satellite identifier ("04", "05", "07", or "08")
* `LLLL` is a [processing correction level](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-levels-processing) (L1TP/L1GT/L1GS for level-1 data, L2SP/L2SR for level-2 data)
* `PPP` is a [WRS](https://landsat.gsfc.nasa.gov/about/worldwide-reference-system) path
* `RRR` is a [WRS](https://landsat.gsfc.nasa.gov/about/worldwide-reference-system) row
* `YYYYMMDD` is the acquisition year, month, day
* `yyyymmdd` is the processing year, month, day
* `CC` is the collection number (always "02" in this dataset)
* `TX`is the [collection category](https://www.usgs.gov/media/videos/landsat-collections-what-are-tiers) ("RT" for real-time, "T1" for tier 1, or "T2" for tier 2)

Putting that all together, a complete scene folder for a Landsat 8 image from February 8, 2020 looks like:

`https://landsateuwest.blob.core.windows.net/landsat-c2/level-2/standard/oli-tirs/2020/011/021/LC08_L2SP_011021_20200208_20200823_02_T1/`

### Landsat 8 file names

#### Landsat 8 image files

Within each scene, Landsat 8 files follow the [Landsat 8-9 Collection 2 Level 2 specification](https://prd-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/atoms/files/LSDS-1328_Landsat8-9-OLI-TIRS-C2-L2-DFCB-v6.pdf); see the specification for complete documentation of both data and metadata.

This section will provide a short summary of the files within each scene folder.  All filenames are prefixed with the scene ID.

Listing *.tif will enumerate all images, with suffixes indicating bands according to the following:

* `B1`: Band 1 Visible (0.43-0.45 µm) 30m
* `B2`: Band 2 Visible (0.450-0.51 µm) 30m
* `B3`: Band 3 Visible (0.53-0.59 µm) 30m
* `B4`: Band 4 Red (0.64-0.67 µm) 30m
* `B5`: Band 5 Near-infrared (0.85-0.88 µm) 30m
* `B6`: Band 6 SWIR 1(1.57-1.65 µm) 30m
* `B7`: Band 7 SWIR 2 (2.11-2.29 µm) 30m
* `B8`: Band 8 Panchromatic (PAN) (0.50-0.68 µm) 15m (level-1 data only)
* `B10`: Band 10 TIRS 1 (10.6-11.19 µm) 100m (resampled to 30m)

* `B9`: Band 9 Cirrus (1.36-1.38 um) 30m (level-1 data only)
* `B11`: Band 11 TIRS 2 (11.50-12.51 µm) 100m (level-1 data only)

For example, the band 2 image in the example scene above is at:

`https://landsateuwest.blob.core.windows.net/landsat-c2/level-2/standard/oli-tirs/2020/011/021/LC08_L2SP_011021_20200615_20200823_02_T2/LC08_L2SP_011021_20200615_20200823_02_T2_SR_B2.TIF`

Level-2 files will end with "_SR_B[N]", indicating "surface reflectance"; level-1 files will end with just "_B[N].TIF".

Landsat 8 Level-2 scenes include the following derived images:

* `[sceneID]_ST_TRAD.tif`: thermal image
* `[sceneID]_ST_URAD.tif`: upwelled radiance image
* `[sceneID]_ST_ATRAN.tif`: atmospheric transmission image
* `[sceneID]_ST_CDIST.tif`: distance (in km) from each pixel to the nearest cloud pixel
* `[sceneID]_ST_DRAD.tif`: downwelled radiance image
* `[sceneID]_ST_EMIS.tif`: emissivity image
* `[sceneID]_ST_EMSD.tif`: emissivity standard deviation

#### Landsat 8 metadata files

* `[sceneID]_MTL.xml`: scene metadata file, in .xml format.  The metadata file includes, among other things, geometry information, a cloud cover percentage, information about sensor saturation, and radiance/reflectance calibration information.
* `[sceneID]_MTL.txt`: the same information in .txt format
* `[sceneID]_MTL.json`: the same information in .json format (level-2 only)
* `[sceneID]_ANG.txt`: [angular coefficients file](https://www.usgs.gov/faqs/what-landsat-collections-angle-coefficient-file-and-how-it-used?qt-news_science_products=0#), which allow users to compute solar and sensor viewing angles on a per-pixel basis 
* `[sceneID]_SR_stac.json`: [STAC](https://stacspec.org/) metadata for the surface reflectance product (level-2 only)
* `[sceneID]_ST_stac.json`: [STAC](https://stacspec.org/) metadata for the surface temperature product (level-2 only)

#### Landsat 8 quality assessment files

* `[sceneID]_QA_PIXEL.tif`: [quality assessment band](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-quality-assessment-bands)
* `[sceneID]_QA_RADSAT.tif`: [saturation quality assessment image](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-quality-assessment-bands), indicating which sensors were saturated on a per-pixel basis
* `[sceneID]_SR_QA_AEROSOL.tif`: [quality assessment band](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-quality-assessment-bands) indicating the aerosol correction applied in atmospheric correction (level-2 only)
* `[sceneID]_ST_QA.tif`: [quality assessment band](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-quality-assessment-bands) for the surface temperature products

#### Landsat 8 thumbnails

* `[sceneID]_thumb_large.jpeg`: large RGB thumbnail
* `[sceneID]_thumb_small.jpeg`: small RGB thumbnail


## Sample code

A complete Python example of accessing and plotting Landsat data - using the NASA CMR API to query for scenes of interest - is available in the notebook provided under the &ldquo;data access&rdquo; link.


## Region information

Large-scale processing is best performed in the West Europe Azure region, where the images are stored.  If you are using Landsat data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/landsat_800w.png" width=500px;><br/><span style='font-size:80%'>Natural-color rendering (Landsat 8 bands 4/3/2) of an area near Auckland, New Zealand.</span>


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=landsat%20question).


## Notices

MICROSOFT PROVIDES AZURE OPEN DATASETS ON AN "AS IS" BASIS. MICROSOFT MAKES NO WARRANTIES, EXPRESS OR IMPLIED, GUARANTEES OR CONDITIONS WITH RESPECT TO YOUR USE OF THE DATASETS. TO THE EXTENT PERMITTED UNDER YOUR LOCAL LAW, MICROSOFT DISCLAIMS ALL LIABILITY FOR ANY DAMAGES OR LOSSES, INCLUDING DIRECT, CONSEQUENTIAL, SPECIAL, INDIRECT, INCIDENTAL OR PUNITIVE, RESULTING FROM YOUR USE OF THE DATASETS. 

This dataset is provided under the original terms that Microsoft received source data. The dataset may include data sourced from Microsoft. 


