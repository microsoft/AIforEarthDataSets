# Copernicus DEM

## Overview

Global topographic information from the Copernicus program.

The [Copernicus DEM](https://spacedata.copernicus.eu/explore-more/news-archive/-/asset_publisher/Ye8egYeRPLEs/blog/id/434960) is a digital surface model (DSM), which represents the surface of the Earth including buildings, infrastructure, and vegetation. This DSM is based on radar satellite data acquired during the TanDEM-X Mission, which was funded by a public-private partnership between the German Aerospace Centre (DLR) and Airbus Defence and Space. Copernicus DEM is available at both 30-meter and 90-meter resolution.

Copernicus DEM is available on Azure in cloud-optimized GeoTIFF (COG) format; COG files were sourced from [OpenTopography](https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.032021.4326.1).

This file documents the storage structure for Copernicus DEM data; you can also use the [Planetary Computer search API](https://planetarycomputer.microsoft.com/docs/quickstarts/reading-stac/) ([example](https://planetarycomputer.microsoft.com/dataset/cop-dem-glo-30#Example-Notebook)) to search for Copernicus DEM data.

## Storage resources

COG files are stored in blobs in the West Europe Azure region, in the following blob container:

`https://elevationeuwest.blob.core.windows.net/copernicus-dem`

Within that container, data are named according to:

`COP[resolution-m]_hh/Copernicus_DSM_COG_[resolution-arc]_[latitude-string]_00_[longitude-string]_00_DEM.tif`

* `resolution-m` is the data set resolution in meters (30 for the 30m dataset, 90 for the 90m dataset)
* `resolution-arc` is the data set resolution in arc-seconds (10 for the 30m dataset, 30 for the 90m dataset)
* `latitude-string` specifies the lower latitude bound of the tile, as [N&#124;S]nn, e.g. "N03" or "S87"
* `longitude-string` specifies the lower longitude bound of the tile, as [W&#124;E]nnn, e.g. "W160" or "E059"

For example, the following file:

<https://elevationeuwest.blob.core.windows.net/copernicus-dem/COP30_hh/Copernicus_DSM_COG_10_N03_00_W160_00_DEM.tif>

...contains 30m-resolution data for the tile whose lower latitude bound is +3.0 degrees, and whose lower longitude bound is -160.0 degrees.


## Mounting the container

We provide a read-only SAS (shared access signature) token to allow access to Copernicus DEM data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2020-08-04&si=copernicus-dem-ro&sr=c&sig=1su5qTAP5BEasRdKVjDRV4dYfpv3oL6FHUV%2BjyWaaVc%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing is best performed in the West Europe Azure data center, where the images are stored.  If you are using this data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Sample code

A complete Python example of accessing and plotting Copernicus DEM data is available in the accompanying [sample notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/copernicus-dem.ipynb).


## License and attribution information

Use of Copernicus DEM data is governed by the <a href="https://docs.sentinel-hub.com/api/latest/static/files/data/dem/resources/license/License-COPDEM-30.pdf">Licence for the use of the Copernicus WorldDEM</a>.


## Pretty picture


<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/copernicus-dem.png" style="width:350px;"><br/>

<p style="font-size:80%;margin-left:15px;">Topography in the Mount Fuji area.</p>


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=copernicus-dem%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.

