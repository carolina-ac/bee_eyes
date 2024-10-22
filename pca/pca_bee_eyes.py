#################################################
#
#     LOADING IMPORTANT LIBRARIES AND DATA
#
#################################################

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

# Root Directory
root_directory = 'F:/open_git/bee_eyes'

# Load data
eyes = pd.read_csv('eyes_df.txt', delimiter='\t')

#################################################
#
#           PRINCIPAL COMPONENT ANALYSIS
#
#################################################

# Selecting numerical columns for PCA
features = ['nf', 'vf', 'ff', 'df', 'co', 'ea', 'nfa', 'di']  # adjust as necessary
x = eyes.loc[:, features].values
y = eyes.loc[:, ['FamHab']].values

# Normalizing the data
x = StandardScaler().fit_transform(x)

# PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])

# Concatenating principal components with 'FamHab'
finalDf = pd.concat([principalDf, eyes[['FamHab']]], axis=1)

# Loadings (eigenvectors)
loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

# Plot data
fig, ax = plt.subplots(figsize=(10, 8))

targets = eyes['FamHab'].unique()
colors = ['orange', 'purple', 'brown', 'green', 'blue']
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['FamHab'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
               finalDf.loc[indicesToKeep, 'principal component 2'],
               c=color,
               s=50, label=target)

# Add arrows for each loading (original variable)
for i, feature in enumerate(features):
    ax.arrow(0, 0, loadings[i, 0], loadings[i, 1], color='r', alpha=0.5)
    ax.text(loadings[i, 0] * 1.15, loadings[i, 1] * 1.15, feature, color='g', ha='center', va='center')

ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_title('PCA Biplot with Variable Loadings')
ax.legend()
#ax.grid()
plt.savefig('eyes_pca.png')
plt.show()
