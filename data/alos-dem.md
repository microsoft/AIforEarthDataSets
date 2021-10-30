# ALOS World 3D-30m (ALOS DEM)

## Overview

Global topographic information from the JAXA ALOS PRISM instrument.

The [ALOS World 3D-30m](https://www.eorc.jaxa.jp/ALOS/en/aw3d30/index.htm) DSM dataset is a 30 meter resolution global Digital Surface Model (DSM). The dataset is based on a 5 meter resolution dataset developed by the Japan Aerospace Exploration Agency (JAXA) since 2014, named "ALOS World 3D". The AW3D dataset was developed using 3 million scenes acquired by the PRISM panchromatic optical sensor on the Advanced Land Observing Satellite "DAICHI" (ALOS), operated from 2006 to 2011.

ALOS DEM is available on Azure in cloud-optimized GeoTIFF (COG) format; COG files were sourced from [OpenTopography](https://portal.opentopography.org/raster?opentopoID=OTALOS.112016.4326.2).

This file documents the storage structure for ALOS DEM data; you can also use the [Planetary Computer search API](https://planetarycomputer.microsoft.com/docs/quickstarts/reading-stac/) ([example](https://planetarycomputer.microsoft.com/dataset/alos-dem#Example-Notebook)) to search for ALOS DEM data.


## Storage resources

COG files are stored in blobs in the West Europe Azure region, in the following blob container:

`https://ai4edataeuwest.blob.core.windows.net/alos-dem`

Within that container, data are named according to:

`AW3D30_globa/ALPSMLC30_[latitude-string][longitude-string]_DSM.tif`

* `latitude-string` specifies the lower latitude bound of the tile, as [N|S]nnn, e.g. "N016" or "001"
* `longitude-string` specifies the lower longitude bound of the tile, as [W|E]nnn, e.g. "W011" or "E020"

For example, the following file:

<https://ai4edataeuwest.blob.core.windows.net/alos-dem/AW3D30_global/ALPSMLC30_N015W011_DSM.tif>

...contains data for the tile whose lower latitude bound is 15 degrees, and whose lower longitude bound is -11 degrees.


## Mounting the container

We provide a read-only SAS (shared access signature) token to allow access to ALOS DEM data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2020-08-04&si=alos-dem-ro&sr=c&sig=cq0uO8aUcFFTvj6f50qgp%2BS6Vjy1UO30cWjEQVhvCok%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing is best performed in the West Europe Azure data center, where the images are stored.  If you are using this data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Sample code

A complete Python example of accessing and plotting ALOS DEM data is available in the accompanying [sample notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/alos-dem.ipynb).


## License and attribution information

Use of ALOS DEM data is governed by the <a href="https://earth.jaxa.jp/en/data/policy/">JAXA Terms of Use of Research Data</a>.


## Pretty picture


<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/alos-dem.png" style="width:350px;"><br/>

<p style="font-size:80%;margin-left:15px;">Topography in the Mount Fuji area.</p>


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=alos-dem%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.

