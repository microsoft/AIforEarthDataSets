### Container information

Data are stored in blobs in the West Europe Azure region, in the following blob container:

`https://astersa.blob.core.windows.net/aster-cogs`

HDF files are temporarily available in the following blob container:

`https://astersa.blob.core.windows.net/aster`


### Scene names

Within the COG container, each scene corresponds to a folder, named according to:

images/L1T/`[year]`/`[month]`/`[day]`/`[scene name]`

* `[year]`, `[month]`, and `[day]` are the four-digit year and two-digit month/day

`scene name` follows the [ASTER naming convention](https://lpdaac.usgs.gov/data/get-started-data/collection-overview/missions/aster-overview/#aster-naming-conventions), with the exception that the "AST_L1T" prefix has been removed.  So scene names look like:

<span style="background-color:#aaffff;">VVV</span><span style="background-color:#ffaaff;">YYYYMMDHHMMSS</span>_<span style="background-color:#ffffaa;">yyyymmddhhmmss</span>_<span style="background-color:#dddddd;">id</span>

* `VVV` is always "003", for ASTER collection 003
* `MMDDYYYYHHMMSS` is the acquisition month, day, year, hour, minute, second	
* `mmddyyyyhhmmss` is the processing month, day, year, hour, minute, second
* `id` is a unique acquisition identifier.

For example:

`00306042003004247_20150428235500_35366`

Putting that all together, a complete scene folder for an ASTER image from June 4, 2003 looks like:

`https://astersa.blob.core.windows.net/aster-cogs/images/L1T/2003/06/04/00306042003004247_20150428235500_35366/`


### ASTER image files

Documentation pending finalization of the still-provisional COG format.