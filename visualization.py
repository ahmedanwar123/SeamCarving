# import numpy as np
# import cv2
# import matplotlib.pyplot as plt
# import os
# from typing import List


# class ImageVisualizer:
#     """Handles image visualization and saving."""

#     @staticmethod
#     def save_results(
#         original: np.ndarray,
#         seam_visualizations: List[np.ndarray],
#         resized: np.ndarray,
#         output_dir: str,
#         filename: str,
#     ) -> None:
#         """
#         Save images to disk.

#         :param original: Original image.
#         :param seam_visualizations: List of images showing seam removal steps.
#         :param resized: Final resized image.
#         :param output_dir: Directory for saving results.
#         :param filename: Base filename for saving.
#         """
#         os.makedirs(output_dir, exist_ok=True)

#         original_bgr = cv2.cvtColor(original, cv2.COLOR_RGB2BGR)
#         resized_bgr = cv2.cvtColor(resized, cv2.COLOR_RGB2BGR)

#         # Save original and final images
#         cv2.imwrite(os.path.join(output_dir, f"{filename}_original.jpg"), original_bgr)
#         cv2.imwrite(os.path.join(output_dir, f"{filename}_resized.jpg"), resized_bgr)

#         # Save seam visualizations
#         for i, vis in enumerate(seam_visualizations):
#             vis_bgr = cv2.cvtColor(vis, cv2.COLOR_RGB2BGR)
#             cv2.imwrite(os.path.join(output_dir, f"{filename}_seam_{i+1}.jpg"), vis_bgr)

#         print(f"Results saved to {output_dir}")

#     @staticmethod
#     def show_images(original: np.ndarray, seam_visualizations: List[np.ndarray], resized: np.ndarray) -> None:
#         """
#         Display original, seam visualization steps, and final resized images.

#         :param original: Original image.
#         :param seam_visualizations: List of images showing seam removal steps.
#         :param resized: Final resized image.
#         """
#         num_images = len(seam_visualizations) + 2  # Original + Seams + Resized
#         plt.figure(figsize=(15, 5))

#         # Show original image
#         plt.subplot(1, num_images, 1)
#         plt.title("Original Image")
#         plt.imshow(original)
#         plt.axis("off")

#         # Show seam visualization steps
#         for i, vis in enumerate(seam_visualizations):
#             plt.subplot(1, num_images, i + 2)
#             plt.title(f"Seam {i+1}")
#             plt.imshow(vis)
#             plt.axis("off")

#         # Show final resized image
#         plt.subplot(1, num_images, num_images)
#         plt.title("Resized Image")
#         plt.imshow(resized)
#         plt.axis("off")

#         plt.show()

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

        :param image: The original image.
        :param seams: List of seams (each seam is an array of indices).
        :return: Image with all seams drawn.
        """
        img_with_seams = image.copy()

        for seam in seams:
            for row, col in enumerate(seam):
                img_with_seams[row, col] = [255, 0, 0]  # Draw seams in RED

        return img_with_seams

    @staticmethod
    def save_results(original: np.ndarray, seams: list[np.ndarray], resized: np.ndarray, output_dir: str, filename: str) -> None:
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
        cv2.imwrite(os.path.join(output_dir, f"{filename}_seams.jpg"), img_with_seams_bgr)
        cv2.imwrite(os.path.join(output_dir, f"{filename}_resized.jpg"), resized_bgr)

        print(f"Results saved to {output_dir}")

    @staticmethod
    def show_images(original: np.ndarray, seams: list[np.ndarray], resized: np.ndarray) -> None:
        """
        Display original image with seams and the final resized image.

        :param original: Original image.
        :param seams: List of seams.
        :param resized: Final resized image.
        """
        img_with_seams = ImageVisualizer.overlay_seams(original, seams)

        plt.figure(figsize=(15, 5))
        
        plt.subplot(1, 2, 1)
        plt.title("Seams to be Removed")
        plt.imshow(img_with_seams)
        plt.axis("off")

        plt.subplot(1, 2, 2)
        plt.title("Final Resized Image")
        plt.imshow(resized)
        plt.axis("off")

        plt.show()
