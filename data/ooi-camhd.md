# Ocean Observatories Initiative CamHD data

## Overview

Video data from the [Ocean Observatories Initiative](https://oceanobservatories.org/) seafloor camera deployed at [Axial Volcano](https://en.wikipedia.org/wiki/Axial_Seamount) on the Juan de Fuca Ridge.

## Overview

The [OOICloud Project](https://github.com/ooicloud) is making data from the Ocean Observatories Initiative ([OOI](https://oceanobservatories.org)) publicly available on Azure and accessible through a [Pangeo](http://pangeo.io/) interface. A primary goal of the project is to provide these data to the scientific community using a cloud-performant object storage model, and to provide large-scale data-proximate compute capabilities for research investigations. The OOI sensor network consists of 89 scientific platforms with approximately 830 instruments, and provides nearly 5 TB of data each month for the study of the ocean-atmosphere system from the continental margins to the mid-ocean ridges. A core component of OOI is the [Regional Cabled Array](https://oceanobservatories.org/regional-cabled-array/), which uses a fiber-optic cable to connect and power the largest array of networked oceanographic instruments in the world, delivering data in real-time to shore. 

[CamHD](https://oceanobservatories.org/instrument-class/camhd/) is a high-definition video camera connected to the OOI's fiber optic cable at Axial Seamount and provides data that can support a wide range of oceanographic, biological, and geophysical investigations. Every three hours, the camera scans a hydrothermal vent chimney, imaging the entire chimney over the course of about fifteen minutes. The accompanying [sample notebook](ooi-camhd.ipynb) demonstrates how to load video data from CamHD and demonstrates the basic usage of the pycamhd library, which can be used to extract frames from the ProRes-encoded Quicktime files. 


## Storage resources 

All available video files are listed in a [JSON file](https://ooiopendata.blob.core.windows.net/camhd/dbcamhd.json) that has useful information such as the Unix timestamp (seconds) of the first frame in each video, and the total number of frames in each video. Data are stored as bock blobs on Azure Blob storage in the following  container:

`https://ooiopendata.blob.core.windows.net/camhd`

We also provide a read-only SAS (<a href="https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview">shared access signature</a>) token to allow access to NAIP data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2019-12-12&si=camhd-aod-ro&sr=c&sig=zFVfMOqa1YW9mxbEusUsKfPrKjkBFyD2YAUJficSuCo%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).
Large-scale processing using this dataset is best performed in the East US Azure data center, where the data are stored. Computational resources are available at [ooi.pangeo.io](https://ooi.pangeo.io/), and if you are using CamHD data for environmental science applications, you may also consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.


## Pretty picture

<img src="https://oceanobservatories.org/wp-content/uploads/2016/01/HD_Camera_Thermisor_OSMO.jpg" width=650px;><br/>

The HD camera (orange triangular frame) images the 14 ft-tall actively venting hot spring deposit &ldquo;Mushroom&rdquo; located within the caldera for Axial Seamount. The vent rests on an old lava flow. Radiating cracks in the flow are filled with white bacterial mats and small tube worms, marking sites of diffusely flowing fluids that issue from the fractures in the basalt. The 3-D temperature array in the background encloses a tube worm bush, sending 24 temperature measurements live to shore every second.


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=oocamhd%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses - including direct, consequential, special, indirect, incidental, or punitive - resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.

