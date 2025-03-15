import cv2
from seam_carver import SeamCarver


def main():
    image_path = input("Enter image path: ")
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    print(
        "Choose resizing option:\n1 - Resize Width\n2 - Resize Height\n3 - Resize Both"
    )

    option = int(input("Enter option (1/2/3): "))

    carver = SeamCarver(img_rgb)

    if option == 1:
        target_width = int(input("Enter target width: "))
        resized_img = carver.carve_width(target_width)
    elif option == 2:
        target_height = int(input("Enter target height: "))
        resized_img = carver.carve_height(target_height)
    elif option == 3:
        target_width = int(input("Enter target width: "))
        target_height = int(input("Enter target height: "))
        resized_img = carver.carve_both(target_width, target_height)

    # Get seam visualization
    seam_visualization = carver.get_seam_visualization()

    # Save results
    cv2.imwrite("seams_visual.jpg", cv2.cvtColor(seam_visualization, cv2.COLOR_RGB2BGR))
    cv2.imwrite("resized_result.jpg", cv2.cvtColor(resized_img, cv2.COLOR_RGB2BGR))

    print("Seam visualization saved as seams_visual.jpg")
    print("Final resized image saved as resized.jpg")


if __name__ == "__main__":
    raise SystemExit(main())
