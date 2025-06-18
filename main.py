import cv2
import matplotlib.pyplot as plt

def intensity_levels_changing(image, level):
    factor = 256 // level
    reduced_image = (image // factor) * factor
    return reduced_image

if __name__ == "__main__":
    img = cv2.imread("flower-image.jpg")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis("off")
    plt.show()

    for levels in [2, 4, 8, 16, 32, 64, 128]:
        reduced = intensity_levels_changing(img, levels)
        cv2.imwrite(f"output/reduced_levels_{levels}.jpg", reduced)
