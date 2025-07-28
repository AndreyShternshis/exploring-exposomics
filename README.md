# Tool for exploring exposome datasets and co-exposures

The tool produces results from paper "Modeling and exploring co-exposures to environmental chemicals and endogenous metabolites". It allows to obtain additional results or apply it to other exposome data.

**Instructions**

Thw tool is done on the format of python notebook _Exp(2)_v1.ipynb_. Tabs with all functioaliity are followed by all function and methods.

All packages and their versions are listed in requirements.txt.

Run all cells and scroll to the tool - the last cell of the notebook.

<img width="484" height="430" alt="image" src="https://github.com/user-attachments/assets/1ef51b19-0580-41ea-927e-8ef3b0c8929f" />


**Data is extracred from the following files**


Original file names are used below:
- "3WP_LC_samples_6_visits": Metadata containing subjects' id and visit number
- "Data/S3WP_annotated_Levels_1_2_pos&neg": 519 annotated features followed by Labels of samples e.g. subject's id, visit number, sex, age, etc. Each feature has class, sublclass, description, and name.
- "S3WP_LC_unannotaed_neg_final": unannotated features discovered in negative electrospray ionization mode
-  "S3WP_LC_unannotaed_pos_final": unannotated features discovered in the positive mode

**Data speciality**
- For annotated data, one sample, 200th in metadata, has excessive number of 0s and it is considered as an outlier
- For unannotated data, second time point of two participants were swapped.
