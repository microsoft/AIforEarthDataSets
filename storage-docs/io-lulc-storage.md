Data are stored as cloud-optimized GeoTIFF images in Blob Storage in the West Europe Azure region, in the following folder:

`https://ai4edataeuwest.blob.core.windows.net/io-lulc/io-lulc-model-001-v01-composite-v03-supercell-v02-clip-v01/`

Within that folder, files are named according to:

`[gzd]_[start-date]_[end-date].tif`

* `gzd` is a three-character [MGRS grid zone designator](https://en.wikipedia.org/wiki/Military_Grid_Reference_System#Grid_zone_designation)
* For all images presently available (for the 2020 land cover map), `start-date` is "20200101" and `end-date` is "20210101"

For example, Auckland is in MRGS zone 60H, so the following tile includes land cover information for Auckland:

`https://ai4edataeuwest.blob.core.windows.net/io-lulc/io-lulc-model-001-v01-composite-v03-supercell-v02-clip-v01/60H_20200101-20210101.tif`

Tiles closely approximate areas corresponding to MGRS three-character prefixes, but deviate slightly to allow some overlap between images and to wrap tightly to coastlines.  Precise geometry for all tiles is available <a href="https://ai4edataeuwest.blob.core.windows.net/io-lulc/io-lulc-model-001-v01-composite-v03-supercell-v02-clip-v01.geojson">here</a> (geojson).