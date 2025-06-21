import cv2
import matplotlib.pyplot as plt

def intensity_levels_changing(image, level):
    factor = 256 // level
    return (image // factor) * factor

if __name__ == "__main__":
    img = cv2.imread("../flower-image3.jpg")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    levels_list = [2, 4, 8, 16, 32, 64, 128, 256]

    fig, axes = plt.subplots(2, 4, figsize=(10, 5), dpi=100)
    for idx, level in enumerate(levels_list):
        reduced = intensity_levels_changing(img_rgb, level)
        cv2.imwrite(f"output/reduced_levels_RGB{level}.jpg", cv2.cvtColor(reduced, cv2.COLOR_RGB2BGR))
        ax = axes[idx//4, idx%4]
        ax.imshow(intensity_levels_changing(img_rgb, level))
        ax.set_title(f"{level} levels", fontsize=10)
        ax.axis('off')
    plt.tight_layout(pad=1) 
    plt.show()

    fig, axes = plt.subplots(2, 4, figsize=(10, 5), dpi=100)
    for idx, level in enumerate(levels_list):
        reduced_gray = intensity_levels_changing(img_gray, level)
        cv2.imwrite(f"output/reduced_levels_GRAY{level}.jpg", reduced_gray)
        ax = axes[idx//4, idx%4]
        ax.imshow(reduced_gray, cmap='gray')
        ax.set_title(f"{level} levels", fontsize=10)
        ax.axis('off')
    plt.tight_layout(pad=1)
    plt.show()


