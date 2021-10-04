Data are stored in blob storage in the West Europe Azure region, in the following folder:

`https://cpdataeuwest.blob.core.windows.net/cpdata/raw/fia`

Data are stored in [Parquet](https://parquet.apache.org/) format.  Within the above folder, data are organized according to:

`/[table].parquet`

`table` is one of the FIA tables:

- boundary
- cond
- cond_dwm_calc
- county
- dwm_coarse_woody_debris
- dwm_duff_litter_fuel
- dwm_fine_woody_debris
- dwm_microplot_fuel
- dwm_residual_pile
- dwm_transect_segment
- dwm_visit
- grnd_cvr
- invasive_subplot_spp
- lichen_lab
- lichen_plot_summary
- lichen_visit
- ozone_biosite_summary
- ozone_plot
- ozone_plot_summary
- ozone_species_summary
- ozone_validation
- ozone_visit
- p2veg_subp_structure
- p2veg_subplot_spp
- plot
- plot_regen
- plotgeom
- plotsnap
- pop_estn_unit
- pop_eval
- pop_eval_attribute
- pop_eval_grp
- pop_eval_typ
- pop_plot_stratum_assgn
- pop_stratum
- seedling
- seedling_regen
- sitetree
- soils_erosion
- soils_lab
- soils_sample_loc
- soils_visit
- subp_cond
- subp_cond_chng_mtrx
- subplot
- subplot_regen
- survey
- tree
- tree_grm_begin
- tree_grm_component
- tree_grm_estn
- tree_grm_midpt
- tree_grm_threshold
- tree_regional_biomass
- tree_woodland_stems
- veg_plot_species
- veg_quadrat
- veg_subplot
- veg_subplot_spp
- veg_visit

We also provide a read-only SAS (<a href="https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview">shared access signature</a>) token to allow access to this data via, e.g., BlobFuse, which allows you to mount blob containers as drives:

`?sv=2019-12-12&si=cpdata-ro&sr=c&sig=tqRGrmdYYa9WYkaPi0wWOD0nalRdNGTZNe97GL2enDA%3D`

Mounting instructions for Linux are [here](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-how-to-mount-container-linux).

Large-scale processing is best performed in the West Europe Azure data center, where the data are stored.  If you are using this data for environmental science applications, consider applying for an [AI for Earth grant](http://aka.ms/ai4egrants) to support your compute requirements.