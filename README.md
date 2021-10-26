# AI for Earth Data Sets

The <a href="http://aka.ms/aiforearth">Microsoft AI for Earth program</a> hosts geospatial data on Azure that is important to environmental sustainability and Earth science.  This repo hosts documentation and demonstration notebooks for all the data that is managed by AI for Earth.  It also serves as a "staging ground" for the [Planetary Computer Data Catalog](https://planetarycomputer.microsoft.com/catalog).

If you have feedback about any of this data, or want to request additions to our data program, email [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=data%20question).


# Table of contents

* [ASTER L1T (2000-2006)](#aster-l1t-2000-2006)
* [Daymet](#daymet)
* [Deltares Global Flood Maps](#deltares-global-flood-maps)
* [Esri 10m Land Cover](#esri-10m-land-cover)
* [Global Biodiversity Information Facility (GBIF)](#global-biodiversity-information-facility-gbif)
* [Harmonized Global Biomass](#harmonized-global-biomass)
* [Harmonized Landsat Sentinel-2](#harmonized-landsat-sentinel-2)
* [High Resolution Electricity Access (HREA)](#high-resolution-electricity-access-hrea)
* [High Resolution Ocean Surface Wave Hindcast](#high-resolution-ocean-surface-wave-hindcast)
* [Labeled Information Library of Alexandria: Biology and Conservation (LILA BC)](#labeled-information-library-of-alexandria-biology-and-conservation-lila-bc)
* [Landsat TM/MSS Collection 2](#landsat-tmmss-collection-2)
* [Landsat 7 Collection 2 Level-2](#landsat-7-collection-2-level-2)
* [Landsat 8 Collection 2 Level-2](#landsat-8-collection-2-level-2)
* [MODIS (40 individual products)](#modis-40-individual-products)
* [Monitoring Trends in Burn Severity Mosaics](#monitoring-trends-in-burn-severity-mosaics)
* [National Solar Radiation Database](#national-solar-radiation-database)
* [NASADEM](#nasadem)
* [NOAA Climate Data Records (CDR)](#noaa-climate-data-records-cdr)
* [NOAA Climate Forecast System (CFS)](#noaa-climate-forecast-system-cfs)
* [NOAA GFS Warm Start Initial Conditions](#noaa-gfs-warm-start-initial-conditions)
* [NOAA GOES-R](#noaa-goes-r)
* [NOAA Global Ensemble Forecast System (GEFS)](#noaa-global-ensemble-forecast-system-gefs)
* [NOAA Global Forecast System (GFS)](#noaa-global-forecast-system-gfs)
* [NOAA Global Hydro Estimator](#noaa-global-hydro-estimator-ghe)
* [NOAA High-Resolution Rapid Refresh (HRRR)](#noaa-high-resolution-rapid-refresh-hrrr)
* [NOAA Integrated Surface Data (ISD)](#noaa-integrated-surface-data-isd)
* [NOAA Monthly US Climate Gridded Dataset (NClimGrid)](#noaa-monthly-us-climate-gridded-dataset-nclimgrid)
* [NOAA Rapid Refresh (RAP)](#noaa-rapid-refresh-rap)
* [NOAA US Climate Normals](#noaa-us-climate-normals)
* [National Agriculture Imagery Program](#national-agriculture-imagery-program)
* [National Land Cover Database](#national-land-cover-database)
* [NatureServe Map of Biodiversity Importance (MoBI)](#natureserve-map-of-biodiversity-importance-mobi)
* [Ocean Observatories Initiative CamHD](#ocean-observatories-initiative-camhd)
* [Sentinel-1 GRD](#sentinel-1-grd)
* [Sentinel-1 SLC](#sentinel-1-slc)
* [Sentinel-2 L2A](#sentinel-2-l2a)
* [Sentinel-3 L2](#sentinel-3-l2)
* [Sentinel-5P](#sentinel-5p)
* [TerraClimate](#terraclimate)
* [UK Met Office CSSP China 20CRDS](#uk-met-office-cssp-china-20crds)
* [UK Met Office Global Weather Data for COVID-19 Analysis](#uk-met-office-global-weather-data-for-covid-19-analysis)
* [University of Miami Coupled Model for Hurricanes Ike and Sandy](#university-of-miami-coupled-model-for-hurricanes-ike-and-sandy)
* [USFS Forest Inventory and Analysis](#usfs-forest-inventory-and-analysis)
* [USGS 3DEP Seamless DEMs](#usgs-3dep-seamless-dems)
* [USGS Gap Land Cover](#usgs-gap-land-cover)


# Data sets

## ASTER L1T (2000-2006)

The [ASTER](https://terra.nasa.gov/about/terra-instruments/aster) instrument, launched on-board NASA's [Terra](https://terra.nasa.gov/) satellite in 1999, provides multispectral images of the Earth at 15m-90m resolution.  This data set represents ASTER data from 2000-2006.

* [Source](https://terra.nasa.gov/about/terra-instruments/aster)
* [Documentation](data/aster.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/aster.ipynb)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/aster-l1t)

## Daymet

Estimates of daily weather parameters in North America on a one-kilometer grid, with monthly and annual summaries.

* [Source](https://daymet.ornl.gov/)
* [Documentation](data/daymet.md)
* [Notebook (Zarr)](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/daymet-zarr.ipynb)
* [Notebook (NetCDF)](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/daymet-nc.ipynb)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/group/daymet)

## Deltares Global Flood Maps

Global estimates of coastal inundation under various sea level rise conditions and return periods at 90m, 1km, and 5km resolutions. Also includes estimated coastal inundation caused by named historical storm events going back several decades.

* [Source](https://www.deltares.nl/en/)
* [Documentation](data/deltares-floods.md)
* [Notebook (NetCDF)](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/deltares-floods.ipynb)

## Esri 10m Land Cover

Global estimates of 10-class land use/land cover (LULC) for 2020, derived from ESA Sentinel-2 imagery at 10m resolution, produced by [Impact Observatory](impactobservatory.com).

* [Source](https://livingatlas.arcgis.com/landcover/)
* [Documentation](data/io-lulc.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/io-lulc.ipynb)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/io-lulc)

## Global Biodiversity Information Facility (GBIF)

Exports of global species occurrence data from the GBIF network.

* [Source](https://www.gbif.org)
* [Documentation](data/gbif.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/gbif.ipynb)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/gbif)

## Harmonized Global Biomass

Global maps of aboveground and belowground biomass carbon density for the year 2010 at 300m resolution.

* [Source](https://www.nature.com/articles/s41597-020-0444-4)
* [Documentation](data/hgb.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/hgb.ipynb)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/hgb)

## Harmonized Landsat Sentinel-2

Satellite imagery from the Landsat 8 and Sentinel-2 satellites, aligned to a common grid and processed to compatible color spaces.

* [Source](https://hls.gsfc.nasa.gov/)
* [Documentation](data/hls.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/hls.ipynb)

## High Resolution Electricity Access (HREA)

Settlement-level measures of electricity access, reliability, and usage derived from VIIRS satellite imagery.

* [Source](http://www-personal.umich.edu/~brianmin/HREA/index.html)
* [Documentation](data/hrea.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/hrea.ipynb)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/hrea)

## High Resolution Ocean Surface Wave Hindcast

Long-term wave hindcast data for the U.S. Exclusive Economic Zone (EEZ), developed by the U.S. Department of Energy's Water Power Technologies Office.

* [Source](https://github.com/openEDI/documentation/blob/main/US_Wave.md)
* [Documentation](data/doe-wave.md)

## Labeled Information Library of Alexandria: Biology and Conservation (LILA BC)

AI for Earth and partners have assembled a repository of labeled information related to wildlife conservation, particularly wildlife imagery.

* [lila.science](http://lila.science)

## Landsat TM/MSS Collection 2

Global optical imagery from the Landsat MSS and TM instruments, which imaged the Earth from 1972 to 2013, aboard the Landsat 1-5 satellites.

Landsat TM/MSS data are in preview; access is granted by request.

* [Source](https://landsat.gsfc.nasa.gov/)
* [Documentation](data/landsat-tm-mss.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/landsat-tm-mss.ipynb)

## Landsat 7 Collection 2 Level-2

Global optical imagery from the Landsat 7 satellite, which has imaged the Earth since 1999.

Landsat 7 data are in preview; access is granted by request.

* [Source](https://landsat.gsfc.nasa.gov/)
* [Documentation](data/landsat-7.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/landsat-7.ipynb)

## Landsat 8 Collection 2 Level-2

Global optical imagery from the Landsat 8 satellite, which has imaged the Earth since 2013.

* [Source](https://landsat.gsfc.nasa.gov/)
* [Documentation](data/landsat-8.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/landsat-8.ipynb)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/landsat-8-c2-l2)

## MODIS (40 individual products)

Satellite imagery from the Moderate Resolution Imaging Spectroradiometer (MODIS).

* [Source](https://modis.gsfc.nasa.gov/)
* [Documentation](data/modis.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/modis.ipynb)

## Monitoring Trends in Burn Severity Mosaics

Annual burn severity mosaics for the continental United States and Alaska.

* [Source](https://www.mtbs.gov/)
* [Documentation](data/mtbs.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/mtbs.ipynb)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/mtbs)

## National Solar Radiation Database

Hourly and half-hourly values of the three most common measurements of solar radiation – global horizontal, direct normal, and diffuse horizontal irradiance - along with meteorological data.

* [Source](https://nsrdb.nrel.gov/)
* [Documentation](data/nsrdb.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/nsrdb.ipynb)

## NASADEM

Global topographic information from the NASADEM program.

* [Source](https://earthdata.nasa.gov/esds/competitive-programs/measures/nasadem)
* [Documentation](data/nasadem.md)
* [Notebook (COG)](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/nasadem-cog.ipynb)
* [Notebook (NetCDF)](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/nasadem-nc.ipynb)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/nasadem)

## NOAA Climate Data Records (CDR)

Historical global climate information.

* [Source](https://www.ncei.noaa.gov/products/climate-data-records)
* [Documentation](data/noaa-cdr.md)

## NOAA Climate Forecast System (CFS)

Model output data from the [NOAA NCEP Climate Forecast System Version 2](https://cfs.ncep.noaa.gov/).

* [Source](https://cfs.ncep.noaa.gov/)
* [Documentation](data/noaa-cfs.md)

## NOAA GFS Warm Start Initial Conditions

Warm start initial conditions for the [NOAA Global Forecast System](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs).

* [Source](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs)
* [Documentation](data/gfs-warm-start.md)

## NOAA GOES-R

Weather imagery from the GOES-16 and GOES-17 satellites.

* [Source](https://www.nesdis.noaa.gov/GOES-R-Series-Satellites)
* [Documentation](data/goes-r.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/goes-r-abi-l2-mcmipf.ipynb)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/goes-cmi)

## NOAA Global Ensemble Forecast System (GEFS)

Model output data from the [NOAA Global Ensemble Forecast System](https://www.ncei.noaa.gov/products/weather-climate-models/global-ensemble-forecast).

* [Source](https://www.ncei.noaa.gov/products/weather-climate-models/global-ensemble-forecast)
* [Documentation](data/noaa-gefs.md)

## NOAA Global Forecast System (GFS)

Model output data from the [NOAA Global Forecast System](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs).

* [Source](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs)
* [Documentation](data/noaa-gfs.md)

## NOAA Global Hydro Estimator (GHE)

Global rainfall estimates in 15-minute intervals.

* [Source](https://www.ospo.noaa.gov/Products/atmosphere/ghe/)
* [Documentation](data/ghe.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/ghe.ipynb)

## NOAA High-Resolution Rapid Refresh (HRRR)

Weather forecasts for North America at 3km spatial resolution and 15 minute temporal resolution.

* [Source](https://www.nco.ncep.noaa.gov/pmb/products/hrrr/)
* [Documentation](data/noaa-hrrr.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/noaa-hrrr.ipynb)

## NOAA Integrated Surface Data (ISD)

Historical global weather information.

* [Source](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database)
* [Documentation](data/noaa-isd.md)


## NOAA Monthly US Climate Gridded Dataset (NClimGrid)

Gridded climate data for the US from 1895 to the present.

* [Source](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00332)
* [Documentation](data/noaa-nclimgrid.md)

## NOAA Rapid Refresh (RAP)

Weather forecasts for North America at 13km resolution.

* [Source](https://www.nco.ncep.noaa.gov/pmb/products/rap/)
* [Documentation](data/noaa-rap.md)

## NOAA US Climate Normals

Typical climate conditions for the United States from 1981 to the present.

* [Source](https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals)
* [Documentation](data/noaa-climatenormals.md)

## National Agriculture Imagery Program

NAIP provides US-wide, high-resolution aerial imagery.  This data set includes NAIP images from 2010 to the present.

* [Source](https://www.fsa.usda.gov/programs-and-services/aerial-photography/imagery-programs/naip-imagery/)
* [Documentation](data/naip.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/naip.ipynb)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/naip)

## National Land Cover Database

US-wide data on land cover and land cover change at a 30m resolution with a 16-class legend.

* [Source](https://www.mrlc.gov/)
* [Documentation](data/nlcd.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/nlcd.ipynb)

## NatureServe Map of Biodiversity Importance (MoBI)

Habitat information for 2,216 imperiled species occurring in the conterminous United States.

* [Source](https://www.natureserve.org/conservation-tools/projects/map-biodiversity-importance)
* [Documentation](data/mobi.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/mobi.ipynb)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/mobi)

## Ocean Observatories Initiative CamHD

Video data from the [Ocean Observatories Initiative](https://oceanobservatories.org/) seafloor camera deployed at [Axial Volcano](https://en.wikipedia.org/wiki/Axial_Seamount) on the Juan de Fuca Ridge.

* [Source](https://oceanobservatories.org/instrument-class/camhd/)
* [Documentation](data/ooi-camhd.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/ooi-camhd.ipynb)

## Sentinel-1 GRD

Global synthetic aperture radar (SAR) data from 2017-present, projected to ground range.

Sentinel-1 GRD data are in preview; access is granted by request.

* [Source](https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-1-sar/products-algorithms/level-1-algorithms/ground-range-detected)
* [Documentation](data/sentinel-1-grd.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/sentinel-1-grd.ipynb)

## Sentinel-1 SLC

Global synthetic aperture radar (SAR) data for the last 90 days.

Sentinel-1 SLC data are in preview; access is granted by request.

* [Source](https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-1-sar/products-algorithms/level-1-algorithms/single-look-complex)
* [Documentation](data/sentinel-1-slc.md)

## Sentinel-2 L2A

Global optical imagery at 10m resolution from 2016-present.

* [Source](https://sentinel.esa.int/web/sentinel/missions/sentinel-2)
* [Documentation](data/sentinel-2.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/sentinel-2.ipynb)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/sentinel-2-l2a)

## Sentinel-3 L2

Global multispectral imagery at 300m resolution, with a revisit rate of less than two days, from 2016-present.

Sentinel-3 data are in preview; access is granted by request.

* [Source](https://sentinel.esa.int/web/sentinel/missions/sentinel-3)
* [Documentation](data/sentinel-3.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/sentinel-3.ipynb)

## Sentinel-5P

Global atmospheric data from 2018-present.

Sentinel-5P data are in preview; access is granted by request.

* [Source](https://sentinel.esa.int/web/sentinel/missions/sentinel-5p)
* [Documentation](data/sentinel-5p.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/sentinel-5p.ipynb)

## TerraClimate

Monthly climate and climatic water balance for global terrestrial surfaces from 1958-2019.

* [Source](http://www.climatologylab.org/terraclimate.html)
* [Documentation](data/terraclimate.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/terraclimate.ipynb)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/terraclimate)

## UK Met Office CSSP China 20CRDS

Historical climate data for China, from 1851-2010.

* [Source](https://www.metoffice.gov.uk/research/approach/collaboration/newton/climate-science-for-service-partnership-china)
* [Documentation](data/uk-met-20crds.md)

## UK Met Office Global Weather Data for COVID-19 Analysis

Data for COVID-19 researchers exploring relationships between COVID-19 and environmental factors.

* [Source](https://medium.com/informatics-lab/met-office-and-partners-offer-data-and-compute-platform-for-covid-19-researchers-83848ac55f5f)
* [Documentation](data/uk-met-covid-19.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/uk-met-covid-19.ipynb)

## University of Miami Coupled Model for Hurricanes Ike and Sandy

Modeled wind, wave, and current data for Hurricanes Ike and Sandy, produced by the National Renewable Energy Laboratory.

* [Source](https://github.com/openEDI/documentation/blob/main/UMCM_Hurricanes.md)
* [Documentation](data/umcm-hurricanes.md)

## USFS Forest Inventory and Analysis

Status and trends on U.S. forest location, health, growth, mortality, and production, from the US Forest Service's  [Forest Inventory and Analysis](https://www.fia.fs.fed.us/) (FIA) program.

* [Source](https://www.fia.fs.fed.us/)
* [Documentation](data/forest-inventory-and-analysis.md)
* [Notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/forest-inventory-and-analysis.ipynb)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/fia)

## USGS 3DEP Seamless DEMs

* [Source](https://www.usgs.gov/core-science-systems/ngp/3dep)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/3dep-seamless)

## USGS Gap Land Cover

* [Source](https://www.usgs.gov/core-science-systems/science-analytics-and-synthesis/gap/science/land-cover-data-download)
* [Planetary Computer collection](https://planetarycomputer.microsoft.com/dataset/gap)


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
