import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from PIL import Image
import imagehash
import matplotlib.pyplot as plt


class ImageDuplicateFinder:
    def __init__(self):
        self.image_hashes = {}
        self.duplicates = {}

    def load_images_from_folder_generator(self, folder: str):
        """
        Loading images from a specified folder
        Adding path and image_name into list images
        """
        if not os.path.exists(folder):
            print('Folder does not exist')
            return

        try:
            for filename in os.listdir(folder):
                if filename.lower().endswith((".jpeg", ".jpg", ".png", ".bmp")):
                    img_path = os.path.join(folder, filename)
                    try:
                        with Image.open(img_path) as img:
                            yield img_path, img.copy()
                    except IOError:
                        print(f"Error loading image {img_path}")
        except PermissionError:
            print(f'Permission denied to access folder {folder}')

    def calculate_image_hashes(self, images_generator) -> None:
        """Calculating perceptual hashes for loaded images"""
        for img_path, img in images_generator:
            img = img.convert('RGB').resize((256, 256), Image.Resampling.LANCZOS)
            hash_val = imagehash.phash(img)
            self.image_hashes[img_path] = hash_val

    def find_duplicates(self) -> None:
        """Finding duplicate images based on hashes"""
        for img_path, hash_val in self.image_hashes.items():
            if hash_val in self.duplicates:
                self.duplicates[hash_val].append(img_path)
            else:
                self.duplicates[hash_val] = [img_path]

        self.duplicates = {hash_val: img_paths for hash_val, img_paths in self.duplicates.items() if len(img_paths) > 1}

    def print_duplicates(self) -> None:
        """Printing the found duplicate images"""
        for hash_val, img_paths in self.duplicates.items():
            print(f"Duplicate hash: {hash_val}")
            for img_path in img_paths:
                print(f"\t{img_path}")

    def process_folders(self, folders: list) -> None:
        """Process images from multiple folders using ThreadPoolExecutor"""
        with ThreadPoolExecutor(max_workers=4) as executor:
            future_to_folder = {executor.submit(self.load_images_from_folder_generator, folder): folder for folder in
                                folders}

            for future in as_completed(future_to_folder):
                folder = future_to_folder[future]
                try:
                    images_generator = future.result()
                    self.calculate_image_hashes(images_generator)
                except Exception as exc:
                    print(f"Error processing {folder}: {exc}")

        self.find_duplicates()

        if not self.duplicates:
            print("No duplicates found.")
        else:
            self.print_duplicates()

    def show_images(self, limit: int) -> None:
        """Show images via matplotlib"""
        count = 0
        plt.figure(figsize=(10, 10))
        for img_paths in self.duplicates.values():
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


if __name__ == "__main__":
    folders = [
        os.path.join("5 Flower Types Classification Dataset", "Lilly"),
        os.path.join("5 Flower Types Classification Dataset", "Lotus"),
        os.path.join("5 Flower Types Classification Dataset", "Orchid"),
        os.path.join("5 Flower Types Classification Dataset", "Sunflower"),
    ]

    start_time = time.time()

    finder = ImageDuplicateFinder()
    finder.process_folders(folders)
    finder.show_images(20)

    total_time = time.time() - start_time
    print(f"Total time taken: {total_time} seconds")
