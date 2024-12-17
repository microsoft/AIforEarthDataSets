# NEXRAD L2

## Overview

Recent level II data from the NEXRAD weather radar system.

[NEXRAD](https://www.nws.noaa.gov/om/marine/nexrad.htm) (Next-Generation Radar) is a network of 159 radar stations across the US that is operated by the [National Oceanic and Atmospheric Administration](https://www.noaa.gov/) (NOAA).  This dataset is used for weather forecasting and climate science.

This dataset is available on Azure thanks to the [NOAA Open Data Dissemination (NODD) Program](https://www.noaa.gov/information-technology/open-data-dissemination).

Data are available for the most recent 90 days; older data are available in archive storage and may be made available on request (contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=nexrad%20question)).


## Storage resources

Data are stored in blobs (one blob per scan) in the East US data center, in the following blob container:

`https://nexradsa.blob.core.windows.net/nexrad-l2`

Scans are placed according to the following convention:

`https://nexradsa.blob.core.windows.net/nexrad-l2/year/month/day/station/filename`

Individual file names follow the following convention:

`[station][year][month][day][time]`

For example, the following file contains one scan from the KHPX station, on July 7, 1997, at 00:08.27 GMT:

`https://nexradsa.blob.core.windows.net/nexrad-l2/1997/07/07/KHPX/KHPX19970707_000827.gz`

We also provide an API to get read-only SAS (shared access signature) tokens to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://planetarycomputer.microsoft.com/api/sas/v1/token/nexradsa/nexrad-l2`

API documentation is at `https://planetarycomputer.microsoft.com/api/sas/v1/docs`.
Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

NEXRAD data can consume hundreds of terabytes, so large-scale processing is best performed in the East US Azure data center, where the scans are stored.


## Index

A list of all NEXRAD files is available here, as a zipped .txt file:

`https://nexradsa.blob.core.windows.net/nexrad-index/nexrad-index.zip`

We also maintain a SQLite database to facilitate querying images by location and time; see the accompanying [sample notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/nexrad-l2.ipynb) for details.


## Sample code

A complete Python example of accessing and plotting a NEXRAD scan is available in the accompanying [sample notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/nexrad-l2.ipynb)


## Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/nexrad.png" width=350px;><br/>

<p style="font-size:80%;margin-left:15px;">A weather scan near Oklahoma City from June 5, 1991.</p>


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=nexrad%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
