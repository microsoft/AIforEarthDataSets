# High Resolution Electricity Access (HREA)

Settlement-level measures of electricity access, reliability, and usage
derived from the complete archive of nightly VIIRS satellite imagery. 

The [HREA](http://www-personal.umich.edu/~brianmin/HREA/index.html) project aims to provide open access to new indicators of electricity access and reliability across the world. Leveraging satellite imagery with computational methods, these high resolution data provide new tools to track progress towards reliable and sustainable energy access across the world.

Specifically HREA provides these derived, nationally and yearly segmented datasets:

1. **Access**: Predicted likelihood that a settlement is electrified, based on night-by-night comparisons of each settlement against matched uninhabited areas over a calendar year.

2. **Reliability**
Proportion of nights a settlement is statistically brighter than matched uninhabited areas. Areas with more frequent power outages or service interruptions have lower rates.

3. **Usage**
Higher levels of brightness indicate more robust usage of outdoor lighting, which is highly correlated with overall energy consumption.

4. **Nighttime Lights**
Annual composites of VIIRS nighttime light output.

For more information and methodology, please visit the [HREA website](http://www-personal.umich.edu/~brianmin/HREA/index.html).

## Storage structure

Data are stored in blobs in the West Europe data center, in the following blob container:

https://hreadatasa.blob.core.windows.net/hrea/

Within that container, data are organized according to:
The data is organized within folders with the names `[COUNTRY_YEAR_version]/*`

...for example:

`/HREA_Burkina_Faso_2016_v1/`

### Data Contents

On each folder, data are available as 15 arcsecond COG GeoTIFFs in country-year for each of the 3 data products:

1. `[COUNTRY]_rade9lnmu_[YEAR].tif`: Nighttime light annual composite
2. `[COUNTRY]_set_zscore_sy_[YEAR].tif`: Statistically estimated brightness levels. Higher levels indicate more robust usage of outdoor lighting, which is correlated with overall energy consumption
3. `[COUNTRY]_set_lightscore_sy_[YEAR].tif`: Predicted likelihood that a settlement is electrified (0 to 1)
4. `[COUNTRY]_set_prplit_conf90_sy_[YEAR].tif`: Proportion of nights a settlement is statistically brighter than matched uninhabited areas.

For example, the Nighttime light annual composite for Djibouti in 2019 is located in:
`https://hreadatasa.blob.core.windows.net/hrea/HREA/HREA_Djibouti_2019_v1/Djibouti_rade9lnmu_2019.tif`

The data hosted on Azure is derived from [the source](http://www-personal.umich.edu/~brianmin/HREA/index.html) by converting into COG file, using [rio cogeo 2.1.2](https://github.com/cogeotiff/rio-cogeo) `rio cogeo create [input] [output]`

## How to Cite

If you use the HREA data, please cite as follows:

Min, Brian and O'Keeffe, Zachary. 2021. High Resolution Electricity Access Indicators Dataset. Ann Arbor, MI: Center for Political Studies, University of Michigan.

## Sample picture

![](kisii_prplit_2019.png)
Proportion of lights Lit for Kisii in 2019.

## Contact

For questions about this hosted instance of the dataset, contact aiforearthdatasets@microsoft.com.

For questions about the dataset, methodology or further questions, please see their [website](http://www-personal.umich.edu/~brianmin/HREA/data.html) 

## Data License

The ["High Resolution Electricity Access"](http://www-personal.umich.edu/~brianmin/HREA/) by [Brian Min](http://www-personal.umich.edu/~brianmin/) is licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1)

## Notices

MICROSOFT PROVIDES AZURE OPEN DATASETS ON AN “AS IS” BASIS. MICROSOFT MAKES NO WARRANTIES, EXPRESS OR IMPLIED, GUARANTEES OR CONDITIONS WITH RESPECT TO YOUR USE OF THE DATASETS. TO THE EXTENT PERMITTED UNDER YOUR LOCAL LAW, MICROSOFT DISCLAIMS ALL LIABILITY FOR ANY DAMAGES OR LOSSES, INCLUDING DIRECT, CONSEQUENTIAL, SPECIAL, INDIRECT, INCIDENTAL OR PUNITIVE, RESULTING FROM YOUR USE OF THE DATASETS.

This dataset is provided under the original terms that Microsoft received source data. The dataset may include data sourced from Microsoft.
