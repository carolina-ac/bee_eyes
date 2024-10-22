# Bee Eye Morphology Analysis
This project contains analyses related to the morphology of bee eyes, focusing on visual system adaptations in different species. The data used in this project are derived from the study by **Caetano et al. (2023)**, which investigates the relationship between body size and the architecture of the visual system in crepuscular, facultative crepuscular and diurnal bees.

## Project Overview
The project currently includes analyses using Principal Component Analysis (PCA) and clustering methods to explore patterns in eye morphology. Additional analyses using Generalized Additive Models for Location, Scale, and Shape (GAMLSS) and Generalized Linear Mixed Models (GLMM) will be added soon.

## Data Source
The data used for this project is based on the study:

Caetano, C., Araújo, P., Schlindwein, C., Alves-Dos-Santos, I., & Mota, T. (2023). Body size and the architecture of the visual system in crepuscular and diurnal bees. Biological Journal of the Linnean Society, 138(3), 328-340.

## Current Analyses

1. Principal Component Analysis (PCA)
Objective: Reduce the dimensionality of the dataset while maintaining the variance to better understand the key factors driving variations in eye morphology.
Methods: Standardized the data using StandardScaler and applied PCA to extract the first two principal components.
Visualization: A biplot is generated, showing the influence of different variables (e.g., number of facets, size of facets ) on the principal components.

3. Clustering Analysis
Objective: Identify natural groupings in the data to differentiate between crepuscular, facultative crepuscular, and diurnal bees based on eye morphology.
Methods: Applied hierarchical and K-Means clustering to the standardized data.
Visualization: Dendrograms and scatter plots are used to visualize the clusters formed.

### Future Work
* GAMLSS: Planned analysis to model the relationship between morphological measurements and temporal habit, adjusting for non-normal distributions.
* GLMM: Planned analysis to incorporate random effects, modeling the hierarchical structure of the data (e.g., species nested within families).
  
### Repository Structure
* data/: Contains the raw data used for analysis (not included in this repository due to privacy).
* results/: Contains the results of the analyses, including PCA plots, clustering visualizations, and statistical summaries.
* src/: Contains the R and Python scripts used for the analyses.

### Citation
If you use this data, please cite the original study:

Caetano, C., Araújo, P., Schlindwein, C., Alves-Dos-Santos, I., & Mota, T. (2023). Body size and the architecture of the visual system in crepuscular and diurnal bees. Biological Journal of the Linnean Society, 138(3), 328-340.
