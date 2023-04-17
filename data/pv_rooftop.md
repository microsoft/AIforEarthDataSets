# PV Rooftop Database

## Overview

The National Renewable Energy Laboratory's (NREL) PV Rooftop Database (PVRDB) is a lidar-derived, geospatially-resolved dataset of suitable roof surfaces and their PV technical potential for 128 metropolitan regions in the United States. The source lidar data and building footprints were obtained by the U.S. Department of Homeland Security Homeland Security Infrastructure Program for 2006-2014. Using GIS methods, NREL identified suitable roof surfaces based on their size, orientation, and shading parameters Gagnon et al. (2016). Standard 2015 technical potential was then estimated for each plane using NREL's System Advisory Model.

The PVRDB is down-loadable by city and year of lidar collection. Four geospatial layers are available for each city and year: 1) the raster extent of the lidar collection, 2) buildings identified from the lidar data, 3) suitable developable planes for each building, and 4) aspect values of the developable planes.

## Storage Resources

The pv-rooftop Dataset is made available in Parquet format in the following container:

`https://nrel.blob.core.windows.net/oedi`

### Data

The data are located in the `pv-rooftops/` directory. The four main datasets are stored in the following subdirectories:

Main datasets
 - `/aspects`
 - `/buildings`
 - `/developable_planes`
 - `/rasd`

Each partition is stored in an individual folder within each subdirectory.

Partitions

- `/city_year=<city>_<state>_<year>`

e.g. `/city_year=dover_de_09`

### Data Format

The PV Rooftops dataset is provided in geoparquet format partitioned by city_year. There are 4 core datasets:
 
