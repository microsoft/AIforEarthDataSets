### Harmonized Global Biomass

#### Overview

Global maps of aboveground and belowground biomass carbon density for the year 2010 at 300m resolution.

This dataset provides temporally consistent and harmonized global maps of aboveground and belowground biomass carbon density for the year 2010 at 300m resolution. The aboveground biomass map integrates land-cover specific, remotely sensed maps of woody, grassland, cropland, and tundra biomass. Input maps were amassed from the published literature and, where necessary, updated to cover the focal extent or time period. The belowground biomass map similarly integrates matching maps derived from each aboveground biomass map and land-cover specific empirical models. Aboveground and belowground maps were then integrated separately using ancillary maps of percent tree cover and landcover and a rule-based decision tree. Maps reporting the accumulated uncertainty of pixel-level estimates are also provided.

Source: Oak Ridge National Laboratory

Source Location: <https://doi.org/10.3334/ORNLDAAC/1763>

Domain: Global, 2010

Resolution: 300m


#### Storage resources

Data are stored in blobs in the West Europe Azure region, in the following blob folder:

https://carbonplan.blob.core.windows.net/carbonplan-data/raw/2010-harmonized-biomass/global/300m/

Images are stored in cloud optimized GeoTIFF format. 

A complete Python example of accessing and plotting HGB data is available in the notebook provided under &ldquo;data access&rdquo;.

We also provide a read-only SAS (<a href="https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview">shared access signature</a>) token to allow access to this data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2019-12-12&si=cpdata-ro&sr=c&sig=tqRGrmdYYa9WYkaPi0wWOD0nalRdNGTZNe97GL2enDA%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing is best performed in the West Europe Azure data center, where the data are stored.  If you are using this data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


#### Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=hgb%20question).


#### Notices

MICROSOFT PROVIDES AZURE OPEN DATASETS ON AN "AS IS" BASIS. MICROSOFT MAKES NO WARRANTIES, EXPRESS OR IMPLIED, GUARANTEES OR CONDITIONS WITH RESPECT TO YOUR USE OF THE DATASETS. TO THE EXTENT PERMITTED UNDER YOUR LOCAL LAW, MICROSOFT DISCLAIMS ALL LIABILITY FOR ANY DAMAGES OR LOSSES, INCLUDING DIRECT, CONSEQUENTIAL, SPECIAL, INDIRECT, INCIDENTAL OR PUNITIVE, RESULTING FROM YOUR USE OF THE DATASETS. 

This dataset is provided under the original terms that Microsoft received source data. The dataset may include data sourced from Microsoft.
