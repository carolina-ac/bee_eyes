# Clustering Analysis of Eye Morphology in Species

## Overview

This repository contains tools and scripts for performing both hierarchical and non-hierarchical clustering analyses in Python and R to explore variations in eye morphology among different species. These analyses aim to identify distinct groups based on morphological metrics, providing insights into evolutionary patterns and adaptive strategies in visual systems. The analysis is suitable for exploratory numeric data analysis across various fields.

## Features

- **Hierarchical Clustering**: Utilizes `AgglomerativeClustering` in Python and `hclust` in R to explore the hierarchical structure of the data.
- **Non-Hierarchical Clustering (K-Means)**: Applies `KMeans` clustering in Python and equivalent methods in R to partition the data into distinct groups.
- **Silhouette Analysis**: Employs silhouette scores in both Python and R to evaluate the effectiveness of the clustering configurations.
- **Data Visualization**: Includes dendrogram and pairplot visualizations in Python and equivalent plot types in R to represent clustering results.
- **Descriptive Statistics**: Provides statistical summaries in both Python and R to characterize and compare clusters.

## Getting Started

### Prerequisites

For Python:
- Python installation
- Required packages: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `scipy`

For R:
- R installation
- Required packages: `tidyverse`, `cluster`, `factoextra`, `dendextend`

### Installation

#### Python
Install the required Python packages using pip:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn scipy
```
#### R
```
install.packages(c("tidyverse", "cluster", "factoextra", "dendextend"))
```

### Reference

Caetano, C., Araújo, P., Schlindwein, C., Alves-Dos-Santos, I., & Mota, T. (2023). Body size and the architecture of the visual system in crepuscular and diurnal bees. Biological Journal of the Linnean Society, 138(3), 328-340.
