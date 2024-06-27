import os
import time
from src.process_dublicate.process_dublicate import DuplicateProcessor

if __name__ == "__main__":
    folders = [
        os.path.join("5 Flower Types Classification Dataset", "Lilly"),
        os.path.join("5 Flower Types Classification Dataset", "Lotus"),
        os.path.join("5 Flower Types Classification Dataset", "Orchid"),
        os.path.join("5 Flower Types Classification Dataset", "Sunflower"),
    ]

    start_time = time.time()

    processor = DuplicateProcessor()
    processor.process_folders(folders)
    processor.show_images(20)

    total_time = time.time() - start_time
    print(f"Total time taken: {total_time} seconds")

