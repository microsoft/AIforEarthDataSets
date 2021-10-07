# Sentinel-1 SLC

## Overview

The [Sentinel-1](https://sentinel.esa.int/web/sentinel/missions/sentinel-1) program provides global synthetic aperture radar imaging with a revisit time of approximately six days.  The [Single Look Complex](https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-1-sar/products-algorithms/level-1-algorithms/single-look-complex) (SLC) product includes images in the slant range, in the plane in which images are acquired.

This dataset represents the most recent 90 days of the Sentinel-1 SLC archive, in the [SAFE](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/data-formats/safe-specification) format in which images are provided by the European Space Agency.

Sentinel-1 data on Azure are maintained by [Sinergise](https://sinergise.com/).

Sentinel-1 SLC data is currently in preview on Azure; email [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=sentinel1%20question) to request access.

We also maintain a complete archive of Sentinel-1 GRD data, in cloud-optimized format; see the [GRD documentation](https://aka.ms/ai4edata-sentinel-1).

## Storage resources

### Container information

Data are stored in blobs in the West Europe Azure region, in the following blob container:

`https://sentinelintake.blob.core.windows.net/s1-slc`


### Scene names

Within that container, each scene corresponds to a folder, named according to:

`SLC/[year]/[month]/[day]/[acquisition-mode]/[polarization]/[scene_name]`

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

Putting that all together, a complete scene file looks like:

`https://sentinelintake.blob.core.windows.net/s1-slc/SLC/2021/10/7/IW/SH/S1A_IW_SLC__1SSH_20211007T012134_20211007T012201_040006_04BC4B_7D74.zip`


### Data archiving

Scenes older than 90 days are stored in the same container, but have been retired to [Azure archive storage](https://azure.microsoft.com/en-us/services/storage/archive/#overview).  Those scenes will still be enumerated when listing blobs in the container, but they will not be readable with read-only access tokens.


## Region information

Large-scale processing is best performed in the West Europe Azure region, where the images are stored.  If you are using Sentinel-1 data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=sentinel-1%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.

