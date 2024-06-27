from PIL import Image
import matplotlib.pyplot as plt


class ImageDisplay:
    @staticmethod
    def show_images(duplicates, limit):
        """
        Show images via matplotlib.
        """
        count = 0
        plt.figure(figsize=(10, 10))
        for img_paths in duplicates.values():
            for img_path in img_paths:
                if count >= limit:
                    plt.show()
                    return
                try:
                    with Image.open(img_path) as img:
                        count += 1
                        plt.subplot((limit + 1) // 2, 2, count)
                        plt.imshow(img)
                        plt.axis('off')
                        plt.title(f'Duplicate {count}')
                except IOError:
                    print(f"Error loading image {img_path}")
        plt.show()
