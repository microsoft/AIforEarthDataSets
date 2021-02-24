### Sentinel-2 L2A

#### Overview

The [Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2) program provides global optical imagery at 10m-60m resolution.  This dataset represents the global Sentinel-2 archive (currently from 2018-realtime), processed to L2A (bottom-of-atmosphere) using [Sen2Cor](https://step.esa.int/main/snap-supported-plugins/sen2cor/) and converted to [cloud-optimized GeoTIFF](https://www.cogeo.org/) format.

Sentinel-2 imagery is currently in preview on Azure; email [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=sentinel2%20question) to request access.


#### Storage resources

##### Container information

Data are stored in blobs in the West Europe Azure region, in the following blob container:

`https://sentinel2l2a01.blob.core.windows.net/sentinel2-l2`

As per above, this container is not world-readable; email [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=sentinel2%20question) to request an access token.

##### Scene names

Within that container, each scene corresponds to a folder, named according to:

`[UTM longitude zone]/[MGRS latitude band]/[tile code]/[year]/[month]/[day]/[scene name]`

* `UTM longitude zone` is a two-digit [UTM longitude code](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system) from 01 to 60
* `MGRD latitude band` is a one-letter [UTM latitude code](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system#Latitude_bands_2), from "C" to "X" (except "I" and "O")
* `tile code` is a two-letter code from the Sentinel-2 tiling grid ([kml](https://sentinel.esa.int/documents/247904/1955685/S2A_OPER_GIP_TILPAR_MPC__20151209T095117_V20150622T000000_21000101T000000_B00.kml),[geojson](https://github.com/bencevans/sentinel-2-grid)), which is aligned to the [Military Grid Reference System](https://en.wikipedia.org/wiki/Military_Grid_Reference_System)
* `year`, `month`, and `day` are zero-padded to four, two, and two digits respectively

`scene name` follows the [Sentinel-2 scene name convention](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/naming-convention):

`MMM_MSIXXX_YYYYMMDDHHMMSS_Nxxyy_ROOO_Txxxxx_[Product Discriminator].SAFE`

* `MMM` is satellite (S2A or S2B)
* `MSIXXX` is always "MSIL2A", indicating the Level-2A product level
* `YYYYMMDDHHMMSS` is the sensing start time (UTC)
* `Nxxyy` indicates the version of the processing toolset
* `ROOO` is the [relative orbit number](https://sentinel.esa.int/web/sentinel/missions/sentinel-2/satellite-description/orbit), from R001 to R143
* `Txxxxx` is the five-digit tile identifier, will match the UTM longitude zone, MGRS latitude band, and two-letter tile code from the folde rname
* `Product discriminator` is a processing date

Putting that all together, a complete scene folder looks like:

`https://sentinel2l2a01.blob.core.windows.net/sentinel2-l2/11/C/MM/2020/11/26/S2B_MSIL2A_20201126T154319_N0212_R125_T11CMM_20201127T152008.SAFE`

##### Image files

Within a scene folder, recursively listing *.tif will enumerate all images, with suffixes indicating bands according to the following:

* `AOT_10m`: aerosol optical thickness (10m)
* `BO2_10m`: band 2 (490nm) (blue) (10m)
* `BO3_10m`: band 3 (560nm) (green) (10m)
* `BO4_10m`: band 4 (665nm) (red) (10m)
* `BO8_10m`: band 8 (842nm) (near IR) (10m)
* `TCI_10m`: true color image (10m)
* `WVP_10m`: water vapor (10m)

* `AOT_20m`: aerosol optical thickness (20m)
* `BO2_20m`: band 2 (490nm) (blue) (20m)
* `BO3_20m`: band 3 (560nm) (green) (20m)
* `BO4_20m`: band 4 (665nm) (red) (20m)
* `BO5_20m`: band 5 (705nm) (vegetation classification) (20m)
* `BO6_20m`: band 6 (740nm) (vegetation classification) (20m)
* `BO7_20m`: band 7 (783nm) (vegetation classification) (20m)
* `BO8_20m`: band 8 (842nm) (near IR) (20m)
* `B8A_20m`: band 8A (865nm) (vegetation classification) (20m)
* `B11_20m`: band 11 (1610nm) (snow/ice/cloud classification) (20m)
* `B12_20m`: band 12 (2190nm) (snow/ice/cloud classification) (20m)
* `SCL_20m`: scene classification (20m)
* `TCI_20m`: true color image (20m)
* `WVP_20m`: water vapor (20m)

* `AOT_60m`: aerosol optical thickness (60m)
* `BO2_60m`: band 2 (490nm) (blue) (60m)
* `BO3_60m`: band 3 (560nm) (green) (60m)
* `BO4_60m`: band 4 (665nm) (red) (60m)
* `BO5_60m`: band 5 (705nm) (vegetation classification) (60m)
* `BO6_60m`: band 6 (740nm) (vegetation classification) (60m)
* `BO7_60m`: band 7 (783nm) (vegetation classification) (60m)
* `BO9_60m`: band 9 (945nm) (water vapor) (60m)
* `B8A_60m`: band 8A (865nm) (vegetation classification) (60m)
* `B11_60m`: band 11 (1610nm) (snow/ice/cloud classification) (60m)
* `B12_60m`: band 12 (2190nm) (snow/ice/cloud classification) (60m)
* `SCL_60m`: scene classification (60m)
* `TCI_60m`: true color image (60m)
* `WVP_60m`: water vapor (60m)

For example, the 10m image for band 2 in the example scene above is at:

`https://sentinel2l2a01.blob.core.windows.net/sentinel2-l2/11/C/MM/2020/11/26/S2B_MSIL2A_20201126T154319_N0212_R125_T11CMM_20201127T152008.SAFE/GRANULE/L2A_T11CMM_A019456_20201126T154359/IMG_DATA/R10m/T11CMM_20201126T154319_B02_10m.tif`


#### Sample code

A complete Python example of accessing and plotting Sentinel-2 data - using the Copernicus Open Access Hub API to query for scenes of interest - is available in the notebook provided under the &ldquo;data access&rdquo; link.


#### Region information

Large-scale processing is best performed in the West Europe Azure region, where the images are stored.  If you are using Sentinel-2 data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


#### Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/sentinel-2.png" width=350px;><br/>

<p style="font-size:80%;margin-left:15px;">A <i>mostly</i> cloudless day in Seattle.</p>


#### Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=sentinel-2%20question).


#### Notices

MICROSOFT PROVIDES AZURE OPEN DATASETS ON AN "AS IS" BASIS. MICROSOFT MAKES NO WARRANTIES, EXPRESS OR IMPLIED, GUARANTEES OR CONDITIONS WITH RESPECT TO YOUR USE OF THE DATASETS. TO THE EXTENT PERMITTED UNDER YOUR LOCAL LAW, MICROSOFT DISCLAIMS ALL LIABILITY FOR ANY DAMAGES OR LOSSES, INCLUDING DIRECT, CONSEQUENTIAL, SPECIAL, INDIRECT, INCIDENTAL OR PUNITIVE, RESULTING FROM YOUR USE OF THE DATASETS. 

This dataset is provided under the original terms that Microsoft received source data. The dataset may include data sourced from Microsoft. 


