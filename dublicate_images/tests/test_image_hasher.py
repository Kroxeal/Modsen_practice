import unittest
from PIL import Image
from src.image_hasher.image_hasher import ImageHasher


class TestImageHasher(unittest.TestCase):

    def test_calculate_image_hashes(self):
        img = Image.new('RGB', (100, 100))

        images_generator = [("test_image.jpg", img)]

        hasher = ImageHasher()
        image_hashes = hasher.calculate_image_hashes(images_generator)

        self.assertEqual(len(image_hashes), 1)
        self.assertIn("test_image.jpg", image_hashes)
        self.assertIsInstance(image_hashes["test_image.jpg"], int)


if __name__ == '__main__':
    unittest.main()
