Data are stored as cloud-optimized GeoTIFF images in Blob Storage in the West Europe Azure region, in the following folder:

`https://ai4edataeuwest.blob.core.windows.net/mobi/spatial_data`

Within that folder, files are named according to:

`[variable]_[taxonomic-grouping].tif`

* `variable` is one of &lsquo;SpeciesRichness&rsquo;, &lsquo;RSR&rsquo; (range-size rarity), or &lsquo;PWRSR_GAP12_SUM&rsquo; (protection-weighted range-size rarity)
* `taxonomic-grouping` is one of &lsquo;All&rsquo;, &lsquo;AquaticInverts&rsquo;, &lsquo;Plants&rsquo;, &lsquo;PollinatorInverts&rsquo;, or &lsquo;Vertebrates&rsquo;