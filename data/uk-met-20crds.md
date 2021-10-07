# UK Met Office CSSP China 20CRDS dataset

## Overview

This data facilitates the exploration of climate variability over China and surrounding countries from 1851-2010.

## License

Users are required to acknowledge the Met Office as the source of these data by including the following attribution statement in any resulting products, publications or applications: “Contains Met Office data licensed under the Open Government Licence v2.0”.

This data is made available under the [Open Government License version 2](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/).

## About the data

This dataset covers the whole of China for the period 1851 to 2010 at a horizontal resolution of 25 km. For more details see <a href="https://journals.ametsoc.org/view/journals/apme/58/10/jamc-d-19-0083.1.xml">Amato et al, 2019</a>.

The dataset include monthly, daily, three-hourly, and hourly frequencies for the historical period of 1851-2010. Data are stored in <a href="https://zarr.readthedocs.io/en/stable/">Zarr</a> format and contain the following variables:

<table>
  <tr>
    <th>Variable</th>
    <th>Description</th>
    <th>Frequency</th>
  </tr>
  <tr>
    <td>cape</td>
    <td>Atmosphere-specific dilute convective available potential energy</td>
    <td>daily</td>
  </tr>
  <tr>
    <td>pr</td>
    <td>Precipitation rate</td>
    <td>daily, monthly</td>
  </tr>
  <tr>
    <td>prmsl</td>
    <td>Air pressure at sea level</td>
    <td>daily, monthly, three-hourly</td>
  </tr>
  <tr>
    <td>ps</td>
    <td>Surface air pressure</td>
    <td>daily, monthly</td>
  </tr>
  <tr>
    <td>rh850</td>
    <td>Relative humidity at 850 hPa</td>
    <td>daily, monthly</td>
  </tr>
  <tr>
    <td>t2m</td>
    <td>Air temperature at 2 meters above the surface</td>
    <td>daily, monthly, three-hourly</td>
  </tr>
  <tr>
    <td>t850</td>
    <td>Air temperature at 850 hPa</td>
    <td>daily, monthly</td>
  </tr>
  <tr>
    <td>u250</td>
    <td>Eastward wind at 250 hPa</td>
    <td>daily, monthly</td>
  </tr>
  <tr>
    <td>u850</td>
    <td>Eastward wind at 850 hPa</td>
    <td>daily, monthly</td>
  </tr>
  <tr>
    <td>v250</td>
    <td>Northward wind at 250 hPa</td>
    <td>daily, monthly</td>
  </tr>
  <tr>
    <td>v850</td>
    <td>Northward wind at 850 hPa</td>
    <td>daily, monthly</td>
  </tr>
  <tr>
    <td>z200</td>
    <td>Geopotential height at 200 hPa</td>
    <td>daily, monthly</td>
  </tr>
  <tr>
    <td>z500</td>
    <td>Geopotential height at 500 hPa</td>
    <td>daily, monthly</td>
  </tr>
  <tr>
    <td>z1000</td>
    <td>Geopotential height at 1000 hPa</td>
    <td>daily, monthly</td>
  </tr>
  <tr>
    <td>ts</td>
    <td>Surface temperature</td>
    <td>daily, monthly</td>
  </tr>
  <tr>
    <td>rh1.5</td>
    <td>Relative humidity at 1.5 meters</td>
    <td>daily, monthly, three-hourly</td>
  </tr>
  <tr>
    <td>sh1.5</td>
    <td>Specific humidity at 1.5 meters</td>
    <td>daily, monthly, three-hourly</td>
  </tr>
  <tr>
    <td>u10m</td>
    <td>u component of 10m wind</td>
    <td>daily, monthly, Hourly</td>
  </tr>
  <tr>
    <td>v10m</td>
    <td>v component of 10m wind</td>
    <td>daily, monthly, Hourly</td>
  </tr>
  <tr>
    <td>clt</td>
    <td>Cloud area fraction</td>
    <td>daily, monthly, three-hourly</td>
  </tr>
  <tr>
    <td>rsds</td>
    <td>Surface downwelling shortwave radiation</td>
    <td>daily, monthly, three-hourly</td>
  </tr>
  <tr>
    <td>rlds</td>
    <td>Surface downwelling longwave radiation</td>
    <td>daily, monthly, three-hourly</td>
  </tr>
  <tr>
    <td>omega500</td>
    <td>Langrangean tendency of air pressure at 500 hPa</td>
    <td>daily, monthly</td>
  </tr>
</table>

For more information about CSSP China project, see the <a href=https://www.metoffice.gov.uk/research/approach/collaboration/newton/cssp-china/index>
       CSSP China homepage</a>.
	   
Jupyter Notebooks to access and analysis the data are available on <a href=https://github.com/MetOffice/PyPRECIS/tree/master/notebooks/CSSP_20CRDS_Tutorials>GitHub</a>.


## Storage location

This dataset is stored in the East US 2 Azure region, in the following blob container:

`https://metdatasa.blob.core.windows.net/metoffice-20cr-ds`

Allocating compute resources in East US 2 is recommended for affinity. 


## How the data is organized

The root of the container includes folders for each time scale: `hourly`, `3hrly`, `6hrly`, `daily`, and `monthly`.  Each of these folders represents a Zarr dataset, with one variable or aggregated variable per folder.  For example, the folder: 

`https://metdatasa.blob.core.windows.net/metoffice-20cr-ds/daily/surface_temperature_max`

...contains maximum surface temperature at daily granularity.


## Contact information

For questions, please contact us at <a href="mailto:enquiries@metoffice.gov.uk">enquiries@metoffice.gov.uk</a>.</p>


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.

