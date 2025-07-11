# Tool for exploring expossome datasets and co-exposures

**Data is extracred from the following files**
Original file names used in the analysis follow:
- "3WP_LC_samples_6_visits": Metadata containing subjects' id and visit number
- "Data/S3WP_annotated_Levels_1_2_pos&neg": 519 annotated features followed by Labels of samples e.g. subject's id, visit number, sex, age, etc. Each feature has class, sublclass, description, and name.
- "S3WP_LC_unannotaed_neg_final": unannotated features discovered in negative electrospray ionization mode
-  "S3WP_LC_unannotaed_pos_final": unannotated features discovered in the positive mode

**Data speciality**
- For annotated data, one sample, 200th in metadata, has excessive number of 0s and it is considered as an outlier
- For unannotated data, second time point of two participants were swapped.
