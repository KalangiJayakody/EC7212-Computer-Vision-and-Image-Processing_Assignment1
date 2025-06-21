import cv2
import matplotlib.pyplot as plt
import numpy as np

def block_average(image, block_size):
    h, w = image.shape[:2]
    new_image = np.zeros_like(image)

    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            block = image[y:y+block_size, x:x+block_size]
            avg_color = np.mean(block, axis=(0, 1)).astype(np.uint8)
            new_image[y:y+block_size, x:x+block_size] = avg_color
    return new_image

if __name__ == "__main__":
    img = cv2.imread("../flower-image3.jpg")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    block_sizes = [3, 5, 7]

    fig, axes = plt.subplots(1, 3, figsize=(12, 4), dpi=100)
    for i, b in enumerate(block_sizes):
        blocked = block_average(img_rgb, b)
        cv2.imwrite(f"output/block_avg_RGB_{b}x{b}.jpg",
                    cv2.cvtColor(blocked, cv2.COLOR_RGB2BGR))
        axes[i].imshow(blocked)
        axes[i].set_title(f"{b}x{b}", fontsize=10)
        axes[i].axis('off')
    plt.tight_layout(pad=1.2)
    plt.show()

    fig, axes = plt.subplots(1, 3, figsize=(12, 4), dpi=100)
    for i, b in enumerate(block_sizes):
        blocked = block_average(img_gray, b)
        cv2.imwrite(f"output/block_avg_Gray_{b}x{b}.jpg", blocked)
        axes[i].imshow(blocked, cmap='gray')
        axes[i].set_title(f"{b}x{b}", fontsize=10)
        axes[i].axis('off')
    plt.tight_layout(pad=1.2)
    plt.show()
