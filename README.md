# Tool for exploring exposome datasets and co-exposures

The tool produces results from paper "Modeling human exposures to environmental chemicals and metabolites in a prospective cohort". It allows a user to analyze data, obtain results complementing the paper, or apply it to other exposome data.

**Instructions**

The tool is done in the format of python notebook _Exp2ML-v1.ipynb_. Tabs with all functionality are followed by all functions and methods.

All packages and their versions are listed in requirements.txt. They can be installed by command !pip install -r requirements.txt.

Run all cells and scroll to the tool - the last cell of the notebook.

<img width="639" height="626" alt="image" src="https://github.com/user-attachments/assets/cf230b8c-f6ea-4902-bfcb-c55011aaea68" />


To access a python notebook in a local computer, one can launch Jupyter Notebook or JupyterLab via Anaconda Navigator https://www.anaconda.com.

An alternative option to try the tool is uploading it to https://colab.google. All output files then should be saved manually and session time can be limited.

**Data is extracted from the following files**


Original file names are used below:
- "3WP_LC_samples_6_visits": Metadata containing subjects' id and visit number
- "Data/S3WP_annotated_Levels_1_2_pos&neg": 519 annotated features followed by Labels of samples e.g. subject's id, visit number, sex, age, etc. Each feature has class, subclass, description, and name.
- "S3WP_LC_unannotaed_neg_final": unannotated features discovered in negative electrospray ionization mode
-  "S3WP_LC_unannotaed_pos_final": unannotated features discovered in the positive mode

**Data speciality**
- For annotated data, one sample, 200th in metadata, has excessive number of zeros and it is considered as an outlier
- For unannotated data, the second time point of two participants was swapped.

**Outputs**

Files generated in some tabs and may be required in others follow. The most of files can be obtained in **Data Extraction** tab. Measures for Graphs are calculated and saved in **Measures** tab.
- .json files contain all generated samples in **Prediction** tab. All other output files have .npy extension. It includes samples made for imputation.
- Outliers.npy is a list of outliers specified by a user.
- Data.npy contains all annotated features without outliers in a shape (number of samples, exposome dimensionality)
- Labels.npy are labels of classes of participants
- Label_names.npy are the names of labels
- Class.info.npy is a description of each feature including its class.
- timepoints.npy and participants.npy are time points and participants id corresponding to the order of samples in Data.
- _full.npy files include outliers
- Files with _unanot tag include unannotated data.
- Metric_i.npy represents a measure _Metric_ calculated at time point _i_. Where _0 means using all time points.
- ICC.npy and DF.npy are intercalss correlation and detection frequency calculated for all features.
-   Results_mean_Method.npy and Results_std_Method are mean and standard deviation of accuracy of participants clustering by a visualization _Method_.
