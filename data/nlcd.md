# National Land Cover Database

## Overview

The [National Land Cover Database](https://www.mrlc.gov/national-land-cover-database-nlcd-2016) (NLCD) provides US-wide data on land cover and land cover change at a 30m resolution with a 16-class legend.  This Azure dataset reflects the CONUS and Alaska portions of NLCD 2016, which includes land cover for years 2001, 2003, 2006, 2008, 2011, 2013, and 2016.

Source: U.S. Geological Survey (USGS)

Domain: continental US and Alaska, 2001-2016

Resolution: 30m

This dataset was curated and brought to Azure by [CarbonPlan](https://carbonplan.org/).


## Storage resources

Data are stored in blobs in the West Europe Azure region, in the following blob folder:

`https://cpdataeuwest.blob.core.windows.net/cpdata/raw/nlcd`

Within that folder, data are organized according to:

`[region]/30m/[year].tif`

`region` is the spatial domain; currently `conus` or `ak`.

`year` is the four-digit year (e.g. 2014).

Images are stored in cloud-optimized GeoTIFF format.  The one and only image channel contains land cover labels according to the [NLCD legend](https://www.mrlc.gov/data/legends/national-land-cover-database-2016-nlcd2016-legend):

<img alt="NLCD Legend" src="https://github.com/microsoft/AIforEarthDataSets/raw/main/data/nlcd_color_labels.jpg" style="margin-left:30px;width:300px;"/>

We also provide a read-only SAS (<a href="https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview">shared access signature</a>) token to allow access to this data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2019-12-12&si=cpdata-ro&sr=c&sig=tqRGrmdYYa9WYkaPi0wWOD0nalRdNGTZNe97GL2enDA%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing is best performed in the West Europe Azure data center, where the data are stored.


## Sample code

A complete Python example of accessing and plotting NLCD data is available in the accompanying [sample notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/nlcd.ipynb).


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=nlcd%20question).


## Pretty picture

<img alt="NLCD rendered map" src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/nlcd.png">

<p style="font-size:80%;margin-left:15px;">US national land cover for 2001.</p>

## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
