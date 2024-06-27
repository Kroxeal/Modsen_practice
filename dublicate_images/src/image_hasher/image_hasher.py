from PIL import Image
import imagehash


class ImageHasher:
    @staticmethod
    def calculate_image_hashes(images_generator):
        """
        Calculate perceptual hashes for loaded images.
        """
        image_hashes = {}
        for img_path, img in images_generator:
            img = img.convert('RGB').resize((256, 256), Image.Resampling.LANCZOS)
            hash_val = imagehash.phash(img)
            image_hashes[img_path] = hash_val
        return image_hashes
