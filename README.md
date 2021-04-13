# Overview

The <a href="http://aka.ms/aiforearth">Microsoft AI for Earth program</a> hosts geospatial data on Azure that is important to environmental sustainability and Earth science.  This repo hosts documentation and demonstration notebooks for all the data that is managed by AI for Earth.  If you have feedback about any of this data, or want to request additions to our data program, email [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=data%20question).

# Data sets

## MODIS (40 individual products)

Satellite imagery from the Moderate Resolution Imaging Spectroradiometer (MODIS).

* [Source](https://modis.gsfc.nasa.gov/)
* [Documentation](data/modis.md)

### MODIS MCD43A4 (BRDF-Corrected Surface Reflectance)

This is a legacy version of the MCD43A4 MODIS archive, now superseded by the availability of the full MODIS archive.

* [Source](https://lpdaac.usgs.gov/products/mcd43a4v006/)
* [Documentation](data/modis-mcd43a4.md)
* [Notebook](data/modis-mcd43a4.ipynb)

## National Agriculture Imagery Program

NAIP provides US-wide, high-resolution aerial imagery.  This dataset includes NAIP images from 2010 to the present.

* [Source](https://www.fsa.usda.gov/programs-and-services/aerial-photography/imagery-programs/naip-imagery/)
* [Documentation](data/naip.md)
* [Notebook](data/naip.ipynb)

## NOAA GOES-16

Weather imagery from the GOES-16 satellite.

* [Source](https://www.nesdis.noaa.gov/GOES-R-Series-Satellites)
* [Documentation](data/goes-16.md)
* [Notebook](data/goes-16-abi-l2-mcmipf.ipynb)

## Harmonized Landsat Sentinel-2

Satellite imagery from the Landsat 8 and Sentinel-2 satellites, aligned to a common grid and processed to compatible color spaces.

* [Source](https://hls.gsfc.nasa.gov/)
* [Documentation](data/hls.md)
* [Notebook](data/hls.ipynb)

## Sentinel-2 L2A (preview)

Global optical imagery at 10m resolution from 2016-present.

Sentinel-2 data are in preview; access is granted by request.

* [Source](https://sentinel.esa.int/web/sentinel/missions/sentinel-2)
* [Documentation](data/sentinel-2.md)
* [Notebook](data/sentinel-2.ipynb)

## Sentinel-1 GRD (preview)

Global synthetic aperture radar (SAR) data from 2017-present.

Sentinel-1 GRD data are in preview; access is granted by request.

* [Source](https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-1-sar/products-algorithms/level-1-algorithms/ground-range-detected)
* [Documentation](data/sentinel-1-grd.md)
* [Notebook](data/sentinel-1-grd.ipynb)

## Landsat 8 Collection 2 Level-2  (preview)

Global optical imagery from the Landsat 8 satellite, which has imaged the Earth since 2013.

Landsat data are in preview; access is granted by request.

* [Source](https://landsat.gsfc.nasa.gov/)
* [Documentation](data/landsat-8.md)
* [Notebook](data/landsat-8.ipynb)

## Landsat 7 Collection 2 Level-2  (preview)

Global optical imagery from the Landsat 7 satellite, which has imaged the Earth since 1999.

Landsat data are in preview; access is granted by request.

* [Source](https://landsat.gsfc.nasa.gov/)
* [Documentation](data/landsat-7.md)
* [Notebook](data/landsat-7.ipynb)

## ASTER L1T (2000-2006) (preview)

The [ASTER](https://terra.nasa.gov/about/terra-instruments/aster) instrument, launched on-board NASA's [Terra](https://terra.nasa.gov/) satellite in 1999, provides multispectral images of the Earth at 15m-90m resolution.  This data set represents ASTER data from 2000-2006.

ASTER data are in preview; access is granted by request.

* [Source](https://terra.nasa.gov/about/terra-instruments/aster)
* [Documentation](data/aster.md)
* [Notebook](data/aster.ipynb)

## NASADEM

Global topographic information from the NASADEM program.

* [Source](https://earthdata.nasa.gov/esds/competitive-programs/measures/nasadem)
* [Documentation](data/nasadem.md)
* [Notebook](data/nasadem.ipynb)

## NOAA Global Hydro Estimator

Global rainfall estimates in 15-minute intervals.

* [Source](https://www.ospo.noaa.gov/Products/atmosphere/ghe/)
* [Documentation](data/ghe.md)
* [Notebook](data/ghe.ipynb)

## Daymet

Estimates of daily weather parameters in North America on a one-kilometer grid, with monthly and annual summaries.

* [Source](https://daymet.ornl.gov/)
* [Documentation](data/daymet.md)
* [Notebook (Zarr)](data/daymet-zarr.ipynb)
* [Notebook (NetCDF)](data/daymet-nc.ipynb)

## USFS Forest Inventory and Analysis

Status and trends on U.S. forest location, health, growth, mortality, and production, from the US Forest Service's  [Forest Inventory and Analysis](https://www.fia.fs.fed.us/) (FIA) program.  

* [Source](https://www.fia.fs.fed.us/)
* [Documentation](data/forest-inventory-and-analysis.md)
* [Notebook](data/forest-inventory-and-analysis.ipynb)

## NOAA GFS Warm Start Initial Conditions

Warm start initial conditions for the [NOAA Global Forecast System](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs).

* [Source](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs)
* [Documentation](data/gfs-warm-start.md)

## Harmonized Global Biomass

Global maps of aboveground and belowground biomass carbon density for the year 2010 at 300m resolution.

* [Source](https://www.nature.com/articles/s41597-020-0444-4)
* [Documentation](data/hgb.md)
* [Notebook](data/hgb.ipynb)

## Monitoring Trends in Burn Severity Mosaics

Annual burn severity mosaics for the continental United States and Alaska.

* [Source](https://www.mtbs.gov/)
* [Documentation](data/mtbs.md)
* [Notebook](data/mtbs.ipynb)

## NOAA NEXRAD L2

Recent level II data from the NEXRAD weather radar system.

* [Source](https://www.ncdc.noaa.gov/data-access/radar-data/nexrad)
* [Documentation](data/nexrad-l2.md)
* [Notebook](data/nexrad-l2.ipynb)

## National Land Cover Database

US-wide data on land cover and land cover change at a 30m resolution with a 16-class legend.

* [Source](https://www.mrlc.gov/)
* [Documentation](data/nlcd.md)
* [Notebook](data/nlcd.ipynb)

## Ocean Observatories Initiative CamHD

Video data from the [Ocean Observatories Initiative](https://oceanobservatories.org/) seafloor camera deployed at [Axial Volcano](https://en.wikipedia.org/wiki/Axial_Seamount) on the Juan de Fuca Ridge.

* [Source](https://oceanobservatories.org/instrument-class/camhd/)
* [Documentation](data/ooi-camhd.md)
* [Notebook](data/ooi-camhd.ipynb)

## TerraClimate

Monthly climate and climatic water balance for global terrestrial surfaces from 1958-2019.

* [Source](http://www.climatologylab.org/terraclimate.html)
* [Documentation](data/terraclimate.md)
* [Notebook](data/terraclimate.ipynb)

## UK Met Office Global Weather Data for COVID-19 Analysis

Data for COVID-19 researchers exploring relationships between COVID-19 and environmental factors.

* [Source](https://medium.com/informatics-lab/met-office-and-partners-offer-data-and-compute-platform-for-covid-19-researchers-83848ac55f5f)
* [Documentation](data/uk-met-covid-19.md)
* [Notebook](data/uk-met-covid-19.ipynb)

## UK Met Office CSSP China 20CRDS

Historical climate data for China, from 1851-2010.

* [Source](https://www.metoffice.gov.uk/research/approach/collaboration/newton/climate-science-for-service-partnership-china)
* [Documentation](data/uk-met-20crds.md)

## High Resolution Electricity Access (HREA)

Settlement-level measures of electricity access, reliability, and usage derived from the nightly VIIRS satellite imagery. 

* [Source](http://www-personal.umich.edu/~brianmin/HREA/index.html)
* [Documentation](data/hrea.md)
* [Notebook](data/hrea.ipynb)

## NatureServe Map of Biodiversity Importance (MoBI)

AI for Earth and partners have assembled a repository of labeled information related to wildlife conservation, particularly wildlife imagery.

* [Source](https://www.natureserve.org/conservation-tools/projects/map-biodiversity-importance)
* [Documentation](data/mobi.md)
* [Notebook](data/mobi.ipynb)

## Labeled Information Library of Alexandria: Biology and Conservation (LILA BC)

AI for Earth and partners have assembled a repository of labeled information related to wildlife conservation, particularly wildlife imagery.

* [lila.science](http://lila.science)

# Legal stuff

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

