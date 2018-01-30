RNAseq_cell_cycle
=============================

A development project to use single-cell RNA-seq data to build a model of transcription during the cell cycle and use it to identify interactions impacted in different populations of single cells with various cell cycle diseases (primarily cancers).

The project is initially training on data from Karlsson et al.  JMB 2017, "Transcriptomic Characterization of Human Cell Cycle in Individual Unsynchronized Cells".

An additional labelled dataset is available from Leng et al. Nature Methods 2015, "Oscope identifies oscillatory genes in unsynchronized single-cell RNA-seq experiments", and may need to be used, although hESCs have sufficiently unique cell cycle transcriptomics that I would prefer use differentiated cells (even if cancerous), if possible.
Additional unlabelled single-cell RNA-seq data from various sources is available from the ARCHS4 web resource and will be used as the test data.

The workflow will be as follows:
- Read-counts are normalized to TPM.
- A supervised classifier is built to predict cell cycle stage.
- The classifier is used to label unlabelled cells in other datasets.
- Cell-cycle trajectories are built from individual cells.
- A multi-dimensional LTSM RNN is built to model the cell cycle transcriptome for the labelled data.
- Then do transfer learning on the new data.
- Finally, compare the pre-trained and final models to identify edges and nodes that are differently weighted in the different populations.

Current status:
The supervised classifier is not performing as well as desired.  I am investigating unsupervised clustering to see if cytometric cell cycle staging is the best way to classify the data

The ARCHS4 data is processed using Kallisto and a more recent annotation than the Karlsson paper used.  Before deploying, I will need to reprocess that fasta files so that all the data is preprocessed consistently.



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
