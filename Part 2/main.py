import cv2
import matplotlib.pyplot as plt

def spatial_average(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))

if __name__ == "__main__":
    img = cv2.imread("../flower-image3.jpg")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel_sizes = [3, 10, 20]

    fig, axes = plt.subplots(1, 3, figsize=(12, 4), dpi=100)
    for i, k in enumerate(kernel_sizes):
        blurred_rgb = spatial_average(img_rgb, k)
        cv2.imwrite(f"output/blur_RGB_{k}x{k}.jpg",cv2.cvtColor(blurred_rgb, cv2.COLOR_RGB2BGR))
        axes[i].imshow(blurred_rgb)
        axes[i].set_title(f"{k}x{k} Kernel", fontsize=10)
        axes[i].axis('off')
    plt.tight_layout(pad=1.2)
    plt.show()

    fig, axes = plt.subplots(1, 3, figsize=(12, 4), dpi=100)
    for i, k in enumerate(kernel_sizes):
        blurred_gray = spatial_average(img_gray, k)
        cv2.imwrite(f"output/blur_Gray_{k}x{k}.jpg", blurred_gray)  
        axes[i].imshow(blurred_gray, cmap='gray')
        axes[i].set_title(f"{k}x{k} Kernel", fontsize=10)
        axes[i].axis('off')
    plt.tight_layout(pad=1.2)
    plt.show()
