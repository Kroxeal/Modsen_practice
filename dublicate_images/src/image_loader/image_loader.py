import os
from PIL import Image


class ImageLoader:
    @staticmethod
    def load_images_from_folder(folder: str):
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
