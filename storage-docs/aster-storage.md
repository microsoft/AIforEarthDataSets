### Container information

Data are stored in blobs in the West Europe Azure region, in the following blob container:

`https://astersa.blob.core.windows.net/aster`


### Scene names

Within the COG container, each scene corresponds to a prefix, named according to:

images/L1T/`[year]`/`[month]`/`[day]`/`[scene name]`

`[year]`, `[month]`, and `[day]` are the four-digit year and two-digit month/day.

`scene name` follows the [ASTER naming convention](https://lpdaac.usgs.gov/data/get-started-data/collection-overview/missions/aster-overview/#aster-naming-conventions):

AST_L1T<span style="background-color:#aaffff;">VVV</span><span style="background-color:#ffaaff;">YYYYMMDHHMMSS</span>_<span style="background-color:#ffffaa;">yyyymmddhhmmss</span>_<span style="background-color:#dddddd;">id</span>

* `VVV` is always "003", for ASTER collection 003
* `MMDDYYYYHHMMSS` is the acquisition month, day, year, hour, minute, second
* `mmddyyyyhhmmss` is the processing month, day, year, hour, minute, second
* `id` is a unique acquisition identifier.

For example:

`AST_L1T_00306042003004247_20150428235500_35366`

Putting that all together, a complete scene prefix for an ASTER image from June 4, 2003 looks like:

`https://astersa.blob.core.windows.net/aster/images/L1T/2003/06/04/AST_L1T_00306042003004247_20150428235500_35366`


### Image files

All scenes contain one or more of the following files (not all bands are present in all ASTER scenes), separated from the prefix with ".":

* SWIR.tif (ASTER shortwave infrared bands 4, 5, 6, 7, 8, and 9; at 30m resolution)
* VNIR.tif (ASTER visible and near-infrared bands 1, 2, and 3; at 15m resolution)
* TIR.tif (ASTER thermal infrared bands 10, 11, 12, 13, and 14; at 90m resolution)

So, for example, the VNIR COG file for the example scene above is available at:

https://astersa.blob.core.windows.net/aster/images/L1T/2003/06/04/AST_L1T_00306042003004247_20150428235500_35366.VNIR.tif