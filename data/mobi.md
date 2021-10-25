# NatureServe Map of Biodiversity Importance (MoBI)

## Overview

This data set contains spatial data for the fifteen layers included in the [Map of Biodiversity Importance](https://www.natureserve.org/conservation-tools/projects/map-biodiversity-importance).

MoBI data are not available via anonymous access to Azure storage; you can use the Planetary Computer API ([example](https://planetarycomputer.microsoft.com/dataset/mobi)) to access MoBI data.  If your needs preclude the use of the Planetary Computer API, email [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=mobi%20question) to request access.

## About MoBI

The [Map of Biodiversity Importance](https://www.natureserve.org/conservation-tools/projects/map-biodiversity-importance) (MoBI) consists of a series of raster maps that combine habitat information for 2,216 imperiled species occurring in the conterminous United States, using weightings based on range size and degree of protection to identify areas of high importance for biodiversity conservation. Species included in the project are those which, as of September 2018, had a global conservation status of G1 (critical imperiled) or G2 (imperiled) or which are listed as threatened or endangered at the full species level under the United States Endangered Species Act. Taxonomic groups included in the project are vertebrates (birds, mammals, amphibians, reptiles, turtles, crocodilians, and freshwater and anadromous fishes), vascular plants, selected aquatic invertebrates (freshwater mussels and crayfish) and selected pollinators (bumblebees, butterflies, and skippers).

There are three types of spatial data provided, described in more detail below: species richness, range-size rarity, and protection-weighted range-size rarity.  For each type, this data set includes five different layers &ndash; one for all species combined, and four additional tiffs that break the data down by taxonomic group (vertebrates, plants, freshwater invertebrates, and pollinators) &ndash; for a total of fifteen layers.

These data layers are intended to identify areas of high potential value for on-the-ground biodiversity protection efforts. As a synthesis of predictive models, they cannot guarantee either the presence or absence of imperiled species at a given location. For site-specific decision-making, these data should be used in conjunction with field surveys and/or documented occurrence data, such as is available from the NatureServe Network.


### Species Richness

Species richness is simply a count of the number of imperiled species with habitat in a grid cell. While intuitive, it can be misleading when used to identify areas of high conservation significance. By definition, the rarest species have small distributions and are thus unlikely to co-occur with other imperiled species. Species richness can tell you where at-risk species are on the landscape, but high values do not correspond with areas where conservation need is necessarily greatest.


### Range-Size Rarity

Range-size rarity (RSR) explicitly considers range-size. Each species is assigned a range-size rarity score equal to the inverse of the total area mapped as habitat, and those scores are summed for each species occurring in a grid cell. High values identify areas where species with very small ranges (and thus fewer conservation opportunities) are likely to occur; the presence of multiple imperiled species contributes to higher scores.


### Protection-Weighted Range-Size Rarity

Protection-weighted range-size rarity (PWRSR) maps combine information on both range-size rarity and the degree to which habitat for the species is protected. We defined protected habitat as that occurring within protected areas managed for biodiversity (i.e., Gap Status 1 and 2 lands in the USGS Protected Areas Database; PAD-US 2.0).  Each species was assigned a PWRSR score equal to the product of range-size rarity and the percent of habitat that is unprotected. The PWRSR raster sums these scores for all species with habitat in a cell to identify areas of greatest conservation need – i.e. locations with species that have limited conservation opportunities due to both restricted range size and falling outside of protected areas.


## Storage resources

Data are stored as cloud-optimized GeoTIFF images in Blob Storage in the West Europe Azure region, in the following folder:

`https://ai4edataeuwest.blob.core.windows.net/mobi/spatial_data`

Within that folder, files are named according to:

`[variable]_[taxonomic-grouping].tif`

* `variable` is one of &lsquo;SpeciesRichness&rsquo;, &lsquo;RSR&rsquo; (range-size rarity), or &lsquo;PWRSR_GAP12_SUM&rsquo; (protection-weighted range-size rarity)
* `taxonomic-grouping` is one of &lsquo;All&rsquo;, &lsquo;AquaticInverts&rsquo;, &lsquo;Plants&rsquo;, &lsquo;PollinatorInverts&rsquo;, or &lsquo;Vertebrates&rsquo;


## Symbology files

ArcGIS symbology (.lyrx) files are provided to facilitate rendering MoBI data in ArcGIS tools, within the folder:

`https://ai4edataeuwest.blob.core.windows.net/mobi/symbology`

That folder contains the following files:

* `PWRSR_bright_15class.lyrx` (for rendering PWRSR data for all taxonomic groupings)
* `RSR_bright_15class.lyrx` (for rendering RSR data for all taxonomic groupings)

...plus one file for each taxonomic grouping for the "Species Richness" layers:

* SpeciesRichness_All.tif.lyrx
* SpeciesRichness_AquaticInverts.tif.lyrx
* SpeciesRichness_Plants.tif.lyrx
* SpeciesRichness_PollinatorInverts.tif.lyrx
* SpeciesRichness_Vertebrates.tif.lyrx


## Sample code

A complete Python example of accessing and plotting MoBI data is available in the accompanying [sample notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/mobi.ipynb).


## Region information

Large-scale processing is best performed in the West Europe Azure region, where the images are stored.  If you are using MoBI data for conservation applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Accessing via the Esri Living Atlas

MoBI layers are also available via the [Esri Living Atlas](https://livingatlas.arcgis.com/en/browse/#d=2&srt=name&q=mobi%20owner%3ANatureServe).


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=mobi%20question).


## License information

This dataset was created by NatureServe in collaboration with NatureServe network partners, Esri, and The Nature Conservancy.

NatureServe reserves all rights in all intellectual property provided.  Distribution of the data or any intellectual property in whole or in part, or any products derived from the data or any intellectual property for commercial purposes is strictly prohibited. To see the full terms of use click [here](http://natureserve.maps.arcgis.com/sharing/rest/content/items/8992236b63184422905ed208f050a12e/data).


## Pretty picture

<img src="https://ai4edatasetspublicassets.blob.core.windows.net/assets/aod_images/mobi_800w.png" style="width:500px;"><br/><span style='font-size:80%'>MoBI vertebrate species richness layer.</span>


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.

