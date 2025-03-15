# Implementation of Seam Carving for Content-Aware Image Resizing

Seam carving is an image processing technique that resizes images while preserving important content. This project implements seam carving using energy-based seam removal.

## **Steps**
1. **Compute Energy Map** – Identify important regions (energy map) in the image using a gradient-based energy function.
2. **Find Optimal Seams** – Use **dynamic programming** to find the least important vertical/horizontal seams.
3. **Remove Seams** – Remove seams for resizing image.
4. **Visualize Seams** – Display the removed seams on the original image.
5. **Generate Final Resized Image** – Output the transformed image.

---

## **Example Results**

### **Original Image**
![Original](images/cat.png)

### **Seams Visualization**
_This image highlights the seams that will be removed._

![Seams Visualization](images/seams_visual.jpg)

### **Final Resized Image**
_This is the output after seam carving._

![Final Result](images/resized_result.jpg)

---

## **Key Functions**  

### `compute_energy()`
- Computes the **energy map** using a gradient-based filter.
- Helps in identifying important and unimportant areas.

### `find_vertical_seam()`
- Uses **dynamic programming** to locate the least important vertical seam.
- Finds the **lowest-energy** path from top to bottom.

### `remove_seam(seam)`
- Removes the **selected seam** from the image, reducing its width.
### `get_seam_visualization()`
- Draws seams on the original image for better **understanding**.
- Visualized in **red** to indicate removable pixels.

---

## **References**
- Avidan, S., & Shamir, A. (2007). _Seam Carving for Content-Aware Image Resizing._ ACM Transactions on Graphics.

---
