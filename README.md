# 🛰️ Hyperspectral Image Segmentation using K-Means Clustering

## 👩‍🔬 Bioinformatics-Inspired Unsupervised Learning

This project applies **K-Means clustering** to hyperspectral image data to segment pixels into groups based on spectral similarity.

Inspired by **bioinformatics clustering techniques**, this work demonstrates how pattern-based grouping methods can be extended from biological data to hyperspectral imaging.

---

## 🧠 Core Idea

Each pixel in a hyperspectral image contains values across multiple wavelength bands, forming a **high-dimensional spectral vector**.

Similar to:
- Gene expression profiles in bioinformatics  
- Protein clustering based on similarity  

We apply clustering to group pixels with similar spectral signatures.

---

## 🚀 Methodology

1. Load hyperspectral dataset (NumPy format)
2. Reshape image into 2D data (pixels × spectral bands)
3. Apply **K-Means clustering**
4. Assign cluster labels to each pixel
5. Reshape results back into image form
6. Visualize segmented regions

---

## 📊 Dataset

- **Indian Pines Hyperspectral Dataset**
- Dimensions: **145 × 145 × 220**
- Each pixel = spectral signature

---

## 🛠️ Technologies Used

- Python  
- NumPy  
- Matplotlib  
- Scikit-learn  

---

## 📷 Output

- Segmented hyperspectral image  
- Each color represents a cluster  
- Regions correspond to different materials or land types  

---

## 🔬 Applications

- 🛰️ Remote sensing  
- 🌾 Agricultural analysis  
- 🛡️ Defence surveillance  
- 🧠 Pattern recognition  

---

## 💡 Key Insight

> “Clustering hyperspectral pixels is analogous to clustering genes or proteins based on similarity in bioinformatics.”

---

## 👩‍💻 Author

**Harinii S**  
B.Tech Bioinformatics (AI/ML Minor)  
SASTRA Deemed University  

---

## 🌟 Future Improvements

- Compare clustering with ground truth labels  
- Optimize number of clusters (k selection)  
- Apply advanced clustering (DBSCAN, hierarchical clustering)  
- Integrate machine learning models  

---
