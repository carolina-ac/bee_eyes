# Incremental Modeling and Predictive Analysis of Bee Eye Data Using GAMLSS

This repository contains code for incremental modeling and visualization of bee eye data using mixed models with the `gamlss` package. The analysis workflow includes model fitting, AIC-based model selection, diagnostic plots, and visualizations of observed versus predicted values, with distinct lines for each `group level`, and the addition of a random variable to capture inherent variability not explained by fixed effects.

The `gamlss` package is particularly suitable for small datasets, as it allows flexible modeling of distributional parameters (mean, scale, and shape) using covariates, which can help capture more complex data patterns even with limited observations.

## Requirements

To run this code, you will need the following R packages:
- `car`
- `gamlss`
- `ggplot2`

Install any missing packages using `install.packages("package_name")`.

## Data Preparation

We start by loading and cleaning the data, filtering out specific species, and ensuring the `Species` and `Habit` variables are properly set as factors.

```r
library(car)
library(gamlss)
```