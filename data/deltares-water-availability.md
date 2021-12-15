# Deltares Global Water Availability

## Overview

[Deltares](https://www.deltares.nl/en/) has produced a hydrological model approach to simulate historical daily reservoir variations for 3,236 locations across the globe for the period 1970-2020 using the distributed [wflow_sbm](https://deltares.github.io/Wflow.jl/dev/model/sbm/) model. The model outputs long-term daily information on reservoir volume, inflow and outflow dynamics, as well as information on upstream hydrological forcing.

They hydrological model was forced with 5 different precipitation products. Two products (ERA5 and CHIRPS) are available at the global scale, while for Europe, USA and Australia a regional product was use (i.e. EOBS, NLDAS and BOM, respectively). Using these different precipitation products, it becomes possible to assess the impact of uncertainty in the model forcing. A different number of basins upstream of reservoirs are simulated, given the spatial coverage of each precipitation product.

See the complete [methodology documentation](https://deltaresreservoirssa.blob.core.windows.net/reservoirs/v2021.12/pc-deltares-water-availability-documentation.pdf) for more information.

## Storage resources

Data are stored in netCDF files in Azure Blob Storage in the West Europe Azure region, in the following folder:

<https://deltaresreservoirssa.blob.core.windows.net/reservoirs/v2021.12/>

Within that folder, data files are organized according to the precipitation product used as the model forcing function, using the following structure:

`reservoirs_[name]`, where `name` can be one of: `ERA5`, `CHIRPS`, `EOBS`, `NLDAS`, or `BOM`.

A fully constructed path would look like this:

<https://deltaresreservoirssa.blob.core.windows.net/reservoirs/v2021.12/reservoirs_BOM.nc>


### Dataset coverages

| Name   | Scale                    | Period    | Number of basins |
|--------|--------------------------|-----------|------------------|
| ERA5   | Global                   | 1967-2020 | 3236             |
| CHIRPS | Global (+/- 50 latitude) | 1981-2020 | 2951             |
| EOBS   | Europe/North Africa      | 1979-2020 | 682              |
| NLDAS  | USA                      | 1979-2020 | 1090             |
| BOM    | Australia                | 1979-2020 | 116              |


### File contents

#### Dimension

| Name          | Description                                         |
|---------------|-----------------------------------------------------|
| `time`        | Daily timesteps corresponding to period             |
| `GrandID`     | GrandID number of the reservoir of interest         |
| `Ksathorfrac` | Five different value lateral anisotropy values used |

#### Variables

| Variable   | Description                                                                    |
|------------|--------------------------------------------------------------------------------|
| `P`        | Average precipitation upstream of reservoir (mm per day)                       |
| `Eta`      | Average simulated actual evapotransporation upstream of reservoir (mm per day) |
| `Snow`     | Average simulated snow depth upstream of reservoir (mm)                        |
| `Melt`     | Average simulated snow melt upstream of reservoir mm per day)                  |
| `Temp`     | Average surface temperature upstream of reservoir (degrees C)                  |
| `P_res`    | Average precipitation into reservoir (mm per day)                              |
| `Ea_res`   | Average simulated actual evapotransporation out of reservoir (mm per day)      |
| `Qout_res` | Simulated reservoir outflow (m3 per s)                                         |
| `Qin_res`  | Simulated reservoir inflow (m3 per s)                                          |
| `S_res`    | Simulated reservoir volume (m3)                                                |
| `FracFull` | Simulated reservoir storage fraction of being full (-)                         |

## Sample code

A complete Python example of accessing and plotting water availability data is available in the accompanying [sample notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/deltares-water-availability.ipynb).

## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=deltares-floods%20question).

## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset. To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset. This dataset is provided under the original terms that Microsoft received source data.
