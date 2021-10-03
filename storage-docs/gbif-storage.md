Data are stored in [Parquet](https://parquet.apache.org/) files in Azure Blob Storage in the West Europe Azure region, in the following blob container:

`https://ai4edataeuwest.blob.core.windows.net/gbif`

Within that container, the periodic occurrence snapshots are stored in `occurrence/YYYY-MM-DD`, where `YYYY-MM-DD` corresponds to the date of the snapshot.

The snapshot includes all CC-BY licensed data published through GBIF that have coordinates which passed automated quality checks.

Each snapshot contains a `citation.txt` with instructions on how best to cite the data, and the data files themselves in Parquet format: `occurrence.parquet/*`.

Therefore, the data files for the first snapshot are at

`https://ai4edataeuwest.blob.core.windows.net/gbif/occurrence/2021-04-13/occurrence.parquet/*`

and the citation information is at

`https://ai4edataeuwest.blob.core.windows.net/gbif/occurrence/2021-04-13/citation.txt`

The Parquet file schema is described below.  Most field names correspond to [terms from the Darwin Core standard](https://dwc.tdwg.org/terms/), and have been interpreted by GBIF's systems to align taxonomy, location, dates etc.
Additional information may be retrived using the [GBIF API](https://www.gbif.org/developer/summary).

|              Field¹              |     Type      | Nullable | Description                   |
|----------------------------------|---------------|----------|-------------------------------|
| gbifid                           | BigInt        | N        | GBIF's identifier for the occurrence |
| datasetkey                       | String (UUID) | N        | GBIF's UUID for the [dataset](https://www.gbif.org/developer/registry#datasets) containing this occurrence |
| publishingorgkey                 | String (UUID) | N        | GBIF's UUID for the [organization](https://www.gbif.org/developer/registry#organizations) publishing this occurrence. |
| occurrencestatus                 | String        | N        | See [dwc:occurrenceStatus](https://dwc.tdwg.org/terms/#occurrenceStatus). Either the value `PRESENT` or `ABSENT`.  **Many users will wish to filter for `PRESENT` data.** |
| basisofrecord                    | String        | N        | See [dwc:basisOfRecord](https://dwc.tdwg.org/terms/#basisOfRecord).  One of `PRESERVED_SPECIMEN`, `FOSSIL_SPECIMEN`, `LIVING_SPECIMEN`, `OBSERVATION`, `HUMAN_OBSERVATION`, `MACHINE_OBSERVATION`, `MATERIAL_SAMPLE`, `LITERATURE`, `UNKNOWN`. |
| kingdom                          | String        | Y        | See [dwc:kingdom](https://dwc.tdwg.org/terms/#kingdom).  This field has been aligned with the [GBIF backbone taxonomy](https://doi.org/10.15468/39omei). |
| phylum                           | String        | Y        | See [dwc:phylum](https://dwc.tdwg.org/terms/#phylum).  This field has been aligned with the GBIF backbone taxonomy. |
| class                            | String        | Y        | See [dwc:class](https://dwc.tdwg.org/terms/#class).  This field has been aligned with the GBIF backbone taxonomy. |
| order                            | String        | Y        | See [dwc:order](https://dwc.tdwg.org/terms/#order).  This field has been aligned with the GBIF backbone taxonomy. |
| family                           | String        | Y        | See [dwc:family](https://dwc.tdwg.org/terms/#family).  This field has been aligned with the GBIF backbone taxonomy. |
| genus                            | String        | Y        | See [dwc:genus](https://dwc.tdwg.org/terms/#genus).  This field has been aligned with the GBIF backbone taxonomy. |
| species                          | String        | Y        | See [dwc:species](https://dwc.tdwg.org/terms/#species).  This field has been aligned with the GBIF backbone taxonomy. |
| infraspecificepithet             | String        | Y        | See [dwc:infraspecificEpithet](https://dwc.tdwg.org/terms/#infraspecificEpithet).  This field has been aligned with the GBIF backbone taxonomy. |
| taxonrank                        | String        | Y        | See [dwc:taxonRank](https://dwc.tdwg.org/terms/#taxonRank).  This field has been aligned with the GBIF backbone taxonomy. |
| scientificname                   | String        | Y        | See [dwc:scientificName](https://dwc.tdwg.org/terms/#scientificName).  This field has been aligned with the GBIF backbone taxonomy. |
| verbatimscientificname           | String        | Y        | The scientific name as provided by the data publisher |
| verbatimscientificnameauthorship | String        | Y        | The scientific name authorship provided by the data publisher. |
| taxonkey                         | Integer       | Y        | The numeric identifier for the [taxon](https://www.gbif.org/developer/species#nameUsages) in GBIF's backbone taxonomy corresponding to `scientificname`. |
| specieskey                       | Integer       | Y        | The numeric identifier for the taxon in GBIF's backbone taxonomy corresponding to `species`. |
| typestatus                       | String        | Y        | See [dwc:typeStatus](https://dwc.tdwg.org/terms/#typeStatus). |
| countrycode                      | String        | Y        | See [dwc:countryCode](https://dwc.tdwg.org/terms/#countryCode).  GBIF's interpretation has set this to an ISO 3166-2 code. |
| locality                         | String        | Y        | See [dwc:locality](https://dwc.tdwg.org/terms/#locality). |
| stateprovince                    | String        | Y        | See [dwc:stateProvince](https://dwc.tdwg.org/terms/#stateProvince). |
| decimallatitude                  | Double        | Y²       | See [dwc:decimalLatitude](https://dwc.tdwg.org/terms/#decimalLatitude).  GBIF's interpretation has normalized this to a WGS84 coordinate. |
| decimallongitude                 | Double        | Y²       | See [dwc:decimalLongitude](https://dwc.tdwg.org/terms/#decimalLongitude).  GBIF's interpretation has normalized this to a WGS84 coordinate. |
| coordinateuncertaintyinmeters    | Double        | Y        | See [dwc:coordinateUncertaintyInMeters](https://dwc.tdwg.org/terms/#coordinateUncertaintyInMeters). |
| coordinateprecision              | Double        | Y        | See [dwc:coordinatePrecision](https://dwc.tdwg.org/terms/#coordinatePrecision). |
| elevation                        | Double        | Y        | See [dwc:elevation](https://dwc.tdwg.org/terms/#elevation).  If provided by the data publisher, GBIF's interpretation has normalized this value to metres. |
| elevationaccuracy                | Double        | Y        | See [dwc:elevationAccuracy](https://dwc.tdwg.org/terms/#elevationAccuracy).  If provided by the data publisher, GBIF's interpretation has normalized this value to metres. |
| depth                            | Double        | Y        | See [dwc:depth](https://dwc.tdwg.org/terms/#depth).  If provided by the data publisher, GBIF's interpretation has normalized this value to metres. |
| depthaccuracy                    | Double        | Y        | See [dwc:depthAccuracy](https://dwc.tdwg.org/terms/#depthAccuracy).  If provided by the data publisher, GBIF's interpretation has normalized this value to metres. |
| eventdate                        | String        | Y        | See [dwc:eventDate](https://dwc.tdwg.org/terms/#eventDate).  GBIF's interpretation has normalized this value to an ISO 8601 date with a local time. |
| year                             | Integer       | Y        | See [dwc:year](https://dwc.tdwg.org/terms/#year). |
| month                            | Integer       | Y        | See [dwc:month](https://dwc.tdwg.org/terms/#month). |
| day                              | Integer       | Y        | See [dwc:day](https://dwc.tdwg.org/terms/#day). |
| individualcount                  | Integer       | Y        | See [dwc:individualCount](https://dwc.tdwg.org/terms/#individualCount). |
| establishmentmeans               | String        | Y        | See [dwc:establishmentMeans](https://dwc.tdwg.org/terms/#establishmentMeans). |
| occurrenceid                     | String        | Y³       | See [dwc:occurrenceID](https://dwc.tdwg.org/terms/#occurrenceID). |
| institutioncode                  | String        | Y³       | See [dwc:institutionCode](https://dwc.tdwg.org/terms/#institutionCode). |
| collectioncode                   | String        | Y³       | See [dwc:collectionCode](https://dwc.tdwg.org/terms/#collectionCode). |
| catalognumber                    | String        | Y³       | See [dwc:catalogNumber](https://dwc.tdwg.org/terms/#catalogNumber). |
| recordnumber                     | String        | Y        | See [dwc:recordNumber](https://dwc.tdwg.org/terms/#recordNumber). |
| recordedby                       | String        | Y        | See [dwc:recordedBy](https://dwc.tdwg.org/terms/#recordedBy). |
| identifiedby                     | String        | Y        | See [dwc:identifiedBy](https://dwc.tdwg.org/terms/#identifiedBy). |
| dateidentified                   | String        | Y        | See [dwc:dateIdentified](https://dwc.tdwg.org/terms/#dateIdentified). An ISO 8601 date. |
| mediatype                        | String array  | N⁴       | See [dwc:mediaType](https://dwc.tdwg.org/terms/#mediaType).  May contain `StillImage`, `MovingImage` or `Sound` (from [enumeration](http://api.gbif.org/v1/enumeration/basic/MediaType), detailing whether the occurrence has this media available. |
| issue                            | String array  | N⁴       | A list of [issues](https://gbif.github.io/gbif-api/apidocs/org/gbif/api/vocabulary/OccurrenceIssue.html) encountered by GBIF in processing this record. More details are available on these issues and flags in [this blog post](https://data-blog.gbif.org/post/issues-and-flags/).|
| license                          | String        | N        | See [dwc:license](https://dwc.tdwg.org/terms/#license). Either [`CC0_1_0`](https://creativecommons.org/publicdomain/zero/1.0/) or [`CC_BY_4_0`](https://creativecommons.org/licenses/by/4.0/).  `CC_BY_NC_4_0` records are not present in this snapshot. |
| rightsholder                     | String        | Y        | See [dwc:rightsHolder](https://dwc.tdwg.org/terms/#rightsHolder). |
| lastinterpreted                  | String        | N        | The ISO 8601 date when the record was last processed by GBIF. Data are reprocessed for several reasons, including changes to the backbone taxonomy, so this date is not necessarily the date the occurrence record last changed. |

¹ Field names are lower case, but in later snapshots this may change to camelCase, for consistency with Darwin Core and the GBIF API.

² Occurrences without coordinates are excluded from this snapshot, although this may change in the future.

³ Either `occurrenceID`, or `institutionCode` + `collectionCode` + `catalogNumber`, or both, will be present on every record.

⁴ The array may be empty.