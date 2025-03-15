import numpy as np


class SeamFinder:
    """Finds minimum energy seams."""

    @staticmethod
    def calculate_cumulative_energy_map(energy: np.ndarray) -> np.ndarray:
        """
        Compute the cumulative energy map for vertical seam removal.

        :param energy: Energy matrix of the image.
        :return: Cumulative energy map.
        """
        height, width = energy.shape
        cumulative_energy = np.zeros_like(energy, dtype=np.float64)

        cumulative_energy[0, :] = energy[0, :]

        for i in range(1, height):
            for j in range(width):
                if j == 0:
                    cumulative_energy[i, j] = energy[i, j] + min(
                        cumulative_energy[i - 1, j], cumulative_energy[i - 1, j + 1]
                    )
                elif j == width - 1:
                    cumulative_energy[i, j] = energy[i, j] + min(
                        cumulative_energy[i - 1, j - 1], cumulative_energy[i - 1, j]
                    )
                else:
                    cumulative_energy[i, j] = energy[i, j] + min(
                        cumulative_energy[i - 1, j - 1],
                        cumulative_energy[i - 1, j],
                        cumulative_energy[i - 1, j + 1],
                    )

        return cumulative_energy

    @staticmethod
    def find_minimum_energy_seam(cumulative_energy: np.ndarray) -> np.ndarray:
        """
        Find the minimum energy seam.

        :param cumulative_energy: Cumulative energy map.
        :return: Array containing seam indices for each row.
        """
        height, width = cumulative_energy.shape
        seam = np.zeros(height, dtype=np.int32)

        seam[-1] = np.argmin(cumulative_energy[-1, :])

        for i in range(height - 2, -1, -1):
            j = seam[i + 1]
            if j == 0:
                seam[i] = j + np.argmin(
                    [cumulative_energy[i, j], cumulative_energy[i, j + 1]]
                )
            elif j == width - 1:
                seam[i] = (
                    j
                    - 1
                    + np.argmin([cumulative_energy[i, j - 1], cumulative_energy[i, j]])
                )
            else:
                seam[i] = (
                    j
                    - 1
                    + np.argmin(
                        [
                            cumulative_energy[i, j - 1],
                            cumulative_energy[i, j],
                            cumulative_energy[i, j + 1],
                        ]
                    )
                )

        return seam
