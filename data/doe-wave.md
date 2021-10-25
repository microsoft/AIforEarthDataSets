# High Resolution Ocean Surface Wave Hindcast

## Overview

This is the highest resolution publicly available long-term wave hindcast dataset that – when complete – will cover the entire U.S. Exclusive Economic Zone (EEZ). The data can be used to investigate the historical record of wave
statistics at any U.S. site. As such, the dataset could also be of value to any entity with marine operations inside the U.S. EEZ.

The development of this dataset was funded by the U.S. Department of Energy, Office of Energy Efficiency and Renewable Energy, [Water Power Technologies Office](https://www.energy.gov/eere/water/water-power-technologies-office) to improve our understanding of U.S. wave energy resources and to provide critical information for wave energy project development and wave energy converter design.

## Technical summary

A technical summary of the dataset is as follows:

* 32-year wave hindcast (1979-2010), 3-hour temporal resolution
* Unstructured grid spatial resolution ranges from 200 meters in shallow water to ~10 km in deep water
* Spatial coverage: EEZ offshore of all U.S territories

The following variables are included in the dataset:

* Mean Wave Direction: Direction normal to the wave crests
* Significant Wave Height: Calculated as the zeroth spectral moment (i.e., H_m0)
* Mean Absolute Period: Calculated as a ratio of spectral moments (m_0/m_1)
* Peak Period: The period associated with the maximum value of the wave energy spectrum
* Mean Zero-Crossing Period: Calculated as a ratio of spectral moments (sqrt(m_0/m_2))
* Energy Period: Calculated as a ratio of spectral moments (m_-1/m_0)
* Directionality Coefficient: Fraction of total wave energy traveling in the direction of maximum wave power
* Maximum Energy Direction: The direction from which the most wave energy is traveling
* Omni-Directional Wave Power: Total wave energy flux from all directions
* Spectral Width: Spectral width characterizes the relative spreading of energy in the wave spectrum

Data are divided into the following regions (parentheses indicate region names as they appear in file paths):

* West Coast United States (`West_Coast`)
* East Coast United States (`Atlantic`)
* Alaskan Coast (`Alaska`)
* Hawaiian Islands (`Hawaii`)

The following regions will be added in future releases:

* Gulf of Mexico, Puerto Rico, and U.S. Virgin Islands
* U.S. Pacific Island Territories


## Model

The multi-scale, unstructured-grid modeling approach using [WaveWatch III](https://polar.ncep.noaa.gov/waves/wavewatch/) and [SWAN](https://www.tudelft.nl/en/ceg/about-faculty/departments/hydraulic-engineering/sections/environmental-fluid-mechanics/research/swan) enabled long-term (decades) high-resolution hindcasts in a large regional domain. In particular, the dataset was generated from the unstructured-grid SWAN model output that was driven by a WaveWatch III model with global-regional nested grids. The unstructured-grid SWAN model simulations were performed with a spatial resolution as fine as 200 meters in shallow waters. The dataset has a 3-hour timestep spanning 32 years from 1979 through 2010.

The models were extensively validated not only for the most common wave parameters, but also six IEC resource parameters and 2D spectra with high quality spectral data derived from publicly available buoys. Additional details
on definitions of the variables found in the dataset, the SWAN and WaveWatch III model configurations and model validation are available in technical report and peer-reviewed publications (see below). This work was funded by the U.S. Department of Energy, Office of Energy Efficiency & Renewable Energy, Water Power Technologies Office under Contract DE-AC05-76RL01830 to Pacific Northwest National Laboratory (PNNL).

## Directory structure

High Resolution Ocean Surface Wave Hindcast data is made available as a series of three-hourly .h5 files in Azure Blob Storage in the East US Azure region, in the following folder:

`https://nrel.blob.core.windows.net/nrel-wave`

Within that container, files are named as:

`v1.0.0/[region]/[region]_wave_[year].h5`

For example, the following file contains data for Hawaii from 1992:

<https://nrel.blob.core.windows.net/nrel-wave/v1.0.0/Hawaii/Hawaii_wave_1992.h5>

Hourly virtual buoy data is also available in hourly .h5 files, names as follows:

`v1.0.0/virtual_buoy/[region]/[region_virtual_boy_[year].h5`

For example, the following file contains virtual buoy data for the U.S. West coast for 1985:

<https://nrel.blob.core.windows.net/nrel-wave/v1.0.0/virtual_buoy/West_Coast/West_Coast_virtual_buoy_1985.h5>


## Data Format

The data is provided in high density data file (.h5) separated by year. The variables mentioned above are provided in two-dimensional time-series arrays with dimensions (time x location). The temporal axis is defined by the `time_index` dataset, while the positional axis is defined by the `coordinate` dataset. The units for the variable data is also provided as an attribute (`units`). The SWAN and IEC variable names are also provide under the attributes `SWAWN_name` and `IEC_name`.


## Mounting the container

We also provide a read-only SAS (shared access signature) token to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://nrel.blob.core.windows.net/nrel-wave?sv=2020-08-04&si=nrel-wave-ro&sr=c&sig=VACZ6rXzsE7l2eFQMvYMQCgy8dT23%2Bs1eDPYa%2FBCnEM%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).



## Citation

Please cite the most relevant publication below when referencing this dataset:

* [Wu W-C, et al. Development and validation of a high-resolution regional wave hindcast model for US West Coast wave resource characterization. Renewable Energy 152 (2020): 736-753.](https://www.osti.gov/biblio/1599105)
* [Yang Z, García-Medina G, Wu W, Wang T.  Characteristics and variability of the Nearshore Wave Resource on the U.S. West Coast. Energy. 2020.](https://doi.org/10.1016/j.energy.2020.117818)
* [Yang Z et al. High-Resolution Regional Wave Hindcast for the US West Coast. No. PNNL-28107. Pacific Northwest National Lab.(PNNL), Richland, WA (United States), 2018.](https://doi.org/10.2172/1573061)
* [Ahn S, Neary VS, Allahdadi N, He R. Nearshore wave energy resource characterization along the East Coast of the United States, Renewable Energy, 2021, 172.](https://doi.org/10.1016/j.renene.2021.03.037)
* [Yang Z, Neary VS. High-resolution hindcasts for U.S. wave energy resource characterization. International Marine Energy Journal, 2020, 3, 65-71.](https://doi.org/10.36688/imej.3.65-71)
* [Allahdadi MN, He R, Neary VS. Predicting ocean waves along the US East Coast during energetic winter storms: sensitivity to whitecapping parameterizations, Ocean Sci., 2019, 15, 691-715.](https://doi.org/10.5194/os-15-691-2019)
* [Allahdadi MN, Gunawan J, Lai J, He R, Neary VS. Development and validation of a regional-scale high-resolution unstructured model for wave energy resource characterization along the US East Coast, Renewable Energy, 2019, 136, 500-511.](https://doi.org/10.1016/j.renene.2019.01.020)


## Disclaimer and Attribution

The National Renewable Energy Laboratory (“NREL”) is operated for the U.S. Department of Energy (“DOE”) by the Alliance for Sustainable Energy, LLC ("Alliance"). Pacific Northwest National Laboratory (PNNL) is managed and operated by Battelle Memorial Institute ("Battelle") for DOE. As such the following rules apply:

This data arose from worked performed under funding provided by the United States Government. Access to or use of this data ("Data") denotes consent with the fact that this data is provided "AS IS," “WHEREIS” AND SPECIFICALLY FREE FROM ANY EXPRESS OR IMPLIED WARRANTY OF ANY KIND, INCLUDING BUT NOT LIMITED TO ANY IMPLIED WARRANTIES SUCH AS MERCHANTABILITY AND/OR FITNESS FOR ANY PARTICULAR PURPOSE. Furthermore, NEITHER THE UNITED STATES GOVERNMENT NOR ANY OF ITS ASSOCITED ENTITES OR CONTRACTORS INCLUDING BUT NOT LIMITED TO THE DOE/PNNL/NREL/BATTELLE/ALLIANCE ASSUME ANY LEGAL LIABILITY OR RESPONSIBILITY FOR THE ACCURACY, COMPLETENESS, OR USEFULNESS OF THE DATA, OR REPRESENT THAT ITS USE WOULD NOT INFRINGE PRIVATELY OWNED RIGHTS. NO ENDORSEMENT OF THE DATA OR ANY REPRESENTATIONS MADE IN CONNECTION WITH THE DATA IS PROVIDED. IN NO EVENT SHALL ANY PARTY BE LIABLE FOR ANY DAMAGES, INCLUDING BUT NOT LIMITED TO SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES ARISING FROM THE PROVISION OF THIS DATA; TO THE EXTENT PERMITTED BY LAW USER AGREES TO INDEMNIFY DOE/PNNL/NREL/BATTELLE/ALLIANCE AND ITS SUBSIDIARIES, AFFILIATES, OFFICERS, AGENTS, AND EMPLOYEES AGAINST ANY CLAIM OR DEMAND RELATED TO USER'S USE OF THE DATA, INCLUDING ANY REASONABLE ATTORNEYS FEES INCURRED.

The user is granted the right, without any fee or cost, to use or copy the Data, provided that this entire notice appears in all copies of the Data. In the event that user engages in any scientific or technical publication utilizing this data user agrees to credit DOE/PNNL/NREL/BATTELLE/ALLIANCE in any such publication consistent with respective professional practice.


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=nlcd%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses * including direct, consequential, special, indirect, incidental, or punitive * resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.
