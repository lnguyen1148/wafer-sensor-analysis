# Wafer sensor analysis

Work in progress. Notebook 1 of 5 is done.

## What this project is about

Making chips means running wafers through hundreds of process steps, so a small problem at one step can quietly scrap many wafers before anyone notices. Part of a yield engineer’s work is tracing bad test results back to the step where the problem started. As an aspiring yield/process engineer, I want to build a project that shows I can work with real manufacturing data, look for the sensor signals linked to bad wafers, and connect what I find to what I’m learning about semiconductor manufacturing.

## Data

Equipment sensor data and wafer test results from Infineon Technologies Austria and KAI, published on Zenodo: [Zenodo record 4322353](https://zenodo.org/records/4322353).

The raw files are not stored in this repo because they are large. To run the notebooks, download the files from the link above and put them in `data/raw/`.

## Notebooks

1. `01_load_and_inspect`: load the files, check them, clean the response file (done)
2. `02_feature_engineering`: turn 176 readings per wafer into one row per wafer (in progress)
3. `03_spc_exploration`: control charts (not started)
4. `04_feature_importance`: which sensors relate to bad wafers (not started)
5. `05_modeling`: predict good or bad wafers (not started)

## What I've found so far

- There are no missing values, and all sensor columns are numeric.
- The response file has 2,638 rows but only 1,319 unique wafers. The copies are identical, so I removed them.
- Equipment 1 covers 971 of the 1,319 wafers. I haven't decided yet how to handle the other 348.
- 20% of wafers are bad, but 25 of 54 lots have no bad wafers and lot27 is entirely bad, so I will split train and test data by lot.

## How to run it

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    jupyter lab
