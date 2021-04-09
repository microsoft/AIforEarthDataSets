# Harmonized Global Biomass

## Overview

Global maps of aboveground and belowground biomass carbon density for the year 2010 at 300m resolution.

This dataset provides temporally consistent and harmonized global maps of aboveground and belowground biomass carbon density for the year 2010 at 300m resolution. The aboveground biomass map integrates land-cover specific, remotely sensed maps of woody, grassland, cropland, and tundra biomass. Input maps were amassed from the published literature and, where necessary, updated to cover the focal extent or time period. The belowground biomass map similarly integrates matching maps derived from each aboveground biomass map and land-cover specific empirical models. Aboveground and belowground maps were then integrated separately using ancillary maps of percent tree cover and landcover and a rule-based decision tree. Maps reporting the accumulated uncertainty of pixel-level estimates are also provided.

Source: Oak Ridge National Laboratory

Source Location: <https://doi.org/10.3334/ORNLDAAC/1763>

Domain: Global, 2010

Resolution: 300m


## Storage resources

Data are stored in blobs in the West Europe Azure region, in the following blob folder:

`https://cpdataeuwest.blob.core.windows.net/cpdata/raw/2010-harmonized-biomass/global/300m/`

Images are stored in cloud optimized GeoTIFF format. 

A complete Python example of accessing and plotting HGB data is available is available in the accompanying [sample notebook](hgb.ipynb).

We also provide a read-only SAS (<a href="https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview">shared access signature</a>) token to allow access to this data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2019-12-12&si=cpdata-ro&sr=c&sig=tqRGrmdYYa9WYkaPi0wWOD0nalRdNGTZNe97GL2enDA%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing is best performed in the West Europe Azure data center, where the data are stored.  If you are using this data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Citation

If you use this data set in a publication, cite as:

Spawn, S.A., and H.K. Gibbs. 2020. Global Aboveground and Belowground Biomass Carbon Density Maps for the Year 2010. ORNL DAAC, Oak Ridge, Tennessee, USA.


## Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/hgb.png" width=350px;><br/>

<p style="font-size:80%;margin-left:15px;">Global above-ground biomass estimates in 2010.</p>


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=hgb%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
