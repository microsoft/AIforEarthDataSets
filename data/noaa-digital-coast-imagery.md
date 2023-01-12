# NOAA Digital Coast Imagery

## Overview

This dataset contains high resolution (1 meter or less) imagery collected by a number of sources and contributed to the NOAA Digital Coast. The majority of datasets in this collection were acquired by the NOAA National Geodetic Survey for shoreline mapping and emergency response. Most of the datasets are either 3-band RGB or CIR, 4-band RGBN, or single band infrared imagery. A few datasets consist of hyperspectral imagery.

For more information, see the [project's documentation](https://coast.noaa.gov/digitalcoast/data/highresortho.html).

This dataset is available on Azure thanks to the [NOAA Big Data Program](https://www.noaa.gov/organization/information-technology/big-data-program).

## Storage resources

Data are stored primarily in [Cloud Optimized GeoTIFF](https://www.cogeo.org/) format.

COG files are stored as blobs in the West Europe Azure region in the following blob container.

`https://coastalimagery.blob.core.windows.net/digitalcoast`

The blobs are named using the following pattern `{location}_{tide-stage}_{data-type}_{year}_{OCM-id}/{filename}`

where

* `location` = Location name. May include the 2 letter state at end in capital letters.
* `tide-stage` = optional tide stage. (MLLW, MSL, MHW). Missing if not tidally controlled data.
* `data-type` = data type. (RGB, RGBN, IR, HSI)
* `year` = Year of collection
* `OCM-id` = NOAA OCM identifier. The identifier can be used for more information on the dataset, including the footprint, by substituting it in URL https://coast.noaa.gov/dataviewer/#/imagery/search/where:ID=IIII

The filename conventions may vary with the data collection and provider. A common form is `EEEEEEeNNNNNNn.tif`

where

* `EEEEEE` is the eastings for the UTM zone
* `NNNNNN` is the northings for the UTM zone

So an example full file path is `https://coastalimagery.blob.core.windows.net/digitalcoast/SenecaNY_RGB_2019_8967/335000e4730000n.tif`

Where the information is 3-band RGB imagery from 2019 in Seneca, New York. For more information on this dataset, query the WMS map service at https://maps.coast.noaa.gov/arcgis/rest/services/DAV/ImageryFootprints/MapServer/0 using ID=8967 (the IIII value from the directory).

In addition to the data files, directories will also contain a metadata file (`*_met.xml`) and a tile index shapefile (`tileindex_{LLLLL}{_TTTT}_{tttt}_{YYYY}.zip`).

## Region information

Large-scale processing is best performed in the West Europe Azure region, where the data are stored.

## Contact

For questions, please contact the NOAA Big Data Program Team at [`noaa.bdp@noaa.gov`](mailto:noaa.bdp@noaa.gov?subject=azure%20gefs%20question).

## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
