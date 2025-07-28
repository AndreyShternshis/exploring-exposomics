# Tool for exploring exposome datasets and co-exposures

The tool produces results from paper "Modeling and exploring co-exposures to environmental chemicals and endogenous metabolites". It allows to obtain additional results or apply it to other exposome data.

**Instructions**

The tool is done on the format of python notebook _Exp(2)-v1.ipynb_. Tabs with all functioaliity are followed by all function and methods.

All packages and their versions are listed in requirements.txt.

Run all cells and scroll to the tool - the last cell of the notebook.

<img width="484" height="430" alt="image" src="https://github.com/user-attachments/assets/1ef51b19-0580-41ea-927e-8ef3b0c8929f" />

To access python notebook in a local computer, one can launch Jupyter Notebook or JupyterLab via Anaconda Navigator https://www.anaconda.com.

Alternative option to try the tool is uploading it to https://colab.google. All output files then should be saved manually and session time can be limited.

**Data is extracred from the following files**


Original file names are used below:
- "3WP_LC_samples_6_visits": Metadata containing subjects' id and visit number
- "Data/S3WP_annotated_Levels_1_2_pos&neg": 519 annotated features followed by Labels of samples e.g. subject's id, visit number, sex, age, etc. Each feature has class, sublclass, description, and name.
- "S3WP_LC_unannotaed_neg_final": unannotated features discovered in negative electrospray ionization mode
-  "S3WP_LC_unannotaed_pos_final": unannotated features discovered in the positive mode

**Data speciality**
- For annotated data, one sample, 200th in metadata, has excessive number of 0s and it is considered as an outlier
- For unannotated data, second time point of two participants were swapped.

**Outputs**

Files generated in some tabs and may be required in others follow. The most of files can be obtained in **Data Extraction** tab. Measures for Graphs are calculated and saved in **Measures** tab.
- .json files contain all generated samples in **Prediction** tab. All other output files have .npy extension.
- Outliers.npy is a list of outliers specified by a user.
- Data.npy contains all annotated features without outliers in a shape (number of samples, exposome dimensionality)
- Labels.npy are labels of classes of participants
- Label_names.npy are the names of labels
- Class.info.npy is description of each feature including its class.
- timepoints.npy and participants.npy are time points and participants id correspoding to the order of samples in Data.
- _full.npy files include outliers
- Files with _unanot tag include unannotated data.
- Metric_i.npy represent a measure _Metric_ calculated at time point _i_. Where _0 means using all time points.
- ICC.npy and DF.npy are intercalss correlation and detection frequency calculated for all features.
-   Results_mean_{Method}.npy and Results_std_{Method} are mean and standard deviation of accuraccy of participants clustering.
