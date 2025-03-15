import numpy as np
import cv2
from energy import EnergyCalculator
from seam import SeamFinder


# class SeamCarver:
#     """Performs seam carving operations."""

#     def __init__(self, img: np.ndarray):
#         self.img = img.copy()
#         self.seam_visualizations = []

#     def remove_seam(self, seam: np.ndarray) -> None:
#         """Removes a seam and stores visualization."""
#         height, width = self.img.shape[:2]
#         output = np.zeros((height, width - 1, 3), dtype=self.img.dtype)

#         seam_visual = self.img.copy()
#         for i in range(height):
#             seam_visual[i, seam[i]] = [255, 0, 0]  # Mark seam in red
#             output[i, :, :] = np.delete(self.img[i, :, :], seam[i], axis=0)

#         self.seam_visualizations.append(seam_visual)
#         self.img = output

#     def carve_width(self, new_width: int) -> tuple[np.ndarray, list[np.ndarray]]:
#         """Resize width by removing vertical seams."""
#         while self.img.shape[1] > new_width:
#             energy = EnergyCalculator.calculate_energy(self.img)
#             cumulative_energy = SeamFinder.calculate_cumulative_energy_map(energy)
#             seam = SeamFinder.find_minimum_energy_seam(cumulative_energy)
#             self.remove_seam(seam)

#         return self.img, self.seam_visualizations

#     def carve_height(self, new_height: int) -> tuple[np.ndarray, list[np.ndarray]]:
#         """Resize height by removing horizontal seams."""
#         self.img = np.rot90(self.img, 1)  # Rotate 90 degrees to treat height as width
#         self.seam_visualizations = []

#         while self.img.shape[1] > new_height:
#             energy = EnergyCalculator.calculate_energy(self.img)
#             cumulative_energy = SeamFinder.calculate_cumulative_energy_map(energy)
#             seam = SeamFinder.find_minimum_energy_seam(cumulative_energy)
#             self.remove_seam(seam)

#         self.img = np.rot90(self.img, -1)  # Rotate back
#         self.seam_visualizations = [np.rot90(img, -1) for img in self.seam_visualizations]

#         return self.img, self.seam_visualizations

#     def carve_both(self, new_width: int, new_height: int) -> tuple[np.ndarray, list[np.ndarray]]:
#         """Resize both width and height."""
#         img, vis_w = self.carve_width(new_width)
#         self.img = img  # Update with width resized image
#         img, vis_h = self.carve_height(new_height)

#         return img, vis_w + vis_h

class SeamCarver:
    """Performs seam carving operations."""

    def __init__(self, img: np.ndarray):
        self.img = img.copy()
        self.original_img = img.copy()
        self.seams = []  # Store all seams

    def remove_seam(self, seam: np.ndarray) -> None:
        """Removes a seam and stores its path for visualization later."""
        height, width = self.img.shape[:2]
        output = np.zeros((height, width - 1, 3), dtype=self.img.dtype)

        for i in range(height):
            self.seams.append((i, seam[i]))  # Store seam coordinates
            output[i, :, :] = np.delete(self.img[i, :, :], seam[i], axis=0)

        self.img = output

    def carve_width(self, new_width: int) -> np.ndarray:
        """Resize width by removing vertical seams while storing seams."""
        while self.img.shape[1] > new_width:
            energy = EnergyCalculator.calculate_energy(self.img)
            cumulative_energy = SeamFinder.calculate_cumulative_energy_map(energy)
            seam = SeamFinder.find_minimum_energy_seam(cumulative_energy)
            self.remove_seam(seam)

        return self.img

    def carve_height(self, new_height: int) -> np.ndarray:
        """Resize height by removing horizontal seams."""
        self.img = np.rot90(self.img, 1)  # Rotate to treat height as width
        self.seams = []  # Reset seams since it's a new resizing process

        while self.img.shape[1] > new_height:
            energy = EnergyCalculator.calculate_energy(self.img)
            cumulative_energy = SeamFinder.calculate_cumulative_energy_map(energy)
            seam = SeamFinder.find_minimum_energy_seam(cumulative_energy)
            self.remove_seam(seam)

        self.img = np.rot90(self.img, -1)  # Rotate back
        return self.img

    def carve_both(self, new_width: int, new_height: int) -> np.ndarray:
        """Resize both width and height while storing seams."""
        self.carve_width(new_width)
        self.carve_height(new_height)
        return self.img

    def get_seam_visualization(self) -> np.ndarray:
        """Overlay all stored seams onto the original image in red."""
        vis = self.original_img.copy()

        for (row, col) in self.seams:
            vis[row, col] = [255, 0, 0]  # Mark seam in RED

        return vis