#### `oedi/pv-rooftop/aspects`
field | data_type | description
-- | -- | --
`gid` | bigint |  
`city` | string | city of source lidar dataset
`state` | string | state of source lidar dataset
`year` | bigint | year of source lidar dataset
`bldg_fid` | bigint | building id
`aspect` | bigint | aspect value
`the_geom_96703` | string | projected geometry ([US Contiguous Albers Equal Area Conic - SRID 6703](https://spatialreference.org/ref/sr-org/6703/))
`the_geom_4326` | string | geometry ([WGS 1984 - SRID   4326](https://spatialreference.org/ref/epsg/4326/))
`region_id` | bigint |  


#### `oedi/pv-rooftop/buildings`

field | data_type | description
-- | -- | --
`gid` | bigint |  
`bldg_fid` | bigint | the building fid
`the_geom_96703` | string | projected geometry ([US Contiguous Albers Equal Area Conic - SRID 6703](https://spatialreference.org/ref/sr-org/6703/))
`the_geom_4326` | string | geometry ([WGS 1984 - SRID   4326](https://spatialreference.org/ref/epsg/4326/))
`city` | string | the city of the source lidar data
`state` | string | the state of the source lidar data
`year` | bigint | the year of the source lidar data
`region_id` | bigint |  


#### `oedi/pv-rooftop/developable_planes`

field | data_type | description
-- | -- | --
`bldg_fid` | bigint | building ID associated with the developable plane
`footprint_m2` | double | developable plane footprint area (m2)
`slope` | bigint | slope value
`flatarea_m2` | double | flat area of the developable plane (m2)
`slopeconversion` | double | the slope conversion factor used to convert the flat area into the sloped   area
`slopearea_m2` | double | sloped area of the developable plane (m2)
`zip` | string | zipcode
`zip_perc` | double |  
`aspect` | bigint | the aspect value of the developable plane
`gid` | bigint | unique developable plane ID
`city` | string | the city of the source lidar data
`state` | string | the state of the source lidar data
`year` | bigint | the year of the source lidar data
`region_id` | bigint |  
`the_geom_96703` | string | projected geometry ([US Contiguous Albers Equal Area Conic - SRID 6703](https://spatialreference.org/ref/sr-org/6703/))
`the_geom_4326` | string | geometry ([WGS 1984 - SRID   4326](https://spatialreference.org/ref/epsg/4326/))


#### `oedi/pv-rooftop/rasd`

field | data_type | description
-- | -- | --
`gid` | bigint | the unique geographic ID of the raster domain
`the_geom_96703` | string | projected geometry ([US Contiguous Albers Equal Area Conic - SRID 6703](https://spatialreference.org/ref/sr-org/6703/))
`the_geom_4326` | string | geometry ([WGS 1984 - SRID   4326](https://spatialreference.org/ref/epsg/4326/))
`city` | string | the city of the source lidar data
`state` | string | the state of the source lidar data
`year` | bigint | the year of the source lidar data
`region_id` | bigint |  
`serial_id` | bigint |  
`__index_level_0__` | bigint |  


Within each core dataset there are paritions by city_state_year(YY) that can be queried using Apache pyarrow tools or dask, or downloaded as individual geoparquet format data files.

Aspects Lookup:
```
1	337.5 - 22.5	north
2	22.5 - 67.5	northeast
3	67.5 - 112.5	east
4	112.5 - 157.5 southeast
5	157.5 - 202.5	south
6	202.5 - 247.5	southwest
7	247.5 - 292.5	west
8	292.5 - 337.5	northwest
0	flat	flat
```

Regions Lookup:
```
1	Albany	NY	2006-01-01
2	Albany	NY	2013-01-01
3	Albuquerque	NM	2006-01-01
4	Albuquerque	NM	2012-01-01
5	Allentown	PA	2006-01-01
6	Amarillo	TX	2008-01-01
7	Anaheim	CA	2010-01-01
8	Arnold	MO	2006-01-01
9	Atlanta	GA	2008-01-01
10	Atlanta	GA	2013-01-01
11	Augusta	GA	2010-01-01
12	Augusta	ME	2008-01-01
13	Austin	TX	2006-01-01
14	Austin	TX	2012-01-01
15	Bakersfield	CA	2010-01-01
16	Baltimore	MD	2008-01-01
17	Baltimore	MD	2013-01-01
18	Baton Rouge	LA	2006-01-01
19	Baton Rouge	LA	2012-01-01
20	Birmingham	AL	2008-01-01
21	Bismarck	ND	2008-01-01
22	Boise	ID	2007-01-01
23	Boise	ID	2013-01-01
24	Boulder	CO	2014-01-01
25	Bridgeport	CT	2006-01-01
26	Bridgeport	CT	2013-01-01
27	Buffalo	NY	2008-01-01
28	Carson City	NV	2009-01-01
29	Charleston	SC	2010-01-01
30	Charleston	WV	2009-01-01
31	Charlotte	NC	2006-01-01
32	Charlotte	NC	2012-01-01
33	Cheyenne	WY	2008-01-01
34	Chicago	IL	2008-01-01
35	Chicago	IL	2012-01-01
36	Cincinnati	OH	2010-01-01
37	Cleveland	OH	2012-01-01
38	Colorado Springs	CO	2006-01-01
39	Colorado Springs	CO	2013-01-01
40	Columbia	SC	2009-01-01
41	Columbus	GA	2009-01-01
42	Columbus	OH	2006-01-01
43	Columbus	OH	2012-01-01
44	Concord	NH	2009-01-01
45	Corpus Christi	TX	2012-01-01
46	Dayton	OH	2006-01-01
47	Dayton	OH	2012-01-01
48	Denver	CO	2012-01-01
49	Des Moines	IA	2010-01-01
50	Detroit	MI	2012-01-01
51	Dover	DE	2009-01-01
52	El Paso	TX	2007-01-01
53	Flint	MI	2009-01-01
54	Fort Wayne	IN	2008-01-01
55	Frankfort	KY	2012-01-01
56	Fresno	CA	2006-01-01
57	Fresno	CA	2013-01-01
58	Ft Belvoir	DC	2012-01-01
59	Grand Rapids	MI	2013-01-01
60	Greensboro	NC	2009-01-01
61	Harrisburg	PA	2009-01-01
62	Hartford	CT	2006-01-01
63	Hartford	CT	2013-01-01
64	Helena	MT	2007-01-01
65	Helena	MT	2013-01-01
66	Houston	TX	2010-01-01
67	Huntsville	AL	2009-01-01
68	Indianapolis	IN	2006-01-01
69	Indianapolis	IN	2012-01-01
70	Jackson	MS	2007-01-01
71	Jacksonville	FL	2010-01-01
72	Jefferson City	MO	2008-01-01
73	Kansas City	MO	2010-01-01
74	Kansas City	MO	2012-01-01
75	LaGuardia JFK	NY	2012-01-01
76	Lancaster	PA	2010-01-01
77	Lansing	MI	2007-01-01
78	Lansing	MI	2013-01-01
79	Las Vegas	NV	2009-01-01
80	Lexington	KY	2012-01-01
81	Lincoln	NE	2008-01-01
82	Little Rock	AR	2008-01-01
83	Los Angeles	CA	2007-01-01
84	Louisville	KY	2006-01-01
85	Louisville	KY	2012-01-01
86	Lubbock	TX	2008-01-01
87	Madison	WI	2010-01-01
88	Manhattan	NY	2007-01-01
89	McAllen	TX	2008-01-01
90	Miami	FL	2009-01-01
91	Milwaukee	WI	2007-01-01
92	Milwaukee	WI	2013-01-01
93	Minneapolis	MN	2007-01-01
94	Minneapolis	MN	2012-01-01
95	Mission Viejo	CA	2013-01-01
96	Mobile	AL	2010-01-01
97	Modesto	CA	2010-01-01
98	Montgomery	AL	2007-01-01
99	Montpelier	VT	2009-01-01
100	Newark	NJ	2007-01-01
101	New Haven	CT	2007-01-01
102	New Haven	CT	2013-01-01
103	New Orleans	LA	2008-01-01
104	New Orleans	LA	2012-01-01
105	New York	NY	2005-01-01
106	New York	NY	2013-01-01
107	Norfolk	VA	2007-01-01
108	Oklahoma City	OK	2007-01-01
109	Oklahoma City	OK	2013-01-01
110	Olympia	WA	2010-01-01
111	Omaha	NE	2007-01-01
112	Omaha	NE	2013-01-01
113	Orlando	FL	2009-01-01
114	Oxnard	CA	2010-01-01
115	Palm Bay	FL	2010-01-01
116	Pensacola	FL	2009-01-01
117	Philadelphia	PA	2007-01-01
118	Pierre	SD	2008-01-01
119	Pittsburgh	PA	2004-01-01
120	Pittsburgh	PA	2012-01-01
121	Portland	OR	2012-01-01
122	Poughkeepsie	NY	2012-01-01
123	Providence	RI	2004-01-01
124	Providence	RI	2012-01-01
125	Raleigh-Durham	NC	2010-01-01
126	Reno	NV	2007-01-01
127	Richmond	VA	2008-01-01
128	Richmond	VA	2013-01-01
129	Rochester	NY	2008-01-01
130	Rochester	NY	2014-01-01
131	Sacramento	CA	2012-01-01
132	Salem	OR	2008-01-01
133	Salt Lake City	UT	2012-01-01
134	San Antonio	TX	2008-01-01
135	San Antonio	TX	2013-01-01
137	San Diego	CA	2008-01-01
138	San Diego	CA	2013-01-01
139	San Francisco	CA	2013-01-01
140	Santa Fe	NM	2009-01-01
141	Sarasota	FL	2009-01-01
142	Scranton	PA	2008-01-01
143	Seattle	WA	2011-01-01
144	Shreveport	LA	2008-01-01
145	Spokane	WA	2008-01-01
146	Springfield	IL	2009-01-01
147	Springfield	MA	2007-01-01
148	Springfield	MA	2013-01-01
149	St Louis	MO	2008-01-01
150	St Louis	MO	2013-01-01
151	Stockton	CA	2010-01-01
152	Syracuse	NY	2008-01-01
153	Tallahassee	FL	2009-01-01
154	Tampa	FL	2008-01-01
155	Toledo	OH	2006-01-01
156	Toledo	OH	2012-01-01
157	Topeka	KS	2008-01-01
158	Trenton	NJ	2008-01-01
159	Tucson	AZ	2007-01-01
160	Tulsa	OK	2008-01-01
161	Washington	DC	2009-01-01
162	Washington	DC	2012-01-01
163	Wichita	KS	2012-01-01
164	Winston-Salem	NC	2009-01-01
165	Worcester	MA	2009-01-01
166	Youngstown	OH	2008-01-01
167	Andrews AFB	DC	2012-01-01
136	San Bernardino-Riverside	CA	2012-01-01
168	Tampa	FL	2013-01-01
```


## Sample code

A complete Python example of accessing and visualizing some of these data is available in the accompanying [sample notebook](https://nbviewer.jupyter.org/github/microsoft/AIforEarthDataSets/blob/main/data/pv_rooftop.ipynb).

## Mounting the container

We also provide a read-only SAS (shared access signature) token to allow access via, e.g., [BlobFuse](https://github.com/Azure/azure-storage-fuse), which allows you to mount blob containers as drives:

`https://nrel.blob.core.windows.net/oedi?sv=2019-12-12&si=oedi-ro&sr=c&sig=uslpLxKf3%2Foeu79ufIHbJkpI%2FTWDH3lblJMa5KQRPmM%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

## References

Main References:
1. [Rooftop Solar Photovoltaic Technical Potential in the United States: A Detailed Assessment](https://www.nrel.gov/docs/fy16osti/65298.pdf)

2. [Using GIS-based methods and lidar data to estimate rooftop solar technical potential in US cities](https://iopscience.iop.org/article/10.1088/1748-9326/aa7225/pdf)

3. [Estimating rooftop solar technical potential across the US using a combination of GIS-based methods, lidar data, and statistical modeling](https://iopscience.iop.org/article/10.1088/1748-9326/aaa554/pdf)

4. [Rooftop Photovoltaic Technical Potential in the United States](https://data.nrel.gov/submissions/121)

5. [U.S. PV-Suitable Rooftop Resources](https://data.nrel.gov/submissions/47)

Related Reference:

1. [Rooftop Solar Technical Potential for Low-to-Moderate Income Households in the United States](https://www.nrel.gov/docs/fy18osti/70901.pdf)

2. [Rooftop Energy Potential of Low Income Communities in America REPLICA](https://data.nrel.gov/submissions/81)

3. [Puerto Rico Solar-for-All: LMI PV Rooftop Technical Potential and Solar Savings Potential](https://data.nrel.gov/submissions/144)


## Disclaimer and Attribution

Copyright (c) 2020, Alliance for Sustainable Energy LLC, All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


## Contact

For questions about this dataset, contact [`aiforearthdatasets@microsoft.com`](mailto:aiforearthdatasets@microsoft.com?subject=oedi%20question).


## Notices

Microsoft provides this dataset on an "as is" basis.  Microsoft makes no warranties (express or implied), guarantees, or conditions with respect to your use of the dataset.  To the extent permitted under your local law, Microsoft disclaims all liability for any damages or losses * including direct, consequential, special, indirect, incidental, or punitive * resulting from your use of this dataset.  This dataset is provided under the original terms that Microsoft received source data.