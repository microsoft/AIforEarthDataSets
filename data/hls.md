# Harmonized Landsat Sentinel-2

## Overview

Satellite imagery from the Landsat 8 and Sentinel-2 satellites, aligned to a common grid and processed to compatible color spaces.

The [Harmonized Landsat Sentinel-2](https://hls.gsfc.nasa.gov/) (HLS) product includes data from the Landsat-8 and Sentinel-2 satellites, aligned to a common tiling system at 30m resolution, from 2013 to the present for Landsat and 2015 to the present for Sentinel-2.  HLS is administered by the National Aeronautics and Space Administration (NASA).

This dataset is maintained by [Ag-Analytics®](https://analytics.ag). Ag-Analytics® also provides an [API](https://ag-analytics.portal.azure-api.net/docs/services/harmonized-landsat-sentinel-service/operations/hls-service) which accepts an area of interest (AOI) polygon, date range, and other options, and returns processed images for individual MSI bands as well as Normalized Difference Vegetation Index and other metrics, as well as cloud-filtered mosaics.

This dataset is updated weekly.


## Storage resources

Data are stored as [cloud-optimized GeoTIFF](https://www.cogeo.org/) files in the East US 2 data center, in the following blob container:

`https://hlssa.blob.core.windows.net/hls`

Within that container, data are organized according to:

`<product>/HLS.<product>.T<tileid>.<daynum>.<version>_<subdataset>.tif`

* `product` is `L30` for Landsat, `S30` for Sentinel-2
* `tileid` is a four-character tile code from the [Sentinel-2 tiling system](https://hls.gsfc.nasa.gov/wp-content/uploads/2016/10/S2_TilingSystem2-1.txt)
* `daynum` is a four-digit year plus a three-digit day of year (from 001 to 365), e.g. 2019001 represents January 1, 2019
* `version` is always `v1.4`
* `subdataset` is a two-character, 1-indexed string indicating a subdataset (see below)

A mapping from lat/lon to tile IDs can be found [here](https://hls.gsfc.nasa.gov/wp-content/uploads/2016/10/S2_TilingSystem2-1.txt); the accompanying [sample notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/hls.ipynb) demonstrates the use of this table to look up a tile ID by lat/lon.  Tile IDs can also be found using the [Ag-Analytics® API]([API](https://ag-analytics.portal.azure-api.net/docs/services/harmonized-landsat-sentinel-service/operations/hls-service)).

Data are provided for the United States, northern Mexico, southern Canada, France, Ireland, Germany, Ukraine, South Africa, and southeastern Australia; see the [HLS coverage map](https://hls.gsfc.nasa.gov/wp-content/uploads/2018/10/hls1.4_coverage.jpg) for coverage areas.

<!--
Data are provided for the following primary tiles:

['10 U','11 U','12 U','13 U','14 U','15 U','16 U','10 T','11 T','12 T','13 T','14 T','15 T','16 T','17 T','18 T','19 T','10 S','11 S','12 S','13 S','14 S','15 S','16 S','17 S','18 S','12 R','13 R','14 R','15 R','16 R','17 R']
-->

Bands are as follows:

<table>
<tr><td>Band name</td><td>OLI band number</td><td>MSI band number</td><td>L30 subdatasetnumber</td><td>S30 subdatasetnumber</td></tr>
<tr><td>Coastal aerosol</td><td>1</td><td>1</td><td>01</td><td>01</td></tr>
<tr><td>Blue</td><td>2</td><td>2</td><td>02</td><td>02</td></tr>
<tr><td>Green</td><td>3</td><td>3</td><td>03</td><td>03</td></tr>
<tr><td>Red</td><td>4</td><td>4</td><td>04</td><td>04</td></tr>
<tr><td>Red-edge 1</td><td></td><td>5</td><td></td><td>05</td></tr>
<tr><td>Red-edge 2</td><td></td><td>6</td><td></td><td>06</td></tr>
<tr><td>Red-edge 3</td><td></td><td>7</td><td></td><td>07</td></tr>
<tr><td>NIR broad</td><td></td><td>8</td><td></td><td>08</td></tr>
<tr><td>NIR narrow</td><td>5</td><td>8A</td><td>05</td><td>09</td></tr>
<tr><td>SWIR 1</td><td>6</td><td>11</td><td>06</td><td>12</td></tr>
<tr><td>SWIR 2</td><td>7</td><td>12</td><td>07</td><td>13</td></tr>
<tr><td>Water vapor</td><td></td><td>9</td><td></td><td>10</td></tr>
<tr><td>Cirrus</td><td>9</td><td>10</td><td>08</td><td>11</td></tr>
<tr><td>Thermal infrared 1</td><td>10</td><td></td><td>09</td><td></td></tr>
<tr><td>Thermal infrared 2</td><td>11</td><td></td><td>10</td><td></td></tr>
<tr><td>QA</td><td></td><td></td><td>11</td><td>14</td></tr>
</table>

For example the following filename, HLS.S30.T16TDL.2019206.v1.4_01.tif  would be located at https://hlssa.blob.core.windows.net/hls/S30/HLS.S30.T16TDL.2019206.v1.4_03.tif and would represent Sentinel-2 (S30) HLS data for tile 16TDL (primary tile 16T, sub-tile DL) for dataset band 03 (MSI Band 3, Green) for the 206th day of 2019.

Use https://planetarycomputer.microsoft.com/api/sas/v1/token/hlssa/hls to generate read-only SAS tokens to access this data.

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

HLS data can consume hundreds of terabytes, so large-scale processing is best performed in the East US 2 Azure data center where the images are stored.


## Sample code

A complete Python example of accessing and plotting HLS data is available in the accompanying [sample notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/hls.ipynb).


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=hls%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
