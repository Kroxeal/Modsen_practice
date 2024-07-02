import os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

import imagehash
from PIL import Image

from src.image_loader.image_loader import ImageLoader
from src.image_hasher.image_hasher import ImageHasher
from src.duplicate_finder.duplicate_finder import DuplicateFinder
from src.show_image.show_image import ImageDisplay


class DuplicateProcessor:
    def __init__(self):
        self.duplicate_finder = DuplicateFinder()

    def process_folders(self, folders: list):
        """
        Process images from multiple folders using ThreadPoolExecutor.
        """
        with ThreadPoolExecutor(max_workers=4) as executor:
            future_to_folder = {executor.submit(self._load_images, folder): folder for folder in folders}

            for future in as_completed(future_to_folder):
                folder = future_to_folder[future]
                try:
                    images_generator = future.result()
                    if images_generator:
                        self._process_images(images_generator)
                except Exception as exc:
                    print(f"Error process {folder}: {exc}")

        self.duplicate_finder.find_duplicates()

        if not self.duplicate_finder.get_duplicates():
            pass
        else:
            print("No duplicates found.")
            self.duplicate_finder.print_duplicates()

    def _load_images(self, folder: str):
        return list(ImageLoader.load_images_from_folder(folder))

    def _process_images(self, images_generator):
        with ProcessPoolExecutor() as executor:
            future_to_image = {executor.submit(self._hash_image, img_path, img): (img_path, img) for img_path, img in images_generator}
            image_hashes = {}
            for future in as_completed(future_to_image):
                try:
                    img_path, hash_val = future.result()
                    image_hashes[img_path] = hash_val
                except Exception as exc:
                    img_path, _ = future_to_image[future]
                    print(f"Error process hash {img_path}: {exc}")
            self.duplicate_finder.add_image_hashes(image_hashes)

    @staticmethod
    def _hash_image(img_path, img):
        img = img.convert('RGB').resize((256, 256), Image.Resampling.LANCZOS)
        hash_val = imagehash.phash(img)
        return img_path, hash_val

    def show_images(self, limit: int):
        """
        Show duplicate images
        """
        duplicates = self.duplicate_finder.get_duplicates()
        ImageDisplay.show_images(duplicates, limit)
