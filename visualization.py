import numpy as np
import cv2
import matplotlib.pyplot as plt
import os


class ImageVisualizer:
    """Handles image visualization and saving."""

    @staticmethod
    def overlay_seams(image: np.ndarray, seams: list[np.ndarray]) -> np.ndarray:
        """
        Overlay all seams on the original image.
        """
        img_with_seams = image.copy()

        for seam in seams:
            for row, col in enumerate(seam):  # Ensure seam[row] correctly maps to col
                if 0 <= col < img_with_seams.shape[1]:  # Prevent out-of-bounds errors
                    img_with_seams[row, col] = [255, 0, 0]  # Draw seams in red

        return img_with_seams

    @staticmethod
    def save_results(
        original: np.ndarray,
        seams: list[np.ndarray],
        resized: np.ndarray,
        output_dir: str,
        filename: str,
    ) -> None:
        """
        Save original image with seams and final resized image.

        :param original: Original image.
        :param seams: List of seam paths.
        :param resized: Final resized image.
        :param output_dir: Directory for saving results.
        :param filename: Base filename for saving.
        """
        os.makedirs(output_dir, exist_ok=True)

        # Convert to BGR for OpenCV saving
        original_bgr = cv2.cvtColor(original, cv2.COLOR_RGB2BGR)
        resized_bgr = cv2.cvtColor(resized, cv2.COLOR_RGB2BGR)

        # Overlay seams on the original image
        img_with_seams = ImageVisualizer.overlay_seams(original, seams)
        img_with_seams_bgr = cv2.cvtColor(img_with_seams, cv2.COLOR_RGB2BGR)

        # Save images
        cv2.imwrite(
            os.path.join(output_dir, f"{filename}_seams.jpg"), img_with_seams_bgr
        )
        cv2.imwrite(os.path.join(output_dir, f"{filename}_resized.jpg"), resized_bgr)

        print(f"Results saved to {output_dir}")

    @staticmethod
    def show_images(
        original: np.ndarray, seams: list[np.ndarray], resized: np.ndarray
    ) -> None:
        """
        Display original image with seams and the final resized image.
        """
        img_with_seams = ImageVisualizer.overlay_seams(original, seams)

        plt.figure(figsize=(15, 5))

        plt.subplot(1, 3, 1)
        plt.title("Original Image")
        plt.imshow(original)
        plt.axis("off")

        plt.subplot(1, 3, 2)
        plt.title("Seam Overlay")
        plt.imshow(img_with_seams)
        plt.axis("off")

        plt.subplot(1, 3, 3)
        plt.title("Final Resized Image")
        plt.imshow(resized)
        plt.axis("off")

        plt.show()
