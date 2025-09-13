# Synthetic-Data-Generation-Hackathon-Vienna

Generate realistic synthetic household energy consumption data using GANs and clustering.

## Overview

This project analyzes London smart meter data (2013) from 4,125 households and generates synthetic energy consumption patterns that preserve statistical and temporal characteristics. Uses K-means clustering to group similar households, then trains specialized GANs for each cluster.

## Team:
1. Andreas A.D. Liess
2. Pratiksha Jagat
3. Volodymyr Borysenko 
4. Sviatoslav Matviluk

## Features

- Multi-level clustering by consumption patterns
- Cluster-specific GAN training
- Seasonal consumption modeling
- Comprehensive evaluation metrics


## Requirements

- Python 3.8+
- TensorFlow 2.8+
- See `requirements.txt` for a complete list
  
## Quick Start

```bash
git clone https://github.com/yourusername/energy-consumption-gan
cd energy-consumption-gan
pip install -r requirements.txt
```


## Data Setup 📊

The dataset for this project is not included in the repository due to its size.

1.  Download the `Smart_meters_london_2013.csv` file from this link:
    * [**[Smart_meters_london_2013](https://1drv.ms/f/c/590086cda647cfb8/Er4YA9-y1pJMlmzy5ChaC8cB9NB3XBkdPPfyb_PZbt8Rng?e=83zcJG)**]

2.  Create the necessary folders and place the downloaded file in `Data/raw/`. The final structure should look like this:

    ```
    Your-Project-Folder/
    └── Data/
        ├── processed/
        │   └── clusters/
        └── raw/
            └── metersdata.csv   <-- Place downloaded file here
    ```
3. The clusters folder will later be populated with the clustered data files after executing the data analysis notebooks. 


### Usage
1. Run `notebooks/01_data_analysis_seasonal.ipynb` for clustering
2. Run `notebooks/03_gan_training.ipynb` for model training  
3. Run `evaluation/eval.ipynb` for quality assessment


## Methodology

1. **Preprocessing**: Extract temporal and seasonal features
2. **Clustering**: Group households by consumption patterns (23/103 clusters)
3. **GAN Training**: Train separate models per cluster with feature matching
4. **Evaluation**: Compare synthetic vs real data distributions and trends

## Dataset

London Smart Meter Dataset (2013): 4,125 households, half-hourly readings, full year coverage.

## Results

Generates synthetic data, maintaining:
- Original statistical distributions
- Daily/weekly/seasonal patterns  
- Household clustering structure
- Low RMSE across evaluation metrics


