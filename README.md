# Implementation for Seam Carving for Content-Aware Image Resizing paper

Seam carving is an image processing technique that resizes images while preserving important content. This project implements seam carving using energy-based seam removal.

## The process follows key steps:

1. **Compute Energy Map** – Identify important regions in the image using a gradient-based energy function.
2. **Find Optimal Seams** – Use dynamic programming to find the least important vertical/horizontal seams.
3. **Remove/Insert Seams** – Remove seams for shrinking, or duplicate them for expansion.
4. **Visualize Seams** – Show the removed seams on the original image.
5. **Generate Final Resized Image** – Output the transformed image.

---

## Example Results

### **Original Image**
![Original](images/cat.png)

### **Seams Visualization**
_This image shows the seams that will be removed._
![Seams Visualization](images/seams_visual.jpg)

### **Final Resized Image**
_This is the final image after seam carving._
![Final Result](images/resized_result.jpg)

---

## Key Functions  

### `compute_energy()`
Calculates the energy of each pixel using a gradient-based filter.  
This helps in identifying the most important and least important parts of the image.

### `find_vertical_seam()`
Finds the least important vertical seam using **dynamic programming**.  
The seam is selected based on the lowest energy path from top to bottom.

### `remove_seam(seam)`
Removes the selected seam from the image, effectively reducing its width.  
This is the core step in **seam carving**.

### `get_seam_visualization()`
Draws seams on the original image for better understanding.  
Seams are typically visualized in **red** to indicate which pixels will be removed.

