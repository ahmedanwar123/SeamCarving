import numpy as np
from energy import EnergyCalculator
from seam import SeamFinder


class SeamCarver:
    """Performs seam carving operations."""

    def __init__(self, img: np.ndarray):
        self.img = img.copy()
        self.original_img = img.copy()
        self.seams = []  # Store all seam coordinates
        self.seam_visualizations = []  # Store images with seams

    # def remove_seam(self, seam: np.ndarray) -> None:
    #     """Removes a seam and stores its path for visualization later."""
    #     height, width = self.img.shape[:2]
    #     output = np.zeros((height, width - 1, 3), dtype=self.img.dtype)

    #     for i in range(height):
    #         self.seams.append((i, seam[i]))  # Store seam coordinates
    #         output[i, :, :] = np.delete(self.img[i, :, :], seam[i], axis=0)

    #     self.img = output  # Update the image after removing the seam
    def remove_seam(self, seam: np.ndarray) -> None:
        """Removes a seam and stores its path for visualization later."""
        height, width = self.img.shape[:2]
        output = np.zeros((height, width - 1, 3), dtype=self.img.dtype)

        seam_indices = []  # Store entire seam for correct visualization

        for i in range(height):
            seam_indices.append(seam[i])  # Store seam column index per row
            output[i, :, :] = np.delete(self.img[i, :, :], seam[i], axis=0)

        self.seams.append(np.array(seam_indices))  # Store full seam path as an array
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
        """Draw seams on the original image, mapping them from the resized dimensions, control thickness of seams visualizations."""
        img_with_seams = self.original_img.copy()
        thickness = 1

        # Compute scaling factors to map seams from resized image to original image
        scale_x = self.original_img.shape[1] / self.img.shape[1]  # Width scale
        scale_y = self.original_img.shape[0] / self.img.shape[0]  # Height scale

        for seam in self.seams:
            for row, col in enumerate(seam):
                orig_row = int(row * scale_y)
                orig_col = int(col * scale_x)

                # Ensure we stay within bounds
                for i in range(-thickness, thickness + 1):
                    for j in range(-thickness, thickness + 1):
                        r, c = orig_row + i, orig_col + j
                        if (
                            0 <= r < img_with_seams.shape[0]
                            and 0 <= c < img_with_seams.shape[1]
                        ):
                            img_with_seams[r, c] = [255, 0, 0]

        return img_with_seams
