import numpy as np
import cv2


class EnergyCalculator:
    """Calculates energy of an image using gradient magnitude."""

    @staticmethod
    def calculate_energy(img: np.ndarray) -> np.ndarray:
        """
        Calculate energy of an image using gradient magnitude:
        e = |dI/dx| + |dI/dy|

        :param img: Input image as a NumPy array.
        :return: Energy matrix of the image.
        """
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        gradient_x = np.zeros_like(gray, dtype=np.float64)
        gradient_x[:, :-1] = np.abs(
            gray[:, 1:].astype(np.float64) - gray[:, :-1].astype(np.float64)
        )

        gradient_y = np.zeros_like(gray, dtype=np.float64)
        gradient_y[:-1, :] = np.abs(
            gray[1:, :].astype(np.float64) - gray[:-1, :].astype(np.float64)
        )

        return gradient_x + gradient_y
