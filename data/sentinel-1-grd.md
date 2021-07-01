# Sentinel-1 GRD

## Overview

The [Sentinel-1](https://sentinel.esa.int/web/sentinel/missions/sentinel-1) program provides global synthetic aperature radar imaging with a revisit time of approximately six days.  The [Ground Range Detected](https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-1-sar/products-algorithms/level-1-algorithms/ground-range-detected) (GRD) product has been detected and projected to ground range.

This dataset represents the global Sentinel-1 GRD archive, from 2017 to the present, converted to [cloud-optimized GeoTIFF](https://www.cogeo.org/) format.

Sentinel-1 data on Azure are maintained by [Sinergise](https://sinergise.com/).

Sentinel-1 GRD imagery is currently in preview on Azure; email [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=sentinel1%20question) to request access.


## Storage resources

### Container information

Data are stored in blobs in the West Europe Azure region, in the following blob container:

`https://sentinel1euwest.blob.core.windows.net/s1-grd`


### Scene names

Within that container, each scene corresponds to a folder, named according to:

`GRD/[year]/[month]/[day]/[acquisition-mode]/[polarization]/[scene_name]`

* `year` is a four-digit year
* `month` is the 1-indexed, non-zero-padded month
* `day` is the 1-indexed, non-zero-padded day
* `acquisition-mode` is the [acquisition mode](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/acquisition-modes) for this scene, one of IW (interferometric wide swath), SM (stripmap), EW (extra-wide swath), or WV (wave)
* `polarization` is the [polarization mode](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-1-sar/product-overview/polarimetry) for this scene, typically one of SH (single HH), SV (single VV), DH (dual HH+HV), or DV (dual VV+VH); HH, HV, VV, and VH also occur

`scene name` follows the [Sentinel-1 scene name convention](https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-1-sar/products-algorithms/level-1-product-formatting):

`MMM_BB_TTTR_LFPP_YYYYMMDDTHHMMSS_YYYYMMDDYHHMMSS_OOOOOO_DDDDDD_CCCC`

* `MMM` is satellite (S1A or S1B)
* `BB` is the acquisition mode
* `TTT` is the product type (always `GRD` in this data set)
* `L` is the processing level (always `1` in this data set)
* `F` is the product class (always `S` (for "SAR standard") in this dataset)
* `PP` is the polarization (SH, SV, DH, DV, HH, HV, VV, or VH)
* `YYYYMMDDTHHMMSS_YYYYMMDDTHHMMSS` is the scene start and stop capture time
* `OOOOOO` is an absolute orbit number
* `DDDDDD` is the "mission data take identifier" 
* `CCCC` is a checksum

Putting that all together, a complete scene folder looks like:

`https://sentinel1euwest.blob.core.windows.net/s1-grd/GRD/2021/1/29/IW/DV/S1B_IW_GRDH_1SDV_20210129T020125_20210129T020150_025363_030553_F429`

### Image files

Within a scene folder, recursively listing *.tiff will enumerate all images; all of these files will be within the `measurement` folder.  For example, for an IW-mode, DV-polarized image:

* `measurement/iw-vh.tiff`
* `measurement/iw-vv.tiff`

For example, the iw-vh image for the example scene above is at:

`https://sentinel1euwest.blob.core.windows.net/s1-grd/GRD/2021/1/29/IW/DV/S1B_IW_GRDH_1SDV_20210129T020125_20210129T020150_025363_030553_F429/measurement/iw-vh.tiff`

### Metadata files

Metadata files follow the [Sentinel-1 product specification](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/document-library/-/asset_publisher/1dO7RF5fJMbd/content/sentinel-1-product-specification); see the specification for complete documentation of both data and metadata.

This section will provide a short summary of each file within each scene folder.

* `manifest.safe`: index file listing all files in this scene and their checksums... basically the machine-readable version of this section of the documentation.
* `productInfo.json`: .json-formatted scene metadata, with footprint information and a list of available files
* `preview/product-preview.html`: index file listing all files in this scene, along with a thumbnail
* `preview/quick-look.png`: a handy thumbnail for this scene
* `preview/map-overlay.html`: kml-formatted scene footprint
* `annotation/*.xml`: metadata associated with the GRD production (detection, projection)


## Sample code

A complete Python example of accessing and plotting Sentinel-1 GRD data - using the Copernicus Open Access Hub API to query for scenes of interest - is available in the accompanying [sample notebook](sentinel-1-grd.ipynb).


## Region information

Large-scale processing is best performed in the West Europe Azure region, where the images are stored.  If you are using Sentinel-1 data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/sentinel-1-grd.png" width=500px;><br/><span style='font-size:80%'>False color rendering of Sentinel-1 GRD data near Seattle, WA, USA.</span>


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=sentinel-1%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.

