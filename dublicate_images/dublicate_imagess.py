import os
from PIL import Image
import imagehash


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.lower().endswith((".jpeg", ".jpg")):
            img_path = os.path.join(folder, filename)
            try:
                img = Image.open(img_path)
                images.append((img_path, img))
            except IOError:
                print(f"Error loading image {img_path}")
    return images


def calculate_image_hashes(images):
    image_hashes = []
    for img_path, img in images:
        hash_val = imagehash.phash(img)
        image_hashes.append((img_path, hash_val))
    return image_hashes


def find_duplicates(image_hashes):
    duplicates = {}
    hash_dict = {}

    for img_path, hash_val in image_hashes:
        if hash_val in hash_dict:
            if hash_val not in duplicates:
                duplicates[hash_val] = [hash_dict[hash_val]]
            duplicates[hash_val].append(img_path)
        else:
            hash_dict[hash_val] = img_path

    return duplicates


def print_duplicates(duplicates):
    for hash_val, img_paths in duplicates.items():
        print(f"Duplicate hash: {hash_val}")
        for img_path in img_paths:
            print(f"\t{img_path}")


def main(folder1, folder2=None):
    images1 = load_images_from_folder(folder1)
    image_hashes1 = calculate_image_hashes(images1)

    if folder2:
        images2 = load_images_from_folder(folder2)
        image_hashes2 = calculate_image_hashes(images2)
        image_hashes = image_hashes1 + image_hashes2
    else:
        image_hashes = image_hashes1

    duplicates = find_duplicates(image_hashes)
    print_duplicates(duplicates)


folder1 = r"D:\downloads_chrome\5 Flower Types Classification Dataset\Lilly"
folder2 = r"D:\downloads_chrome\5 Flower Types Classification Dataset\Rose"

main(folder1, folder2)
