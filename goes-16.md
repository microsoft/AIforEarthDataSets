### NOAA GOES-16

#### Overview

Weather imagery from the GOES-16 satellite.

The [GOES-R](https://www.goes-r.gov/) (Geostationary Operational Environmental Satellite) program images weather phenomena from a set of satellites in geostationary orbits.  The GOES-16 satellite is the first of four planned GOES-R satellites; GOES-16's orbit provides a view of the Americas. 

This dataset currently includes the ABI-L2-MCMIPF product (<u>A</u>dvanced <u>B</u>aseline <u>I</u>mager, <u>L</u>evel <u>2</u>, <u>M</u>ulti-band <u>C</u>loud and <u>M</u>oisture <u>I</u>magery, <u>F</u>ull-disk) and the ABI-L1b-RadF product (<u>A</u>dvanced <u>B</u>aseline <u>I</u>mager, <u>L</u>evel <u>1b</u>, <u>F</u>ull-disk). We may on-board other GOES-16 and GOES-17 products on request; please contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=goes16%20question) if you are interested in using additional GOES data on Azure.

This dataset is available on Azure thanks to the [NOAA Big Data Program](https://www.noaa.gov/organization/information-technology/big-data-program).


#### Storage resources 

Data are stored in blobs in [NetCDF](https://www.unidata.ucar.edu/software/netcdf/) format (one blob per image) in the East US data center, in the following blob container:

`https://goes.blob.core.windows.net/noaa-goes16`

Within that container, data are named as:

`[product]/[year]/[day]/[hour]/[filename]`

* <i>product</i> is a product name; currently ABI-L2-MCMIPF and ABI-L1b-RadF are available on Azure
* <i>year</i> is a four-digit year
* <i>day</i> is a three-digit day-of-year code, starting with 001
* <i>hour</i> is a two-digit hour-of-day code, starting with 00
* <i>filename</i> encodes the product, date, and time; details are available in the [GOES Users' Guide](https://www.goes-r.gov/products/docs/PUG-L2%2B-vol5.pdf)

For example, this file:

https://goes.blob.core.windows.net/noaa-goes16/ABI-L2-MCMIPF/2020/003/00/OR_ABI-L2-MCMIPF-M6_G16_s20200030000215_e20200030009534_c20200030010031.nc

...contains data from January 3, 2020, between midnight and 1am UTC (hour 00).

Data channels and wavelengths are described [here](https://www.ncdc.noaa.gov/data-access/satellite-data/goes-r-series-satellites/glossary).

A complete Python example of accessing and plotting a GOES-16 image is available in the notebook provided under &ldquo;<a href="https://azure.microsoft.com/en-us/services/open-datasets/catalog/goes-16?tab=data-access">data access</a>&rdquo;.

We also provide a read-only SAS (shared access signature) token to allow access to GOES-16 data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`st=2020-04-11T23%3A55%3A25Z&se=2032-04-12T23%3A55%3A00Z&sp=rl&sv=2018-03-28&sr=c&sig=IVSoHKVscKyu8K99I7xfman%2Bzp0ISkFbnbAqE6wkv6A%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing using this dataset is best performed in the East US Azure data center, where the data is stored.  If you are using GOES data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


#### Citation

If you use this data in a publication, please cite as:

GOES-R Series Program, (2019): NOAA GOES-R Series Advanced Baseline Imager (ABI) Level 0 Data. [indicate subset used]. NOAA National Centers for Environmental Information. doi:10.25921/tvws-w071.


#### Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/goes-16.png" width=350px;><br/>

<p style="font-size:80%;margin-left:15px;">Moisture imagery of the Americas on Jan 2, 2020.</p>


#### Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=goes%20question).


#### Notices

MICROSOFT PROVIDES AZURE OPEN DATASETS ON AN "AS IS" BASIS. MICROSOFT MAKES NO WARRANTIES, EXPRESS OR IMPLIED, GUARANTEES OR CONDITIONS WITH RESPECT TO YOUR USE OF THE DATASETS. TO THE EXTENT PERMITTED UNDER YOUR LOCAL LAW, MICROSOFT DISCLAIMS ALL LIABILITY FOR ANY DAMAGES OR LOSSES, INCLUDING DIRECT, CONSEQUENTIAL, SPECIAL, INDIRECT, INCIDENTAL OR PUNITIVE, RESULTING FROM YOUR USE OF THE DATASETS. 

This dataset is provided under the original terms that Microsoft received source data. The dataset may include data sourced from Microsoft.
