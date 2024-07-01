import unittest
import os
from PIL import Image
from io import BytesIO
from src.image_loader.image_loader import ImageLoader


class TestImageLoader(unittest.TestCase):

    def test_load_images_from_folder(self):
        folder = "test_data"
        if not os.path.exists(folder):
            os.makedirs(folder)

        test_image = Image.new('RGB', (100, 100))
        test_image_path = os.path.join(folder, "test_image.jpg")
        test_image.save(test_image_path)

        loader = ImageLoader()
        images_generator = loader.load_images_from_folder(folder)

        img_path, img_obj = next(images_generator)

        self.assertEqual(img_path, test_image_path)
        self.assertIsInstance(img_obj, Image.Image)

        os.remove(test_image_path)
        os.rmdir(folder)


if __name__ == '__main__':
    unittest.main()
