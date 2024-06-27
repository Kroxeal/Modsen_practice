import os
from concurrent.futures import ThreadPoolExecutor, as_completed

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
            future_to_folder = {executor.submit(ImageLoader.load_images_from_folder, folder): folder for folder in folders}

            for future in as_completed(future_to_folder):
                folder = future_to_folder[future]
                try:
                    images_generator = future.result()
                    if images_generator:
                        image_hashes = ImageHasher.calculate_image_hashes(images_generator)
                        self.duplicate_finder.add_image_hashes(image_hashes)
                except Exception as exc:
                    print(f"Error processing {folder}: {exc}")

        self.duplicate_finder.find_duplicates()

        if not self.duplicate_finder.get_duplicates():
            print("No duplicates found.")
        else:
            self.duplicate_finder.print_duplicates()

    def show_images(self, limit: int):
        """
        Show duplicate images.
        """
        duplicates = self.duplicate_finder.get_duplicates()
        ImageDisplay.show_images(duplicates, limit)
