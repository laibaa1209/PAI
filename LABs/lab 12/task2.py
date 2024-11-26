# a. Import the libraries and relevant data set
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the handwritten digits dataset
digits = load_digits()
data = pd.DataFrame(digits.data, columns=digits.feature_names)
data['number_label'] = digits.target

# b. Create a new DataFrame called pixels
pixels = data.drop(columns=['number_label'])

# c. Grab a single image row representation
first_image_row = pixels.iloc[0]

# d. Convert the single row Series into a numpy array
first_image_array = first_image_row.to_numpy()

# e. Reshape this numpy array into an (8, 8) array
reshaped_image = first_image_array.reshape(8, 8)

# f. Use Matplotlib or Seaborn to display the array as an image
plt.figure(figsize=(5, 5))
plt.imshow(reshaped_image, cmap='gray')
plt.title("Handwritten Digit Representation (First Row)")
plt.axis('off')
plt.show()

# g. Scale the pixel feature DataFrame using Scikit-Learn
scaler = StandardScaler()
scaled_pixels = scaler.fit_transform(pixels)

# h. Perform PCA on the scaled pixel data set with 2 components
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_pixels)

# i. Show how much variance is explained by 2 principal components
explained_variance = pca.explained_variance_ratio_
print(f"Variance explained by the 2 principal components: {explained_variance.sum():.2f}")

# j. Create a scatterplot of the digits in 2D PCA space
pca_df = pd.DataFrame(pca_result, columns=['PCA1', 'PCA2'])
pca_df['number_label'] = data['number_label']

plt.figure(figsize=(10, 8))
sns.scatterplot(
    x='PCA1', y='PCA2',
    hue='number_label',
    palette='tab10',
    data=pca_df,
    legend='full',
    alpha=0.8
)
plt.title("Digits in 2D PCA Space")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title="Digit")
plt.grid()
plt.show()
