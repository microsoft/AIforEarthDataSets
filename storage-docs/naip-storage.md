Data are stored in cloud-optimized GeoTIFF files in Azure Blob Storage in the West Europe Azure region, in the following blob container:

`https://naipeuwest.blob.core.windows.net/naip`

Within that container, data are organized according to:

`v002/[state]/[year]/[state]_[resolution]_[year]/[quadrangle]/[filename].tif`

...for example:

<a href="https://naipeuwest.blob.core.windows.net/naip/v002/al/2015/al_100cm_2015/30086/m_3008601_ne_16_1_20150804.tif">v002/al/2015/al_100cm_2015/30086/m_3008601_ne_16_1_20150804.tif</a>

More details on these fields:

- <b>Year</b>: Four-digit year.  Images are collected in each state every 3-5 years, with any given year containing some (but not all) states. For example, Alabama has data in 2011 and 2013, but not in 2012, while California has data in 2012, but not 2011 or 2013. Esri provides information about NAIP coverage in their [interactive NAIP annual coverage map](https://www.arcgis.com/home/webmap/viewer.html?webmap=17944d45bbef42afb05a5652d7c28aa5).
- <b>State</b>: Two-letter state code.
- <b>Resolution</b>: String specification of image resolution, which has varied throughout NAIP&rsquo;s history.  Depending on year and state, this may be &ldquo;050cm&rdquo;, &ldquo;060cm&rdquo;, or &ldquo;100cm&rdquo;.
- <b>Quadrangle</b>: <a href="https://catalog.data.gov/dataset/usgs-map-indices-downloadable-data-collection0f236">USGS quadrangle identifier</a>, specifying a 7.5 minute x 7.5 minute area.

The filename component of the path (m_3008601_ne_16_1_20150804 in this example) is preserved from USDA's original archive to allow consistent referencing across different copies of NAIP.  Minor variation in file naming exists, but filenames are generally formatted as:

`m_[quadrangle]_[quarter-quad]_[utm zone]_[resolution]_[capture date].tif`

...for example, the above file is in USGS quadrangle 30086, in the NE quarter-quad, which is in <a href="https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system">UTM zone</a> 16, with 1m resolution, and was captured on 8/4/2014.  In some cases, an additional date may be appended to the filename; in these cases, the first date represents the capture date, and the second date represents the date at which a subsequent version of the image was released to allow for a correction.  For example:

`v002/nc/2018/nc_060cm_2018/36077/m_3607744_se_18_060_20180903_20190210.tif`

...was captured on 9/3/2018, and re-released on 2/10/2019.  If you're reading this because you want to digest this filename, the first date is <i>almost</i> definitely what you're interested in.

Files are stored as [cloud-optimized GeoTIFF](https://www.cogeo.org/) images, with a .tif extension.  These files were produced (from the original, USDA-provided format) and organized by <a href="https://www.esri.com/en-us/home">Esri</a>.

Small thumbnails are also available for each image; substitute &ldquo;.tif&rdquo; with &ldquo;.200.jpg&rdquo; to retrieve the thumbnail.  For example, a thumbnail rendering of the image used in the naming convention example above is available at:

https://naipeuwest.blob.core.windows.net/naip/v002/al/2015/al_100cm_2015/30086/m_3008601_ne_16_1_20150804.200.jpg

We also provide an API to get read-only SAS (shared access signature) tokens to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://planetarycomputer.microsoft.com/api/sas/v1/token/naip`

API documentation is at `https://planetarycomputer.microsoft.com/api/sas/v1/docs`.
Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

NAIP data can consume hundreds of terabytes, so large-scale processing is best performed in the West Europe Azure data center, where the images are stored.

A copy of NAIP is also available in the East US Azure region, and will be maintained there until at least the end of 2021, but we encourage users to migrate to the West Europe copy.  The East US data is in the following container:

`https://naipblobs.blob.core.windows.net/naip`
