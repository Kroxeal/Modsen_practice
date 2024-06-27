class DuplicateFinder:
    def __init__(self):
        self.image_hashes = {}
        self.duplicates = {}

    def find_duplicates(self):
        """
        Find duplicate images based on hashes.
        """
        for img_path, hash_val in self.image_hashes.items():
            if hash_val in self.duplicates:
                self.duplicates[hash_val].append(img_path)
            else:
                self.duplicates[hash_val] = [img_path]

        self.duplicates = {hash_val: img_paths for hash_val, img_paths in self.duplicates.items() if len(img_paths) > 1}

    def add_image_hashes(self, image_hashes):
        self.image_hashes.update(image_hashes)

    def print_duplicates(self):
        """
        Print the found duplicate images.
        """
        for hash_val, img_paths in self.duplicates.items():
            print(f"Duplicate hash: {hash_val}")
            for img_path in img_paths:
                print(f"\t{img_path}")

    def get_duplicates(self):
        return self.duplicates
