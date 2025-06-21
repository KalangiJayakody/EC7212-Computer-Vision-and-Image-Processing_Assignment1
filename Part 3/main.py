import cv2
import matplotlib.pyplot as plt
import numpy as np

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    rot_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, rot_matrix, (w, h), flags=cv2.INTER_LINEAR)

if __name__ == "__main__":
    img = cv2.imread("../flower-image3.jpg")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("output/original_image_gray.jpg", img_gray)
    cv2.imwrite("output/original_image.jpg", cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))

    angles = [45, 90]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5), dpi=100)
    axes[0].imshow(img_rgb)
    axes[0].set_title("Original Image", fontsize=12)
    axes[0].axis('off')
    for i, angle in enumerate(angles, start=1):
        rotated = rotate_image(img_rgb, angle)
        cv2.imwrite(f"output/rotated_{angle}.jpg", cv2.cvtColor(rotated, cv2.COLOR_RGB2BGR))
        axes[i].imshow(rotated)
        axes[i].set_title(f"Rotated {angle}°", fontsize=12)
        axes[i].axis('off')
    plt.tight_layout(pad=1.2)
    plt.show()

    fig, axes = plt.subplots(1, 3, figsize=(15, 5), dpi=100)
    axes[0].imshow(img_gray, cmap='gray')
    axes[0].set_title("Original Image", fontsize=12)
    axes[0].axis('off')
    for i, angle in enumerate(angles, start=1):
        rotated = rotate_image(img_gray, angle)
        cv2.imwrite(f"output/rotated_gray_{angle}.jpg", rotated)
        axes[i].imshow(rotated, cmap='gray')
        axes[i].set_title(f"Rotated {angle}°", fontsize=12)
        axes[i].axis('off')
    plt.tight_layout(pad=1.2)
    plt.show()

