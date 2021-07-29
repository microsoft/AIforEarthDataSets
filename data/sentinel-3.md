# Sentinel-5P

## Overview

The [Sentinel-3](https://sentinel.esa.int/web/sentinel/missions/sentinel-3) mission provides global multispectral imagery at a resolution of 300m-500m, with a revisit time of approximately two days, from 2016 to the present.

This dataset represents a global archive of the Sentinel-3 Level 2 products derived from the following Sentinel-3 instruments:

* [OLCI](https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-3-olci/level-2/products-description) (ocean and land color instrument) (300m resolution)
* [SLSTR](https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-3-slstr/level-2/products) (sea and land surface temperature radiometer) (500m resolution)
* [SRAL](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-3-altimetry/product-types/level-2-sral-mwr) (SAR radar altimeter) (300m resolution)

This dataset also includes the Sentinel-3 [Synergy](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-3-synergy) product that combines the OLCI and SLSTR instruments.

Sentinel-3 data on Azure are maintained by [Sinergise](https://sinergise.com/).

Sentinel-3 data are currently in preview on Azure; email [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=sentinel3%20question) to request access.


## Storage resources

### Container information

Data are stored as NetCDF files in Azure Blob Storage in the West Europe Azure region, in the following blob container:

`https://sentinel3euwest.blob.core.windows.net/sentinel-3`


### Scene names

Within that container, each scene corresponds to a folder, named according to:

`[instrument]/[product]/[year]/[month]/[day]/[scene_name]`

* `instrument` is one of `OLCI`, `SLSTR`, `SRAL`, or `SYNERGY` (see instrument names above)
* `product` is a product identifier, one of the following (each appears only in the folder for the corresponding instrument):
   
   * `OL_2_LFR___`: [full-resolution land color](https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-3-olci/level-2/land-products) (from the OLCI instrument)
   * `OL_2_WFR___`: [full-resolution ocean color](https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-3-olci/level-2/ocean-products) (from the OLCI instrument)
   
   * `SL_2_FRP___`: [fire radiative power](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-3-slstr/product-types/level-2-frp) (from the SLSTR instrument)
   * `SL_2_LST___`: [land surface temperature](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-3-slstr/product-types/level-2-lst) (from the SLSTR instrument)
   * `SL_2_WST___`: [sea surface temperature](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-3-slstr/product-types/level-2-wst) (from the SLSTR instrument)
   
   * `SR_2_LAN___`: [land altimetry](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-3-altimetry/product-types/level-2-sral-mwr) (from the SRAL instrument)
   * `SR_2_WAT___`: [ocean altimetry](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-3-altimetry/product-types/level-2-sral-mwr) (from the SRAL instrument)
   
   * `SY_2_AOD___`: [aerosol](https://sentinels.copernicus.eu/web/sentinel/level-2-aod)
   * `SY_2_SYN___`: [surface reflectance and aerosol parameters over land](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-3-synergy/product-types/level-2-syn)
   * `SY_2_V10___`: [10-day surface reflectances and NDVI](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-3-synergy/product-types/level-2-vg1-v10)
   * `SY_2_VG1___`: [1-day surface reflectances and NDVI](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-3-synergy/product-types/level-2-vg1-v10)
   * `SY_2_VGP___`: [vegetation-like product](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-3-synergy/product-types/level-2-vgp)
   
* `year` is the four-digit year  
* `month` is the 1-indexed, zero-padded month
* `day` is the 1-indexed, zero-padded day of month

`scene name` follows the Sentinel-3 naming convention, which is consistent across instruments, but is documented separately for [OLCI](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-3-olci/naming-convention), [SLSTR](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-3-slstr/naming-convention), [SRAL](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-3-altimetry/naming-conventions), and [SYNERGY](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-3-synergy/naming-conventions) products:

MMM_OL_L_TTTTTT_yyyymmddThhmmss_YYYYMMDDTHHMMSS_YYYYMMDDTHHMMSS_[instance ID]_GGG_[class ID].SEN3

* `MMM` is the mission indicator (S3A or S3B, or S3_ for combined products)
* `OL` is the source instrument (OL, SL, SR, or SY for OLCI, SLSTR, SRAL, or SYNERGY, respectively)
* `L` is a processing level, always 2 in this dataset
* `TTTTTT` is the product ID, and should match the last six characters of the product component of the folder name
* `yyyymmddThhmmss` is the sensing start time for this scene (`T` is the character 'T')
* `YYYYMMDDTHHMMSS` is the sensing stop time for this scene (`T` is the character 'T')
* `[instance ID]` is a 17-character tile identifier, formatted as `DDDD_CCC_LLL_FFFF` (see documentation for infrequent cases where the instance ID format deviates from this convention):
  * `DDDD`: duration of the sensing interval in seconds
  * `CCC`: cycle number at the sensing start time
  * `LLL`: relative orbit number
  * `FFFF`: frame number
* `GGG` identifies the processing center that created this product
* `[class ID]` is the classification of this product, formatted as `P_XX_NNN`:
  * `P`: platform status (O for operational, F for reference, D for development, R for reprocessing)
  * `XX`: timeliness of the processing workflow (NR for near real time, ST for short time critical, NT for not time critical)
  * `NNN`: baseline collection
* .SEN3 is a fixed extension

Putting that all together, the following is a complete URL to a folder containing an OLCI product from April 2, 2019

`https://sentinel3euwest.blob.core.windows.net/sentinel-3/OLCI/OL_2_LFR___/2019/04/02/S3A_OL_2_LFR____20190402T000107_20190402T000407_20190403T034838_0179_043_116_1800_LN1_O_NT_002.SEN3/`


### Image files

Each scene folder may contain several NetCDF files.  See the complete product specifications for details of all files ([OLCI](https://sentinel.esa.int/documents/247904/1872756/Sentinel-3-OLCI-Product-Data-Format-Specification-OLCI-Level-2-Land.pdf), [SLSTR](https://sentinels.copernicus.eu/documents/247904/0/Sentinel-3-SLSTR-Product-Data-Format-Specification-Level-2-Land/e587c02b-1454-46ff-b74e-bfc91943ae78), [SRAL](https://sentinels.copernicus.eu/documents/247904/0/Sentinel-3-Product-Data-Format-Specification-Level-2-Land/a176f07a-d9bd-4589-8c29-92c3487a9c7b), [SYN](https://sentinels.copernicus.eu/documents/247904/0/Sentinel-3_Product_Data_Format_Specification-Synergy_Level-1-2_Products/02b9c289-80e5-4328-b186-126797f77edb), but some frequently-used files for each product are listed here:

#### OLCI image files

## Sample code

A complete Python example of accessing and plotting Sentinel-3 data is available in the accompanying [sample notebook](sentinel-3.ipynb).


## Region information

Large-scale processing is best performed in the West Europe Azure region, where the images are stored.  If you are using Sentinel-3 data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/sentinel-3.png" width=400px;><br/><span style='font-size:80%'></span>


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=sentinel-3%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.

