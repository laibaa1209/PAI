# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (adjust file path as necessary)
df = pd.read_csv('cement_slump.csv')

# Set Seaborn pastel theme
sns.set_theme(style="darkgrid", palette="pastel")

# Step 1: Dataset Overview
print("Dataset Summary:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())

# Step 2: Outlier Detection with Box Plots
plt.figure(figsize=(20, 18))
sns.boxplot(data=df.select_dtypes(include=np.number))
plt.title("Box Plot of Numerical Features")
plt.show()

# Step 3: Distribution Analysis with Histograms
numeric_cols = df.select_dtypes(include=np.number).columns

# Set up the subplot grid
n_cols = 2  # Adjust the number of columns as needed
n_rows = (len(numeric_cols) + n_cols - 1) // n_cols  # Calculate rows needed
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 20))
axes = axes.flatten()  # Flatten axes for easy indexing

# Plot each numerical column in its own subplot
for i, col in enumerate(numeric_cols):
    sns.histplot(df[col], bins=15, kde=True, color="skyblue", edgecolor="white", ax=axes[i])
    axes[i].set_title(f"Distribution of {col}", color="slateblue")

# Hide any unused subplots if there are any
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.suptitle("Distribution of Numerical Features", color="slateblue", fontsize=16, y=1.02)
plt.tight_layout()

# Step 4: Correlation Analysis
plt.figure(figsize=(10, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='viridis', vmin=-1, vmax=1)
plt.title("Correlation Heatmap", color="slateblue")
plt.show()

# Step 5: Analyzing Relationships between Highly Correlated Features
# Define most correlated pairs
high_corr_pairs = correlation_matrix[(correlation_matrix > 0.7) & (correlation_matrix < 1)].stack().reset_index()
high_corr_pairs.columns = ["Feature1", "Feature2", "Correlation"]
print("Highly Correlated Feature Pairs:")
print(high_corr_pairs)

# Scatter plot for a selected pair
sns.regplot(x='Cement', y='Compressive Strength (28-day)(Mpa)', data=df, scatter_kws={"color": "peachpuff"}, line_kws={"color": "lightcoral"})
plt.title("Relationship between Cement and Strength", color="slateblue")
plt.show()

# Step 6: Summary of Insights
print("\nKey Insights:")
print("1. Distribution: Each feature's distribution and central tendency were visualized.")
print("2. Outliers: Box plots indicate potential outliers in [notable features].")
print("3. Correlations: Strong correlations exist between [features with high correlation].")
print("4. Trends: Relationship observed between Cement and Strength.")
