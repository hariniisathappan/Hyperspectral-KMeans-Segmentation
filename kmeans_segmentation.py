"""
===========================================================
Hyperspectral Image Segmentation using K-Means Clustering
===========================================================

Description:
This project applies K-Means clustering to hyperspectral data
to group pixels with similar spectral signatures into clusters.

Each cluster represents a region with similar material properties.

===========================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def main():
    print("=== Hyperspectral Segmentation using K-Means ===")

    # Load hyperspectral data
    image = np.load("indianpinearray.npy")

    print("Original Shape:", image.shape)

    rows, cols, bands = image.shape

    # Convert to 2D
    reshaped = image.reshape(rows * cols, bands)

    # Apply K-Means clustering
    k = 5
    kmeans = KMeans(n_clusters=k, random_state=42)

    labels = kmeans.fit_predict(reshaped)

    # Convert back to image
    segmented_image = labels.reshape(rows, cols)

    # Display segmented image
    plt.figure(figsize=(6,6))
    plt.imshow(segmented_image, cmap='viridis')
    plt.title("K-Means Segmentation of Hyperspectral Image")
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    main()