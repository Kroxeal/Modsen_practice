import os
from PIL import Image
import imagehash


class ImageDuplicateFinder:
    def __init__(self):
        self.images = []
        self.image_hashes = {}
        self.duplicates = {}

    def load_images_from_folder(self, folder: str) -> None:
        """
        Loading images from a specified folder
        Adding path and image_name into list images
        """
        for filename in os.listdir(folder):
            if filename.lower().endswith((".jpeg", ".jpg")):
                img_path = os.path.join(folder, filename)
                try:
                    img = Image.open(img_path)
                    self.images.append((img_path, img))
                except IOError:
                    print(f"Error loading image {img_path}")

    def calculate_image_hashes(self):
        """Calculating perceptual hashes for loaded images"""
        for img_path, img in self.images:
            hash_val = imagehash.phash(img)
            self.image_hashes[img_path] = hash_val

    def find_duplicates(self):
        """Finding duplicate images based on hashes"""
        for img_path, hash_val in self.image_hashes.items():
            if hash_val in self.duplicates:
                self.duplicates[hash_val].append(img_path)
            else:
                self.duplicates[hash_val] = [img_path]

        self.duplicates = {hash_val: img_paths for hash_val, img_paths in self.duplicates.items() if len(img_paths) > 1}

    def print_duplicates(self):
        """Printing the found duplicate images"""
        for hash_val, img_paths in self.duplicates.items():
            print(f"Duplicate hash: {hash_val}")
            for img_path in img_paths:
                print(f"\t{img_path}")

    def process_folders(self, folder1:str, folder2:str =None):
        """Process images from one or two folders"""
        self.load_images_from_folder(folder1)
        self.calculate_image_hashes()

        if folder2:
            self.load_images_from_folder(folder2)
            self.calculate_image_hashes()

        self.find_duplicates()
        self.print_duplicates()


if __name__ == "__main__":
    folder1 = os.path.join("5 Flower Types Classification Dataset", "Lilly")
    folder2 = os.path.join("5 Flower Types Classification Dataset", "Lotus")

    finder = ImageDuplicateFinder()
    finder.process_folders(folder1, folder2)
