# Sentinel-5P

## Overview

The [Sentinel-5P](https://sentinel.esa.int/web/sentinel/missions/sentinel-5p) mission provides daily global atmospheric measurements at a resolution of 3.5km x 7km on most bands.

This dataset represents the global archive of Sentinel-5P [Level 2](http://www.tropomi.eu/data-products/level-2-products) products, from 2018 to the present, in NetCDF format.  

Sentinel-5P data on Azure are maintained by [Sinergise](https://sinergise.com/).

Sentinel-5P data are currently in preview on Azure; email [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=sentinel5p%20question) to request access.


## Storage resources

### Container information

Data are stored in blobs in the West Europe Azure region, in the following blob container:

`https://sentinel5euwest.blob.core.windows.net/sentinel-5p`


### Scene names

Within that container, each scene corresponds to a folder, named according to:

`TROPOMI/[product]/[year]/[month]/[day]/[scene_name]`

* `product` is a product identifier, one of:
  * `L2__AER_AI`: UV aerosol index
  * `L2__AER_LH`: Aerosol layer height
  * `L2__CH4___`: Methane (CH<sub>4</sub>)
  * `L2__CLOUD_`: Cloud
  * `L2__CO____`: Carbon monoxide (CO)
  * `L2__HCHO__`: Formaldehyde (HCHO)
  * `L2__NO2___`: Nitrogen dioxide (NO<sub>2</sub)
  * `L2__O3____`: Ozone (O<sub>3</sub>
  * `L2__O3_TCL`: Tropospheric ozone
  * `L2__SO2___`: Sulfur dioxide (SO<sub>2</sub>)
  * `L2__NP_BD3`: Cloud from the [Suomi NPP](https://www.nasa.gov/mission_pages/NPP/main/index.html) mission, band 3
  * `L2__NP_BD6`: Cloud from the [Suomi NPP](https://www.nasa.gov/mission_pages/NPP/main/index.html) mission, band 6
  * `L2__NP_BD7`: Cloud from the [Suomi NPP](https://www.nasa.gov/mission_pages/NPP/main/index.html) mission, band 7
* `year` is the four-digit year  
* `month` is the 1-indexed, zero-padded month
* `day` is the 1-indexed, zero-padded day of month

`scene name` follows the [Sentinel-5P file name convention](https://sentinels.copernicus.eu/documents/247904/2506504/FFS-Tailoring-Sentinel-5P.pdf):

* `S5P` is the mission indicator (Sentinel-5P)
* `CCCC` is a file class, one of:
  * `NRTI` (near-real-time processing)
  * `OFFL` (offline processing)
  * `RPRO` (reprocessed) (uncommon)
* `L2` indicates level-2 data
* `PPPPPPPPPP` is a ten-character product identifier, matching the `product` field above
* `yyyymmddThhmmss` is the sensing start time for this scene (`T` is the character 'T')
* `YYYYMMDDTHHMMSS` is the sensing stop time for this scene (`T` is the character 'T')
* `oooooo` is an absolute orbit number
* `cc` is a collection number (always 01)
* `pppppp` is the version number of the toolkit used to produce the L2 product`
* `xxxxxxxxxxxxxxx` is a processing date and time

Putting that all together, the following is a complete URL to a methane product from Jan 5, 2021:

`https://sentinel5euwest.blob.core.windows.net/sentinel-5p/TROPOMI/L2__CH4___/2021/01/05/S5P_OFFL_L2__CH4____20210105T001436_20210105T015606_16736_01_010400_20210106T172254/`


### Image files

Each scene folder contains a single NetCDF file whose name matches the scene name; for example, the above folder contains one file called:

`S5P_OFFL_L2__CH4____20210105T001436_20210105T015606_16736_01_010400_20210106T172254.nc`


## Sample code

A complete Python example of accessing and plotting Sentinel-5P data is available in the accompanying [sample notebook](sentinel-5p.ipynb).

## Region information

Large-scale processing is best performed in the West Europe Azure region, where the images are stored.  If you are using Sentinel-5P data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/sentinel-5p.png" width=400px;><br/><span style='font-size:80%'>Ozone concentration around East Atlantic longitudes on Jan 1, 2021.</span>


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=sentinel-5%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.

