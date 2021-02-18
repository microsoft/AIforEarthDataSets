Recent level II data from the NEXRAD weather radar system.

[NEXRAD](https://www.nws.noaa.gov/om/marine/nexrad.htm) (Next-Generation Radar) is a network of 159 radar stations across the US that is operated by the [National Oceanic and Atmospheric Administration](https://www.noaa.gov/) (NOAA).  This dataset is used for weather forecasting and climate science.

This dataset is available on Azure thanks to the [NOAA Big Data Program](https://www.noaa.gov/organization/information-technology/big-data-program).

Data are available for the most recent 90 days; older data are available in archive storage and may be made available on request (contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=nexrad%20question)).


#### Storage resources

Data are stored in blobs (one blob per scan) in the East US data center, in the following blob container:

`https://nexradsa.blob.core.windows.net/nexrad-l2`

Scans are placed according to the following convention:

`https://nexradsa.blob.core.windows.net/nexrad-l2/year/month/day/station/filename`

Individual file names follow the following convention:

`[station][year][month][day][time]`

For example, the following file contains one scan from the KHPX station, on July 7, 1997, at 00:08.27 GMT:

`https://nexradsa.blob.core.windows.net/nexrad-l2/1997/07/07/KHPX/KHPX19970707_000827.gz`

A complete Python example of accessing and plotting a NEXRAD scan is available in the notebook provided under &ldquo;<a href="https://azure.microsoft.com/en-us/services/open-datasets/catalog/nexrad-l2?tab=data-access">data access</a>&rdquo;.

We also provide a read-only SAS (shared access signature) token to allow access to NEXRAD data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`https://nexradsa.blob.core.windows.net/nexrad-l2?st=2019-07-26T22%3A26%3A29Z&se=2034-07-27T22%3A26%3A00Z&sp=rl&sv=2018-03-28&sr=c&sig=oHaHPOVn3hs9Dm2WtAKAT64zmZkwwceam8XD8HSVrSg%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

NEXRAD data can consume hundreds of terabytes, so large-scale processing is best performed in the East US Azure data center, where the scans are stored.  If you are using NEXRAD data for environmental science applications, including weather forecasting, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


#### Index

A list of all NEXRAD files is available here, as a zipped .txt file:

`https://nexradsa.blob.core.windows.net/nexrad-index/nexrad-index.zip`

We also maintain a SQLite database to facilitate querying images by location and time; see the [sample notebook](https://azure.microsoft.com/en-us/services/open-datasets/catalog/nexrad-l2?tab=data-access) for details.


#### Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/nexrad.png" width=350px;><br/>

<p style="font-size:80%;margin-left:15px;">A weather scan near Oklahoma City from June 5, 1991.</p>


#### Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=nexrad%20question).


#### Notices

MICROSOFT PROVIDES AZURE OPEN DATASETS ON AN "AS IS" BASIS. MICROSOFT MAKES NO WARRANTIES, EXPRESS OR IMPLIED, GUARANTEES OR CONDITIONS WITH RESPECT TO YOUR USE OF THE DATASETS. TO THE EXTENT PERMITTED UNDER YOUR LOCAL LAW, MICROSOFT DISCLAIMS ALL LIABILITY FOR ANY DAMAGES OR LOSSES, INCLUDING DIRECT, CONSEQUENTIAL, SPECIAL, INDIRECT, INCIDENTAL OR PUNITIVE, RESULTING FROM YOUR USE OF THE DATASETS. 

This dataset is provided under the original terms that Microsoft received source data. The dataset may include data sourced from Microsoft.
