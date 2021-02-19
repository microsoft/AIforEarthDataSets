### NASADEM

#### Overview

Global topographic information from the NASADEM program.

[NASADEM](https://earthdata.nasa.gov/esds/competitive-programs/measures/nasadem) provides global topographic data at 1 arc-second (~30m) horizontal resolution, derived primarily from data captured via the [Shuttle Radar Topography Mission](https://www2.jpl.nasa.gov/srtm/) (SRTM).


#### Storage resources

Data are stored in blobs in the West Europe Azure region, in the following blob container:

`https://nasademeuwest.blob.core.windows.net/nasadem-nc`

Within that container, data are organized according to:

`v001/NASADEM_NC_[lat_tile][lon_tile].[extension]`

`lat_tile` is a character ('n' or 's') plus a two-digit latitude value, derived from the latitude represented by each tile.  To find the latitude code for a given latitude, perform a floor() operation, then take the absolute value, then prefix with 'n' for positive latitudes (including zero) and 's' for negative latitudes, and zero-pad to two digits.  For example, the latitude 35.3606 becomes 'n35'.

`long_tile` is a character ('e' or 'w') plus a three-digit longitude value, derived from the longitude represented by each tile.  To find the longitude code for a given longitude, perform a floor() operation, then take the absolute value, then prefix with 'e' for positive latitudes (including zero) and 'w' for negative latitudes, and zero-pad to three digits.  For example, the longitude 138.72 becomes 'e138'.

For each tile, filenames with three extensions are present:

* 1.jpg (a preview image)
* nc (the data itself)
* nc.xml (tile creation metadata)

Images are stored in [NetCDF](https://en.wikipedia.org/wiki/NetCDF) format.

A complete Python example of accessing and plotting NASADEM data is available in the notebook provided under &ldquo;<a href="https://azure.microsoft.com/en-us/services/open-datasets/catalog/nasadem?tab=data-access">data access</a>&rdquo;.

We also provide a read-only SAS (shared access signature) token to allow access to NASADEM data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2019-12-12&si=nasadem-ro&sr=c&sig=6rAbZIvIjQVTov2bGUpqH9T0fzTipRahkooOSf2XCuo%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing is best performed in the East US Azure data center, where the images are stored.  If you are using NASADEM data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.

A copy of NASADEM is also available in the East US Azure region, and will be maintained there until at least the end of 2021, but we encourage users to migrate to the West Europe copy.  The East US data is in the following container:

`https://nasadem.blob.core.windows.net/nasadem-nc`


#### Index

A full list of files is available [here](https://nasadem.blob.core.windows.net/nasadem-nc/v001/index/nasadem_file_list.txt).


#### License and attribution information

NASADEM data may be used without restriction for any purpose whatsoever, commercial or otherwise, free of any royalties or other restrictions. No special permission or compensation is required, even for reselling the exact data, images or other derived products.

If possible, when using this data, please attribute to &ldquo;Courtesy NASA/JPL-Caltech&rdquo;.


#### Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/nasadem.png" width=350px;><br/>

<p style="font-size:80%;margin-left:15px;">Topography in the Mount Fuji area.</p>


#### Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=nasadem%20question).


#### Notices

MICROSOFT PROVIDES AZURE OPEN DATASETS ON AN "AS IS" BASIS. MICROSOFT MAKES NO WARRANTIES, EXPRESS OR IMPLIED, GUARANTEES OR CONDITIONS WITH RESPECT TO YOUR USE OF THE DATASETS. TO THE EXTENT PERMITTED UNDER YOUR LOCAL LAW, MICROSOFT DISCLAIMS ALL LIABILITY FOR ANY DAMAGES OR LOSSES, INCLUDING DIRECT, CONSEQUENTIAL, SPECIAL, INDIRECT, INCIDENTAL OR PUNITIVE, RESULTING FROM YOUR USE OF THE DATASETS. 

This dataset is provided under the original terms that Microsoft received source data. The dataset may include data sourced from Microsoft. 


