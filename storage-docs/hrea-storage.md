Data are stored in blobs in the West Europe Azure region, in the following blob container:

`https://hreadatasa.blob.core.windows.net/hrea`

Within that container, data are organized within folders named according to:

`HREA_[country]_[year]_v1`

* `country` is one of the supported countries, enumerated below
* `year` is a four-digit year from 2012 to 2019

For example, the following folder contains data for Burkina Faso from 2016:

`HREA_Burkina_Faso_2016_v1`

Within each folder, data are available as 15 arc-second cloud-optimized GeoTIFF files, with four files per folder:

* `[country]_rade9lnmu_[year].tif`: Nighttime light annual composite.
* `[country_set_zscore_sy_[year].tif`: Statistically estimated brightness levels. Higher levels indicate more robust usage of outdoor lighting, which is correlated with overall energy consumption.
* `[country]_set_lightscore_sy_[year].tif`: Predicted likelihood that a settlement is electrified (0 to 1).
* `[country]_set_prplit_conf90_sy_[year].tif`: Proportion of nights a settlement is statistically brighter than matched uninhabited areas.

For example, the nighttime light annual composite for Djibouti in 2019 is located in:

`https://hreadatasa.blob.core.windows.net/hrea/HREA/HREA_Djibouti_2019_v1/Djibouti_rade9lnmu_2019.tif`

The data hosted on Azure is derived from the [source](http://www-personal.umich.edu/~brianmin/HREA/index.html) by converting each file into cloud-optimized GeoTIFF format file using [rio cogeo 2.1.2](https://github.com/cogeotiff/rio-cogeo).